# rpi4 configuration
The anemic [raspberry pi 4](https://www.raspberrypi.com/products/raspberry-pi-4-model-b/) is useful as a [rtl-sdr](https://www.rtl-sdr.com/) host for less challenging, narrowband emitters.

## Initial Configuration Steps
1. Create an image using the [raspberry pi imager](https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/).  Currently this is "Raspberry Pi OS (64 bit)" which is a port of "Debian Bookworm" released 2023-12-05.
1. Configuration as a rpi4 host requires:
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

1. Add wombat user group and minion account (for rsync(1))
    1. ```groupadd wombat```
    1. ```useradd -m -s /bin/bash minion```
    1. ```adduser minion wombat```
    1. from minion@housekeeper ```ssh-copy-id -i ~/.ssh/id_ed25519.pub rpi4d```

1. Create the export directory
    1. ```mkdir /var/mellow```
    1. ```chgrp wombat /var/mellow```
    1. ```chmod 775 /var/mellow```
    1. Each collection system needs a raw subdirectory under /var/mellow, i.e. "/var/mellow/hyena/raw" and should be readable from minion user group (for rsync(1) to copy).

## Debian Bookworm
1. [changes])(https://www.debian.org/releases/bookworm/amd64/release-notes/ch-information.en.html)
1. rsyslog is gone, replaced with journalctl (oh, this sucks...) journalctl -fe
1. nmcli is the latest sparkly network management tool
    1. https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/configuring-an-ethernet-connection_configuring-and-managing-networking
    1. ```nmcli c show```
    1. ```nmcli c modify preconfigured connection.id pogonip```
    1. ```nmcli c modify "Wired connection 1" connection.id "eth0"```
    1. ```nmcli c show eth0```
    1. ```nmcli c modify eth0 ipv4.method manual ipv4.addresses 10.168.1.81/18 ipv4.gateway 10.168.1.1 ipv4.dns '10.168.1.1,8.8.8.8' ipv4.dns-search braingang.net```
    1. ```reboot```
    1. ```ip address show eth0```
    1. ```ip route show default```

## Validation
1.  Can ping other hosts on local wombatnet (eth)
1.  Can obtain software updates via wombatnet (eth) and not via wifi
1.  Can build and execute librtlsdr, dump1090, etc.
1.  Can obtain from github and run applications like mellow-hyena, etc
1.  Collection results appear in /var/mellow/application/raw
1.  Collection output files have correct device
1.  rsync(8) from housekeeper is able to copy collection files (cron(8) in minion account)
1.  ansible ping from housekeeper works
1.  aws cli is able to write collection files to s3 via wombatnet (eth)

## Cleanup
1.  Update [inventory.md](https://github.com/guycole/mellow-wombat/blob/main/infra/inventory.md)

## Relevant Links
1. https://repost.aws/questions/QUHZgXbr_vTjqk8VNX-GLGzA/installing-aws-cli-v2-on-raspberry-pi-4b-with-raspbian-os