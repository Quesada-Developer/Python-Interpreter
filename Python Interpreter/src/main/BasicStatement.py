'''
Created on Apr 27, 2013

@author: Cisco
'''
import abc

class BasicStatement(object):
    __metaclass__ = abc.ABCMeta
    
    def __init__(self):
        '''stuff goes here'''
    
    @abc.abstractmethod
    def execute(self):
        return
    