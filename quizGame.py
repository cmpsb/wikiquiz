# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 2013

@author: ian
"""

import setQuestion

def main():
    points = 100
    
    while(points >= 0):
        if(setQuestion.setQuestion()==True):
            points += 5
        else:
            points -= 10
            
        print "Points:", points
            
    intro()
    
    print "Hello World"
    
    
def intro():
    print "Test"
    
    
if __name__ == '__main__':
    main()