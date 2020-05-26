import sys
import string


languages = {
    'Python': 'Guido van Rossum',
    'Ruby': 'Yukihiro Matsumoto',
    'PHP': 'Rasmus Lerdorf',
    }

x = list(languages.keys())
print(x[0], "was created by", languages[str(x[0])])
print(x[1], "was created by", languages[str(x[1])])
print(x[2], "was created by", languages[str(x[2])])
