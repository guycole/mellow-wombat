# odroid c4 configuration
Each crate typically has one [odroid c4](https://www.hardkernel.com/shop/odroid-c4/) as a wired ethernet to wifi bridge.  This is the gateway device for wombatnet, and offers a reverse proxy for mellow wombat.

## Configuration Steps
1. Create an image using the [balena etcher](https://github.com/balena-io/etcher).  Currently this is [Ubuntu Minimal 20.04.4 LTS (v1.5)](https://wiki.odroid.com/odroid-c4/os_images/ubuntu/minimal/20220228).

1. Configuration as a gateway requires:
    1.  Create a [/etc/netplan file](https://github.com/guycole/mellow-wombat/blob/main/infra/50-cloud-init.yaml) file to configure network interfaces wlan0 and eth0.
        1. wombatnet will expect gateway to be at 10.168.x.1 where 'x' is crate number.
    1.  Update the hostname to reflect the crate
        1.  ```hostnamectl set-hostname wombat01```
    1.  Update /etc.rc.local to configure ip masquerade at boot.
```
#
ip route show
#
echo 1 > /proc/sys/net/ipv4/ip_forward
#
iptables --list
#
# IP masqurade 
iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
```        

## Nginx Reverse Proxy

## Hardware
1. [ODROID-C4](https://www.hardkernel.com/shop/odroid-c4/)
1. [USB WiFi](https://www.hardkernel.com/shop/wifi-module-5bk/)
1. [12V2A Wall Wart](https://www.hardkernel.com/shop/12v-2a-power-supply-us-plug/)

## Relevant Links
1. https://linuxconfig.org/ubuntu-20-04-connect-to-wifi-from-command-line
1. https://www.digitalocean.com/community/tutorials/how-to-configure-nginx-as-a-reverse-proxy-on-ubuntu-22-04
