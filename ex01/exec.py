import sys


def ft_exec(s1):
	size = 1
	list1 = list(s1)
	list2 = sys.argv
	while size != len(sys.argv):
		i = len(sys.argv[size]) - 1
		j = 0
		while i != -1:
			if 65 <= ord(list2[size][i]) <= 90:
				list1.insert(j, chr(ord(list2[size][i]) + 32))
			elif 97 <= ord(list2[size][i]) <= 122:
				list1.insert(j, chr(ord(list2[size][i]) - 32))
			else:
				list1.insert(j, list2[size][i])
			j += 1
			i -= 1
		list1.insert(j, ' ')
		size += 1
	s1 = ''.join(list1)
	print(s1)
	return


str1 = ''
ft_exec(str1)
