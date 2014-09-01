from base64 import b64decode
from math import sqrt, log
from binascii import hexlify, unhexlify

def hamming(a,b):
	return sum(map(int,"{0:b}".format(int(hexlify(xor_s(a,b)),16))))

def find_key_len_candidates(string):
	min_score_len_candidates = []
	min_score = float("inf")
	for l in range(10,40):
		score = hamming(string[:l],string[l:2*l])
		score += hamming(string[2*l:3*l],string[3*l:4*l])
		score += hamming(string[4*l:5*l],string[5*l:6*l])
		score += hamming(string[6*l:7*l],string[7*l:8*l])

		score /= float(8 * l)
		# print l,":",score
		if score < min_score:
			min_score = score
			min_score_len_candidates.append(l)

	min_score_len_candidates.sort()
	return min_score_len_candidates[:5]

def transpose_block(string, size):
	return [string[z::size] for z in range(size)]

def compute_histogram(string):
	hist = {}
	for c in string:
		hist[c] = hist.get(c,0) + 1
	n = sum(hist.values())
	for k,v in hist.iteritems():
		hist[k] = float(v) / n;
	return hist

def score(string):
	score = 0
	dist = compute_histogram(string)
	for c in string:
		score += (dist[c] - norm_freq.get(c,100))**2
	score = sqrt(score) / len(string)
	return score

def xor_s(a,b):
	if(len(a) != len(b)):
		print "Size mismatch",a,b,len(a),len(b)
	else:
		res = ""
		for x,y in zip(a,b):
			res += chr(ord(x) ^ ord(y))
		return res

def single_char_xor_key(string):
	best_key = ""
	best_score = float("inf")
	for c in range(256):
		key = chr(c)  * (len(string))
		sc = score(xor_s(string, key))
		if sc < best_score:
			# print sc
			best_score = sc
			best_key = key

	# print "-"*50
	return best_key[0]

def main():
	f = open("6.txt",'r')
	ciphertext = f.read()
	ciphertext = b64decode(ciphertext)

	key_lens = find_key_len_candidates(ciphertext)

	candidate_plaintext = ""
	min_score = float("inf")
	for key_len in key_lens:
		blocks = transpose_block(ciphertext, key_len)
		key = ""
		for block in blocks:
			key += single_char_xor_key(block)

		key = (key * (len(ciphertext) / key_len + 1))[:len(ciphertext)]
		candidate_plaintext = xor_s(ciphertext, key)

		if score(candidate_plaintext) < min_score:
			plaintext = candidate_plaintext
			min_score = score(candidate_plaintext)

	print plaintext

def test():
	f = open("6.txt",'r')
	ciphertext = f.read()
	ciphertext = b64decode(ciphertext)
	key_len = find_key_len(ciphertext)
	# ciphertext = unhexlify("7b5a4215415d544115415d5015455447414c155c46155f4058455c5b523f")
	# key = single_char_xor_key(ciphertext)
	# key = key * (len(ciphertext) / len(key))
	# print xor_s(key, ciphertext)
	# f = open("4.txt",'r')
	# blocks = f.read().split('\n')


g = open("huckfinn.txt")
norm_freq = compute_histogram(g.read())
print
main()
# test()