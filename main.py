#Import modules:
import process
import encode
import decode

#Prompt the user to encode or decode:
process.process()

#Based on previous input, launch encode or decode function:
if process.process == 'e':
    encode.encode()
elif process.process == 'd':
    decode.decode()
