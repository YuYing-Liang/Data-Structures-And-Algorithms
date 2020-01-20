/*Question Five*/
#include <stdlib.h>
int g(char *array, int n);

int g(char *array, int n){
	if(array == NULL){ return -1;}
	array = (char *)malloc(n * sizeof(char));
	return 0;
}

