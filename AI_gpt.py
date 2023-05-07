from abc import ABC, abstractmethod


class Minion(ABC):
    @abstractmethod 
    def attack(self):  
        """ """     
    @abstractmethod  
    def move(self): 
        """ """ 
class Tower(Minion): 
    def attack(self):  
        return "Bullets..."  
     
    def move(self):  
        raise NotImplementedError
