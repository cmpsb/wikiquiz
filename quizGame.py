# -*- coding: utf-8 -*-
"""
Short quiz game to drive getQuestion and setQuestion Python files.
Demonstrates retrieving and forming a question naively from wikipedia articles.

Replicates a simple method that might be used to reward correct answers.
Designed to be replaced with a functioning quiz game to keep track of correct answers,
player scores, set questions etc.

@author: ian
gooddeed89@gmail.com
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
