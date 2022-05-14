/*
 * Title:utility.c 
 * 
 * Overview/Description: wombat housekeeping status daemon 
 * 
 * Compiler/Operating System: 
 *   gcc version 8.3.0 (Debian 8.3.0-6)
 *   BeagleBoard.org Debian Buster IoT Image 2020-04-06 
 */
#include <stdio.h>
#include <string.h>

#include "wombatd.h"

const char *version_string2()
{
  char buffer[128];

  sprintf(buffer, "wombatd %d.%d compiled on %s at %s", VERSION_MAJOR_ID,
          VERSION_MINOR_ID, __DATE__, __TIME__);

  return strdup(buffer);
}
