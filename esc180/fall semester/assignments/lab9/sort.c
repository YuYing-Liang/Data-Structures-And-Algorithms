int bubbleSort(int *array, int size);

int bubbleSort(int *array, int size){
	int nLength;
	int swapped;

	nLength = size;
	swapped = 1;

	if(array == NULL){
		return -1;
	}

	while(swapped){
		int i;
		int temp;
		swapped = 0;
		for(i = 1; i < nLength; i++){
			if(array[i-1] > array[i]){
				temp = array[i];
				array[i] = array[i-1];
				array[i-1] = temp;
				swapped = 1;
			}	
		}
	}
	
	return 0;
}	
				
