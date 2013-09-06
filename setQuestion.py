# -*- coding: utf-8 -*-
"""
Created on Thu Aug 29 2013

@author: ian
"""

import getQuestion
import difflib #Important for fuzzy matching on answer string

def main():
   
    setQuestion()        
    
def setQuestion():
    '''
    Primary function outputs a single question and context information, waits for an answer, and compares the users input to wiki-generated answer
    '''
    question, answer, additional, data = getQuestion.Retrieve_question()  
    
    dates = getQuestion.Get_dates(data)
    
    showData(question, answer, additional, data, dates)  #Debug function to demonstrate the inut/outpot of the question retrieved
    
    displayQuestion(question, additional, dates)
   
    guess = raw_input("A:")
    
    correct = compareGuess(guess, answer)
    
    return correct #Returns bool value of answer match. #True if correct   
   
def displayQuestion(question, additional, dates):
    '''Displays question and supporting information suitably formatted to the console'''
    print "question:\n", question, additional
    for date in dates:
        if date != None:
            print date  
        
def compareGuess(guess, answer):
    ''' 
    Compare the user's guess to the given answer from Wiki.  Attempt to allow fuzzy matches to compensate for minor miss-spellings, and punctuation errors.
    Returns boolean value on sufficient match percentage
    TODO://Consider dynamic match percentage based on length/complexity of wiki-answer
    '''
    answer = answer.lower() #COnvert to lower at time of comparison to maintain formatting for display
    guess = guess.lower()
    
    matchPercent = (difflib.SequenceMatcher(isjunk=None, a=guess, b=answer, autojunk=True).ratio()) * 100 #Give a match percentage on guess and answer
    print matchPercent, "***Debug match percentage value***"
      
    if(matchPercent > 80):
        return True   
    return False      

def showData(question, answer, additional, data, dates):
    '''Debug function to show relevant information to understand the workings of the program''' 
    print '\nQ:', question, additional
    for date in dates:
        if date != None:
            print date            
            
    print 'A:', answer, '\n\n'
    
    print data, '\n\n\n'
   
    
if __name__ == '__main__':
    main()