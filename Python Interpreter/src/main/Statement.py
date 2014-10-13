'''
Created on Apr 27, 2013

@author: Cisco
'''

class Statement(object):
    Max_Line_Number = 999
    Min_Line_Number = 0
    
    def __init__(self, lineNum, stmt):
        if(not stmt):
            raise Exception("null statement argument")
        if (lineNum < self.Min_Line_Number or lineNum > self.Max_Line_Number):
            raise Exception("invalid line number argument")
        self.lineNum = lineNum
        self.stmt = stmt
        
    def getLineNumber(self):
        return self.lineNum
    
    def getBasicStatement(self):
        return self.stmt