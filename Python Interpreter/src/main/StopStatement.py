'''
Created on Apr 27, 2013

@author: Cisco
'''
from BasicStatement import BasicStatement

class StopStatement(BasicStatement):
    def __init__(self):
        super(StopStatement, self).__init__()
        pass
    
    def execute(self, prog):
        ''''''