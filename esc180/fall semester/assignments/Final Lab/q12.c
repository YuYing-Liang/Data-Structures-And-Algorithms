/*Question 12*/
#include <stdlib.h>
struct data{
	int valid;
	int value;
	int frequency;
};

typedef struct data data;

int histogram(int *n, data *m, int s);

int histogram(int *n, data *m, int s){
	int i = 0; int nextNonZeroVal = -1;
	int x = 0;
	
	if(m == NULL || n == NULL || s < 1){ return -1;}
	
	/*check for frequencies of zeros first*/ 
	m[x].value = 0;
	for(i = 0; i < s; i++){
		if(n[i] == 0){
			m[x].frequency += 1;
		}else if(nextNonZeroVal == -1){
			nextNonZeroVal = i;
		}
	}
	if(m[x].frequency != 0) { x++; }
	
	while(1){
		m[x].value = n[nextNonZeroVal];
		nextNonZeroVal = -1;
		for(i = nextNonZeroVal; i < s; i++){
			if(n[i] == 0){
				m[x].frequency += 1;
				n[i] = 0;
			}else if(nextNonZeroVal == -1){
				nextNonZeroVal = i;
			}
		}
		if(nextNonZeroVal == -1) {break;}
	}
	
	return 0;
}
	
