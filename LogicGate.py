class LogicGate:
    def __int__(self,label):
        self.label=label
        self.output=None
    def get_output(self):
        self.output=self.perfrom_logic()
        return self.output
