#
# Title:makefile
#
# Description:
#
#   'make size' returns the quantity of lines in this directory
#   'make clean' removes all core and object files
#   'make ultraclean' removes all executables
#
# Operating System/Environment:
#   BeagleBoard.org Debian Buster IoT Image 2020-04-06
#   GNU Make 4.21
#
#
# Directories.
#
DEVDIR = $(HOME)
INCDIR = $(DEVDIR)/include
LIBDIR = $(DEVDIR)/lib

#
# Header Files.
#

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

#
# Object Files.
#
OBJS =

#
# Finally, some work...
#
all:

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
	-@wc -l *.cc makefile

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
	-@rm -f *~
