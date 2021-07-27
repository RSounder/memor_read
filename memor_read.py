import pyttsx3
import csv

engine = pyttsx3.init()
startCount = input('Enter starting number: ')
stopCount = input('Enter stop number (total 763): ')

with open('words.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    
    for row in csv_reader:
        if line_count >= int(startCount) and line_count <= int(stopCount):
            #yes; it looks clumsy and I know it could've been written in a single line
            #But I wanted to make sure I hear the pauses in between.
            engine.setProperty('rate', 130) 
            engine.say(f'word count: {line_count}')
            syns = row[2].rstrip(',')
            print(f'Word count: {line_count} => \nWord: {row[0]}\nMeaning: {row[1]}\nSynonyms: {syns}\n---------------\n')
            engine.setProperty('rate', 127)
            engine.say(f'{row[0]}.')
            engine.say(f'{list(row[0])}.')
            engine.setProperty('rate', 125)
            for i in range(3):
                engine.say(f'{row[0]}.')
                engine.say(f'meaning. {row[1]}.')
                syns = row[2].split(',')
                engine.say(f'synonyms. {syns}.')
            line_count += 1
            engine.runAndWait()
        else:
            line_count += 1
