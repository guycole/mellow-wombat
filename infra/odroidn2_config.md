# Odroid n4
Each crate typically has one [odroid n4](https://www.hardkernel.com/shop/odroid-n2-with-4gbyte-ram-2/) as a wired ethernet (wombatnet) to wifi bridge.  Called the gateway and it offers services like NTP, GPS, logging, network routing, etc for SBC ("collectors") within the crate.

## Provisioning Overview
Provisioning starts w/a USB memory stick (at least 8GB) which is loaded with [Ubuntu Minimal 22.04.4 LTS (v4.9)](https://odroid.in/ubuntu_22.04lts/N2/ubuntu-22.04-4.9-minimal-odroid-n2-20220622.img.xz).  After the generic packages have been installed and configured, the memory stick is copied to larger USB Passport drives which will be the bootable storage for each gateway host.

Put another way: the memory stick is generic and the passport drives are specific to each host.  Provisioning begins w/loading the USB memory stick.

### Install Operating System On Memory Stick
At the end of this step, the n4 should have booted from USB memory stick.

1. Using [balena etcher](https://github.com/balena-io/etcher) copy [Ubuntu Minimal 22.04.4 LTS (v4.9)](https://odroid.in/ubuntu_22.04lts/N2/ubuntu-22.04-4.9-minimal-odroid-n2-20220622.img.xz) to the USB memory stick.

1. Verify copy by booting odroid n4 from USB memory stick.  With the candidate powered off, ensure MMC/SPI slide switch is set to SPI and insert the USB memory stick.  Power the n4 on and petitboot should boot to Ubuntu.

### Configure WiFi and perform package maintenance
For this step, enable WiFi and start updating/installing packages.

1. Install [WiFi Adapter](https://www.tp-link.com/us/home-networking/usb-adapter/archer-t2u-plus/) and verify using lsusb(8).  Configure WiFi device (wlan0) like this:

```
nmcli radio wifi on
nmcli dev wifi list
nmcli dev wifi connect "YOUR_SSID" password "YOUR_PASSWORD"
nmcli dev status
```

1. Once the WiFi is configured, update packages via apt-get(8) update/upgrade, then install debian packages for wombat.

```
apt-get update && apt-get upgrade -y
apt-get install -y atop build-essential emacs git postgresql tmux uuid-runtime
apt-get install -y awscli cmake libusb-1.0-0-dev virtualenv

apt-add-repository --yes --update ppa:ansible/ansible
apt-get install -y ansible

apt-get install iptables-persistent
```

## Configure Gateway Loghost
Gateway acts as loghost for the crate

```
mkdir /var/log/wombat
chown syslog:adm /var/log/wombat
copy 13-wombatnet.conf /etc/rsyslog.d
systemctl restart rsyslog
iptables -A INPUT -p udp --dport 514 -j ACCEPT
iptables -A INPUT -p tcp --dport 514 -j ACCEPT
netfilter-persistent save
```

### Install docker
Install and test docker

```
curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /etc/apt/keyrings/docker.gpg
chmod a+r /etc/apt/keyrings/docker.gpg

echo "deb [arch=arm64 signed-by=/etc/apt/keyrings/docker.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

apt-get update

apt-get -y install docker-ce docker-ce-cli containerd.io docker-buildx-plugin docker-compose-plugin
(reboot to start docker.service)
docker run hello-world
```

### Configure for IP Masquerade and eth0/wlan0 bridge
At the end of this step, the wired collectors should have access to the outside world via gateway and IP Masquerade.  Note the internet consensus is to create a file for netplan (which did not work).  nmtui was a success.

1. Define hostname (using nmtui)

1. Connect a wired collector via ethernet.  Should have a static IP to match wombatnet (each crate has a subnet).

1. Update /etc/sysctl.conf

```
edit /etc/sysctl.conf
net.ipv4.ip_forward=1
sysctl -p /etc/sysctl.conf
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

```
ping -c 5 8.8.8.8
curl -v -L https://www.zapanote.com
```

Must Also test logging

## Checkpoint
At this point, the candidate wombat gateway should have

1. Boot from USB thumb drive
1. Access outside internet via WiFi
1. Freshly updated packages (including mellow-wombat)
1. IP Masquerade works from collectors on eth0
1. Remote loggingd

## Boot from USB Passport Drive
Prepare and move to a bootable USB Passport Drive

1. Insert the USB Passport drive, unmount any filesystems from the drive
1. Invoke the [passport-prep.sh](https://github.com/guycole/mellow-wombat/blob/main/bin/passport-prep.sh) script to partition and format drive
1. Insert the bootable USB thumb drive (from above), unmount any filesystems from the drive
1. Invoke the [odroid-n2.sh](https://github.com/guycole/mellow-wombat/blob/main/bin/odroid-n2.sh) script to copy from thumb drive to passport
1. Install the Passport drive on gateway n2 and verify boot

## Install debian mellow wombat package
This step installs the debian mellow wombat package, which creates the wombat user.

1. Install debian mellow wombat packages

```
(as root) wget -O - https://guycole.github.io/mellow-wombat/KEY.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/mellow-wombat.gpg > /dev/null
(as root) echo "deb [signed-by=/usr/share/keyrings/mellow-wombat.gpg] https://guycole.github.io/mellow-wombat ./" | tee /etc/apt/sources.list.d/mellow-wombat.list
apt update
apt install mellow-wombat
usermod -aG docker wombat
```

## Wombat Account Setup
When the "mellow-wombat" package was installed, the "wombat" user account was created.  The "wombat" account is used for running wombat jobs, managing the collectors via ansible, etc.

1. Create the GitHub key for access.  Each gateway needs a dedicated key, login as wombat, create the key and add to GitHub.  Then clone the mellow-wombat repo.
```
ssh-keygen -t ed25519 -C "guycole@gmail.com"
git clone git@github.com:guycole/mellow-wombat.git
```

1. Configure AWS account.  Each gateway has a dedicated AWS key.

## Prepare Ansible
The gateway is also an ansible control node for the collectors in this crate.

need syslog config