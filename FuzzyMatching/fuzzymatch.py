from fuzzywuzzy import process
from fuzzywuzzy import fuzz
from fuzzywuzzy import process

s1 = "This is sample test for fuzzy wuzzy"
s2 = "This is sample for fuzzy"
print("FuzzyWuzzy Ratio: ", fuzz.ratio(s1, s2))
print("FuzzyWuzzy PartialRatio: ", fuzz.partial_ratio(s1, s2))
print("FuzzyWuzzy TokenSortRatio: ", fuzz.token_sort_ratio(s1, s2))
print("FuzzyWuzzy TokenSetRatio: ", fuzz.token_set_ratio(s1, s2))
print("FuzzyWuzzy WRatio: ", fuzz.WRatio(s1, s2))
print("               ")
print("               ")


# for process library,
query = 'fuzzy for matching strings'
choices = ['fuzzy for matching', 'fuzzy fuzzy', 'fs. for fuzzy strings']
print("List of ratios: ")
print(process.extract(query, choices))
print("Best among the above list: ", process.extractOne(query, choices))