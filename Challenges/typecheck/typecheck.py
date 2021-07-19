#Write a function named only_ints that takes two parameters.
#Your function should return True if both parameters are integers, and False otherwise.

#For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.


class typecheck():
    def check(self,arg1,arg2):
        if type(arg1) == int:
            if type(arg1) == type(arg2):
                return True
            else:
                return False

if __name__ == "__main__":
    checkObj = typecheck()
    print(checkObj.check(1,2))
    print(checkObj.check(1, '2'))