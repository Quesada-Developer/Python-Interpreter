'''
Created on Apr 28, 2013

@author: Cisco
'''
class ParserException(Exception):
    
    def __init__(self, message, rowNum, columnNum="-1"):

        self.message = message
        if rowNum <= 0:
            raise ValueError ("invalid row number argument")
        self.rowNum = rowNum
        if columnNum <= 0:
            raise ValueError ("invalid column number argument")
        self.columnNum = columnNum  
        
    def __str__(self):
        return (self.message + " expected at row: " + str(self.rowNum) + " column: " + str(self.columnNum))
