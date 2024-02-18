# mellow-wombat
Physical packaging, control and monitoring of RF collection systems like [heeler](https://github.com/guycole/mellow-heeler), [hyena](https://github.com/guycole/mellow-hyena) and [manatee](https://github.com/guycole/mellow-manatee).

## Introduction
Mellow Wombat is a physical framework which supports a portable RF collection system consisting of radio receivers, computers, networking and storage.  MW is designed to fit within [Costco Storage Crates](https://costco.com/.product.4000205525.html) which are weather resistant durable and inexpensive.  The only required external resources to an MW crate are external power and antennas.

Within the "crate" is a wooden "frame" which contains "shelves" where the subsystems reside.  MW provides power, network and RF distribution to the shelves.  There is a "housekeeper" computer which monitors and controls the shelves as necessary.

Mellow Wombat can run autonomously for extended periods, and will share observations to a remote host when connectivity is restored.  MW can also be remotely tasked when connectivity exists.  The housekeeper also supports scheduled activities.  

Mellow Wombat is different from most [SDR](https://en.wikipedia.org/wiki/Software-defined_radio) projects in that the user interface (provided by housekeeper) is minimal, and there is an emphasis on automatic collection/storage of selected emitters.

## Overview
![overview](https://github.com/guycole/mellow-wombat/blob/main/grafix/overview.png)

## Shelf Catalog
+ [Housekeeping](https://github.com/guycole/mellow-wombat/blob/main/housekeeping/README.md)
+ [HackRF One collection](https://github.com/guycole/mellow-wombat/tree/main/hackrf1/README.md)
+ [RTL-SDR collection](https://github.com/guycole/mellow-wombat/tree/main/rtlsdr/README.md)
+ [USRP collection](https://github.com/guycole/mellow-wombat/tree/main/usrp1/README.md)
+ [WiFi collection](https://github.com/guycole/mellow-wombat/tree/main/wifi/README.md)

## Crate Catalog
| Crate | Description (Shelves)                                      |
| ----- | ---------------------------------------------------------- |
|     1 | Original Mellow Wombat development container               |
|     2 | Mellow Wombat system: housekeeping, heeler, hyena, manatee |
|     3 | Mellow Wombat system: housekeeping, heeler, hyena, manatee |

## Assembled
![dimensions](https://github.com/guycole/mellow-wombat/blob/main/grafix/crate_dimensions.png)
![first_power](https://github.com/guycole/mellow-wombat/blob/main/grafix/first_power.png)
