#include <stdio.h>
#include <stdlib.h>

struct llnode_char{
   char value;
   struct llnode_char *next;
};
typedef struct llnode_char llnode_char;

int llnode_print_from_head(llnode_char *x) {
   if (x==NULL) { return 0; }
   else {
      printf("%c\n",x->value);
      return llnode_print_from_head(x->next);
   }
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

int main(void) {
   int n=0; 
   char value;
   int rvalue=0;
   llnode_char *input_list=NULL;


   while (scanf("%c",&value) != EOF) {
      n=n+1;
      llnode_add_to_tail(&input_list, value);
   }

   printf("INFO: you entered %d items\n",n);
   rvalue=llnode_print_from_tail(input_list);
   if ( !(rvalue==0) ) { printf("ERR: llnode_print returned an error\n"); }

   return 0;
}
