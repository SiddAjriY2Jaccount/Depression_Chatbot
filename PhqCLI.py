### to directly write into output file
#import sys

#orig_stdout = sys.stdout
#f = open('out.txt', 'w')
#sys.stdout = f
###

#for i in range(2):
#    print 'i = ', i

print("PHQ-9 Test")
print("====================================================================================================================\n")
print("Over the last 2 weeks, how often have you been bothered by any of the following problems?\n")

def score(i, answers):
    print(i,"\n")
    for j in answers:
        print(j,"\n")
    choice = int(input("Enter Choice\n"))
    choice = choice - 1
    temp = choice
    return temp


total=0

questions = ["\nLittle interest or pleasure in doing things?",
            "\nFeeling down, depressed, or hopeless?",
            "\nTrouble falling or staying asleep, or sleeping too much?",
            "\nFeeling tired or having little energy?",
            "\nPoor appetite or overeating?",
            "\nFeeling bad about yourself — or that you are a failure or have let yourself or your family down?",
            "\nTrouble concentrating on things, such as reading the newspaper or watching television?",
            "\nMoving or speaking so slowly that other people could have noticed? Or so fidgety or restless that you have been moving a lot more than usual?",
            "\nThoughts that you would be better off dead, or thoughts of hurting yourself in some way?"
            ]

#"How difficult have these problems made it for you to do your work, take care of things at home, or get along with other people?"

answers = ["1) Not at all", "2) Several Days", "3) More than Half the days", "4) Nearly every day"]

rescomments = ["Monitor; may not require treatment", "Use clinical judgment (symptom duration, functional impairment) to determine necessity of treatment", "Warrants active treatment with psychotherapy, medications, or combination"]

for i in questions:
    temp1 = score(i, answers)
    total += temp1
    if i == questions[1]:
        if total <= 3:
            print("You are not suffering from any form of illness, cheer up\n")
            print("Total Score is:",total,"\n")
            exit()

print("Total Score :", total,"\n")
print("FINAL DIAGNOSIS should be made with clinical interview and mental status examination including assessment of patient’s level of distress and functional impairment.\n")
print("=========================================================================================================\n")
if total in range(0,5):
    print("Minimal or None\n",rescomments[0],"\n")

if total in range(5,10):
    print("Mild\n",rescomments[1],"\n")

if total in range(10,15):
    print("Moderate\n",rescomments[1],"\n")

if total in range(15,20):
    print("Moderately Severe\n",rescomments[2],"\n")

if total in range(20,28):
    print("Severe\n",rescomments[2],"\n")


#def score(i, answers):
#    for j in answers:
#        print(j,"\n")
#    choice = input("Enter Choice")
#    choice = choice - 1
#    temp = choice
#    return temp



#print("Little interest or pleasure in doing things?\n")

### to directly write into file
#sys.stdout = orig_stdout
#f.close()
