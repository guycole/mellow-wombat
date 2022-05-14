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
  fprintf(stderr, "usage: wombatd -f config_file\n");
  exit(0);
}

const char *get_version_string()
{
  char buffer[64];

  sprintf(buffer, "wombatd %d.%d compiled on %s at %s", VERSION_MAJOR_ID, VERSION_MINOR_ID, __DATE__, __TIME__);

  return strdup(buffer);
}

int main(int argc, char *argv[])
{
  char *version_string = get_version_string(); 
  fprintf(stdout, "%s\n", version_string;
  openlog("wombatd", LOG_CONS|LOG_PID, LOG_LOCAL0);
  syslog(LOG_INFO, version_string);
  free(version_string);

  int run_flag = 0;
  while(run_flag) {
	  print("run flag true");
	  sleep(5);
  }

  syslog(LOG_INFO, "graceful exit");
  closelog();
}
