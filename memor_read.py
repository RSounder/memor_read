#code optimised for windowsOS as the modules used have issues with linuxOS

import pyttsx3
import csv
import requests
import io
import time

#url = "https://raw.githubusercontent.com/RSounder/memor_read/main/words.csv"

sheet_url = "https://docs.google.com/spreadsheets/d/1nJ0x1d1AVdZNGuPRykUgs9QqUsSVeeEERjGFl6l7Xww/export?format=csv&gid=240701129"

download = requests.get(sheet_url).content

engine = pyttsx3.init()
startCount = input('Enter starting number: ')
stopCount = input('Enter stop number (total 763): ')

#open('words.csv')
with io.StringIO(download.decode('utf-8')) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        if line_count >= int(startCount) and line_count <= int(stopCount):
            #yes; it looks clumsy and I know it could've been written in a single line
            #But I wanted to make sure I hear the pauses in between.
            engine.setProperty('rate', 130) 
            engine.say(f'word count: {line_count}')
            syns = row[2].rstrip(',')
            print(f'Word count: {line_count} => \nWord: {row[0]}\nMeaning: {row[1]}\nUsage: {row[3]}\nSynonyms: {syns}\n---------------\n')
            engine.setProperty('rate', 127)
            engine.say(f'{row[0]}.')
            engine.say(f'{list(row[0])}.')
            engine.setProperty('rate', 125)
            for i in range(3):
                engine.say(f'{row[0]}.')
                engine.say(f'meaning. {row[1]}.')
                engine.say(f'usage. {row[3]}.')
                syns = row[2].split(',')
                engine.say(f'synonyms. {syns}.')
                time.sleep(2)
            line_count += 1
            engine.runAndWait()
            time.sleep(5)
        else:
            line_count += 1
