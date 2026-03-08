#!/bin/bash
#
# Title: heeler_score.sh
# Description: daily boxscore of heeler stats
# Development Environment: Ubuntu 22.04.05 LTS
# Author: Guy Cole (guycole at gmail dot com)
#
PATH=/bin:/usr/bin:/etc:/usr/local/bin; export PATH
#
echo "start score"
#
docker rm heeler;docker run -e stuntbox=score --name heeler heeler:latest
#
echo "end score"
#
