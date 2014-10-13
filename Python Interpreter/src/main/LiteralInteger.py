'''
Created on Apr 27, 2013

@author: Cisco
'''
from Expression import Expression

class LiteralInteger(Expression):
    def __init__(self, value):
        self.value = value
        
    def evaluate(self):
        return self.value