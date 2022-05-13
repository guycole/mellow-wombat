/*
 * Title:main.c 
 *
 * Overview/Description: wombat housekeeping status daemon
 *
 * Compiler/Operating System:
 *   gcc version 8.3.0 (Debian 8.3.0-6)
 *   BeagleBoard.org Debian Buster IoT Image 2020-04-06
 */

#include "wombatd.h"

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <syslog.h>

extern const char *version_string();

void usage(char *progname)
{
  fprintf(stderr, "usage: %s sound_directory\n", progname);
  exit(0);
}

int main(int argc, char *argv[])
{
  printf("%s\n", version_string());

  openlog("wombatd", LOG_CONS | LOG_PID, LOG_LOCAL0);
  syslog(LOG_ERR, "woot woot");
  closelog();
}
