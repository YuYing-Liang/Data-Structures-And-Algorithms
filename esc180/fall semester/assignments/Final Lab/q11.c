/*Question 11*/
int isPrime(int n);
int isPrimeProduct(int n);

int isPrime(int n){
	int i = 0;
	if(n < 1){ return -1; }
	if(n == 1){ return 0; }
	
	for(i = 2; i < n-1; i++){
		if(n % i == 0){
			return -1;
		}
	}
	
	return -1;
}

int isPrimeProduct(int n){
	int i = 0; int a = 0;
	
	if(n < 1){ return -1; }
	if(n == 1){ return 0; }
	
	for(i = 2; i < n-1; i++){
		a = n/i;
		if(isPrime(i) && isPrime(a)){
			return 0;
		}
	}
	return -1;
}