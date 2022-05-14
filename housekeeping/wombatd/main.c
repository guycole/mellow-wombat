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
#include <unistd.h>

extern const char *version_string();

void usage(char *progname)
{
  fprintf(stderr, "usage: wombatd -f config_file\n");
  exit(0);
}

CONFIGURATION_PTR prepare_configuration()
{
  char buffer[64];
  sprintf(buffer, "wombatd %d.%d compiled on %s at %s", VERSION_MAJOR_ID,
          VERSION_MINOR_ID, __DATE__, __TIME__);

  CONFIGURATION_PTR cp = (CONFIGURATION_PTR) malloc(sizeof(CONFIGURATION));
  cp->configuration_filename = CONFIG_FILENAME;
  cp->lock_filename = LOCK_FILENAME;
  cp->version_string = strdup(buffer);

  return (cp);
}

extern int eclectic(void);

int main(int argc, char *argv[])
{
  CONFIGURATION_PTR config = prepare_configuration();
  fprintf(stdout, "%s\n", config->version_string);
  openlog("wombatd", LOG_CONS | LOG_PID, LOG_LOCAL0);
  syslog(LOG_INFO, config->version_string);

  int status = eclectic();
  printf("return status:%d\n", status);

  syslog(LOG_INFO, "graceful exit");
  closelog();
}
