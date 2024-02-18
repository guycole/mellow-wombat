# mellow-wombat
Physical packaging, control and monitoring of RF collection systems like [heeler](https://github.com/guycole/mellow-heeler), [hyena](https://github.com/guycole/mellow-hyena) and [manatee](https://github.com/guycole/mellow-manatee).

Mellow Wombat is different from most [SDR](https://en.wikipedia.org/wiki/Software-defined_radio) projects in that the user interface (provided by [housekeeper](https://github.com/guycole/mellow-wombat/blob/main/shelf/housekeeper.md)) is minimal, and there is an emphasis on automatic collection/storage of selected emitters.

## Introduction
Mellow Wombat is a physical framework which supports a portable RF collection system consisting of radio receivers, computers, networking and storage.  MW is designed to fit within [Costco Storage Bin](https://costco.com/.product.4000205525.html) which are weather resistant, durable and inexpensive.  The only external resources to an "storage bin" is power and antennas.

Within the "storage bin" is a [wooden "crate"](https://github.com/guycole/mellow-wombat/blob/main/grafix/crate_dimensions.png) which contains ["shelves"](https://github.com/guycole/mellow-wombat/blob/main/grafix/first_power.png) where the subsystems reside.  Mellow Wombat provides power, network and RF distribution to the shelves.  There is a ["housekeeper"](https://github.com/guycole/mellow-wombat/blob/main/shelf/housekeeper.md) computer which monitors and controls the shelves as necessary.

Mellow Wombat can run autonomously for extended periods, and will share observations to a remote host when connectivity is restored.  MW can also be remotely tasked when connectivity exists.  The housekeeper also supports scheduled activities.  

## Deployment
![deployment](https://github.com/guycole/mellow-wombat/blob/main/grafix/deployment_18feb.png)

## Shelf Catalog
+ [Mellow Heeler](https://github.com/guycole/mellow-wombat/blob/main/shelf/heeler.md)
+ [Mellow Hyena](https://github.com/guycole/mellow-wombat/blob/main/shelf/hyena.md)
+ [Mellow Koala](https://github.com/guycole/mellow-wombat/blob/main/shelf/koala.md)
+ [Mellow Manatee](https://github.com/guycole/mellow-wombat/blob/main/shelf/manatee.md)
+ [Mellow Wombat](https://github.com/guycole/mellow-wombat/blob/main/shelf/housekeeper.md)

## Crate Catalog
| Crate                                                                     | Description (Shelves)                                      |
| ------------------------------------------------------------------------- | ---------------------------------------------------------- |
| [01](https://github.com/guycole/mellow-wombat/blob/main/crate/crate01.md) | Original Mellow Wombat development container               |
| [02](https://github.com/guycole/mellow-wombat/blob/main/crate/crate02.md) | Mellow Wombat system: housekeeping, heeler, hyena, manatee |
| [03](https://github.com/guycole/mellow-wombat/blob/main/crate/crate03.md) | Mellow Wombat system: housekeeping, heeler, hyena, manatee |
