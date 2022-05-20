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

#include <signal.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <syslog.h>
#include <time.h>
#include <unistd.h>

extern int eclectic(CONFIGURATION_PTR configuration);

CONFIGURATION gConfiguration;

void usage(char *progname)
{
  fprintf(stderr, "usage: wombatd -f config_file\n");
  exit(0);
}

void setup()
{
  char buffer[64];
  int status;

  sprintf(buffer, "wombatd %d.%d compiled on %s at %s", VERSION_MAJOR_ID,
          VERSION_MINOR_ID, __DATE__, __TIME__);

  gConfiguration.configuration_filename = strdup(CONFIG_FILENAME);
  gConfiguration.lock_filename = strdup(LOCK_FILENAME);
  gConfiguration.version_string = strdup(buffer);

  openlog("wombatd", LOG_CONS | LOG_PID, LOG_LOCAL0);
  syslog(LOG_INFO, "%s", gConfiguration.version_string);

  timer_t timer_id = 0;

  status = timer_create(CLOCK_REALTIME, NULL, &timer_id);
  if (status != 0) {
    // TODO should be fatal
    fprintf(stderr, "timer create failure\n");
  }

  struct itimerspec timer_value;
  timer_value.it_value.tv_sec = TIMER_DELAY;
  timer_value.it_value.tv_nsec = 0;
  timer_value.it_interval.tv_sec = TIMER_DELAY;
  timer_value.it_interval.tv_nsec = 0;

  status = timer_settime(timer_id, TIMER_ABSTIME, &timer_value, NULL);
  if (status != 0) {
    // TODO should be fatal
    fprintf(stderr, "timer set failure\n");
  }

  printf("set status:%d\n", status);
}

void shutdown()
{
  free(gConfiguration.configuration_filename);
  free(gConfiguration.lock_filename);
  free(gConfiguration.version_string);

  syslog(LOG_INFO, "graceful exit");
  closelog();
}

void signal_handler(int signal)
{
  printf("inside handler:%d\n", signal);

  switch (signal) {
    case SIGALRM:              // poll for changes
      printf("alarm noted\n");
      int status = eclectic(&gConfiguration);
      // TODO bad status should be fatal
      printf("return status:%d\n", status);
      break;
    case SIGHUP:               // reset
      printf("sighup noted\n");
      break;
  }
}

int main(int argc, char *argv[])
{
  if(geteuid()!=0)
    fprintf(stderr, "must run as root user\n");
    return (WOMBAT_NOT_ROOT);
}

  signal(SIGALRM, signal_handler);
//  signal(SIGINT, signal_handler);
  signal(SIGHUP, signal_handler);

  setup();

  fprintf(stdout, "%s\n", gConfiguration.version_string);

  //TODO command line options
  //TODO assert lock
  //TODO demon

  for (int ndx = 0; ndx < 10; ndx++) {
    printf("%d\n", ndx);
    sleep(1);
  }

  shutdown();

  return (WOMBAT_OK);
}
