'''
Created on Apr 27, 2013

@author: Cisco
'''

from BasicStatement import BasicStatement
from Statement import Statement

class GotoStatement(BasicStatement):
    def __init__(self, lineNum):
        super(GotoStatement, self).__init__()
        if (lineNum < Statement.Min_Line_Number or lineNum > Statement.Max_Line_Number):
            raise Exception("")
        self.lineNum = lineNum
        
    def execute(self, prog):
        try:
            prog.setProgramCounter(self.lineNum)
        except:
            raise Exception("null Program argument")
        