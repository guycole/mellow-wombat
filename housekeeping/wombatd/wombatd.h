/*
 * Title:wombatd.h 
 *
 * Overview/Description: wombat housekeeping status daemon 
 *
 * Compiler/Operating System: 
 *   gcc version 8.3.0 (Debian 8.3.0-6)   
 *   BeagleBoard.org Debian Buster IoT Image 2020-04-06    
 */
#ifndef __WOMBAT_DAEMON
#define __WOMBAT_DAEMON

#define VERSION_MAJOR_ID 0
#define VERSION_MINOR_ID 0

#define CONFIG_FILENAME "/etc/wombatd"
#define LOCK_FILENAME "/var/lock/wombatd"
#define VERSION_STRING "wombatd"

#define WOMBAT_OK 0
#define WOMBAT_WIPE -1
#define WOMBAT_MISSING_CONFIG -2
#define GPS_SHMEM_FAILURE -3
#define GPS_NO_FIX -4
#define GPS_TIME_DELTA -5
#define TEMPERATURE_MISSING -6
#define HUMIDITY_MISSING -7
#define DOOR_0_EVENT -100
#define DOOR_1_EVENT -101

#define TIMER_DELAY 1

/*
 * boolean definitions
 */
typedef enum {
  FALSE, TRUE
} BOOLEAN;

/*
 * power relay status
 */
#define MAX_POWER_PINS 8
typedef BOOLEAN POWER_ARRAY[MAX_POWER_PINS];

/*
 * wombatd configuration
 */
typedef struct configuration_struct {
  char *configuration_filename;
  char *lock_filename;
  char *version_string;
  POWER_ARRAY power_array;
} CONFIGURATION, *CONFIGURATION_PTR;

#endif
