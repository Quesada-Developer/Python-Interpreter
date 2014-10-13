'''
Created on Apr 27, 2013

@author: Cisco
'''
from BasicStatement import BasicStatement
from Memory import Memory

class PrintStatement(BasicStatement):
    def __init__(self, var):
        super(PrintStatement, self).__init__()
        self.var = var
        

    def execute(self, prog):
        print(Memory.fetch(self.var.getCh()))
        