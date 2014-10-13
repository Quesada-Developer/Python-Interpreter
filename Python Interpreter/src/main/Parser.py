'''
Created on Apr 27, 2013

@author: Cisco
'''

from Program import Program
from ParserException import ParserException
from LexicalAnalyzer import LexicalAnalyzer
from Statement import Statement
from TokenType import TokenType
from StopStatement import StopStatement
from GotoStatement import GotoStatement
from IfStatement import IfStatement
from PrintStatement import PrintStatement
from LetStatement import LetStatement
from BooleanExpression import BooleanExpression
from Expression import Expression
from LiteralInteger import LiteralInteger
from Id import Id

class Parser(object):
    
    def __init__(self, fileName):
        if not fileName:
            raise Exception ("null string argument")
        self.lex = LexicalAnalyzer(fileName)
        
    def parse(self):
        prog = Program()
        tok = self.lex.getLookaheadToken()
        while(tok.getTokenType() != TokenType.EOS):
            stmt = self.getStatement()
            prog.add(stmt)
            tok = self.lex.getLookaheadToken()
        return prog
    
    def getStatement(self):
        lineNum = self.getLineNumber()
        stmt = self.getBasicStatement()
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.EOLN)
        return Statement(lineNum, stmt)
    
    def getBasicStatement(self):
        tok = self.lex.getLookaheadToken()
        if(tok.getTokenType() == TokenType.PRINT):
            stmt = self.getPrintStatement()
        elif(tok.getTokenType() == TokenType.IF):
            stmt = self.getIfStatement()
        elif(tok.getTokenType() == TokenType.LET):
            stmt = self.getLetStatement()
        elif(tok.getTokenType() == TokenType.GOTO):
            stmt = self.getGotoStatement()
        elif(tok.getTokenType() == TokenType.STOP):
            stmt = self.getStopStatement();
        else:
            raise ParserException("statement expected at line number: ", tok.getLineNumber(), tok.getColumnNumber())
        return stmt
    
    def getStopStatement(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.STOP)
        return StopStatement()
    
    def getGotoStatement(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.GOTO)
        lineNum = self.getLineNumber()
        return GotoStatement(lineNum)
    
    def getLetStatement(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.LET)
        var = self.getId()
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.ASSIGN_OP)
        expr = self.getExpression()
        return LetStatement(var, expr)
    
    def getIfStatement(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.IF)
        bexpr = self.getBooleanExpression()
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.GOTO)
        lineNum = self.getLineNumber()
        return IfStatement(bexpr, lineNum)
    
    def getPrintStatement(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.PRINT)
        var = self.getId()
        return PrintStatement(var)
    
    def getBooleanExpression(self):
        op = self.getRelativeOperator()
        expr1 = self.getExpression()
        expr2 = self.getExpression()
        return BooleanExpression(op, expr1, expr2)
    
    def getRelativeOperator(self):
        tok = self.lex.getNextToken()
        if(tok.getTokenType() == TokenType.LT):
            op = BooleanExpression.LT
        elif(tok.getTokenType() == TokenType.LE):
            op = BooleanExpression.LE
        elif(tok.getTokenType() == TokenType.EQ):
            op = BooleanExpression.EQ
        elif(tok.getTokenType() == TokenType.NE):
            op = BooleanExpression.NE
        elif(tok.getTokenType() == TokenType.GT):
            op = BooleanExpression.GT
        elif(tok.geTokenType() == TokenType.GE):
            op = BooleanExpression.GE
        else:
            raise ParserException("relative operator expected at line number: ", tok.getLineNumber(), tok.getColumnNumber())
        return op
    
    def getLineNumber(self):
        tok = self.lex.getNextToken()
        self.match(tok, TokenType.INT_LIT)
        try:
            num = int(tok.getLexeme())
        except:
            raise ParserException("invalid line number expected at line number: ", tok.getLineNumber(), tok.getColumnNumber())
        if(num < Statement.Min_Line_Number or num > Statement.Max_Line_Number):
            raise ParserException("invalid line number expected at line number: ", tok.getLineNumber(), tok.getColumnNumber())
        return num
    
    def getExpression(self):
        tok = self.lex.getLookaheadToken()
        if(tok.getTokenType() == TokenType.IDENT):
            expr = self.getId()
        elif(tok.getTokenType() == TokenType.INT_LIT):
            expr = self.getLiteralInteger()
        else:
            op = self.getArithmeticOperator()
            expr1 = self.getExpression()
            expr2 = self.getExpression()
            expr = Expression(op, expr1, expr2)
        return expr
    
    def getArithmeticOperator(self):
        tok = self.lex.getNextToken()
        if(tok.getTokenType() == TokenType.ADD_OP):
            op = Expression.ADD
        elif(tok.getTokenType() == TokenType.SUB_OP):
            op = Expression.SUB
        elif(tok.getTokenType() == TokenType.MULT_OP):
            op = Expression.MUL
        elif(tok.getTokenType() == TokenType.DIV_OP):
            op = Expression.DIV
        else:
            raise ParserException("arithemetic operator expected at line number: ", tok.getLineNumber(), tok.getColumnNumber())
        return op

    def getLiteralInteger(self):
        tok = self.lex.getNextToken()
        try:
            value = int(tok.getLexeme())
        except:
            raise ParserException("literal integer expected at line number: ", tok.getLineNumber(), tok.getColumnNumber())
        return LiteralInteger(value)
    
    def getId(self):
        tok = self.lex.getNextToken()
        return Id(str(tok.getLexeme())[0])
    
    def match(self, tok, expected):
        if(expected != tok.getTokenType()):
            raise ParserException("wrong expected token at line number: ", tok.getLineNumber(), tok.getColumnNumber())
        