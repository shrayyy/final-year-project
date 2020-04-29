import nacl.encoding
import nacl.signing

# Generate a new random signing key
signing_key = nacl.signing.SigningKey.generate()

# Sign a message with the signing key
signed = signing_key.sign(b"Attack at Dawn")

# Obtain the verify key for a given signing key
verify_key = signing_key.verify_key

# Serialize the verify key to send it to a third party
verify_key_hex = verify_key.encode(encoder=nacl.encoding.HexEncoder)

print(verify_key_hex)
print(signed)
sig_file = open("DS-Signature.dsig",'wb')
sig_file.write(verify_key_hex)
sig_file.close()

signed_file = open("DS-SignedData.data",'wb')
signed_file.write(signed)
signed_file.close()

