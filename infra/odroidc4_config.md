# odroid c4 configuration
Each crate typically has one [odroid c4](https://www.hardkernel.com/shop/odroid-c4/) as a wired ethernet to wifi bridge.  This is the gateway device for wombatnet.

## Configuration Steps
1. Create an image using the [balena etcher](https://github.com/balena-io/etcher).  Currently this is [Ubuntu Minimal 20.04.4 LTS (v1.5)](https://wiki.odroid.com/odroid-c4/os_images/ubuntu/minimal/20220228).

1. Configuration as a gateway requires:
    1.  Create a [netplan](fixme) file to configure network interfaces wlan0 and eth0.
        1. wombatnet will expect gateway to be at 10.168.x.1 where 'x' is crate number.
    1.  Update the hostname to reflect the crate
        1.  ```hostnamectl set-hostname crate01```
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

## Hardware
+ [ODROID-C4](https://www.hardkernel.com/shop/odroid-c4/)
+ [USB WiFi](https://www.hardkernel.com/shop/wifi-module-5bk/)
+ [12V2A Wall Wart](https://www.hardkernel.com/shop/12v-2a-power-supply-us-plug/)
