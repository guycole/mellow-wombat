# rpi5 configuration
Each crate typically has one [raspberry pi 5](https://www.raspberrypi.com/products/raspberry-pi-5/) as a [housekeeper](https://github.com/guycole/mellow-wombat/blob/main/shelf/housekeeper.md).

## Initial Configuration Steps
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

## Debian Bookworm
1. [changes])(https://www.debian.org/releases/bookworm/amd64/release-notes/ch-information.en.html)
1. rsyslog is gone, replaced with journalctl (oh, this sucks...) journalctl -fe
1. nmcli is the latest sparkly network management tool
    1. https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/8/html/configuring_and_managing_networking/configuring-an-ethernet-connection_configuring-and-managing-networking
    1. ```nmcli c show```
    1. ```nmcli c modify preconfigured connection.id pogonip```
    1. ```nmcli c modify "Wired connection 1" connection.id "eth0"```
    1. ```nmcli c show wombat-net```
    1. ```nmcli connection modify eth0 ipv4.method manual ipv4.addresses 10.168.1.3/18 ipv4.gateway 10.168.1.1 ipv4.dns '10.168.1.1,8.8.8.8' ipv4.dns-search braingang.net```
    1. ```reboot```
    1. ```ip address show eth0```
    1. ```ip route show default```
1. Will not bridge
    1. https://gist.github.com/plembo/f7abd2d9b6f76e7afdece02dae7e5097

## mellow-net
1. I want simultaneous WiFi and wired ethernet w/IP forwarding.
1. I want access via WiFi and access via wired ethernet.
1. Shelf IP assignments in [housekeeper.md](https://github.com/guycole/mellow-wombat/blob/main/shelf/housekeeper.md)

## ansible
1. do not install via pip, use apt-get ansible
1. do not use ssh-copy-id/authorized keys

## postgresql
1. TBD

## prometheus
1. TBD
