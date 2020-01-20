#include "helper.c"

int main(void){
	int value=0;
	int rvalue=0;
	bstNode *binary_tree=NULL;

	while (scanf("%d",&value) != EOF) {
		rvalue = add_bst(&binary_tree, value);
		if(rvalue == -1){ printf("there is an error."); }
	}

	printTreeInOrder(binary_tree);
}

