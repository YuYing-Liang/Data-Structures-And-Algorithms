/*parenthesis checking*/
#include <stdio.h>
#include <stdlib.h>

struct llnode_char{
   char value;
   struct llnode_char *next;
   struct llnode_char *prev;
};
typedef struct llnode_char llnode_char;

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
   int failed_pos = 0;
   char value;
   int rvalue=0;
   char result;
   int pass_or_fail = 1;

   llnode_char *input_list=NULL;

   while (scanf("%c",&value) != EOF) {
      n=n+1;

      if(value == '(' || value == '[' || value == '{'){
         rvalue = push(&input_list, value);
         if(rvalue == -1) { printf("An error has occurred.");}
      }

      if(value == ')' || value == ']' || value == '}'){

         if(input_list == NULL) {
	    failed_pos = n;
	    pass_or_fail = 0;
            break;
	 }
	 rvalue = pop(&input_list, &result);
	 if(rvalue == -1) { printf("An error has occurred.");}

         if((value == ')' && result != '(') ||
	    (value == ']' && result != '[') ||
	    (value == '}' && result != '{')) {

                failed_pos = n;
		pass_or_fail = 0;
         }
      }

      if(!pass_or_fail){break;}
   }

   if(input_list == NULL && pass_or_fail == 1){
      printf("PASS\n");
   }else{
      if(input_list != NULL){ failed_pos = n; }
      printf("FAIL,%d\n",failed_pos);
   }
   
   return 0;
}
