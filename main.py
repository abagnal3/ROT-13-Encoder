# ROT 13 encoder

def encrypt(message,secret_num):
	result = ""

	# Traverse the text
	
	for i in range(len(message)):
		char = message[i]

		# Encrypt uppercase characters
		
		if (char.isupper()):
			result += chr((ord(char) + secret_num -65) % 26 + 65)

		# Encrypt lowercase characters
		
		else:
			result += chr((ord(char) + secret_num - 97) % 26 + 97)

	return result


# Take message

print ('Please enter the message to be encoded.')
message = input()
secret_num = 13

if True:
        print ("Original message: " + message) 

        print ("ROT13 cipher: " + encrypt(message,secret_num)) 
      
