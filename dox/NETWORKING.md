# Networking
Mellow Wombat uses an interal wired ethernet for connectivity between shelves, and a WiFi gateway (from the housekeeping shelf) for external reporting.

## WiFi
1. Housekeeping shelf acts as WiFi gateway, time server, DNS, etc.
1. DHCP client of WAP
1. Autodiscovery of friendly WAP (i.e. WAP white list)
1. Collection shelves can query housekeeping shelf for connection status.

## Ethernet
1. All wired hosts use static IP
1. 192.168.171.0/24 net
