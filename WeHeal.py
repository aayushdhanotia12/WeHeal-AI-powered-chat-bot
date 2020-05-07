    ### to directly write into output file
#import sys

#orig_stdout = sys.stdout
#f = open('out.txt', 'w')
#sys.stdout = f
###

#for i in range(2):
#    print 'i = ', i
from textblob import TextBlob
print("Over the last 2 weeks, how often have you been bothered by any of the following problems?\n")


questions = ["\nLittle interest or pleasure in doing things?",
            "\nFeeling down, depressed, or hopeless?",
            "\nTrouble falling or staying asleep, or sleeping too much?",
            "\nFeeling tired or having little energy?",
            "\nPoor appetite or overeating?",
            "\nFeeling bad about yourself or that you are a failure or have let yourself or your family down?",
            "\nTrouble concentrating on things, such as reading the newspaper or watching television?",
            "\nMoving or speaking so slowly that other people could have noticed? Or so fidgety or restless that you have been moving a lot more than usual?",
            "\nThoughts that you would be better off dead, or thoughts of hurting yourself in some way?"
            ]

rescomments = ["Monitor; may not require treatment", "Use clinical judgment (symptom duration, functional impairment) to determine necessity of treatment", "Warrants active treatment with psychotherapy, medications, or combination"]

for i in questions:
    print(i)
    answer=input()
    blob = TextBlob(answer)
    for sentence in blob.sentences:
        print(sentence.sentiment.polarity)
        
