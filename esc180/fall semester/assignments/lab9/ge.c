#include<stdlib.h>
#include<stdio.h>
int ge_fw(float *matrix, int rows, int cols, float *matrix_out);
int ge_bw(float *matrix, int rows, int cols, float *matrix_out);


int ge_fw(float *matrix, int rows, int cols, float *matrix_out){
	int r = 0;
	int c = 0;
	int i = 0;
	float temp = 0.0;
	int x = 0;
	int k = 0;
	int j = 0;
	float factor = 0.0;

	if(matrix == NULL){
		return -1;
	}
	if(matrix_out == NULL){
		return -1;
	}
	
	/*copying matrix into matrix_out*/
	for(r = 0; r < rows; r++){
		for(c = 0; c < cols; c++){
			matrix_out[r*cols + c] = matrix[r*cols + c];
		}
	}

	/*find first row with a non-zero entry and exchange with first row*/
	for(r = 0;r < rows;r++){
		if(matrix_out[r*cols] != 0.0){
			if(r*cols != 0){
				/*swap rows*/
				for(i = 0; i < cols; i++){
					temp = matrix_out[r*cols + i];
					matrix_out[r*cols + i] = matrix_out[i];
					matrix_out[i] = temp;				
				}
			}
			break;
		}
	}

	for(x = 0; x < cols; x++){
		for(r = k + 1; r < rows; r++){
			/*if another nonzero beginning row is found*/	
			if(matrix_out[r*cols + x]  == 0){
				for(j = r; j < rows; j++){
					if(matrix_out[j*cols] != 0){
						/*swap rows*/
						for(i = 0; i < cols; i++){
							temp = matrix_out[j*cols + i];
							matrix_out[j*cols + i] = matrix_out[r*cols + i];
							matrix_out[r*cols + i] = temp;
						}
						break;
					}
				}
			}

			factor = matrix_out[r*cols + x]/matrix_out[k*cols + x];

			/*apply factor to the columns of that row*/

			for(c = x; c < cols; c++){
				matrix_out[r*cols + c] -= (factor * matrix_out[k*cols + c]);
			}
		}
		k++;
	}

	return 0;			
							
}

int ge_bw(float *matrix, int rows, int cols, float *matrix_out){
	int r = 0;
	int c = 0;
	int x = 0;
	int lastNonZeroRow = 0;
	float factor = 0.0;
	int factorFound = 0;
	int leadingOneCol = 0;

	/*matrix_out is already changed according to ge_fw matrix is the original matrix*/

	if(matrix_out == NULL){
		return -1;
	}
	if(matrix == NULL){
		return -1;
	}

	/*starting with the last nonzero row, normalize the row by its first nonzero entry*/
	
	/*find the last nonzer row*/
	lastNonZeroRow = -1;
	for(r = rows - 1; r >= 0; r--){
		for(c = 0; c < cols; c++){
			if(matrix_out[r*cols +c] != 0.0){
				lastNonZeroRow = r;
				break;
			}
		}
		if(lastNonZeroRow > -1){
			break;
		}
	}

	/*you want the first nonzero column in the row to be one*/
	for(r = lastNonZeroRow; r >= 0; r--){
		factor = 1;
		factorFound = 0;
		for(c = 0; c < cols; c++){
			if(matrix_out[r*cols + c] != 0.0 && factorFound == 0){
				factor = matrix_out[r*cols + c];
				factorFound = 1;
			}
			matrix_out[r*cols + c] = matrix_out[r*cols + c]/factor;
		}
	}

	/*add multiples of this row to previous rows so that all the entries in the column
 	 *containing leading 1s are zero*/

	for(r = lastNonZeroRow; r > 0; r--){
		/*find column that contains leading 1*/
		for(c = 0; c < cols; c++){
			if(matrix_out[r*cols + c] == 1.0){
				leadingOneCol = c;
				break;
			}
		}
	
		for(c = r-1; c >= 0; c--){
			factor = matrix_out[c*cols + leadingOneCol];
			for(x = leadingOneCol; x < cols; x++){
				matrix_out[c*cols + x] -= factor * matrix_out[r*cols + x];
			}
		}
	}		 	
	return 0;
}
