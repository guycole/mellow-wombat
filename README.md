# mellow-wombat
Physical packaging, control and monitoring of RF collection systems like [heeler](https://github.com/guycole/mellow-heeler), [hyena](https://github.com/guycole/mellow-hyena) and [manatee](https://github.com/guycole/mellow-manatee).

## Introduction
Mellow Wombat is a physical framework which supports a portable RF collection system consisting of radio receivers, computers, networking and storage.  MW is designed to fit within [Costco Storage Crates](https://www.costco.com/greenmade-12-gallon-storage-bin%2c-4-pack.product.4000229972.html) which are weather resistant durable and inexpensive.  The only external resources to an MW crate are an external power source and antennas.

Within the "crate" is a wooden "frame" which contains "shelves" where the subsystems reside.

Mellow Wombat can run autonomously for extended periods, and will share observations to a remote host when connectivity is restored.  MW can also be remotely tasked when connectivity exists.  

Mellow Wombat is different from most [SDR](https://en.wikipedia.org/wiki/Software-defined_radio) projects in that the user interface is minimal, and there is an emphasis on automatic collection/storage of selected emitters.  MW offers 

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
