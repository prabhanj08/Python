#Write a function named mid that takes a string as its parameter.
#Your function should extract and return the middle letter.
#If there is no middle letter, your function should return the empty string.

#For example, mid("abc") should return "b" and mid("aaaa") should return "".

class middleletter():
    def mid(self,string):
        if len(string) % 2 == 0:
            return ""
        else:
            offset = int(len(string) / 2)
            return string[offset: offset + 1]


letter_obj = middleletter()
print(letter_obj.mid('abc'))
print(letter_obj.mid('abcd'))