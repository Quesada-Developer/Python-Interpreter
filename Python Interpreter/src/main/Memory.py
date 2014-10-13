'''
Created on Apr 27, 2013

@author: Cisco
'''
class Memory(object):
    mem = {}
    
    @classmethod
    def store(self, ch, value):
        self.mem.update({ch:value})
        
    @classmethod
    def fetch(self, ch):
        return self.mem[ch]