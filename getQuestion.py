# -*- coding: utf-8 -*-
"""
Created on Mon Aug  5 2013
Script to provide questions from random wiki articles to drive a quiz style game.
TODO://....Consider 'Began' split word...

@author: ian
"""

import urllib2
import re
re.DOTALL

from BeautifulSoup import BeautifulSoup

def  main():
    Retrieve_question()  

def Retrieve_question():
    '''
    Primary function.  Retrieves and formats a question and answer set. 
    '''
    article= "http://en.wikipedia.org/wiki/Special:Random"
   # article = "http://en.wikipedia.org/wiki/Herman_of_Alaska" #Debug article holder for when consistent input is needed
    
    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')] 
    
    resource = opener.open(article)
    rawdata = resource.read()
    resource.close()
    
    data = BeautifulSoup(rawdata)
    data = data.find('div',id="bodyContent").p #Sample only the main paragraph of the article
    
    data = str(data)
    data = Strip_excess(data)

    question, answer, additional = Form_question(data)
    
    return question, answer, additional, data
    
def Strip_excess(data): 
    '''Removes un-needed HTML, format, and pronounciation information from Wiki articles.'''
    
    data = re.sub('<[^<]*?>', '', data) #Strips out HTML information to leave a plain text paragraph
    data = re.sub('\[\d\]','',data) #Strips out Citation link digit
    
    return data
    
def Form_question(data):
    data = Format(data)
    
    phrase = re.search('(.+?) is (.+?\.)', data) #Search for a question in the format 'X is Y.'
              
    if not phrase:
        phrase = re.search('(.+?)\swas\s(.*?\.)', data) #Search for a question in the format 'X was Y'   
        
    extra = ''        
    if phrase:
        if len(phrase.group(2)) < 100:
            findExtra = re.search('\.\s.+?\.', data)
            if findExtra:
                extra = findExtra.group()

        answer = phrase.group(1)
        question = phrase.group(2)
        
        if(len(answer) > len(question)):  #If there is more information in the answer, re-sample
            Retrieve_question()
        
        question = re.sub(answer,'', question) #Remove from the questionthe answer string if it exists
        
        question = re.sub(answer, 'it', question)#Substitute the answer out of the question content if it exists
        extra = re.sub(answer, 'it', extra)  
        
        return question, answer, extra
    else:
        Retrieve_question()#If no question can be formed from the article then re-sample
        return "None", "None", "None"
        #TODO://This does not re-sample. try alternative
        
def Get_dates(data):
    event = ['born', 'founded', 'discovered', 'published', 'died']#Date words to match on for context information
    dates = [None] * len(event)

    for i in range(len(dates)):
        dates[i] = Find(event[i] + '.+?\d\d\d\d', data) #Try first any date that ends in 4 digit year contained within brackets
        if dates[i] == None:
          dates[i] = Find(event[i]+ '.+?\d\d', data) # WIki also uses format: 'Month DD' Format if first fails
    if dates[0] == None:
        dates[0] = Find('\(.+?–.+?\)\s', data)        
        
    return dates
    
def Find(pat, text):
    '''Helper function for regex matching'''
    match = re.search(pat, text) 
    if match:
        return match.group()
    else:
        return None

def Format(data):
    data = re.sub('\(.+?\)\s', '', data) #Strips additional bracketed information
    data = re.sub('i/.+?/', '', data) #Strips pronounciation data outside brackets  
    return data
            
if __name__ == '__main__':
    main()