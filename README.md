# mellow-wombat
Physical packaging, control and monitoring of RF collection systems like [heeler](https://github.com/guycole/mellow-heeler), [hyena](https://github.com/guycole/mellow-hyena) and [manatee](https://github.com/guycole/mellow-manatee).

## Introduction
Mellow Wombat is a physical framework which supports a portable RF collection system consisting of radio receivers, computers, networking and storage.  A MW deployment consists of a [wooden "crate"](https://github.com/guycole/mellow-wombat/blob/main/grafix/crate_dimensions.png) which contains ["shelves"](https://github.com/guycole/mellow-wombat/blob/main/grafix/first_power.png) where the subsystems reside.  Mellow Wombat provides monitoring, power, network and RF distribution to the shelves.  The ["housekeeper"](https://github.com/guycole/mellow-wombat/blob/main/shelf/housekeeper.md) computer is responsible for monitoring and control of the shelves as necessary.

MW is designed to fit within [Costco Storage Bin](https://costco.com/.product.4000205525.html) which are weather resistant, durable and inexpensive.  The only external resources to an "storage bin" is power and antennas.

Mellow Wombat can run autonomously for extended periods, and will share observations to a remote host when connectivity is restored.  MW can also be remotely tasked when connectivity exists.  The housekeeper also supports scheduled activities.  

## Deployment
![deployment](https://github.com/guycole/mellow-wombat/blob/main/grafix/wombat_deployment.jpg)

## Shelf Catalog (Collectors)
+ [Mellow Heeler](https://github.com/guycole/mellow-wombat/blob/main/shelf/heeler.md)
+ [Mellow Hyena](https://github.com/guycole/mellow-wombat/blob/main/shelf/hyena.md)
+ [Mellow Koala](https://github.com/guycole/mellow-wombat/blob/main/shelf/koala.md)
+ [Mellow Manatee](https://github.com/guycole/mellow-wombat/blob/main/shelf/manatee.md)
+ [Mellow Wombat](https://github.com/guycole/mellow-wombat/blob/main/shelf/housekeeper.md)

## Crate Catalog
| Crate                                                                     | Description (Shelves)                           |
| ------------------------------------------------------------------------- | ----------------------------------------------- |
| [01](https://github.com/guycole/mellow-wombat/blob/main/crate/crate01.md) | AC Power to 12V, 2 Shelves, Anderson            |
| [02](https://github.com/guycole/mellow-wombat/blob/main/crate/crate02.md) | AC Power to 12V, 3 Shelves, Vallejo             |
| [03](https://github.com/guycole/mellow-wombat/blob/main/crate/crate03.md) | AC Power, No Shelves: various development hosts |