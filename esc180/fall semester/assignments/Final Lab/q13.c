/*Question 13*/
#include <stdlib.h>
#include "q12.c"
int getmode(data *m, int mode, int s){
	int i = 0;
	int largest = -1;
	
	if(m == NULL || s < 1) { return -1; }
	
	for(i = 0; i < s; i++){
		if(m[i].frequency > largest){
			largest = m[i].frequency;
		}
	}
	mode = largest;
	return 0;
}
