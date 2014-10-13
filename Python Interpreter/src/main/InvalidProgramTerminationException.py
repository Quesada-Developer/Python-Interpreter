'''
Created on Apr 28, 2013

@author: Cisco
'''

class InvalidProgramTerminationException(Exception):
    '''
    classdocs
    '''


    def __init__(self, message):
        '''
        Constructor
        '''
        self.message = message
        
    def __str__(self):
        return self.message
        