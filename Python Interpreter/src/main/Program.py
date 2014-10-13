'''
Created on Apr 27, 2013

@author: Cisco
'''
from Statement import Statement
from StopStatement import StopStatement
from ParserException import ParserException
from InvalidProgramTerminationException import InvalidProgramTerminationException
from MissingStatementException import MissingStatementException

class Program(object):  
    
    def __init__(self):
        self.statements = [0]*1000
        self.programCounter = -1
        self.branchInstruction = False
        
        
    def add(self, stmt):
        if (not self.statements[stmt.getLineNumber()]):
            self.statements[stmt.getLineNumber()] = stmt.getBasicStatement()
        else:
            raise ParserException("duplicate line number", stmt.getLineNumber())
        
    def setProgramCounter(self, programCounter):
        if (programCounter < Statement.Min_Line_Number or programCounter > Statement.Max_Line_Number):
            raise ParserException("duplicate line number", programCounter)
        self.programCounter = programCounter
        self.branchInstruction = True        
        
    def execute(self):
        self.findNextInstruction()
        stmt = self.statements[self.programCounter]
        while not (isinstance(stmt, StopStatement)):
            stmt.execute(self)
            if(self.branchInstruction):
                self.branchInstruction = False
            else:
                self.findNextInstruction()
            stmt = self.statements[self.programCounter]
            if not(stmt):
                raise MissingStatementException("no statement at this line number ", self.programCounter)
            
    def findNextInstruction(self):
        self.programCounter += 1
        while((self.programCounter < Statement.Max_Line_Number) and not (self.statements[self.programCounter])):
            self.programCounter += 1
        if (self.programCounter >= Statement.Max_Line_Number):
            raise InvalidProgramTerminationException("Invalid Program Termination")        
        
        0
        