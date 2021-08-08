#Write a function named capital_indexes.
#The function takes a single parameter, which is a string.
#Your function should return a list of all the indexes in the string that have capital letters.

#For example, calling capital_indexes("HeLlO") should return the list [0, 2, 4].


class capitalindex():
    def capital_indexs(self,input_str):
        return [i for i in range(len(input_str)) if input_str[i].isupper()]

index_obj = capitalindex()

print(index_obj.capital_indexs("HeLlO"))

