#include <stdio.h>
#include <stdlib.h>
#include "ge.c"

int print(float *matrix, int rows, int cols);

int main(void){
	
	int rows = 3, cols = 4;
	float *m = NULL, *n = NULL;	/* init value */
	/*Also tested with static arrays*/
/* 	float m[12] = {2.0, 3.0, 4.0,5.0, 0.0, 0.0, 5.0, 0.0, 4.0, 5.0, 7.0, 9.0};
 *	float n[12];*/
	int r = 0, c = 0;
	int rval = 0;
	float idx = 0.0;
	
	/*getting the row and column values from the user*/

	printf("How many rows? ");
	scanf("%d", &rows);
	printf("How many cols? ");
	scanf("%d", &cols);


	/*dynamically allocates matrices m and n*/

	m = (float *)malloc(sizeof(float)*rows*cols);
	if(m == NULL){
		printf("ERR: unable to allocate array m\n");
		return -1;
 	}
	
	n = (float *)malloc(sizeof(float)*rows*cols);
	if(n == NULL){
		printf("ERR: unable to allocate array n\n");
		return -1;
	}

	/*assigns values*/

	for(r = 0; r < rows; r++){
		for(c = 0; c < cols; c++){
			m[r*cols +c] = idx;
			idx++;
		}
	}	

	
	/*prints assigned values*/
	rval = print(m, rows, cols);
	if(rval != 0){
		printf("ERR: print has an issue\n");
		return -1;
	}

	/*called gaussian elimination functions*/
	rval = ge_fw(m, rows, cols, n);
	printf("done forwards step\n");
	if(rval != 0){
		printf("ERR: gw_fw has an issue\n");
		return -1;
	}

	rval = ge_bw(m, rows, cols, n);
	printf("done backwards step\n");
	if(rval != 0){
		printf("ERR: ge_bw has an issue\n");
		return -1;
	}

	printf("The output matrix is:\n");
	rval = print(n, rows, cols);
	if(rval != 0){
		printf("ERR: print has an issue");
	}
 
	return 0;
}

int print(float *matrix, int rows, int cols){
	int r = 0;
	int c = 0;

	for(r = 0; r < rows; r++){
		for(c = 0; c < cols; c++){
			printf("%5.3f ", matrix[r*cols + c]);
		}
		printf("\n");
	}
	return 0;
}
