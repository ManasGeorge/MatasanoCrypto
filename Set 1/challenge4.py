import binascii
import string

def xors(a,b):
	return "{0:0{1}x}".format((int(a,16) ^ int(b,16)),max(len(a),len(b)))

def main():
	f = open("4.txt")
	print

	for s in f.read().split('\n'):
		n = len(s)/2
		for i in range(1,256):
			k = "{0:02x}".format(i) * n
			m = binascii.unhexlify(xors(s,k))
			fm = "".join(c for c in m if c in string.printable)
			if len(fm) == n and fm.count(' ') > 3:
				print fm


if __name__ == "__main__":
	main()
