odroid c4 for wifi gateway

debian 20.04 Focal Fossa

must update rc.local
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

Debian 20.04 Focal Fossa

## Hardware
+ [ODROID-C4](https://www.hardkernel.com/shop/odroid-c4/)
+ [USB WiFi](https://www.hardkernel.com/shop/wifi-module-5bk/)
+ [12V2A Wall Wart](https://www.hardkernel.com/shop/12v-2a-power-supply-us-plug/)

