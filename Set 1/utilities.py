from math import log, sqrt
from binascii import unhexlify
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

def freq_hist_score(freq, string):
	hist = construct_hist(string)
	score = 0

	for k,v in hist.iteritems():
		score += (v - freq.get(k, float("inf")))**2
		if score == float("inf"):
			return score

	return sqrt(score) / len(string)

def construct_hist(string):
	hist = {}
	for c in string:
		hist[c] = hist.get(c,0) + 1

	n = sum(hist.values())
	if(n == 0):
		return {}

	for k,v in hist.iteritems():
		hist[k] = float(v)/n

	return hist

def hextob64(h):
	return base64.b64encode(binascii.unhexlify(h))

def xor_hex_strings(a,b):
	return "{0:0{1}x}".format(int(a,16) ^ int(b,16),max(len(a),len(b)))

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

def single_char_xor(strings):
	f = open("huckfinn.txt")
	fs = "".join(list(f))

	freqs = construct_hist(fs)

	candidate = ""
	key = ""
	sc = float("inf")

	for s in strings:
		n = len(s)/2
		for i in range(256):
			k = "{0:02x}".format(i) * n
			m = unhexlify(xor_hex_strings(s,k))
			if(freq_hist_score(freqs,m) < sc):
				print s
				candidate = m
				sc = freq_hist_score(freqs, m)
				key = "{0:02x}".format(i)

	return candidate, key

if __name__ == "__main__":
	print
	main()