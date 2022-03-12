# mellow-wombat
Crate and housekeeping shelf for Mellow Wombat

## Introduction
Mellow Wombat is a framework which supports a portable RF collection system consisting of radio receivers, computers, networking and storage.  Mellow Wombat can run autonomously for extended periods, and will share observations to a remote host when connectivity is restored.  Mellow Wombat can also be remotely controlled when connectivity exists.

Mellow Wombat is a modular system which resides in a "crate" and each module is contained on a "shelf" (located within the crate).  Each shelf receives 12 VDC
power and necessary RF connections for the receivers along w/network connectivity via an internal wired LAN.

## Shelf Catalog
+ Housekeeping (Mellow Wombat itself, services for collection shelves)
+ RTL-SDR (a collection system based on the RTL-SDR)
+ KerberosSDR (a DF system based on KerberosSDR)
+ HackRF1 (a collection system based on the Hack RF One device)
+ USRP1 (a collection system based on the Ettus Research USRP1)

## Housekeeping Features
+ 12 VDC power control to client shelves
+ UHF/VHF multicoupler (RF distribution, 25 MHz to 1 GHz)
+ Network gateway (wifi for external, ethernet for internal network)
+ System console (web and REST crate control)
+ System logging, etc.
+ Monitoring (prometheus and logs)
+ Location/time (GPS)
+ Environmental sensors (temperature, humidity, etc)
+ Security sensors (vibration, door monitoring)
+ Solar charging activity
