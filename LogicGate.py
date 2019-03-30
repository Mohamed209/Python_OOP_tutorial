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
    # overriding parent class init method
    def __init__(self,label):
        LogicGate.__init__(self,label) # init binary gate is the same as logic gate , but with two new lines of code ,that init input
        self.pin1=None # input 1
        self.pin2=None # input 2
    # get input for the gate
    def getPin1(self):
        return int(input("Enter Pin 1 input for gate " + self.get_label() + "-->"))
    def getPin2(self):
        return int(input("Enter Pin 2 input for gate " + self.get_label()+ "-->"))
    def setNextPin(self,dest):
        if self.pinA == None:
            self.pinA = dest
        else:
            if self.pinB == None:
                self.pinB = dest
            else:
                print("Cannot Connect: NO EMPTY PINS on this gate")
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
class OrGate(BinaryGate):
    def __int__(self,label):
        BinaryGate.__init__(self,label)
    def perform_logic(self):
        a,b=[self.getPin1(),self.getPin2()]
        return (a or b)
# connector class implements HAS-A relationship
class Connector:
    def __init__(self,gatefrom,gateto): # init with two gates
        self.gatefrom=gatefrom
        self.gateto=gateto

        gateto.setNextPin(self)

    def get_gatefrom(self):
        return self.gatefrom
    def get_gateto(self):
        return self.gateto
g1=AndGate("and1")
print("gate name",g1.get_label())
print("gate inputs ",g1.pin1,g1.pin2,"gate output",g1.output)
print(g1.get_output())
g2=OrGate("or1")
print("gate name",g2.get_label())
print("gate inputs ",g2.pin1,g2.pin2,"gate output",g2.output)
print(g2.get_output())