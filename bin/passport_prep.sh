#!/bin/bash
#
# Title: passport_prep.sh
# Description: prepare a 4TB passport drive for wombat gateway
# Development Environment: 
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
mkfs_ext4="/usr/sbin/mkfs.ext4"
mkfs_vfat="/usr/bin/mkfs.vfat"
sfdisk="/usr/sbin/sfdisk"
#
device_src="/dev/sda"
boot_src="/dev/sda1" # vfat
root_src="/dev/sda2" # ext4
device_dst="/dev/sdb"
boot_dst="/dev/sdb1" # vfat
root_dst="/dev/sdb2" # ext4
#
echo "start passport preparation"
#
$sfdisk $device_dst <<'EOF'
label: gpt
size=256M, type=uefi
type=linux
EOF
#
$sfdisk --part-label $device_dst 1 EFI
$sfdisk --part-label $device_dst 2 ROOT
#
$mkfs_vfat -F32 -n EFI $boot_dst
$mkfs_ext4 -L ROOT $root_dst
#
echo "end passport preparation"
#