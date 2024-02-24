# rpi3 configuration
The [raspberry pi 3](https://www.raspberrypi.com/products/raspberry-pi-3-model-b/) is useful as a [rtl-sdr](https://www.rtl-sdr.com/) host for less challenging, narrowband emitters.

## Initial Configuration Steps
1. Create an image using the [raspberry pi imager](https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/).  Currently this is "Raspberry Pi Legacy (32 bit)" released 2023-12-05.
1. Configuration as a rpi3 host requires:
    1.  SSH enabled (because headless).
        1. Do this as part of creating the image
    1.  WiFi enabled (for initial updates, will disable later).
        1. Associate a WAP as part of creating the image.
    1.  Create a user account.
        1. Via image creation.
    1.  Wired ethernet enabled (for mellow-net).
        1. After image creation.
    1.  Add applications
        1. AWS CLI
        1. GitHub and mellow repositories
        1. rtl-sdr
        1. dump1090
        1. dump978

## Networking
1.  When first booted, there will be WiFi connectivity (wlan0) and eth0 under DHCP
1.  The 32 bit release is unburdened by network manager
1.  Mellow Wombat wants a static address for eth0
    1. IP address depends upon crate and project, see [housekeeper](https://github.com/guycole/mellow-wombat/blob/main/shelf/housekeeper.md)
    1. add to /etc/dhcpcd.conf
    1. ```interface eth0```
    1. ```static ip_address=10.168.1.82/18```
    1. ```static_routers=10.168.1.1```
    1. ```static domain_name_servers=10.168.1.1 8.8.8.8```

## Relevant Links
1. https://www.makeuseof.com/raspberry-pi-set-static-ip/
1. https://www.tomshardware.com/how-to/static-ip-raspberry-pi
1. https://stackoverflow.com/questions/63030641/how-to-install-awscli-version-2-on-raspberry-pi
1. https://vortac.io/2020/06/02/installing-dump1090-on-raspberrypi/