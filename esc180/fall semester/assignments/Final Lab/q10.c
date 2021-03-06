/*Question 10*/
#include <stdlib.h>
int nsum(float *a, float *b, int n, float **output);

int nsum(float *a, float *b, int n, float **output){
	int i = 0;
	
	if(output == NULL || a == NULL || b == NULL || n < 1){ return -1; }
	
	(*output) = (float *) malloc(sizeof(float) * n);
	
	if((*output) == NULL) { return -1; }
	
	for(i = 0; i < n; i++){
		(*output)[i] = a[i] + b[i];
	}
	
	return 0;
}
