/*
** Title:wombatd.h
**
** Overview/Description:
**
** Compiler/Operating System:
**    SunOS 4.1.3 (sun4c)
**    GNU gcc 2.5.8
*/

#define DEFAULT_PLAY "/usr/demo/SOUND/play"

typedef struct filenamez {
	char *name;
	struct filenamez *next;
} FILENAMEZ, *FILENAMEZ_PTR;

extern void candidates(char *path, FILENAMEZ_PTR *root, int *count);
