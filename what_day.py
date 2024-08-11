def whatday(num):
    Days = ['Sun','Mon','Tues','Wednes','Thurs','Fri','Satur']
    for index,values in enumerate(Days):
    #print(index,values)
        if index == num-1:
            return (values+"day")
        elif num > 7 and num < 1:
            return "Wrong, please enter a number between 1 and 7"


def whatday(num):
    Days = ['Sun','Mon','Tues','Wednes','Thurs','Fri','Satur']
    return Days[num-1] + "day" if 1 <= num <= 7 else "Wrong, please enter a number between 1 and 7"