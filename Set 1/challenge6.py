from utilities import hamming

def find_key_len(ciphertext):
	min_score_key = 50
	min_score = 50
	for l in range(3,50):
		score = hamming(ciphertext[:l], ciphertext[l:2*l]) / l
		if score < min_score:
			min_score_key = l
			min_score = score
	return min_score_key

def main():
	f = open("6.txt", 'r')
	ciphertext = "".join(f.readlines()).replace('\n','')
	key_len = find_key_len(ciphertext)
	blocks = ["".join(ciphertext[z::key_len]) for z in range(key_len)]

if __name__ == "__main__":
	print
	main()