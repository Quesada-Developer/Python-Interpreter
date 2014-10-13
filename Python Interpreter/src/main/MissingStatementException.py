'''
Created on Apr 28, 2013

@author: Cisco
'''
class MissingStatementException(Exception):
    
    def __init__(self, message, lineNumber):
        self.message = message
        if(not message):
            raise Exception("null string argument")
        self.lineNumber = lineNumber
        
    def __str__(self):
        return self.message + str(self.lineNumber)