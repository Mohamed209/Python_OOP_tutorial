class Fraction:
    def __init__(self,top,bottom):
        self.num=top
        self.dom=bottom
    def show(self):
        print(self.num,"/",self.dom)
    # implement function to add two fractions
    def add(self,otherfraction):
        #a/b+c/d=ad/bd+cb/bd=ad+cbbd
        newnum = self.num * otherfraction.dom + self.dom * otherfraction.num
        newden = self.dom * otherfraction.dom
        # return new object with newum and newden
        return Fraction(newnum,newden)
    # function to reduce fraction if num is devided by dom
    '''def reduce(self):
        if(self.num>self.dom and self.num%self.dom==0):
            self.num=int(self.num/self.dom)
            self.dom=1
            return self.num
        elif (self.num==self.dom):
            self.num=1
            self.dom=1
            return self.num
        else :pass
    '''
f1=Fraction(1,2)
f2=Fraction(4,2)
f3=f1.add(f2)
f3.show()