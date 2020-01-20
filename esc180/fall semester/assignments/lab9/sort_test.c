#include<stdio.h>
#include "sort.c"
int print(int *array, int size);

int main(void){
	int nums[5] = {3,5,4,2,1};
	int nums2[7] = {7,4,9,2,0,1,8};
	int rval = 0;
	
	print(nums,5);
	rval = bubbleSort(nums, 5);
	if(rval == 0){
		print(nums,5);
	}else{
		printf("ERR: problem sorting array\n");
	}
	
	print(nums2,7);
	rval = bubbleSort(nums2, 7);
	if(rval == 0){
		print(nums2,7);
	}else{
		printf("ERR: problem sorting array\n");
	}
}

int print(int *array, int size){
	int i = 0;

	for(i = 0; i < size; i++){
		printf("%d ",array[i]);
	}
	printf("\n");	
}
