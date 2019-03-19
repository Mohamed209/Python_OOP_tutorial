from utility_functions import gcd
class Fraction:
    def __init__(self,top,bottom):
        self.num=top
        self.dom=bottom
    def show(self):
        print(self.num,"/",self.dom)
    # implement function to add two fractions
    def add(self,otherfraction):
        newnum = self.num * otherfraction.dom+ self.dom * otherfraction.num
        newdom = self.dom * otherfraction.dom
        common = gcd(newnum, newdom)
        # return a new object
        return Fraction(newnum // common, newdom // common)
f1=Fraction(1,2)
f2=Fraction(4,2)
f3=f1.add(f2)
f3.show()