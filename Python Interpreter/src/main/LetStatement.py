'''
Created on Apr 27, 2013

@author: Cisco
'''
from BasicStatement import BasicStatement
from Memory import Memory

class LetStatement(BasicStatement):
    def __init__(self, var, expr):
        super(LetStatement, self).__init__()
        try:
            self.var = var
            self.expr = expr
        except:
            raise Exception("null arguments")
        
    def execute(self, prog):
        Memory.store(self.var.getCh(), self.expr.evaluate())