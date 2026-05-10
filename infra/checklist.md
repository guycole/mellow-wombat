# Crate Checklist
## Gateway
1. Boots from Passport USB drive
1. WiFi is working (i.e. "ping 8.8.8.8")
1. docker is working (i.e. "docker images")
1. postgres is working (i.e. connect via psql)
1. chrony is working (i.e. "chronyc sources" only small deviations)
1. hostname should be same as crate, i.e. 'wombat04'
1. /etc/hosts file should be up to date, generated and have all crates
    1. loopback defined in /etc/hosts like
    ```
    127.0.0.1	localhost
    127.0.1.1	wombat04
    ```
1. /var/log/wombat exists and is owned by syslog:adm
    1. gateway host has recent logfile updates
    1. logfiles are being rotated
1. prometheus is up and servicing web requests
1. there is a wombat user account
    1. there is github access via a dedicated key (for the crate)
    1. there is AWS access via a dedicated key (for the crate)
    1. ansible is working
    1. you can visit all of the collectors without authentication
    1. rsync is working
1. there is /var/wombat (et al)

## Collector
1. hostname is correct
1. only configured for ethernet, no WiFi
1. chrony is working (i.e. "chronyc sources" only small deviations)
    1. chrony gets time from the gateway only
1. remote logging (to gateway) is working
1. there is a wombat user account
    gateway can access without auth
1. there is a /var/wombat (et al)

### Odroid Collector
### RPI Collector
