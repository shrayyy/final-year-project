from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
import binascii
import time

start_time = time.time()
# Import Private key

privateKeyFile = open("..\\data\\KB50-RSA-privKeyPair.pem",'r')      # change name here
privKey = RSA.importKey(privateKeyFile.read())
privateKeyFile.close()

# Decryption

decryptor = PKCS1_OAEP.new(privKey)

in_filename = "..\\data\\KB50-E-RSA.encr"    # path to encrypted file
out_fileRvd = "..\\data\\KB50-D-RSA.recovered.file"      # Path to decrypted file

infile = open(in_filename, 'rb')
outfile = open(out_fileRvd,'wb')

while True:
    chunk = infile.readline()
    chunk = chunk.strip(b'\n')
    iv = b'a\x83\xaeN\x07p\xd9\xe0\xf4Ij\x88\x1d\xc7V\xf0\x87%\x99\xb7\xdf\xae-\xc6Y8\xbb\xad4\xc2\x92q\x96\xc4\xb3\x1f\xf9\x84\xe4n\xd9\xe9\x02\xf7ou\xd5^s\x87\x8awCMUx\xa1\xd2\xcds\x84\xa3\xf1\x83Q\xe1\xf7C\x04\x82\x8b\x03\x90\x02\xf5\x94\xfa\r\xc6\xed-\xa1\xb7\x80\xe9\xd9fA^\xbc\x11(r|\x98\xa2\xbf.\xa4\xb8\xc5l\xc7\xee\xc0\n\x94J\x956"q\x19$<5D\xeeHTelM\xdf\xac\xa5qG'
    if not chunk:
        break
    outfile.write(decryptor.decrypt(iv))

print('Decrypted!')
infile.close()
outfile.close()

#print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 5)/5}")

end_time = time.time()

print(f"Runtime of the program is {end_time - start_time}")
