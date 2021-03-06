/*Question 9 d*/
#include <stdlib.h>
int fil(float *matrixIn, int rows, int cols, float **matrixOut);

int fil(float *matrixIn, int rows, int cols, float **matrixOut){
	int r = 0; int c = 0;
	
	if(matrixOut == NULL || matrixIn == NULL || rows < 1 || cols < 1){ return -1; }
	
	(*matrixOut) = (float *)malloc(sizeof(float) * (rows * cols));
	
	if((*matrixOut) == NULL){ return -1;}
	
	for(r = 0; r < rows; r++){
		for(c = 0; c < cols; cols++){
			if(matrixIn[r * cols + c] < 0){
				(*matrixOut)[r * cols + c] = 0;
			}else{
				(*matrixOut)[r * cols + c] = matrixIn[r * cols + c];
			}
		}
	}
	return 0;
}
