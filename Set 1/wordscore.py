from math import log

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

def main():
	probs = find_probs("huckfinn.txt")

if __name__ == "__main__":
	print
	main()