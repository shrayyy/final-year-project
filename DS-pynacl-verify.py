import nacl.signing

sig_file = open("..\\data\\MB10-Gen-DS.sig",'rb')
verify_key_hex = sig_file.read()
sig_file.close()
# Create a VerifyKey object from a hex serialized public key
verify_key = nacl.signing.VerifyKey(verify_key_hex, encoder=nacl.encoding.HexEncoder)

# Check the validity of a message's signature
# The message and the signature can either be passed separately or
# concatenated together.  These are equivalent:
signed_file = open("..\\data\\MB10-SignedData-DS.data",'rb')
signed = signed_file.read()
signed_file.close()
try:
    if verify_key.verify(signed):
        print('Signature Verified')
except:
    print('Signature Verification Failed!')
#verify_key.verify(signed.message, signed.signature)
