# match-case is used for clean multi-branching matching instead of if else
# similar to switch statement in c++ or java

day = 2
match day:
    case 1:
        print("Monday")
    case 2: 
        print("Tuesday")
    case 3: 
        print("Wednesday")
    case _:              # this is a default case if none matches then this will execute. 
        print("Invalid day")