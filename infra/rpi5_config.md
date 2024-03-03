# rpi5 configuration
Each crate typically has one [raspberry pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) as a [housekeeper](https://github.com/guycole/mellow-wombat/blob/main/shelf/housekeeper.md).

## Configuration Steps
1. Create an image using the [raspberry pi imager](https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/).  Currently this is "Raspberry Pi OS (64 bit)" which is a port of "Debian Bookworm" released 2023-12-05.
1. Configuration as a housekeeper requires:
    1.  SSH enabled (because housekeeper is usually headless).
        1. Do this as part of creating the image
    1.  WiFi enabled (because housekeeper provides WiFi bridge).
        1. Associate a WAP as part of creating the image.
    1.  Create a user account.
        1. Via image creation.
    1.  Wired ethernet enabled (for mellow-net).
        1. After image creation.
    1.  Add applications
        1. After image creation.

1. Add wombat user group and minion account (for rsync(1))
    1. ```groupadd wombat```
    1. ```useradd -m -s /bin/bash minion```
    1. ```adduser minion wombat```
    1. create empty ssh key so rsyn(1) can copy files without a password
        1. ```ssh-keygen -t ed25519 -C "minion@braingang.net"```

1. Add ansible
    1. apt-get install ansible
    1. apt-get install sshpass

1. Add prometheus
    1. apt-get install prometheus

1. Add postgres
    1. apt-get install postgresql-all

1. Python
    1. apt-get install virtualenv
    1. apt-get install gunicorn

## Debian Bookworm
1. [changes])(https://www.debian.org/releases/bookworm/amd64/release-notes/ch-information.en.html)
1. rsyslog is gone, replaced with journalctl (oh, this sucks...) journalctl -fe
1. nmcli is the latest sparkly network management tool
    1. https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/configuring-an-ethernet-connection_configuring-and-managing-networking
    1. ```nmcli c show```
    1. ```nmcli c modify preconfigured connection.id pogonip```
    1. ```nmcli c modify "Wired connection 1" connection.id "eth0"```
    1. ```nmcli c show eth0```
    1. ```nmcli c modify eth0 ipv4.method manual ipv4.addresses 10.168.1.7/18 ipv4.gateway 10.168.1.1 ipv4.dns '10.168.1.1,8.8.8.8' ipv4.dns-search braingang.net```
    1. ```reboot```
    1. ```ip address show eth0```
    1. ```ip route show default```
1. Will not bridge (this does not work)
    1. https://gist.github.com/plembo/f7abd2d9b6f76e7afdece02dae7e5097

## mellow-net
1. Shelf IP assignments in [housekeeper.md](https://github.com/guycole/mellow-wombat/blob/main/shelf/housekeeper.md)

## ansible
1. do not install via pip
    1. apt-get install ansible
    1. apt-get install sshpass
1. do not use ssh-copy-id/authorized keys
1. ```ansible --version```
    ```ansible [core 2.14.3]```

## postgresql
1. apt-get postgresql-all (postgresql 15)
    1. ```PostgreSQL 15.6 (Debian 15.6-0+deb12u1) on aarch64-unknown-linux-gnu, compiled by gcc (Debian 12.2.0-14) 12.2.0, 64-bit```

1. schema creation from django

## prometheus (v2.42.0)
1. apt-get install prometheus

## rsync
1. rsync(1) to copy files from collection shelves to housekeeper
    1. cron(8) from minion account 
    1. /var/mellow (source and destination, must be wombat group)

## Validation
1.  Can ping other hosts on local wombatnet (eth)
1.  Can obtain software updates via wombatnet (eth) and not via wifi
1.  Can obtain from github and run applications like mellow-hyena, etc
1.  Collection results appear in /var/mellow/application/raw
    1. minion crontab invokes rsync(1) every minute
1.  ansible ping works
1.  psql (postgresql) works
1.  prometheus collects node activity
1.  django renders, plays nice with postgresql

## Cleanup
1.  Update [inventory.md](https://github.com/guycole/mellow-wombat/blob/main/infra/inventory.md)

## Relevant Links
1. https://repost.aws/questions/QUHZgXbr_vTjqk8VNX-GLGzA/installing-aws-cli-v2-on-raspberry-pi-4b-with-raspbian-os
