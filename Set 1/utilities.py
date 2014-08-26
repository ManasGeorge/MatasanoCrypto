from math import log
import base64

def bigram_prob(f):
	probs = {}
	for word in f:
		for x,y in zip(word,word[1:]):
			p = probs.get((x,y), 0)
			probs[x,y] = float(p+1)
	return probs

def trigram_prob(f):
	probs = {}
	for word in f:
		for x,y,z in zip(word,word[1:],word[2:]):
			p = probs.get((x,y,z), 0)
			probs[x,y,z] = float(p+1)
	return probs

def find_probs(file):
	f = open(file,'r')
	probs = bigram_prob(f)
	n = sum(probs.values())

	for k in probs.keys():
		probs[k] /= n

	return probs

def score(probs, string):
	score = 1
	
	for x,y in zip(string,string[1:]):
		p = probs.get((x,y), -float("inf"))
		if p == -float("inf"):
			return p
		score *= p
	
	if string == " ":
		return -float("inf")
	
	return log(score) / len(string)

def hextob64(h):
	return base64.b64encode(binascii.unhexlify(h))

def xor_hex_strings(a,b):
	return {"0:0{1}x"}.format(int(a,16) ^ int(b,16),max(len(a),len(b)))

def xor_strings(a,b):
	z = ""
	for x,y in zip(a,b):
		z += str(chr(ord(x)^ord(y)))
	return z

def hamming(a,b):
	x = xor_strings(a,b)
	diff = 0
	for c in x:
		binary = "{0:b}".format(ord(c))
		diff += sum(map(int, binary))
	return diff

def main():
	print "main"

if __name__ == "__main__":
	print
	main()