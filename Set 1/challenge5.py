def otp(string, key):
	n = len(string);
	key = (key * (n / len(key))) + key[:(n % len(key))];
	output = ""

	for x,y in zip(string,key):
		output += "{0:02x}".format(ord(x) ^ ord(y))

	return output

def main():
	string = "Burning 'em, if you and quick and nimble I go crazy when I hear a cymbals"
	key = "ICE"
	print otp(string, key)

if __name__ == "__main__":
	print
	main()