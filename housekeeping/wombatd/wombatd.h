/*
** Title:wombatd.h
**
** Overview/Description: wombat housekeeping status daemon
**
** Compiler/Operating System:
**    BeagleBoard.org Debian Buster IoT Image 2020-04-06
**    gcc version 8.3.0 (Debian 8.3.0-6) 
*/

#define DEFAULT_PLAY "/usr/demo/SOUND/play"

typedef struct filenamez {
	char *name;
	struct filenamez *next;
} FILENAMEZ, *FILENAMEZ_PTR;

extern void candidates(char *path, FILENAMEZ_PTR *root, int *count);
