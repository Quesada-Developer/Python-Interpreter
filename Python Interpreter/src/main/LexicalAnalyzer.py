'''
Created on Apr 27, 2013

@author: Cisco
'''
from Token import Token
from TokenType import TokenType
from LexException import LexException

class LexicalAnalyzer(object):
    
    tokens = []
    def __init__(self, fileName):
        try:
            self.lineNum = 0
            with open(fileName) as fileIn:
                for line in fileIn:
                    self.lineNum += 1
                    self.processLine(line, self.lineNum)
                    self.tokens.append(Token(TokenType.EOLN, "/n", self.lineNum, line.__len__()))
                
            self.tokens.append(Token(TokenType.EOS, "$", self.lineNum, line.__len__()))
        except:
            raise
        
    def processLine(self, line, rowNum):
        index = 0
        done = False
        while not done:
            index = self.skipWhiteSpace(line, index)
            if (index == line.__len__()):
                done = True
            else:
                columnNum = index + 1
                lexeme = self.getLexeme(line, index)
                index += lexeme.__len__()
                tok = self.getTokenType(lexeme, rowNum, columnNum)
                if (not tok):
                    raise LexException("invalid lexeme at ", rowNum, columnNum)
                t = Token(tok, lexeme, rowNum, columnNum)
                self.tokens.append(t)
                
    def getTokenType(self, lexeme, rowNum, columnNum):
        if(str.isalpha(lexeme[0])):
            if(lexeme.__len__() == 1 and str.isupper(lexeme[0]) ):
                tok = TokenType.IDENT
            elif (lexeme == 'LET'):
                tok = TokenType.LET
            elif (lexeme == 'GOTO'):
                tok = TokenType.GOTO
            elif (lexeme == 'IF'):
                tok = TokenType.IF
            elif (lexeme == 'PRINT'):
                tok = TokenType.PRINT
            elif (lexeme == 'STOP'):
                tok = TokenType.STOP
            else:
                raise LexException("invalid lexeme at ", rowNum, columnNum)
        elif(str.isalnum(lexeme[0])):
            i = 1
            while (i < lexeme.__len__() and str.isalnum(lexeme[i])):
                i += 1
            if (i == lexeme.__len__()):
                tok = TokenType.INT_LIT
            else:
                raise LexException("invalid lexeme at ", rowNum, columnNum)
        else:
            if(lexeme[0] == '<'):
                if(lexeme.__len__() == 1):
                    tok = TokenType.LT
                elif(lexeme.__len__() == 2 and lexeme[2] == '='):
                    tok = TokenType.LE
                elif(lexeme.__len__() == 2 and lexeme[2] == '>'):
                    tok = TokenType.NE
                else:
                    raise LexException("invalid lexeme at ", rowNum, columnNum)
            elif(lexeme[0] == '>'):
                if(lexeme.__len__() == 1):
                    tok = TokenType.GT
                elif(lexeme.__len__() == 2 and lexeme[1] == '='):
                    tok = TokenType.GE
                else:
                    raise LexException("invalid lexeme at ", rowNum, columnNum)
            elif(lexeme[0] == '='):
                if(lexeme.__len__() == 1):
                    tok = TokenType.ASSIGN_OP
                elif(lexeme.__len__() == 2 and lexeme[1] == '='):
                    tok = TokenType.EQ
                else:
                    raise LexException("invalid lexeme at ", rowNum, columnNum)
            elif(lexeme[0] == '+'):
                if(lexeme.__len__() == 1):
                    tok = TokenType.ADD_OP
                else:
                    raise LexException("invalid lexeme at ", rowNum, columnNum)
            elif(lexeme[0] == '-'):
                if(lexeme.__len__() == 1):
                    tok = TokenType.SUB_OP
                else:
                    raise LexException("invalid lexeme at ", rowNum, columnNum)
            elif(lexeme[0] == '*'):
                if(lexeme.__len__() == 1):
                    tok = TokenType.MULT_OP
                else:
                    raise LexException("invalid lexeme at ", rowNum, columnNum)
            elif(lexeme[0] == '/'):
                if(lexeme.__len__() == 1):
                    tok = TokenType.DIV_OP
                else:
                    raise LexException("invalid lexeme at ", rowNum, columnNum)
            else:
                raise LexException("invalid lexeme at ", rowNum, columnNum)
        return tok    

    def getLexeme(self, line, index):
        i = index
        while((i < line.__len__()) and (not(str.isspace(line[i])))):
            i+= 1
        return line[index:i]

        
            
    def skipWhiteSpace(self, line, index):
        while((index < line.__len__()) and (str.isspace(line[index]))):
            index+=1
        return index
    
    def getNextToken(self):
        if(not self.tokens):
            raise RuntimeError("no more tokens")
        return self.tokens.pop(0)
    
    def getLookaheadToken(self):
        if(not self.tokens):
            raise RuntimeError("no more tokens")
        return self.tokens[0]
    
    def moreTokens(self):
        if(not self.tokens):
            return False
        else:
            return True
        
        