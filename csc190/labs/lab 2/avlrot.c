#include <stdio.h>
#include <stdlib.h>
#include "helper.c"

int isAVL(avlNode **root);
int rotate(avlNode **root, unsigned int Left0_Right1); /*if 0 go left, if 1 go right*/
int dblrotate(avlNode **root, unsigned int MajLMinR0_MajRMinL1);

int isAVL(avlNode **root){
	/*0 if balanced, -1 if unbalanced*/
	isLeftBalanced = 0;
	isRightBalanced = 0;

	if(root == NULL || *root == NULL) {return -1;}
	(*root) -> balance = 0;
	if((*root) -> l != NULL){ 
		(*root)-> balance -= 1;
		isLeftBalanced = isAVL(avlNode &((*root)->l))	
	}
	if((*root) -> r != NULL){ (*root)-> balance += 1;}
 
	
