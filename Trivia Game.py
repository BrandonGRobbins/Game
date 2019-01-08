#brandon robbins
#1/19
#trivia game
import sys
def open_file(file_name,mode):
    try:
        the_file=open(file_name,mode)
    except IOError as e:
        print("Unable to open file",file_name)
        print(e)
        input("Press enter to exit")
        sys.exit()
    else:
        return the_file

def next_line(the_file):
    line = the_file.readline()
    line = line.replace("/","\n")
    return line
    
def next_block(the_file):
    category=next_line(the_file)
    question=next_line(the_file)
    answers=[]
    for i in range(4):
        answer=next_line(the_file)
        answers.append(answer)
    correct=next_line(the_file)
    if correct:
        correct=correct[0]
    explanation=next_line(the_file)
    return category, question, answers, correct, explanation
def welcome(title):
    print("\t\tWelcome to Trivia Challenge!\n")
    print("\t\t",title, "\n")

def main():
    the_file=open_file("test_question.txt","r")
    title=the_file.readline()
    welcome(title)
    score=0
    category,question,answers,correct,explanation=next_block(the_file)
    while category:
        print(category)
        print(question)
        for i in range(4):
            print(i+1,answer[i])
        user=input("which answer is correct?,input the corresponding number")
        if user==correct:
            print("congrats you got it right")
            score+=1
        else:
            print("you failed that question")
        print(explanation)
        category,question,answers,correct,explanation=next_block(the_file)
        the_file.close()
        print("the game is now over you got",score,'correct!')
        input("press enter to quit")
main()
