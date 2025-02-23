import sys
def dog():
	print("I am a dog")
def default():
	print("Hello World")
def main():
	if sys.argv[1] == "dog":
		dog()
	else:
		default()
if __name__ == '__main__':
    main()
