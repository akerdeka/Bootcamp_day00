import string


phrase = "The right format"
phrase = phrase.zfill(41)
phrase = phrase.replace("0", "-")
print(phrase)
