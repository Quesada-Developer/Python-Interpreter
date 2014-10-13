'''
Created on Apr 27, 2013

@author: Cisco
'''
class Token(object):
    
    def __init__(self, tok, lexeme, lineNum, columnNum):
        self.tok = tok
        self.lexeme = lexeme
        if (lineNum <= 0):
            raise Exception("invalid line number")
        self.lineNum = lineNum
        if (columnNum <= 0):
            raise Exception ("invalid column number")
        self.columnNum = columnNum
        
    def getTokenType(self):
        return self.tok
    
    def getLexeme(self):
        return self.lexeme
    
    def getLineNumber(self):
        return self.lineNum
    
    def getColumnNumber(self):
        return self.columnNum
    
    def __str__(self):
        return self.tok + ": " + self.lexeme + " row: " + self.lineNum + " column: " + self.columNum