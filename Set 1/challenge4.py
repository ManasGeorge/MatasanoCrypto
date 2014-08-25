import binascii
import string
from math import log
from wordscore import find_probs, score

def xors(a,b):
	return "{0:0{1}x}".format((int(a,16) ^ int(b,16)),max(len(a),len(b)))

def main():
	probs = find_probs("huckfinn.txt")
	print "Done settling n-gram probs"
	f = open("4.txt")

	candidate = ""
	sc = -float("inf")

	for s in f.read().split('\n'):
		n = len(s)/2
		for i in range(1,256):
			k = "{0:02x}".format(i) * n
			m = binascii.unhexlify(xors(s,k))
			if(score(probs,m) >= sc):
				candidate = m
				sc = score(probs, m)

	print candidate
	print sc

if __name__ == "__main__":
	# print
	main()
