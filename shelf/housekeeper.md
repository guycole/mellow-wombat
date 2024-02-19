# housekeeper shelf
Housekeeper performs the shared support functions which the application shelves rely on.  

## Housekeeping Shelf Features
+ 12 VDC power control to client shelves (except crate01)
+ Network gateway (wifi for external, wired ethernet for internal network)
+ System console (web and REST crate control)
    + Display recently collected information 
+ System logging, etc.
+ Monitoring (prometheus and logs)
+ Environmental sensors (temperature, humidity, etc)
+ Security sensors (vibration, door monitoring)
+ Audio alert
+ Solar charging monitoring
+ Location/time [Perky Janus](https://github.com/guycole/perky-janus)

## Supporting Crate Features
+ UHF/VHF multicoupler (RF distribution, 25 MHz to 1 GHz)

## Housekeeper V1
+ [Configuration](https://github.com/guycole/mellow-wombat/blob/main/infra/rpi5_config.md)

## MellowNet
+ 10.168.crate.project  
+ 10.168.0.0/18 = 10.168.0.1 to 10.168.63.254
+ 10.168.1.0/24 = 10.168.1.0 to 10.168.1.254 (crate 1 address range)
+ 10.168.2.0/24 = 10.168.2.0 to 10.168.2.254 (crate 2 address range)
+ 10.168.3.0/24 = 10.168.3.0 to 10.168.3.254 (crate 3 address range)
+ 10.168.1.3 boris
+ 10.168.1.5 waifu
+ 10.168.x.1 wombat (gateway)

| CIDR            | First Address | Last Address | Reservation |
| --------------- | ------------- | ------------ | ----------- |
| 10.168.x.0/28   | 10.168.x.1    | 10.168.x.14  | Wombat      |
| 10.168.x.16/28  | 10.168.x.17   | 10.168.x.30  | Heeler      |
| 10.168.x.32/28  | 10.168.x.33   | 10.168.x.46  | Hyena       |
| 10.168.x.48/28  | 10.168.x.49   | 10.168.x.62  | Koala       |
| 10.168.x.64/28  | 10.168.x.65   | 10.168.x.78  | Manatee     |
| 10.168.x.80/28  | 10.168.x.81   | 10.168.x.94  | Available   |
| 10.168.x.96/28  | 10.168.x.97   | 10.168.x.110 | Available   |
| 10.168.x.112/28 | 10.168.x.113  | 10.168.x.126 | Available   |