#include <stdio.h>
#include <stdlib.h>

int main(){
	int *x = 0;
	int *pointer = NULL;
	pointer = 1002;
	x = *pointer;

	printf("%x\n ",x,x);

	a = x & 0x0000FFFF;
	v = (x & 0xFFFF0000) >> 6;

/*
 * 	mask out the part you don't want
 * 	shift to bring the actual value to bring the odd part of the value to the bottom
 *	the amount you shift is known beforehand
 *
 */

/*	in the variable x, the value you are interested in is located in locations 17 to 23
 *	_ _ _ _ _ _    _ 
 *		  2^2  2^0
 *		  pos2 pos1
 *	00000000|11...11|0000
 *		 23 - 17
 *		 23 - 21 = 1 nibble
 *		 20 - 16 = 2 nibbles (add a zero at the end
 *
 * Mask and then Shift
 *	0X00FE0000
 *	y = x & 0x00FE0000
 *	y = y >> 17
 *
 * Shift and then Mask
 * 	y = x >> 17 (now in range 0 to 6)
 *	0 1 1 1 1 1 1 1
 *	8 7 6 5 4 3 2 1
 *	-------	-------
 *	   7   |   F
 *	y = y & 0x7F
 *
 * value of interest: 27 to 14 --> shift by 14
 * 	3FFF
 * 	--> 0011 1111 1111 1111
 *	    ---- ---- ---- ----
 *	      3 | F  | F  | F
 *
 * 	SO y = (x >> 14) & 0x3FFF
 *
 * value of motor speed from 19 to 17
 * 	19 - 17
 * 	0  0  0 	for stop
 * 	1  1  0 	for go
 *
 * 	changing  0 0 0 0	0
 * 	to	  0 1 1 0	6
 *
 * 	x = x | (0x6 << 17)
 *
 * 	pointer = 1004;
 * 	*p = 0x < 0000;
 * 	
 * 	0 ... 0 1 0 ... 0 1 0 ... 0 1 0 ... 0
 * 		23	  20	    17
 * 	   0	     9         2
 * 	0  to 15 =  0000 0000
 * 	16 to 19 =  0010
 * 	20 to 23 =  1001
 *
 * 	what if from 16 to 0 is not just 0? but we still want only 1s at 17, 20, 23
 *	then,
 * 		y = x | 0x92000 --> each number represents 1 nibble
 *
 * 	what if we want 
 * 	lets first make 12, 14 and 20 positions all 1
 *
 * 	m = (0x1 << 12) | (0x1 << 14) | (0x1 << 20)
 * 	f = ~m  --> unary operator (just flips it, does the opposite so the 0s are 1s and vice versa
 * 	s = (0x1 << 14) | (0x1 << 14)
 * 	y = (x & f) | s
 *	
 *	m1  put 1 in pos 30, 24
 *	m0  put 0 in pos 28, 4
 *
 *	m1 = (0x1 << 30) | (0x1 << 24)
 *	m0 = ~ ((0x1 << 28) | (0x1 << 4))
 *	x = (x & m0) | m1
 *
 *
 *	ALWAYS USED unsigned IN FRONT OF A VARIABLE
 *	SHIFT FIRST, MASK LATER!!
 *
 *	4 bits = NIBBLE
 *	8 bits = BYTE
 */	 	
	return 0;
}
