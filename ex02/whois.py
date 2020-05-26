import sys


def whois(nb):
	if nb == 0:
		print("I'm Zero")
	else:
		nb2 = nb % 2
		if nb2 == 0:
			print("I'm Even")
		else:
			print("I'm Odd")


if len(sys.argv) != 2:
	print("Error")
elif not str(sys.argv[1]).isnumeric():
	print("Error")
else:
	whois(nb=int(sys.argv[1]))
