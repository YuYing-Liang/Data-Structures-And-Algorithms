#include <stdio.h> //for input/output library

float bsqrt(float x, float acc);
float myAbs(float x);

int main(void){
	int i=0;
	float sqrt=0;
        for(i=0;i<10;i++){
                sqrt = bsqrt((float)i,0.001);
                printf("The sqrt of %d is %f\n", i, sqrt);
        }
        return 0;
}

float bsqrt(float x, float acc){
        float estimate = 0; 
	estimate = x/2;

	while(myAbs(x - estimate*estimate) > acc){
		estimate = (estimate + x/estimate)/2;
	}
	return estimate;
}

float myAbs(float x){
	if(x >= 0){
		return x;
	}else{
		return -x;
	}
}
