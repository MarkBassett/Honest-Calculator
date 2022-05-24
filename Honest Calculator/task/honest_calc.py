msg_ = [
"Enter an equation",
"Do you even know what numbers are? Stay focused!",
"Yes ... an interesting math operation. You've slept through all classes, haven't you?",
"Yeah... division by zero. Smart move...",
"Do you want to store the result? (y / n):",
"Do you want to continue calculations? (y / n):",
" ... lazy",
" ... very lazy",
" ... very, very lazy",
"You are",
"Are you sure? It is only one digit! (y / n)",
"Don't be silly! It's just one number! Add to the memory? (y / n)",
"Last chance! Do you really want to embarrass yourself? (y / n)",
]

operators = ['+', '-', '/', '*']
input_equation = True
m = 0.0


def is_one_digit(v):
    if -10 < v < 10 and v.is_integer():
        return True
    return False


def check(v1, v2, v3):
    msg = ""
    if is_one_digit(v1) and is_one_digit(v2):
        msg += msg_[6]
    if (v1 == 1 or v2 == 1) and v3 == "*":
        msg += msg_[7]
    if (v1 == 0 or v2 == 0) and (v3 == "*" or v3 == "+" or v3 == "-"):
        msg += msg_[8]
    if msg != "":
        msg = msg_[9] + msg
        print(msg)






while input_equation:
    print(msg_[0])
    x, oper, y = input().split()
    input_equation = False

    if x == "M":
        x = m
    if y == "M":
        y = m

    try:
        x = float(x)
    except ValueError:
        print(msg_[1])
        input_equation = True
    try:
        y = float(y)
    except ValueError:
        print(msg_[1])
        input_equation = True

    check(x, y, oper)

    if oper not in operators:
        print(msg_[2])
        input_equation = True

    if input_equation == False:
        if oper == "+":
            result = x + y
        elif oper == "-":
            result = x - y
        elif oper == "*":
            result = x * y
        elif y == 0:
            print(msg_[3])
            input_equation = True
        else:
            result = x / y

    if input_equation == False:
        print(result)
        print(msg_[4])
        if input() == "y":
            if is_one_digit(result):
                for msg_index in range(10, 13):
                    print(msg_[msg_index])
                    if input() == "n":
                        break
                    if msg_index == 12:
                        m = result
            else:
                m = result

        print(msg_[5])
        if input() == "y":
            input_equation = True
