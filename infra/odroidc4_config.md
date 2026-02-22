# Odroid c4 Configuration
The [odroid c4](https://www.hardkernel.com/shop/odroid-c4/) is a SBC used by mellow as a collector.  Configuration means a bootable SBC which routes through a gateway and can update debian packages.  There should be a user account "wombat" which will be used by ansible.  All wombatnet hosts have static IP addresses.

## Configuration Steps
At the end of this step, the collector will be provisioned with a static IP address and a wombat account.

### Install Operating System On MicroSD card
1. Create an image using [balena etcher](https://github.com/balena-io/etcher) on a micro SD card.  The current candidate is [Ubuntu Minimal 22.04.4 LTS (v4.9)](https://odroid.in/ubuntu_22.04lts/C4_HC4/ubuntu-22.04-4.9-minimal-odroid-c4-hc4-20220705.img.xz), which fits on a 8GB card.

1. Connect HDMI, USB keyboard, ethernet cable and boot for verification and configuration.

### Booted Collector
Now that the collector boots, start w/network configuration.  At the end of this step there should be connectivity through the gateway to the outside world.

1. Update the hostname
```
hostnamectl set-hostname new-hostname
edit /etc/hosts like this 127.0.1.1 wombat02
```

1. Copy the [13-wombatnet.yaml](https://github.com/guycole/mellow-wombat/blob/main/infra/etc/netplan/13-wombatnet.yaml) file to /etc/netplan and tweak for network (i.e. static IP address and gateway).

1. Reboot and verify routing 

```
route -n
Kernel IP routing table
Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
0.0.0.0         10.168.2.1      0.0.0.0         UG    100    0        0 eth0
10.168.0.0      0.0.0.0         255.255.192.0   U     100    0        0 eth0
```

```
ping -c 5 8.8.8.8
curl -v -L https://www.zapanote.com
```

1. Copy the [13-remote](https://github.com/guycole/mellow-wombat/blob/main/infra/etc/rsyslog.d/13-remote.conf) file to /etc/rsyslog.d and tweak gateway reference)

### Update Packages
Update Debian and Mellow Package

```
apt-get update && apt-get upgrade -y
apt-get install -y atop build-essential git rsyslog tmux uuid-runtime
apt-get install -y cmake libusb-1.0-0-dev virtualenv
```

```
wget -O - https://guycole.github.io/mellow-wombat/KEY.gpg | gpg --dearmor | sudo tee /usr/share/keyrings/mellow-wombat.gpg > /dev/null
echo "deb [signed-by=/usr/share/keyrings/mellow-wombat.gpg] https://guycole.github.io/mellow-wombat ./" | tee /etc/apt/sources.list.d/mellow-wombat.list
apt-get update
apt-get install mellow-wombat
```

### Configure Wombat User Account
From the gateway, copy ssh key (example)
```
ssh-copy-id wombat@10.168.2.101
```

### Ansible Test
Invoke ping-crate.sh for the target crate
