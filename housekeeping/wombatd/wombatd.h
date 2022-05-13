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

#define LOCK_FILE "/var/lock/wombatd"
#define VERSION_STRING "wombatd"

#define WOMBAT_OK 0
#define WOMBAT_MISSING_CONFIG -1
#define GPS_SHMEM_FAILURE -2
#define GPS_NO_FIX -3
#define GPS_TIME_DELTA -4

#endif
