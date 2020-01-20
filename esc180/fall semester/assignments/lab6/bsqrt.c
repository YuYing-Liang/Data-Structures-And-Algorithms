float bsqrt(float x, float tol);

float bsqrt(float x, float tol){
	float sqrt_x = 0;
	float abs_sqrt_x = 0; 
	
	sqrt_x = x/2; //estimate
	
	//absolute value
	abs_sqrt_x = x - sqrt_x*sqrt_x;
	if(abs_sqrt_x < 0){
		abs_sqrt_x = -abs_sqrt_x;
	}
 
	while(abs_sqrt_x >= tol){
		sqrt_x = (sqrt_x + x/sqrt_x)/2;
		abs_sqrt_x = x - sqrt_x*sqrt_x;
		
		if(abs_sqrt_x < 0){
			abs_sqrt_x = -abs_sqrt_x;
		}

	}
	return sqrt_x;
}
