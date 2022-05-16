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
INCDIR = $(DEVDIR)/include
LIBDIR = $(DEVDIR)/lib

#
# Header Files.
#
WOMBATD_H = wombatd.h

#
# Libraries.
#

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
LATEX = latex

#
# Executable Names.
#
WOMBATD = wombatd

#
# Object Files.
#
OBJS = eclectic.o main.o utility.o

#
# Finally, some work...
#
all: $(WOMBATD)

$(WOMBATD): $(OBJS)
	$(CC) -o $(WOMBATD) $(OBJS) -lrt

eclectic.o: eclectic.c $(WOMBATD_H)
	$(CC) -c $(CFLAGS) $(CMACS) eclectic.c

main.o: main.c $(WOMBATD_H)
	$(CC) -c $(CFLAGS) $(CMACS) main.c

utility.o: utility.c $(WOMBATD_H)
	$(CC) -c $(CFLAGS) $(CMACS) utility.c

#
#  Format all the source files.
#
.PHONY: indent
indent:
	-indent $(WOMBATD_H)
	-indent eclectic.c
	-indent main.c
	-indent utility.c

#
#  Update the TAGS file.
#
.PHONY: tags
tags:
	-@etags *.cc

#
#  Determine the size of source files in this subdirectory.
#
.PHONY: size
size:
	-@echo "Size: `pwd`"
	-@wc -l *.c makefile

#
#  Generate dependency file
#
.PHONY: depend
depend:
	-@rm ./depend.include
	$(CC) $(DEPEND_FLAG) $(CPPFLAGS) *.cc > ./depend.include

#
#  Cleanup this subdirectory.
#
.PHONY: clean
clean:
	-@rm -f *.o *.BAK core

#
#  Nuke all the executables.
#
.PHONY ultraclean:
ultraclean:
	-@rm -f *~ $(WOMBATD)
