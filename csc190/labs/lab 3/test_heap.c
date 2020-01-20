#include <stdlib.h>
#include <stdio.h>
#include "heap.c"

int main(){
	int i = 0;int r = 0; int key = 0;
        int *output = NULL;
        int o_size;

        HeapType heap;
        r = initHeap(&heap, 50);

        addHeap(&heap, 1);
        addHeap(&heap, 3);
        addHeap(&heap, 6);
        addHeap(&heap, 2);
        addHeap(&heap, 17);

        printf("normal: ");

        for(i = 0; i < heap.end+1; i++){
                printf("%d ", heap.store[i]);
        }

	r = findHeap(&heap, 6); 
       	printf("\nfindHeap: %d\n ", r);

	printf("\ninorder: ");

        inorder(&heap, &output, &o_size);
        for(i = 0; i < o_size; i++){
                printf("%d ", output[i]);
        }
        printf("\npreorder: ");

        preorder(&heap, &output, &o_size);
        for(i = 0; i < o_size; i++){
                printf("%d ", output[i]);
        }
        printf("\npostorder: ");

        postorder(&heap, &output, &o_size);
        for(i = 0; i < o_size; i++){
                printf("%d ", output[i]);
        }
        printf("\n");
        return 0;
}

