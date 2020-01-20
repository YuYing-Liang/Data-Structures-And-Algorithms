def main():
	#unlocked password: "01203031"
	PSWD = "01203031"
	pswdUnlocked = False
	enteredPswd = ""

	while not pswdUnlocked:
		attempt = input("Enter a word: ")
		enteredPswd += checkWord(attempt)

		if enteredPswd == PSWD:
			pswdUnlocked = True
			print("UNLOCKED")
		else:
			areValuesTheSame = True
			lenOfEnteredPswd = len(enteredPswd)
			#checks if each value in attempt is the same as the pswd
			for i in range(0, lenOfEnteredPswd, 1):
				if enteredPswd[i] != PSWD[i]:
					areValuesTheSame = False
			#if not, reset enteredPswd
			if not areValuesTheSame:
				enteredPswd = ""
		

def checkWord(word):
	#case sensitive
	if word == "cat":
		return "0"
	elif word == "dolphin":
		return "1"
	elif word == "bird":
		return "2"
	elif word == "dog":
		return "3"
	else:
		return "4"

main()
