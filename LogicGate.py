class LogicGate: # super class Logic Gate
    def __init__(self,label):# init function to set label and output
        self.label=label
        self.output=None
    # function to check if input is valid boolean value
    '''ef check_valid_input(self):
        assert int(input()) is bool, "0 and 1 are only valid inputs"
        return True'''
    def get_label(self):
        return self.label
    def get_output(self):
        self.output=self.perform_logic()
        return self.output
class BinaryGate(LogicGate):# binary gate class inherits logic gate class
    def __init__(self,label):
        LogicGate.__init__(self,label) # init binary gate is the same as logic gate , but with two new lines of code ,that init input
        self.pin1=None # input 1
        self.pin2=None # input 2
    # get input for the gate
    def getPin1(self):
        return int(input("Enter Pin 1 input for gate " + self.get_label() + "-->"))
    def getPin2(self):
        return int(input("Enter Pin 2 input for gate " + self.get_label()+ "-->"))
class UnaryGate(LogicGate):
    def __init__(self,n):
        LogicGate.__init__(self,n)
        self.pin = None
    def getPin(self):
        return int(input("Enter Pin input for gate "+ self.get_label()+"-->"))
class AndGate(BinaryGate):
    def __int__(self,label):
        BinaryGate.__init__(self,label)
    def perform_logic(self):
        a,b=[self.getPin1(),self.getPin2()]
        return (a and b)
g1=AndGate("and1")
print("gate name",g1.get_label())
print("gate inputs ",g1.pin1,g1.pin2,"gate output",g1.output)
print(g1.get_output())