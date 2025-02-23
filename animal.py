import sys
def cat():
	print("I am a cat")

def default():
	print("Hello World")

def main():
	if sys.argv[1] == 'cat':
		cat()
	else:
		default()

if __name__ == '__main__':
    main()
