'''
Created on Apr 27, 2013

@author: Cisco
'''
class TokenType(object):
    IDENT, INT_LIT, ASSIGN_OP, ADD_OP, SUB_OP, MULT_OP, DIV_OP, LE, LT, GT, GE, EQ, NE, EOLN, EOS, IF, PRINT, LET, GOTO, STOP = range(1, 21)
