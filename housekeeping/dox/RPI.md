# Raspberry Pi
How to configure the rPi as a Mellow Wombat client.

## Assemble Hardware [BOM.md](./BOM.md)
1. USB hard drive
1. Receiver (as required)

## Configure Raspberry Pi

1. Flash fresh Raspberry Pi OS image
    1. [Raspberry Pi OS Lite](https://downloads.raspberrypi.org/raspios_lite_armhf/images/
    raspios_lite_armhf-2022-01-28/2022-01-28-raspios-bullseye-armhf-lite.zip)
    1. Need to install headless, must tweak microSD card of image
        1. [mount image](https://forums.raspberrypi.com/viewtopic.php?t=57775)
        1. ssh (empty) file in /boot
        1. update /etc/hostname
        1. update [/etc/dhcpcd.conf](https://github.com/guycole/mellow-wombat/blob/main/dox/dhcpcd)
        1. update [/etc/hosts](https://github.com/guycole/mellow-wombat/blob/main/dox/hosts) 

1.  Install additional packages
    1. apt-get install emacs
    1. apt-get install build-essential

1.  Add wombat account
    1. useradd -m wombat 
    1. adduser wombat sudo (ensure bash shell)
    1. add .bash_aliases
    1. crontab -e (to create stubbed crontab)
    1. add github key

do I need powered USB hub?

default is BST, make UTC

add wombat as log host to rsyslog.conf

ntpdate ntpstat ntp 

iptables -A OUTPUT -p udp --dport 123 -j ACCEPT
iptables -A INPUT -p udp --sport 123 -j ACCEPT
