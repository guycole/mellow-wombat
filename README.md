# mellow-wombat
Crate, housekeeping and rtlsdr shelves for Mellow Wombat

## Introduction
Mellow Wombat is a framework which supports a portable RF collection system consisting of radio receivers, computers, networking and storage.  Mellow Wombat can run autonomously for extended periods, and will share observations to a remote host when connectivity is restored.  Mellow Wombat can also be remotely tasked when connectivity exists.  

Mellow Wombat is different from most [SDR](https://en.wikipedia.org/wiki/Software-defined_radio) projects in that the user interface is minimal, and there is an emphasis on automatic storage of selected emitters.

Mellow Wombat is a modular system which resides in a "crate" and each module is contained on a "shelf" (located within the crate).  Each shelf receives 12 VDC power and necessary RF connections for the receivers along w/network connectivity via an internal wired LAN.

There are various Mellow Wombat crates, each with varying hardware and collection capabilities.

## Overview
![overview](https://github.com/guycole/mellow-wombat/blob/main/grafix/overview.png)

## Shelf Catalog
+ [Housekeeping](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/README.md)
+ [HackRF One collection](https://github.com/guycole/mellow-wombat/tree/main/hackrf1/README.md)
+ [RTL-SDR collection](https://github.com/guycole/mellow-wombat/tree/main/rtlsdr/README.md)
+ [USRP collection](https://github.com/guycole/mellow-wombat/tree/main/usrp1/README.md)
+ [WiFi collection](https://github.com/guycole/mellow-wombat/tree/main/wifi/README.md)

## Crate Catalog
| Crate | Description                                      |
| ----- | ------------------------------------------------ |
|     1 | Original Mellow Elephant container               |
|     2 | Mellow Wombat system: housekeeping, rtlsdr, wifi |
|     3 | Mellow Wombat system: housekeeping, hackrf1      |

## Assembled
![dimensions](https://github.com/guycole/mellow-wombat/blob/main/grafix/crate_dimensions.png)
![first_power](https://github.com/guycole/mellow-wombat/blob/main/grafix/first_power.png)
