int anlboard(char *T, int sizeT);

int anlboard(char *T, int sizeT){
	int i;
	int open_positions;
	int winningX = 0;
	int winningO = 0;

	if(sizeT != 9){
		return -1;
	}

	for(i = 0; i < sizeT; i++){
		if(!(T[i] == 'X' || T[i] == 'O' || T[i] == '-')){
			return -1;
		}
	}

	/*check columns*/
	for(i = 0; i < 3; i++){
		if(T[i] == T[i + 3] && T[i] == T[i + 6]){
			if(T[i] == 'X'){
				winningX += 1;
			}else if(T[i] == 'O'){
				winningO += 1;
			}
		
		}
	}

	/*check rows*/
	for(i = 0; i < sizeT; i+=3){
		if(T[i] == T[i+1] && T[i] == T[i+2]){
			if(T[i] == 'X'){
				winningX += 1;
			}else if(T[i] == 'O'){
				winningO += 1;
			}
					
		}
	}

	/*check diagonals*/
	if(T[0] == T[4] && T[0] == T[8]){
		if(T[0] == 'X'){
			winningX += 1;
		}else if(T[0] == 'O'){
			winningO += 1;
		}
		
	}else if(T[2] == T[4] && T[2] == T[6]){
		if(T[2] == 'X'){
			winningX += 1;
		}else if(T[2] == 'O'){
			winningO += 1;
		}
		
	}

	/*checking to see if there are invalid winning scenarios*/
	if(winningX > 1 || winningO > 1){
		return -1;
	}

	if(winningX > 0 && winningO > 0){
		return -1;
	}

	/*winning scenarios*/
	if(winningX == 1){
		return 1;
	}

	if(winningO == 1){
		return 2;
	}	

	/*check to see if there is a tie*/
	open_positions = 0;
	for(i=0; i < sizeT; i++){
		if(T[i] == '-'){
			open_positions++;
		}
	}

	if(open_positions == 0){
		return 3; 
	}else{
		return 0;
	}
}	
