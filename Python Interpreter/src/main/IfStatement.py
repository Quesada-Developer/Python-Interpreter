'''
Created on Apr 27, 2013

@author: Cisco
'''

from BasicStatement import BasicStatement
from Statement import Statement

class IfStatement(BasicStatement):
    def __init__(self, bexpr, lineNum):
        super(IfStatement, self).__init__()
        if bexpr is None:
            raise Exception("")
        if (lineNum < Statement.Min_Line_Number or lineNum > Statement.Max_Line_Number):
            raise Exception("")
        self.lineNum = lineNum
        self.bexpr = bexpr
        
    def execute(self, prog):
        if(self.bexpr.evaluate()):
            prog.setProgramCounter(self.lineNum);
        