#!/bin/bash
#
# Title: gateway_copy.sh
# Description: odroid n2 file system load
# Development Environment: 
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
chroot="/usr/sbin/chroot"
mkdir="/usr/bin/mkdir"
mount="/usr/bin/mount"
rsync="/usr/bin/rsync"
uuidgen="/usr/bin/uuidgen"
#
device_src="/dev/sda"
boot_src="/dev/sda1" # vfat
root_src="/dev/sda2" # ext4
device_dst="/dev/sdb"
boot_dst="/dev/sdb1" # vfat
boot_dst_uuid="fixme"
root_dst="/dev/sdb2" # ext4
root_dst_uuid="fixme"
#
echo "start gateway copy"
#
$mount $root_src /mnt/source
$mount $root_dst /mnt/target
#
$mkdir -p /mnt/target/boot
$mount $boot_dst /mnt/target/boot
#
$mkdir -p /mnt/source/boot
$mount -o ro $boot_src /mnt/source/boot
#
$rsync -aAXH --numeric-ids --exclude={"/dev/*","/proc/*","/sys/*","/tmp/*","/run/*","/mnt/*","/media/*","/lost+found"} /mnt/source/ /mnt/target/
#
$rsync -aHv /mnt/source/boot/ /mnt/target/boot/
#
# fix fstab
#
echo "end gateway copy"
#