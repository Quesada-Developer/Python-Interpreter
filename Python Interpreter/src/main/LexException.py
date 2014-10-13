'''
Created on Apr 28, 2013

@author: Cisco
'''
class LexException(Exception):
    def __init__(self, message, rowNumber, columnNumber):
        if(not message):
            raise Exception("null string argument")
        if(rowNumber <= 0):
            raise Exception("invalid row number argument")
        if(columnNumber <= 0):
            raise Exception("invalid column number argument")
        self.message = message
        self.rowNumber = rowNumber
        self.columNumber = columnNumber
        
    def __str__(self):
        return (self.message + " expected at row: " + str(self.rowNum) + " column: " + str(self.columnNum))
