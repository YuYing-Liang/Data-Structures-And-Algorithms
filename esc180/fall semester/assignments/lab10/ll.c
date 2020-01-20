#include <stdio.h>
#include <stdlib.h>
#include "ll.h"

/* One of the lessons here is to see that if we want to use a function to malloc something that
 * is a POINTER in the CALLER of the function, then we must send in the ADDRESS of the POINTER
 * to that function.
 * 
 * Recap: if we want to use a function to modify a VARIABLE in the caller
 *        then the CALLER needs to send in the ADDRESS of the VARIABLE
 *
 * Similarly: if we want to use a function to modify a POINTER in the caller
 *            then the CALLER needs to send in the ADDRESS of the POINTER
 *
 * In the code below, ll_add_to_head and ll_add_to_tail are dynamically creating new
 * nodes to be added to the linked list. Any dynamic creation of a node must be via
 * malloc.
 */

int ll_add_to_head( llnode **head, int val) {
   llnode *old_head;
   if (head == NULL) {
      return -1;
   }
   old_head = *head;

   *head = ( llnode *) malloc(sizeof( llnode));
   (*head) -> val = val;
   (*head) -> next = old_head;
   return 0;
}

int ll_add_to_tail( llnode **head, int val) {
   if (head == NULL) {
      return -1;
   }
   if (*head == NULL) {
      *head = ( llnode *) malloc(sizeof( llnode));
      (*head) -> val = val;
      (*head) -> next = NULL;
      return 0;
   } else { 
	/* recursively call ll_add_to_tail until we get to the tail
	which is the point where the pointer is NULL */
      return ll_add_to_tail(&((*head)->next), val);
   }
}

int ll_print( llnode *p) {
   if (p==NULL) {
      return 0;
   } else {
      printf("val = %d\n",p->val);
      return ll_print(p->next);
   }
}

/*valgrind returns errors with this function*/
int ll_free(llnode *p) {
   if (p==NULL) {
      return -1;
   } else {
      llnode *f = p->next;
      free(p);
      return ll_free(f);
   }
}

/*MY CODE*/
int ll_find_by_value(llnode *pList,int val){	
	llnode *current = pList;

	if(pList == NULL){
		return -1;
	}

	while(current != NULL){
		if(current->val == val){
			return 0;
		}	
		current = current -> next;
	}
	
	return -1;
}

int ll_del_from_tail(llnode **ppList){
	llnode *prev = NULL;
	llnode *curr = (*ppList);

	if(ppList == NULL || curr == NULL){
		return -1;
	}

	while(curr-> next != NULL){
		prev = curr;
		curr = curr -> next;
	}
		
	free(curr);	
	prev -> next = NULL;
		
	return 0;		
}

int ll_del_from_head(llnode **ppList){
	llnode *old_head = NULL;

	if(ppList == NULL || (*ppList) == NULL){
		return -1;
	}

	old_head = *ppList;
	(*ppList) = (*ppList) -> next;
	free(old_head);
	return 0;
}

/*deletes THE FIRST NODE in the list that has this value*/ 
int ll_del_by_value(llnode **ppList,int val){
	llnode *old_node = NULL;
	llnode *curr = (*ppList);

	if(ppList == NULL){
		return -1;
	}

	if(curr -> val == val){
		return ll_del_from_head(ppList);
	}

	while(curr != NULL){
		if(curr -> val == val){							
			old_node -> next = curr -> next;
			free(curr);
			return 0;
		}
		old_node = curr;		
		curr = curr -> next;
	}
	return -1;		
}

int ll_insert_in_order(llnode **ppList,int val){
	/*Head is smallest --> tail is largest, assume list is sorted*/

	llnode *past_node = NULL;
	llnode *new_node = NULL;
	llnode *curr = (*ppList);

	if(ppList == NULL || curr == NULL){
		return -1;
	}

	/*null list or at the beginning*/
	if(curr == NULL || curr -> val > val){
		ll_add_to_head(ppList, val);
		return 0;
	}else{
		curr = curr -> next;
		past_node = curr;
	}
		
	
	while(curr -> next != NULL){
		if(curr -> val > val){
			new_node = (llnode *)malloc(sizeof(llnode));
			past_node -> next = new_node;
			new_node -> val = val;
			new_node -> next = curr;	
			return 0;		
		}else{
			past_node = curr;
			curr = curr -> next;	
		}		
	}

	/*if node is not yet inserted, it is greater than all other elements in list
	  add to end of the list*/
	new_node = (llnode *)malloc(sizeof(llnode));
	new_node -> val = val;
	new_node -> next = NULL;
	curr -> next = new_node;
	return 0;
}

int ll_concat(llnode **pSrcA,llnode **pSrcB){
	llnode *headA = (*pSrcA);
	llnode *headB = (*pSrcB);
	
	if((pSrcA == NULL || pSrcB == NULL) || (headA == NULL || headB == NULL)){
		return -1;
	}

	/*find end of pSrcA*/
	while(headA -> next != NULL){ 
		headA = headA -> next;
	}

	headA -> next = headB;
	return 0;
}

int ll_sort(llnode **ppList){
	int swapped = 0;
	llnode *prev = (*ppList);
	llnode *node = prev -> next;

	if(ppList == NULL || prev == NULL){
		return -1;
	}
	
	swapped = 1;

	while(swapped){
		int i;
		int temp;
		swapped = 0;
		prev = (*ppList);
		node = prev -> next;

		while(prev -> next != NULL){
			if((prev -> val) >= (node -> val)){
				temp = (node -> val);
				node -> val = (prev -> val);
				prev -> val = temp;				
				swapped = 1;
			}
			prev = node;
			node = node -> next;	
		}
	}

	return 0;
}
