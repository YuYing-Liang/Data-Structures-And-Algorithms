/* This is an example of how to use a linked list as a
 * dynamic container to store data that is input with an
 * unknown number of items.
 *
 * Note how we get the data:
 * -while loop (because the number of iterations is unknown)
 * -scanf returns EOF, or End-Of-File, when "nothing" has been input
 * -for each iteration, we stuff the input data into a linked list
 *
 * Usage:
 * gcc getData.c
 * echo "1 2 3 4 5 6 7 8     9      10" | ./a.out
 * should report 10 items read and dump it out
 * -> white space is ignored (space, tab, return)
 *
 * Assignment:
 * -modify this code so that it handles input "char" data
 *  rather than ints (trivial modification)
 * echo "abcdef" | ./a.out
 * should report 7 items read
 * (white space is representable by the char hence the
 * final return you enter is stored as a char)
 */

#include <stdio.h>
#include <stdlib.h>

struct llnode_char{
   char value;
   struct llnode_char *next;
   struct llnode_char *prev;
};
typedef struct llnode_char llnode_char;

int llnode_print_from_head(llnode_char *x) {
   if(x==NULL){ return 0;}
   else {
      printf("%c\n", x->value);
      return llnode_print_from_head(x->next);
   }
}

int llnode_add_to_head(llnode_char **x, char value){
   llnode_char *new_node = NULL;

   if(x==NULL){ return -1;}
   new_node = (llnode_char *) malloc(sizeof(llnode_char));
   new_node->value = value;
   new_node->next = *x;
   *x = new_node;
   return 0;
}

int llnode_add_to_tail(llnode_char **x,char value) {
   if (x==NULL) { return -1; }
   if (*x==NULL) {
      *x = (llnode_char *) malloc(sizeof(llnode_char));
      (*x)->value = value;
      (*x)->next = NULL;
      return 0;
   } else {
      return llnode_add_to_tail(&((*x)->next),value);
   }
}

int llnode_print_from_tail(llnode_char *x) {
   if (x==NULL) { return 0; }
   else {
      if (x->next == NULL) {
         printf("%c\n",x->value);
	 return 0;
      } else {
         llnode_print_from_tail(x->next);
         printf("%c\n",x->value);
	 return 0;
      }
   }
}

int push(llnode_char **x, char value){
	if(x == NULL){ return -1;}
	/*add to head*/
	llnode_add_to_head(x,value);
	return 0;
}

int pop(llnode_char **x, char *return_value){
	llnode_char *temp = NULL;

	if(x == NULL){ return -1;}
	/*take from head*/
	*return_value = ((*x)-> value);
	temp = (*x);
	(*x) = (*x)-> next;
	free(temp);
	return 0;
}

int main(void) {
   int n=0; 
   char value;
   int rvalue=0;
   char result;
   llnode_char *input_list=NULL;

   while (scanf("%c",&value) != EOF) {
      n=n+1;
      /*llnode char*/
      push(&input_list, value);
   }

   printf("INFO: you entered %d items\n",n);
   /*llnode char*/
   while(input_list != NULL){
	rvalue = pop(&input_list, &result);
	printf("%c\n",result);
   	if ( !(rvalue==0) ) { printf("ERR: llnode_print returned an error\n"); }
   }
   return 0;
}
