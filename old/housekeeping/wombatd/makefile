#
# Title:makefile
#
# Description: wombatd makefile
#   'make indent' to format source files.
#   'make size' returns the quantity of lines in this directory
#   'make clean' removes all core and object files
#   'make ultraclean' removes all executables
#
# Operating System/Environment:
#   BeagleBoard.org Debian Buster IoT Image 2020-04-06
#   GNU Make 4.21
#
# Directories.
#
DEVDIR = $(HOME)

#
# Header Files.
#
BEAGLEBONE_H = beaglebone.h
WOMBATD_H = wombatd.h

#
# Configurations.
#
CMACS  = -DTRACE=1
CFLAGS = -g -Wall -I$(INCDIR)

#
# Tools.
#
CC = gcc
INDENT = indent

#
# Executable Names.
#
WOMBATD = wombatd

#
# Source Files.
#
SRCS = beaglebone.c eclectic.c main.c 

#
# Object Files.
#
OBJS = beaglebone.o eclectic.o main.o 

#
# Finally, some work...
#
all: $(WOMBATD)

$(WOMBATD): $(OBJS)
	$(CC) -o $(WOMBATD) $(OBJS) -lrt

beaglebone.o: beaglebone.c $(BEAGLEBONE_H)
	$(CC) -c $(CFLAGS) $(CMACS) beaglebone.c

eclectic.o: eclectic.c $(BEAGLEBONE_H) $(WOMBATD_H)
	$(CC) -c $(CFLAGS) $(CMACS) eclectic.c

main.o: main.c $(WOMBATD_H)
	$(CC) -c $(CFLAGS) $(CMACS) main.c

#
#  Format all the source files.
#
.PHONY: indent
indent:
	-indent $(BEAGLEBONE_H) $(WOMBATD_H) $(SRCS)

#
#  Determine the size of source files in this subdirectory.
#
.PHONY: size
size:
	-@echo "Size: `pwd`"
	-@wc -l *.c makefile

#
#  Cleanup this subdirectory.
#
.PHONY: clean
clean:
	-@rm -f *.o *.BAK core

#
#  Nuke all the executables.
#
.PHONY: ultraclean
ultraclean:
	-@rm -f *~ $(WOMBATD)
