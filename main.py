#Import modules:
import prompt
import encode
import decode

#Prompt the user to encode or decode:
prompt.prompt()

#Based on previous input, launch encode or decode function:
if prompt.prompt == 'e':
    encode.encode()
elif prompt.prompt == 'd':
    decode.decode()