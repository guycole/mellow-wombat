# BeagleBoneBlack
How to configure the BBB as a Mellow Wombat host.

## Assemble Hardware [BOM.md](./BOM.md)
1. Powered USB hub
1. USB WiFi dongle
1. USB GPS receiver
1. USB hard drive
1. Wired ethernet hub
1. Optional shelf power control relays and cape.

## Configure Beaglebone
1. Flash fresh Debian image

1.  Change hostname to "wombatXX"
    1. hostnamectl set-hostname wombat02
    1. update /etc/hosts 

1.  Configure for WiFi
    1. https://www.fis.gatech.edu/how-to-configure-bbw-wifi/

1.  Get latest versions
    1. apt-get update/upgrade

1.  Install additional packages
    1. apt-get install emacs
    1. apt-get install gps
    1. apt-get install gpsd-clients
    1. apt-get install gunicorn
    1. apt-get install ntp

1.  Remove node, bonescript, et al
    1. apt-get purge c9-core-installer
    1. apt-get remove bonescript
    1. apt-get remove nodejs

1. Remove HDMI audio and video in uEnv
    1. https://ofitselfso.com/BeagleNotes/Disabling_Video_On_The_Beaglebone_Black_And_Running_Headless.php

1.  Install python packages
    1. pip3 install virtualenv

1.  Add wombat account
    1. useradd -m wombat 
    1. adduser wombat sudo (ensure bash shell)
    1. add .bash_aliases
    1. crontab -e (to create stubbed crontab)
