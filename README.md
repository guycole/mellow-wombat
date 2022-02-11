# mellow-wombat-housekeeper
Housekeeping shelf for Mellow Wombat

## Introduction
Mellow Wombat is a portable RF collection system consisting of radio receivers,
computers and rotating storage necessary to record observations.  When 
connected to the internet, observations will be written to a host for analysis.

Mellow Wombat is a modular system which resides in a "crate" and each module
contained on a "shelf" (located within the crate).  Each shelf receives 12 VDC
power and necessary RF connections for the receivers.

* Shelf Catalog
+ Housekeeping (services for collection shelves)
+ RTL-SDR (a collection system based on the RTL-SDR)
+ USRP1 (a collection system based on the Ettus Research USRP1)

## Housekeeping Features
1. 12 VDC power control to client shelves
2. UHF/VHF multicoupler (RF distribution)
3. Network Gateway
  1. WiFi to external world
  2. Powered ethernet hub for internal crate communications
4. DHCP 
  1. Provision IP address, time, etc.
5. System Console
  1. Web and REST based crate control
  2. Configure/control client shelves
  3. Prometheus host
  4. Log host
6. Environmental Sensors
  1. Temperature, humidity, etc
7. Security Sensors
  1. Door monitoring
