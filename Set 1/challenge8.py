def main():
	f = open('8.txt', 'r')
	ciphertext = f.readlines()

	most_equal_blocks = -float("inf") 
	ecb_candidate = ""
	for text in ciphertext:
		text = text[:-1] #strip newline
		equal_blocks = count_equal_blocks(text, 16)
		if equal_blocks > most_equal_blocks:
			most_equal_blocks = equal_blocks
			ecb_candidate = text

	print most_equal_blocks
	for block in split_list(ecb_candidate, 16):
		print block

def count_equal_blocks(text,blocksize):
	blocks = split_list(text, blocksize)
	counts = [blocks.count(x) for x in blocks]
	return sum(counts)

def split_list(list,size):
	return [list[x:x+size] for x in range(0,len(list)-size,size)]
	
main()