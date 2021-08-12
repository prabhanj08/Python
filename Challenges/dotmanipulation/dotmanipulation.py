'''
Adding and removing dots
Write a function named add_dots that takes a string and adds "." in between each letter. For example, calling add_dots("test") should return the string "t.e.s.t".

Then, below the add_dots function, write another function named remove_dots that removes all dots from a string. For example, calling remove_dots("t.e.s.t") should return "test".

If both functions are correct, calling remove_dots(add_dots(string)) should return back the original string for any string.

(You may assume that the input to add_dots does not itself contain any dots.)
'''


class dots():
    def add_dots(self,st):
        return '.'.join(st)

    def remove_dots(self,st):
        return st.replace('.','')

    def dot_check(self,input_str):
        if '.' in input_str:
            return self.remove_dots(input_str)
        else:
            return self.add_dots(input_str)


if __name__ == '__main__':
    dotObj = dots()
    print(dotObj.dot_check('abc'))
    print(dotObj.dot_check('a.b.c'))

