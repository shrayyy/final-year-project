import os, random, struct
from Crypto.Cipher import AES

def encrypt_file(key, in_filename, out_filename=None, chunksize=64*1024):
    """ Encrypts a file using AES (CBC mode) with the
        given key.

        key:
            The encryption key - a string that must be
            either 16, 24 or 32 bytes long. Longer keys
            are more secure.

        in_filename:
            Name of the input file

        out_filename:
            If None, '<in_filename>.enc' will be used.

        chunksize:
            Sets the size of the chunk which the function
            uses to read and encrypt the file. Larger chunk
            sizes can be faster for some files and machines.
            chunksize must be divisible by 16.
    """
    if not out_filename:
        out_filename = in_filename + '.enc'

    #iv = ''.join(chr(random.randint(0, 0xFF)) for i in range(16))
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


key2 = b'0123456789abcdef'  # 16 bit key, can use bigger - more bigger means more stronger
encrypt_file(key2,"roadSurfaceMonitoring.jpg", "roadSurfaceMonitoring.encr", 16)
#encrypt_file(key2,"C:\\xampp\\tmp\\roadSurfaceMonitoring.jpg", "C:\\xampp\\tmp\\roadSurfaceMonitoring.encr", 16)
