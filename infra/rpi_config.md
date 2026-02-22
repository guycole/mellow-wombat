# rpi configuration
The raspberry pi is used as a collector host.  Depening on the crate these can by rpi3, rpi4 or rpi5 devices.  Since these are collectors, they all run headless and use the "minimal IoT" image.  All hosts on wombatnet use static IP addresses.  No rpi hosts have bluetooth or wifi enabled.

## Configuration Steps
1. Create an image using the [raspberry pi imager](https://www.raspberrypi.com/news/raspberry-pi-imager-imaging-utility/).  For the rpi3 this will be a 32 bit image, otherwise "2025-12-04 64 bit rPi OS Lite (Debian Trixie)"

1. The fresh image will not be configured for anything but a user account.  You will need a keyboard/mouse and monitor to finish configuration. 

1. Invoke the "nmtui" utility and define a hostname and other eth0 attributes like static IP, gateway, etc.  Check /etc/hosts to ensure the hostname is present.
```
127.0.1.1	wombat02
``` 

1. Ensure sshd starts at boot
```
systemctl enable ssh.service
```

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