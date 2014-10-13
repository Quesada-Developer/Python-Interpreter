'''
Created on Apr 27, 2013

@author: Cisco
'''
class Expression(object):
    
    def __init__(self, op, expr1, expr2):
        try:
            self.op = op
            self.expr1 = expr1
            self.expr2 = expr2
        except:
            raise Exception("null expression argument")
            
    ADD, SUB, MUL, DIV = range(4)
    def evaluate(self):
        value = {
                 self.ADD: self.expr1.evaluate() + self.expr2.evaluate(),
                 self.SUB: self.expr1.evaluate() - self.expr2.evaluate(),
                 self.MUL: self.expr1.evaluate() * self.expr2.evaluate(),
                 self.DIV: self.expr1.evaluate() / self.expr2.evaluate()}[self.op]
        return value
            
        