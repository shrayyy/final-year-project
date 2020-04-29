import timeit

setup_code = """
import os, random, struct
from Crypto.Cipher import AES
"""

statement = """

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):

    if not out_filename:
        out_filename = in_filename + '.enc'

    iv = (16 * '\x01')
    x = bytes(iv, 'utf8')
    print(x,len(x))
    encryptor = AES.new(key, AES.MODE_CBC, x)
    filesize = os.path.getsize(in_filename)

    with open(in_filename, 'rb') as infile:
        with open(out_filename, 'wb') as outfile:
            outfile.write(struct.pack('<Q', filesize))
            outfile.write(x)

            while True:
                chunk = infile.read(chunksize)
                if len(chunk) == 0:
                    break
                elif len(chunk) % 16 != 0:
                    chunk += b' ' * (16 - len(chunk) % 16)

                outfile.write(encryptor.encrypt(chunk))


key2 = b'0123456789abcdef0123456789abcdef'  # 16 byte key, can use bigger - more bigger means more stronger
encrypt_file(key2,"..\\data\\MB500.file", "..\\data\\MB500-E-AES-256.encr", 64)

"""

print(f"Execution time is: {timeit.timeit(setup = setup_code, stmt = statement, number = 5)/5}")
