from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time

# Import Private key

privateKeyFile = open("privKeyPair.pem",'r')
privKey = RSA.importKey(privateKeyFile.read())
privateKeyFile.close()

# Decryption

decryptor = PKCS1_OAEP.new(privKey)

in_filename = "threeEntitiesinMCS.jpg.enc-rsa"    # path to encrypted file
out_fileRvd = "threeEntitiesinMCS-recovered.jpg"      # Path to decrypted file

num_chunks=0
first=0

infile = open(in_filename, 'rb')
outfile = open(out_fileRvd,'wb')

#with open(in_filename, 'rb') as infile:
while True:
    chunk = infile.readline()
    chunk = chunk.strip(b'\n')
    iv = b'\x1a\xfb\xe9`\xf9_\x1a\xb4\xb5\xec\xbft\x87Rp\xad5\x05o\x94\xeeXs\x04\xdcm\xea7\x81\x87:\xe0j\x03s\xa9\x9e\xc5\xe9\x13\xce\xc7n|\x83H\xa2\xe4\xa0xU\x04n\xb0Q\xfdT\xadO\xde\x8fM\xeb[[\x10\xff\xa2\x04\xe6\xfa\xacK?E\xa2g\x81\xf9P\xff)[\xa5X\xda-\xacB\xe4_\xa7f\x01l\xfb\x809\x90Z\xf6*0,\x93\x88$z\x8f-\xfe\xf4\x82}e\xc7\x1cG\xc3\xdf\x8e\x87)\xdc\x85f\x12s'
    if not chunk:
        break
    #elif len(chunk) % 128 != 0:
    #    chunk + = b' ' * (128 - len(chunk) % 128)
    elif first < 6:
        print(first ,'---Start---')
        #print(len(line),str(chunk))
        print(len(chunk),str(chunk))
        first+=1
        print('Decrypting...')

    num_chunks+=1
    #print(num_chunks)    
    outfile.write(decryptor.decrypt(iv))


'''
#with open(in_filename, 'rb') as infile:
while True:
    chunk = infile.readline()
    chunk = chunk.strip(b'\n\n')
    if not chunk:
        break
    #elif len(chunk) % 128 != 0:
    #    chunk + = b' ' * (128 - len(chunk) % 128)
    elif first < 6:
        print(first ,'---Start---')
        #print(len(line),str(chunk))
        print(len(chunk),str(chunk))
        first+=1
        print('Decrypting...')

    num_chunks+=1
    #print(num_chunks)
    
    #outfile.write(decryptor.decrypt(chunk))
    
    #print('lastlineofwhile')
'''

infile.close()
outfile.close()
print('Chunks after Decryption:',num_chunks)
