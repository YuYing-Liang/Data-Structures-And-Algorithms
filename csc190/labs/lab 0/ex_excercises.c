/*Excercises*/
#include <stdio.h>
#include <stdlib.h>

typedef struct {
	int *x;
	int end;
	int len;
}intlist;

int init(intlist *l,int len) {
	if (l==NULL) { return -1; }

	(l->x) = (int *)malloc(len * sizeof(int));
	if ((l->x) == NULL) { return -1; }

	l->end = -1;
	l->len=len;

	return 0;
}

int add_to_end(intlist *l,int val){
	int *temp = NULL;
	int i; int index = -1;
	int len = l->len;

	if (l==NULL) {return -1;}

	if((l->end) + 1 >= len - 1){
		/*list is full*/
		len++;
		temp = (int*)malloc(len * sizeof(int));
		for(i = 0; i < len-1; i++){
			temp[i] = (l->x)[i];
		}
		temp[len-1] = val;
		
		(l->x) = (int *)malloc(len * sizeof(int));
		for(i = 0; i < len; i++){
			(l->x)[i] = temp[i];
		}

		(l->end)++;
		(l->len)++;
	}else{
		/*length not exceeded*/
		(l->x)[l->end + 1] = val;
		(l->end)++;
	}
	return 0;
}

int add_to_start(intlist *l,int val){
	int *temp = NULL;
	int i; int index = -1;
	int len = l->len;

	if (l==NULL) {return -1;}

	if((l->end) + 1 >= len - 1){
		/*list is full*/
		len++;
		temp = (int*)malloc(len * sizeof(int));
		for(i = 1; i < len; i++){
			temp[i] = (l->x)[i-1];
		}
		temp[0] = val;
		
		(l->x) = (int *)malloc(len * sizeof(int));
		for(i = 0; i < len; i++){
			(l->x)[i] = temp[i];
		}

		(l->end)++;
		(l->len)++;
	}else{
		/*length not exceeded*/
		temp = (int*)malloc((l->end+2) * sizeof(int));
		for(i = 1; i < l->end+1; i++){
			temp[i] = (l->x)[i-1];
		}
		temp[0] = val;

		(l->x) = (int *)malloc(len * sizeof(int));
		for(i = 0; i < l->end+2; i++){
			(l->x)[i] = temp[i];
		}
		(l->end)++;
	}
	return 0;
}

int insert_after(intlist *l,int insert_val,int val){
	int *temp = NULL;
	int i; int index = -1;
	int len = l->len;

	if (l==NULL) {return -1;}

	if((l->end) + 1 >= len - 1){
		/*list is full*/
		len++;
		temp = (int*)malloc(len * sizeof(int));
		for(i = 1; i < len; i++){
			temp[i] = (l->x)[insert_val+i];
		}
		temp[0] = val;
		
		(l->x) = (int *)malloc(len * sizeof(int));
		for(i = 0; i < len; i++){
			(l->x)[i] = temp[i];
		}

		(l->end)++;
		(l->len)++;
	}else{
		/*length not exceeded*/
		temp = (int*)malloc((l->end+2) * sizeof(int));
		for(i = 1; i < l->end+1; i++){
			temp[i] = (l->x)[i-1];
		}
		temp[0] = val;

		(l->x) = (int *)malloc(len * sizeof(int));
		for(i = 0; i < l->end+2; i++){
			(l->x)[i] = temp[i];
		}
		(l->end)++;
	}
	return 0;
}

int main(void){
}
