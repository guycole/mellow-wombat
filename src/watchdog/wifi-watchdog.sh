#!/bin/bash

# wifi-watchdog.sh
#
# Run from root cron every 6 minutes.
# Reload 88XXau after 3 consecutive Wi-Fi failures.
#
# sudo install -m 755 wifi-watchdog.sh /usr/local/sbin/wifi-watchdog
#

INTERFACE="wlan0"
MODULE="88XXau"

STATE_DIR="/var/lib/wifi-watchdog"
STATE_FILE="${STATE_DIR}/failures"

LOGGER_TAG="wifi-watchdog"

MAX_FAILURES=3
RELOAD_DELAY=3

mkdir -p "$STATE_DIR"

# Read previous failure count.
if [[ -f "$STATE_FILE" ]]; then
    FAILURES=$(cat "$STATE_FILE" 2>/dev/null)
else
    FAILURES=0
fi

# Protect against a damaged/non-numeric state file.
if ! [[ "$FAILURES" =~ ^[0-9]+$ ]]; then
    FAILURES=0
fi

#
# Healthy if wlan0 is associated with an AP.
#
if iw dev "$INTERFACE" link 2>/dev/null | grep -q '^Connected to '; then
    if (( FAILURES > 0 )); then
        logger -t "$LOGGER_TAG" \
            "$INTERFACE recovered after $FAILURES consecutive failure(s)"
    fi

    echo 0 > "$STATE_FILE"
    exit 0
fi

#
# Failure.
#
FAILURES=$((FAILURES + 1))
echo "$FAILURES" > "$STATE_FILE"

logger -t "$LOGGER_TAG" \
    "$INTERFACE not connected: failure $FAILURES/$MAX_FAILURES"

if (( FAILURES < MAX_FAILURES )); then
    exit 0
fi

#
# Three consecutive failures. Reload the Realtek driver.
#
logger -t "$LOGGER_TAG" \
    "$INTERFACE failed $FAILURES consecutive checks; reloading $MODULE"

if ! modprobe -r "$MODULE"; then
    logger -t "$LOGGER_TAG" \
        "ERROR: failed to unload $MODULE"
    exit 1
fi

sleep "$RELOAD_DELAY"

if ! modprobe "$MODULE"; then
    logger -t "$LOGGER_TAG" \
        "ERROR: failed to load $MODULE"
    exit 1
fi

#
# Reset the counter. Subsequent cron runs will determine whether
# the reload actually restored connectivity.
#
echo 0 > "$STATE_FILE"

logger -t "$LOGGER_TAG" \
    "$MODULE reloaded; waiting for Wi-Fi to reconnect"

exit 0
