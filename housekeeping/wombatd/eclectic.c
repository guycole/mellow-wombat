/*
 * Title:eclectic.c 
 *
 * Overview/Description: wombatd 
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

int eclectic(CONFIGURATION_PTR cp)
{
  printf("eclectic\n");
  printf("%s\n", cp->version_string);

  // test for GPS fix
  // test for GPS time sync
  // ensure power relays match
  // test door switches
  // collect temperature and humidity
  // collect acceleromters

  return (0);
}
