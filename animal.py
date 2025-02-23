#这是一条注释
import sys
def cat():
	print("I am a cat")

def dog():
	print("I am a dog")

def default():
	print("Hello World")

def main():
	if sys.argv[1] == 'cat':
		cat()
	elif sys.argv[1] == "dog":
		dog()
	else:
		default()
if __name__ == '__main__':
    main()
