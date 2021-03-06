/*Question 8b)*/
#include <stdlib.h>
#include "q8_a.c"
int integrate(poly *term);

int integrate(poly *term){
	int n = term -> size;
	int i = 0;
	
	if(term == NULL){ return -1; }
	if(term -> size < 1){ return -1; }
	
	for(i = 0; i < n; i++){
		(term -> exp)[i] += 1;
		(term -> coeff)[i] = (term -> coeff)[i] / ((float) (term -> exp)[i]);
	}
	
	return 0;
}
