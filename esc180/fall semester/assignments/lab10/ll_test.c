#include <stdio.h>
#include "ll.h"

int main(void) {
   llnode *listA = NULL;
   llnode *listB = NULL;
   int r=0;
   int i=0;

   printf("List A\n");
   r=ll_add_to_tail(&listA,100);
   r=ll_add_to_tail(&listA,200);
   r=ll_add_to_tail(&listA,300);
   for(i=0;i<10;i=i+1){
      r=ll_add_to_tail(&listA,i*100);
   }
   r=ll_print(listA);
   printf("\n");

   /*testing find by value function*/
   r=ll_find_by_value(listA,5);
   printf("%d\n\n",r);
   
   /*testing delete from tail*/
   r = ll_del_from_tail(&listA);
   printf("Last Element Deleted\n");
   r = ll_print(listA);
   printf("\n");
   
   /*testing delete from head*/
   r = ll_del_from_head(&listA);
   printf("First Element Deleted\n");
   r = ll_print(listA);
   printf("\n");

   /*testing delete by value ALL VALUES OR JUST THE FIRST ONE????*/
   r = ll_del_by_value(&listA, 200);
   r = ll_del_by_value(&listA, 300);
   r = ll_del_by_value(&listA, 0);
   printf("Value 0,200 and 300 Deleted\n");
   r = ll_print(listA);
   printf("\n");

   /*testing delete from head*/
   r = ll_insert_in_order(&listA, 250);
   r = ll_insert_in_order(&listA, 5);
   r = ll_insert_in_order(&listA, 876);
   printf("Inserted 250,876 and 5 in list A\n");
   r = ll_print(listA);
   printf("\n");
   
   printf("List B\n");
   for(i=0;i<5;i=i+1){
      r=ll_add_to_head(&listB,i*100);
   }
   r=ll_print(listB);
   printf("\n");

   /*joining listB and listA together*/
   r = ll_concat(&listA, &listB);
   printf("New list A\n");
   r = ll_print(listA);
   printf("\n");

   /*sort list B*/
   r = ll_sort(&listB);
   printf("Sorted List B\n");
   r = ll_print(listB);

   r=ll_free(listA);
   r=ll_free(listB);
   return 0;

}
