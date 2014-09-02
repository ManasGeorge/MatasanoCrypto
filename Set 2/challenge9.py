def pkcs_pad(string, blocksize):
	pad = blocksize - len(string)
	return string + ("\\x{0:02x}".format(pad)) * pad

def main():
	print pkcs_pad("YELL", 16)

main()