# odroid n4 configuration
Each crate typically has one [odroid n4](https://www.hardkernel.com/shop/odroid-n2-with-4gbyte-ram-2/) as a wired ethernet (wombatnet) to wifi bridge.  Called the gateway it offers routing for collectors to get updates and a reverse proxy for mellow koala.

## Install Operating System On Thumb Drive
At the end of this step, there should be a bootable USB thumb drive with most of the debian packages needed for a successful wombat deployment.

1. Create an image using [balena etcher](https://github.com/balena-io/etcher) on a USB memory stick.  The current candidate is [Ubuntu Minimal 22.04.4 LTS (v4.9)](https://odroid.in/ubuntu_22.04lts/C4_HC4/ubuntu-22.04-4.9-minimal-odroid-c4-hc4-20220705.img.xz).

1. Verify by booting odroid n4 from USB memory stick.  Petitboot should discover the stick and boot to Ubuntu.  Ensure MMC/SPI slide switch is set to SPI.

## Configure WiFi and perform package maintenance
At the end of this step, the bootable USB thumb drive will have an updated Ubuntu and the packages needed for a happy wombat.

1. Install [WiFi Adapter](https://www.tp-link.com/us/home-networking/usb-adapter/archer-t2u-plus/) and verify using lsusb(8).  Configure WiFi device (wlan0) like this:

```
nmcli radio wifi on
nmcli dev wifi list
nmcli dev wifi connect "YOUR_SSID" password "YOUR_PASSWORD"
nmcli dev status
```

1. Once the WiFi is configured, update packages via apt-get(8) update/upgrade, then install debian packages for wombat.

```
apt-get update && upgrade -y
apt-get install -y atop build-essential emacs git postgresql tmux uuid-runtime
apt-get install -y cmake libusb-1.0-0-dev virtualenv

apt-add-repository --yes --update ppa:ansible/ansible
apt-get install -y ansible

apt-get install iptables-persistent
```

## Install debian mellow wombat package
This step installs the debian mellow wombat package, which creates the wombat user.

1. Install debian mellow wombat packages

```
(as root) wget -O - https://guycole.github.io/mellow-wombat/KEY.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/mellow-wombat.gpg > /dev/null
(as root) echo "deb [signed-by=/usr/share/keyrings/mellow-wombat.gpg] https://guycole.github.io/mellow-wombat ./" | tee /etc/apt/sources.list.d/mellow-wombat.list
apt update
apt install mellow-wombat
```

1. Create the GitHub key for access.  Each gateway needs a dedicated key.  Example is within wombat account.  Then clone the wombat github repository.

```
ssh-keygen -t ed25519 -C "guycole@gmail.com"
git clone git@github.com:guycole/mellow-wombat.git
```

## Configure for Masquerade and eth0/wlan0 bridge
At the end of this step, the wired collectors should have access to the outside world via gateway and IP Masquerade.  Note the internet consensus is to create a file for netplan (which did not work).  nmtui was a success.

1. Connect a wired collector via ethernet.  Should have a static IP to match wombatnet.

1. Update /etc/sysctl.conf

```
edit /etc/sysctl.conf
net.ipv4.ip_forward=1
sysctl -b
```

1. Masquerade rules
```
iptables -t nat -A POSTROUTING -o wlan0 -j MASQUERADE
iptables -A FORWARD -i wlan0 -o eth0 -m state --state RELATED,ESTABLISHED -j ACCEPT
iptables -A FORWARD -i eth0 -o wlan0 -j ACCEPT
netfilter-persistent save
```

```
iptables --list
Chain INPUT (policy ACCEPT)
target     prot opt source               destination         

Chain FORWARD (policy ACCEPT)
target     prot opt source               destination         
ACCEPT     all  --  anywhere             anywhere             state RELATED,ESTABLISHED
ACCEPT     all  --  anywhere             anywhere            

Chain OUTPUT (policy ACCEPT)
target     prot opt source               destination    
```

1. On a wired (ethernet) collector

```
route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.168.2.1      0.0.0.0         UG    100    0        0 eth0
10.168.2.1      0.0.0.0         255.255.255.255 UH    100    0        0 eth0
```

1. On a wired (ethernet) collector

```
ping -c 5 8.8.8.8
curl -v -L https://www.zapanote.com
```

## Checkpoint
At this point, the candidate wombat gateway should have

1. Boot from USB thumb drive
1. Access outside internet via WiFi
1. Freshly updated packages (including mellow-wombat)
1. IP Masquerade works from collectors on eth0

## Boot from USB Passport Drive
Prepare and move to a bootable USB Passport Drive

1. Insert the USB Passport drive, unmount any filesystems from the drive
1. Invoke the [passport-prep.sh](https://github.com/guycole/mellow-wombat/blob/main/bin/passport-prep.sh) script to partition and format drive
1. Insert the bootable USB thumb drive (from above), unmount any filesystems from the drive
1. Invoke the [odroid-n2.sh](https://github.com/guycole/mellow-wombat/blob/main/bin/odroid-n2.sh) script to copy from thumb drive to passport
1. Install the Passport drive on gateway n2 and verify boot



## START HERE


1. Install 50-cloud-init.yaml, then netplan apply


## xxxxxxx

1. Use the [passport-prep.sh](https://github.com/guycole/mellow-wombat/blob/main/bin/passport-prep.sh) script to partition the 4TB [Western Digital Passport USB Drive](https://www.westerndigital.com/products/portable-drives/wd-my-passport-usb-3-0-hdd?sku=WDBPKJ0040BBK-WESN).

1. Use the [odroid-n2.sh](https://github.com/guycole/mellow-wombat/blob/main/bin/odroid-n2.sh) script to copy from the USB memory stick to the passport drive.  When script completes, the passport drive should be bootable.  Remove memory stick and reboot to verify.

## Configure Operating System
1. At the end of this process, there should be WiFi connectivity and the mellow-wombat debian package installed.

1. Login as root/odroid.  

1. Configure WiFi using netplan
nmcli connection show



XXXXXXX start here XXXXXXXX

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
