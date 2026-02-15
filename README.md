# mellow-wombat
Physical packaging, control and monitoring of RF collection systems like [heeler](https://github.com/guycole/mellow-heeler), [hyena](https://github.com/guycole/mellow-hyena) and [manatee](https://github.com/guycole/mellow-manatee).

## Introduction
Mellow Wombat is a framework which supports a RF collection system consisting of radio receivers, computers, networking and storage.  A MW deployment consists of a [wooden "crate"](https://github.com/guycole/mellow-wombat/blob/main/grafix/crate_dimensions.png) where the subsystems reside.  Mellow Wombat provides monitoring, power, network and RF distribution for the subsystems.

MW is designed to fit within [Costco Storage Bin](https://costco.com/.product.4000205525.html) which are weather resistant, durable and inexpensive.  The only external resources to an "storage bin" is power and antennas.

Mellow Wombat can run autonomously for extended periods, and will share observations to a remote host when connectivity is restored.  MW can also be remotely tasked when connectivity exists.

## Deployment
Mellow Wombat consists of a "gateway" which manages a fleet of "collectors".  All computers are connected via ethernet.

![deployment](https://github.com/guycole/mellow-wombat/blob/main/grafix/wombat_deployment.jpg)

## Gateway
There is only one gateway per crate, and it is typically a [Odroid N2](https://www.hardkernel.com/shop/odroid-n2-with-4gbyte-ram-2/) with 4GB of RAM and a 4TB [Western Digital Passport USB Drive](https://www.westerndigital.com/products/portable-drives/wd-my-passport-usb-3-0-hdd?sku=WDBPKJ0040BBK-WESN).  The gateway manages outside (the crate) connectivity (either wired or WiFi).  Gateway configuration described [here](https://github.com/guycole/mellow-wombat/blob/main/infra/odroidn2_config.md).

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