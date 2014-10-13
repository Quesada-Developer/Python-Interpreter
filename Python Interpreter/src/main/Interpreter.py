'''
Created on Apr 27, 2013

@author: Cisco
'''
from LexException import LexException
from ParserException import ParserException
from InvalidProgramTerminationException import InvalidProgramTerminationException
from MissingStatementException import MissingStatementException

from Parser import Parser

if __name__ == '__main__':
    try:
        p = Parser("test4.bas")
        prog = p.parse()
        prog.execute()
    except FileNotFoundError:
        raise Exception("source file not found")
    except LexException as e:
        raise Exception(e.__str__())
    except ParserException as e:
        raise Exception(e.__str__())
    except InvalidProgramTerminationException as e:
        raise Exception(e.__str__())
    except MissingStatementException as e:
        raise Exception(e.__str__())
    except:
        raise Exception("Unknown error occurred - terminating")
        
        