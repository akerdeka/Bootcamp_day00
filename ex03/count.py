import sys
import string


def text_analyzer(s):
	up_case = 0
	low_case = 0
	spaces = s.count(' ')
	pun_mark = 0
	for c in s:
		up_case += c.isupper()
		low_case += c.islower()
		if c in string.punctuation:
			pun_mark += 1
	carac = up_case + low_case + spaces + pun_mark
	print("The text contains", carac, "characters")
	print(up_case, "upper letters")
	print(low_case, "lower letters")
	print(pun_mark, "punctuation marks")
	print(spaces, "spaces")
	return
