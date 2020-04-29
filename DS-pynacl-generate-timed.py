import timeit

setup_code = """

import nacl.encoding
import nacl.signing
"""

statement = """

# Generate a new random signing key
signing_key = nacl.signing.SigningKey.generate()

# Sign a message with the signing key
#signed = signing_key.sign(b"Attack at Dawn")
with open("..\\data\\MB500.file",'rb') as infile:    # change filename
    msg = infile.read()
    signed = signing_key.sign(msg)
# Obtain the verify key for a given signing key
verify_key = signing_key.verify_key

# Serialize the verify key to send it to a third party
verify_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder)

#print(verify_key_hex)
print('signed')
sig_file = open("..\\data\\MB500-Gen-DS.sig",'wb')    # change filename
sig_file.write(verify_key_hex)
sig_file.close()

signed_file = open("..\\data\\MB500-SignedData-DS.data",'wb')    # change filename
signed_file.write(signed)
signed_file.close()

"""

print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 5)/5}")
