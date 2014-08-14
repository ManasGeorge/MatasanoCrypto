import binascii
import base64

h = "49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d"
s = binascii.unhexlify(h)

print base64.b64encode(s)

# The hex string represents an ASCII string, which is what must be converted to Base64