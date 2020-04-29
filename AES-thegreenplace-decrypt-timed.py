import timeit

setup_code = """
import os, random, struct
from Crypto.Cipher import AES
"""

statement = """

def decrypt_file(key, in_filename, out_filename=None, chunksize=24*1024):
    
    if not out_filename:
        out_filename = os.path.splitext(in_filename)[0]

    with open(in_filename, 'rb') as infile:
        origsize = struct.unpack('<Q', infile.read(struct.calcsize('Q')))[0]
        iv = infile.read(16)
        decryptor = AES.new(key, AES.MODE_CBC, iv)

        with open(out_filename, 'wb') as outfile:
            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                outfile.write(decryptor.decrypt(chunk))

            outfile.truncate(origsize)

#key2 = b'0123456789abcdef'      # 16 byte
#key2 = b'0123456789abcdef01234567'     # 24 byte
key2 = b'0123456789abcdef0123456789abcdef'     # 32 byte
decrypt_file(key2, "..\\data\\MB500-E-AES-256.encr", "..\\data\\MB500-D-AES-256.recovered.file", 64)

"""


print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 5)/5}")
