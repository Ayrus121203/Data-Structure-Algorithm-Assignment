#Nmame: Surya Moorthy S/O Sathia Moorthy
#Admin Number: 201296F
#Group: IT2653-03

def encrypt(text,s):
	result =''
	for i in range(len(text)):
		char = text[i]
		#char will store each letter and proceed to if,else statement for encryption

		if (char.isupper()):
			#encrypt all uppercase letter *Note that the formula is fixed, where s is the num of shifts
			#26 is the num of char in the alphabet, making s = 26 will return exact plaintxt val
			result += chr((ord(char)+ s-65) % 26 + 65)    #char65 == 'A'
		else:
			result += chr((ord(char) + s - 97) % 26 + 97)       #char 97 == 'a'

	return result
