#include <stdlib.h>
#include <stdio.h>
#include "heap.h"

int initHeap (HeapType *pHeap,int size){
	if(pHeap == NULL || size < 1){ return -1; }
	(pHeap -> store) = (int *)malloc(sizeof(int) * size);
	pHeap->size = size;
	pHeap->end = -1;
	return 0;
}

int addHeap(HeapType *pHeap, int key){
	int i = 0;
	int lenTemp = pHeap->size + 1;
	int temp[lenTemp];
	int key_index = 0;
	int t = 0;

	if(pHeap == NULL){return -1;}
	


	if(pHeap->end+1 > pHeap->size){
		for(i = 0; i < pHeap->size; i++){
			temp[i] = pHeap->store[i];
		}
		temp[pHeap->size] = key;
		pHeap->size *= 2;
		pHeap->store = (int *)malloc(sizeof(int) * (pHeap->size));
		for(i = 0; i < pHeap->size + 1; i++){
			pHeap->store[i] = temp[i];
		}
		pHeap->end = i;
	}else{
		pHeap->end++;
		(pHeap->store)[pHeap->end] = key;
	}
	
	if(pHeap->end > 0){

		key_index = pHeap->end;
		i = pHeap->end/2;

		if(pHeap->store[key_index] > pHeap->store[i]){
			while(key_index > i){
				t = pHeap->store[i];
				pHeap->store[i] = pHeap->store[key_index];
				pHeap->store[key_index] = t;
				key_index = i;
				i = i/2;
			}
		}
	
	}
	return 0;
}

int delHeap(HeapType *pHeap, int *key){
	int last = pHeap->store[pHeap->end];
	int rootIndex = 0;
	int left = rootIndex*2 + 1;
	int right = rootIndex*2 + 2;
	int temp = 0;

	if(pHeap == NULL){return -1;}

	*key = pHeap->store[rootIndex];
	pHeap->store[rootIndex] = last;
	pHeap->store[pHeap->end] = 0; /*delete last node*/
	pHeap->end--;
	
	if(pHeap->store[rootIndex] < pHeap->store[right] || pHeap->store[rootIndex] < pHeap->store[left]){

		while((left <= pHeap->end && right <= pHeap->end) && 
		      (pHeap->store[rootIndex] < pHeap->store[right] || pHeap->store[rootIndex] < pHeap->store[left]))
		{

			if(pHeap->store[left] >= pHeap->store[right]){
				/*swap with left*/				
				temp = pHeap->store[rootIndex];
				pHeap->store[rootIndex] = pHeap->store[left];
				pHeap->store[left] = temp;
				rootIndex = left;
				left = rootIndex*2;
				right = rootIndex*2 + 1;
			}else{
				/*swap with right*/
				temp = pHeap->store[rootIndex];
				pHeap->store[rootIndex] = pHeap->store[right];
				pHeap->store[right] = temp;
				rootIndex = right;
				right = rootIndex*2 + 1;
				left = rootIndex*2;
			}
		}
	}

}

int findHeap(HeapType *pHeap, int key){
	int i = 0;

	if(pHeap == NULL){return -1;}
	for(i = 0; i <= pHeap->end + 1; i++){
		if((pHeap->store)[i] == key){
			return 1;
		}
	}
	return 0;
}

int inorder(HeapType *pHeap, int **output, int *o_size){
	int x = 0;

	if(pHeap == NULL || output == NULL || pHeap->end <= 0){return -1;}

	*o_size = pHeap->end + 1; 
	(*output) = (int *) malloc(sizeof(int) * (*o_size));
	
	inorder_helper(pHeap->store, &x, *output, pHeap->end + 1, 0);
}

int inorder_helper(int array[], int *index, int *output, int end, int location){
	int i = 0;
	int buffer = location*2 + 1;

	/*left*/
	if(buffer < end){
		inorder_helper(array, index, output,end , buffer);
	}

	/*node*/
	output[(*index)] = array[location];
	(*index)++;

	/*right*/
	if(buffer + 1 < end){
		inorder_helper(array, index, output, end, buffer+1);
	}
	return 0;
}

int preorder(HeapType *pHeap, int **output, int *o_size){
	int x = 0;

	if(pHeap == NULL || output == NULL || pHeap->end <= 0){return -1;}

	*o_size = pHeap->end + 1; 
	(*output) = (int *) malloc(sizeof(int) * (*o_size));
	
	preorder_helper(pHeap->store, &x, *output, pHeap->end + 1, 0);
}

int preorder_helper(int array[], int *index, int *output, int end, int location){
	int i = 0;
	int buffer = location*2 + 1;

	/*node*/
	output[(*index)] = array[location];
	(*index)++;

	/*left*/
	if(buffer < end){
		preorder_helper(array, index, output, end, buffer);
	}

	/*right*/
	if(buffer + 1 < end){
		preorder_helper(array, index, output, end, buffer+1);
	}
	return 0;
}

int postorder(HeapType *pHeap, int **output, int *o_size){
	int x = 0;

	if(pHeap == NULL || output == NULL || pHeap->end <= 0){return -1;}

	*o_size = pHeap->end + 1; 
	(*output) = (int *) malloc(sizeof(int) * (*o_size));
	
	postorder_helper(pHeap->store, &x, *output, pHeap->end + 1, 0);
}

int postorder_helper(int array[], int *index, int *output, int end, int location){
	int i = 0;
	int buffer = location*2 + 1;

	/*left*/
	if(buffer < end){
		postorder_helper(array, index, output, end, buffer);
	}

	/*right*/
	if(buffer + 1 < end){
		postorder_helper(array, index, output, end, buffer+1);
	}

	/*node*/
	output[(*index)] = array[location];
	(*index)++;

	return 0;
}
