# mellow-wombat
Mellow Wombat crate and housekeeping shelf.

## Introduction
Mellow Wombat is a framework which supports a portable RF collection system consisting of radio receivers, computers, networking and storage.  Mellow Wombat can run autonomously for extended periods, and will share observations to a remote host when connectivity is restored.  Mellow Wombat can also be remotely controlled when connectivity exists.

Mellow Wombat is a modular system which resides in a "crate" and each module is contained on a "shelf" (located within the crate).  Each shelf receives 12 VDC
power and necessary RF connections for the receivers along w/network connectivity via an internal wired LAN.

## Housekeeping Features
+ 12 VDC power control to client shelves
+ UHF/VHF multicoupler (RF distribution, 25 MHz to 1 GHz)
+ Network gateway (wifi for external, wired ethernet for internal network)
+ System console (web and REST crate control)
+ System logging, etc.
+ Monitoring (prometheus and logs)
+ Location/time (GPS)
+ Environmental sensors (temperature, humidity, etc)
+ Security sensors (vibration, door monitoring)
+ Solar charging activity

## Documentation
+ [Beaglebone Black](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/dox/BEAGLEBONE.md)
+ [Bill of Materials](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/dox/BOM.md)
+ [Crate Dimensions](https://github.com/guycole/mellow-wombat/blob/main/grafix/crate_dimensions.png)
+ [Database Schema](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/dox/DATABASE.md)
+ [GPS (time and position)](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/dox/GPS.md)
+ [History](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/dox/HISTORY.md)
+ [Monitoring (prometheus)](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/dox/MONITORING.md)
+ [Networking (cratenet)](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/dox/NETWORKING.md)
+ [Power](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/dox/POWER.md)
+ [Web (django)](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/dox/WEB.md)

## Assembled
![first_power](https://github.com/guycole/mellow-wombat/blob/main/grafix/first_power.png)
 
