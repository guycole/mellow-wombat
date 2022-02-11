# mellow-wombat-housekeeper
Housekeeping shelf for Mellow Wombat

## Introduction
Mellow Wombat is a portable RF collection system consisting of radio receivers,
computers and rotating storage necessary to record observations.  When 
connected to the internet, observations will be written to a host for analysis.

Mellow Wombat is a modular system which resides in a "crate" and each module
contained on a "shelf" (located within the crate).  Each shelf receives 12 VDC
power and necessary RF connections for the receivers.

## Shelf Catalog
+ Housekeeping (services for collection shelves)
+ RTL-SDR (a collection system based on the RTL-SDR)
+ USRP1 (a collection system based on the Ettus Research USRP1)

## Housekeeping Features
1. 12 VDC power control to client shelves
1. UHF/VHF multicoupler (RF distribution)
1. Network Gateway (wifi for external, ethernet for internal network)
1. DHCP (provision IP address, time, etc.)
1. System Console (web and REST crate control)
1. Monitoring (prometheus and logs)
1. Environmental Sensors (temperature, humidity, etc)
1. Security Sensors (door monitoring)
