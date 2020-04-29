from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time

print('working....')


#Key generation

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
#privkey = keyPair.blind
print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
print(pubKeyPEM.decode('ascii'))

print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
print(privKeyPEM.decode('ascii'))

# Export private key

privateKeyFile = open("privKeyPair.pem",'w')      # write private key
privateKeyFile.write(privKeyPEM.decode('ascii'))
privateKeyFile.close()

'''
# Import Private key

privateKeyFile = open("privKeyPair.pem",'r')
privKey = RSA.importKey(privateKeyFile.read())
privateKeyFile.close()
'''

# Input files

in_filename = "threeEntitiesinMCS.jpg"     # path to file
out_filename = "threeEntitiesinMCS.jpg.enc-rsa"    # path to output file

#Encryption

encryptor = PKCS1_OAEP.new(pubKey)
num_chunks=0
first=0


#Writing bytes into the file 

with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(16)
                
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)      # Adding padding

                encr = encryptor.encrypt(chunk)
                if first < 6:
                    #print(len(chunk),chunk)
                    print('-----------------------')
                    print(str(encr))
                    first+=1
                
                outfile.write(encr)
                outfile.write(b'\n')
                num_chunks+=1
'''
# Witing string into the file

with open(in_filename, 'rb') as infile:
        with open(out_filename, 'w') as outfile:
            while True:
                chunk = infile.read(16)

                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)      # Adding padding


                encr = encryptor.encrypt(chunk)
                if first < 6:
                    #print(len(chunk),chunk)
                    print('-----------------------')
                    print(encr)
                    first+=1

                outfile.write(str(encr))
                outfile.write('\n\n')
                num_chunks+=1

'''
print('Encryption complete. Sleeping for 2 sec...')
print('Chunks after encryption:',num_chunks)
time.sleep(2)
'''
#Decryption

decryptor = PKCS1_OAEP.new(privKey)
out_file2 = "threeEntitiesinMCS-recovered.jpg"      # Path to decrypted file
num_chunks=0

with open(out_filename, 'rb') as infile:
        with open(out_file2, 'wb') as outfile:
            while True:
                chunk = infile.read(2)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 2 != 0:
                    chunk += b' ' * (2 - len(chunk) % 2)

                print(len(chunk))
                outfile.write(decryptor.decrypt(chunk))
                num_chunks+=1
                print(num_chunks)

print('Chunks after Decryption:',num_chunks)
'''

'''
msg = b'A message for encryption'
encryptor = PKCS1_OAEP.new(pubKey)
encrypted = encryptor.encrypt(data)
print("Encrypted:", binascii.hexlify(encrypted))

decryptor = PKCS1_OAEP.new(keyPair)
decrypted = decryptor.decrypt(encrypted)
print('Decrypted:', decrypted)
'''
