/*
** Title:main.c
**
** Overview/Description:
**    nonseq ("non-sequitur") randomly picks a sound file from
**    the specified directory and plays it.
**
** Compiler/Operating System:
**    SunOS 4.1.3 (sun4c)
**    GNU gcc 2.5.8
*/
static char rcsid[] = "$Id: main.c,v 1.1 1997-12-15 08:44:26 gsc Exp $";

#include "nonseq.h"

#include <stdio.h>
#include <string.h>

void usage(char *progname);

extern int getpid();
extern int execv();
extern int fprintf();
extern int random(void);
extern void srandom(int seed);

int main(int argc, char *argv[])
{
	char *argz[3];

	char *cndx1;
	int list_length;
	int ndx;
	int target;
	FILENAMEZ_PTR root;

	srandom(getpid());

	if (argc < 2) {
		usage(argv[0]);
	}

	candidates(argv[1], &root, &list_length);

	if (list_length == 0) {
		fprintf(stderr, "No Sound Files Noted:%s\n", argv[1]);
		exit(-1);
	}

	/*
	* Attempt to improve random() diversity
	*/
	for (ndx = 0, target = random() % list_length; ndx < target; ndx++)
		random();
	
	target = random() % list_length;

	for (ndx = 0; ndx < target; ndx++)
		root = root->next;

	if ((cndx1 = strrchr(DEFAULT_PLAY, '/')) != (char *) NULL) {
		cndx1++;
		argz[0] = strdup(cndx1);
	}
	else {
		argz[0] = strdup(DEFAULT_PLAY);
	}

	argz[1] = strdup(root->name);
	argz[2] = (char *) NULL;

	execv(DEFAULT_PLAY, argz);
	return (0);
}

void usage(char *progname)
{
	fprintf(stderr, "usage: %s sound_directory\n", progname);
	exit(0);
}
