'''
Created on Apr 27, 2013

@author: Cisco
'''

from Expression import Expression
from Memory import Memory

class Id(Expression):
    def __init__(self, ch):
        self.ch = ch
        
    def evaluate(self):
        return Memory.fetch(self.ch)
    
    def getCh(self):
        return self.ch