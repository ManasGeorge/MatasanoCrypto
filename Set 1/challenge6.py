from base64 import b64decode
from operator import itemgetter
from utilities import hamming, single_char_xor, xor_hex_strings, freq_hist_score, construct_hist, xor_strings
from binascii import hexlify, unhexlify

def find_key_len(ciphertext):
	scores = {}
	min_score_key = 50
	min_score = 50
	for l in range(3,50):
		score  = hamming(ciphertext[:l], ciphertext[l:2*l]) / float(l)
		score += hamming(ciphertext[2*l:3*l], ciphertext[3*l:4*l]) / float(l)
		score += hamming(ciphertext[4*l:5*l], ciphertext[5*l:6*l]) / float(l)
		score += hamming(ciphertext[6*l:7*l], ciphertext[7*l:8*l]) / float(l)
		score /= 4

		scores[l] = score

	s = sorted(scores.iteritems(), key = itemgetter(1))
	print s
	return s[0][0]
		

def scx(string):
	f = open("huckfinn.txt")
	freqs = construct_hist(f.read())
	n = len(string)
	sc = float("inf")
	for c in map(chr,range(256)):
		m = xor_strings(string, c*n)
		if (freq_hist_score(freqs, m) < sc):
			sc = freq_hist_score(freqs, m)
			can = m
			k = c*n

	return k

def main():
	f = open("6.txt", 'r')
	ciphertext = "".join(map(b64decode,(f.read().split('\n'))))
	print len(ciphertext)
	key_len = find_key_len(ciphertext)
	blocks = ["".join(ciphertext[z::key_len]) for z in range(key_len)]

	key = ""
	for block in blocks:
		k = scx(block)
		key += k

	print key
	l = len(ciphertext)
	# kx = key * (l / key_len)
	# print (xor_strings(key, ciphertext))

if __name__ == "__main__":
	print
	main()