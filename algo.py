#----------------------------------Algo for calculate happiness index------------------------------------

def monthsresult(answere):
    # 1 = happy 
    # 2 = neutral 
    # 3 = sad 
    # 4 = very sad
    marks = 0
    
    if answere ==1:
            marks= marks + 1
    elif answere == 2:
            marks = marks + 0.5
    elif answere == 3:
            marks = marks - 0.5 
    elif answere == 4:
            marks = marks - 1
    return marks
def OptionsResult():
    correct= 0
    incorrect = 0
    #quetion1
    #correct answere is option1
    if (answere==option1):
        correct = correct +1
    else:
        incorrect = incorrect +1 
    #quetion2
    #correct answere is option1
    if (answere==option1):
        correct = correct +1
    else:
        incorrect = incorrect +1 
    #quetion3
    #correct answere is option1
    if (answere==option1):
        correct = correct +1
    else:
        incorrect = incorrect +1 
    # total quetions = 10
    avg_marks= (correct - incorrect)*5 
    return avg_marks
marks = 0 
for i in range(1,31):
    answere = int(input("choice an option "))
    y = monthsresult(answere)
    marks = y + marks
    avg_marks = marks * 1.6666667
avg_marks = int(avg_marks)
print(avg_marks)

#optionalMarks=OptionsResult()

total_marks = avg_marks #+ optionalMarks

if total_marks >= 90:
    print("your this month was great")
elif total_marks>= 60 and total_marks < 90:
    print("this month was an average ")
elif total_marks>= 40 and total_marks< 60 :
    print("this month was moderate")
else :
    print("you can have a great month ahead")


