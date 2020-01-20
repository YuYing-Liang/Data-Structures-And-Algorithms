#include <stdio.h>
#include <stdlib.h>

/*Feedback Shift Register*/
unsigned char FSR(unsigned char x) {
   unsigned char oldbit0 = x & 0x1; /* extract bit 0 */
   unsigned char r = x >> 1;        /* shift right   */
   unsigned char newbit7 = oldbit0 << 7; /* move bit0 to the bit7 pos */
   r = r | newbit7; /* rotate the old value of bit 0 into the bit 7 pos */
   return r;
}

unsigned char prng(unsigned char x, unsigned char pattern){
	return FSR(x) ^ pattern;
	
}

int crypt(char *data, unsigned int size, unsigned char password){
	int i = 0;
	unsigned char prngVal = password;
	
	if((int)password == 0 || size < 1){
		return -1;
	}
	
	for(i = 0; i < size; i++){
		prngVal = prng(prngVal, 0xb8);
		data[i] = data[i] ^ prngVal;
	}

	return 0;
}

int main(){
	/*code testing*/
	unsigned char a = 'a';
	unsigned char b = 'b';

	char data[] = {'y','e','l','l','o'};
	unsigned int size = 5;
	unsigned char password = 'w';
	int i = 0;
	int r_val = 0;

	printf("testing FSR function\n");
	for(i = 0; i <= 8; i++){
		a = FSR(a);
		printf("%c %d\n", a);
	}

	printf("testing prng function\n");
	for(i = 0; i <= 16; i++){
		b = prng(b, 0xb8);
		printf("%c %d\n", b);
	};

	printf("testing crypt function\n");
	printf("before:\n");

	for(i = 0; i < size; i++){
		printf("%c ", data[i]);
	}

	printf("\nafter:\n");
	r_val = crypt(data, size, password);

	if(r_val == 0){
		for(i = 0; i < size; i++){
			printf("%c ", data[i]);
		}
	}

	printf("\n");
	return 0;
}
