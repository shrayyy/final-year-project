import timeit

setup_code = """
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time
"""

statement = """

#Key generation

keyPair = RSA.generate(1024)

pubKey = keyPair.publickey()
#privkey = keyPair.blind
#print(f"Public key: (n={hex(pubKey.n)}, e={hex(pubKey.e)})")
pubKeyPEM = pubKey.exportKey()
#print(pubKeyPEM.decode('ascii'))

#print(f"Private key: (n={hex(pubKey.n)}, d={hex(keyPair.d)})")
privKeyPEM = keyPair.exportKey()
#print(privKeyPEM.decode('ascii'))

# Export private key

privateKeyFile = open("..\\data\\KB50-RSA-privKeyPair.pem",'w')      # write private key
privateKeyFile.write(privKeyPEM.decode('ascii'))
privateKeyFile.close()

# Input files

in_filename = "..\\data\\KB50.file"     # path to file
out_filename = "..\\data\\KB50-E-RSA.encr"    # path to output file

#Encryption

encryptor = PKCS1_OAEP.new(pubKey)

#Writing bytes into the file 
first = 0
with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(16)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)      # Adding padding

                encr = encryptor.encrypt(chunk)

                if first < 3:
                    #print(len(chunk),chunk)
                    print('-----------------------')
                    print(len(encr),str(encr))
                    first+=1

                outfile.write(encr)
                outfile.write(b'\\n')

print('Encryption complete.')

"""

print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 1)/1}")
