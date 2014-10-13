'''
Created on Apr 27, 2013

@author: Cisco
'''

class BooleanExpression(object):
    
    LT,LE,EQ,NE,GT,GE = range(6)
    
    def __init__(self, op, expr1, expr2):
        try:
            self.op = op
            self.expr1 = expr1
            self.expr2 = expr2
        except:
            raise Exception("null expression argument")
        
    def evaluate(self):
        result = {
               self.LT: self.expr1.evaluate() < self.expr2.evaluate(),
               self.LE: self.expr1.evaluate() <= self.expr2.evaluate(),
               self.EQ: self.expr1.evaluate() == self.expr2.evaluate(),
               self.NE: self.expr1.evaluate() != self.expr2.evaluate(),
               self.GT: self.expr1.evaluate() > self.expr2.evaluate(),
               self.GE: self.expr1.evaluate() >= self.expr2.evaluate()
               }[self.op]
        return result
        