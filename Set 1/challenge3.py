import binascii
import string

def xors(a,b):
	return "{0:0{1}x}".format((int(a,16) ^ int(b,16)),max(len(a),len(b)))

def main():
	s = "1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736"
	n = len(s)/2

	print

	for i in range(1,256):
		k = hex(i)[2:] * n
		m = binascii.unhexlify(xors(s,k))
		fm = "".join(c for c in m if c in string.printable)
		if len(fm) == n:
			print fm


if __name__ == "__main__":
	main()