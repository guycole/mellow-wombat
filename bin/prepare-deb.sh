#!/bin/bash
#
# Title: prepare-deb.sh
# Description: prepare mellow wombat debian package
# Development Environment: ubuntu 22.04.5 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
cd /home/gsc/Documents/github/mellow-wombat
dpkg-deb --build mellow_wombat_package_1.0_all
dpkg-scanpackages --multiversion . > Packages
gzip -k -f Packages
apt-ftparchive release . > Release
gpg --default-key "guycole@gmail.com" -abs -o - Release > Release.gpg
gpg --default-key "guycole@gmail.com" --clearsign -o - Release > InRelease
