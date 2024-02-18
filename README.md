# mellow-wombat
Physical packaging, control and monitoring of RF collection systems like [heeler](https://github.com/guycole/mellow-heeler), [hyena](https://github.com/guycole/mellow-hyena) and [manatee](https://github.com/guycole/mellow-manatee).

## Introduction
Mellow Wombat is a physical framework which supports a portable RF collection system consisting of radio receivers, computers, networking and storage.  MW is designed to fit within [Costco Storage Crates](https://costco.com/.product.4000205525.html) which are weather resistant durable and inexpensive.  The only required external resources to an MW crate are external power and antennas.

Within the "crate" is a wooden "frame" which contains "shelves" where the subsystems reside.  MW provides power, network and RF distribution to the shelves.  There is a ["housekeeper"](fixme) computer which monitors and controls the shelves as necessary.

Mellow Wombat can run autonomously for extended periods, and will share observations to a remote host when connectivity is restored.  MW can also be remotely tasked when connectivity exists.  The housekeeper also supports scheduled activities.  

Mellow Wombat is different from most [SDR](https://en.wikipedia.org/wiki/Software-defined_radio) projects in that the user interface (provided by housekeeper) is minimal, and there is an emphasis on automatic collection/storage of selected emitters.

## Deployment
![deployment](https://github.com/guycole/mellow-wombat/blob/main/grafix/deployment_18feb.png)

## Shelf Catalog
+ [Mellow Heeler](https://github.com/guycole/mellow-wombat/tree/main/hackrf1/README.md)
+ [Mellow Hyena](https://github.com/guycole/mellow-wombat/tree/main/rtlsdr/README.md)
+ [Mellow Koala](https://github.com/guycole/mellow-wombat/tree/main/usrp1/README.md)
+ [Mellow Manatee](https://github.com/guycole/mellow-wombat/tree/main/wifi/README.md)
+ [Mellow Wombat](https://github.com/guycole/mellow-wombat/blob/main/housekeeper/README.md)

## Crate Catalog
| Crate       | Description (Shelves)                                      |
| ----------- | ---------------------------------------------------------- |
| [01](fixme) | Original Mellow Wombat development container               |
| [02](fixme) | Mellow Wombat system: housekeeping, heeler, hyena, manatee |
| [03](fixme) | Mellow Wombat system: housekeeping, heeler, hyena, manatee |
