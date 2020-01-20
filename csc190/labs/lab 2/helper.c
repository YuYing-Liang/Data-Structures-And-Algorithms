#include <stdlib.h>
#include <stdio.h>

struct bstNode {
	int val;
	struct bstNode *l;
	struct bstNode *r;
};
typedef struct bstNode bstNode;

struct avlNode{	/*can tolerate an imbalance of at most 1*/
	int balance;	/* -1 left, 0 balanced, +1 rigth */
	int val;
	struct avlNode *l;
	struct avlNode *r;
};
typedef struct avlNode avlNode;


struct qNode {
   avlNode *pval;
   struct qNode *nxt;
};
typedef struct qNode qNode;

struct queue{
	bstNode *val;
	struct queue *next;
};
typedef struct queue queue;

/*methods for queue*/
int pushQ(queue **q, bstNode *val){
	/*add to tail*/
	if (q == NULL) { return -1; }
	if (*q == NULL){
		*q = (queue *)malloc(sizeof(queue));
		(*q)->val = val;
		(*q)->next = NULL;
	}else{
		pushQ(&((*q)-> next), val);
	}
	return 0;
}


int shiftQ(queue **q, int *r_val){
	/*take from head*/
	queue *temp = NULL;

	if(q == NULL || *q == NULL){ return -1; }
	*r_val = ((*q)->val)->val;
	temp = (*q);
	(*q) = (*q)-> next;
	free(temp);

	return 0;
}

int add_bst(bstNode **root,int val) {
	if (root == NULL) { return -1; }
	if (*root == NULL) {
		(*root) = (bstNode *)malloc(sizeof(bstNode));		
		(*root)->val = val;
		(*root)->l = NULL;
		(*root)->r = NULL;
		return 0;
	} else {
		if(val > (*root)->val){
			add_bst(&((*root)->r), val);
		}else if(val < (*root)->val){
			add_bst(&((*root)->l), val);
		}
	}
	return 0;
}

int printTreeInOrder(bstNode *root){
	int r_val = 0;

	if(root == NULL){ return -1;}
	if(root->l != NULL){
		r_val = printTreeInOrder(root->l);
	}
	printf("%d\n",root->val);
	if(root->r != NULL){
		r_val = printTreeInOrder(root->r);
	}
	return 0;
}

int printLevelOrder(bstNode *root){
	queue *q = NULL;
	bstNode *currNode = NULL;
	int lenQ = 0;
	int i = 0;
	int r_val = 0;

	if(root == NULL){return -1;}

	pushQ(&q, root); 
	lenQ++;

	while(lenQ > 0){
		currNode = q->val;
		if(currNode->l != NULL){
			pushQ(&q, currNode->l);
			lenQ++;
		}
		if(currNode->r != NULL){
			pushQ(&q, currNode->r);
			lenQ++;
		}
		shiftQ(&q, &r_val);
		lenQ--;
		printf("%d ", r_val);
		
	}
	return 0;
}




