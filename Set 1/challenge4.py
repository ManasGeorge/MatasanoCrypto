import binascii
import string
from math import log
from utilities import construct_hist, freq_hist_score, xor_hex_strings, find_probs, score, single_char_xor

def main():
	f = open("4.txt")
	print single_char_xor(f.read().split('\n'))

if __name__ == "__main__":
	print
	main()