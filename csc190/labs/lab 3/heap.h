typedef struct {
   int key;
   unsigned int valid;
} keyType;

typedef struct {
   int *store;
   unsigned int size;
   unsigned int end;
} HeapType;
/*In order to make calculations easier, 0 index is empty*/

int initHeap (HeapType *pHeap,int size);
int inorder  (HeapType *pHeap, int **output, int *o_size);
int preorder (HeapType *pHeap, int **output, int *o_size);
int postorder(HeapType *pHeap, int **output, int *o_size);
int addHeap(HeapType *pHeap, int key);
int findHeap(HeapType *pHeap, int key);
int delHeap(HeapType *pHeap, int *key);
