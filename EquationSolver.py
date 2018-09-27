# Created by Javier Romero Sanchez



def arithmetic(operation,variable,interval):
    i=interval[0]
    #Replaces [ and { for ( and also for the closing ones and evaluates the equation and transforms it into string.
    while i <= interval[1]:
        print("The result is: ("+str(i)+" , "+str(calculator(i,variable,simpl_oper(operation)))+")")
        i+=interval[2]

#Replaces the [,] and {,}  with (,), also eliminates spaces
def simpl_oper(operation):
    operation = operation.replace('[', '(')
    operation = operation.replace(']', ')')
    operation = operation.replace('{', '(')
    operation = operation.replace('}', ')')
    operation = operation.replace(' ','')
    return operation

# Executes the received operation and returns its numerical value.
def calculator(interval,variable,operation):
    operands=["/","^","*","+"]
    numbers=[] #Saves all the numbers in the operation.
    ops=[] #Saves all the operations and brackets of the operation in execution order.
    i = 0 #Goes through all the characters of the operation.
    while i in range(0, len(operation)):
        if operation[i]==variable:
            numbers.append(interval)
        elif operation[i].isdigit():
            number = operation[i]
            deci=False #Boolean created to know if the number needs to be saved as a float or as an integer.
            i += 1
            #Checks if next char is a digit, in case the number has more than 1 digit.
            while i < (len(operation)) and (operation[i].isdigit() or operation[i]=="."):
                if operation[i]==".": #The character '.' indicates a decimal, and we need to make a difference between a float and integer number.
                    deci=True
                number = str(number) + str(operation[i])
                i += 1
            if deci:
                numbers.append(float(number)) #Adds the number to the numbers stack.
            else:
                numbers.append(int(number))
            continue

        #Recognizes negative values
        elif operation[i]=="-":
            if operation[i+1].isdigit():
                number = int(operation[i+1])*-1
                deci = False
                i += 2
                # The character '.' indicates a decimal, and we need to make a difference between a float and integer number.
                while i < (len(operation)) and (operation[i].isdigit() or operation[i]=="."):
                    if operation[i]==".": #The character '.' indicates a decimal, and we need to make a difference between a float and integer number.
                        deci=True
                    number = str(number) + str(operation[i])
                    i += 1
                if deci:
                    numbers.append(float(number)) #Adds the number to the numbers stack.
                else:
                    numbers.append(int(number))

                if i < len(operation) and operation[i] == '-':
                    ops.append('+')
                continue

            elif operation[i+1]=="(": #In case is -(3+2), the - modifies the whole bracket, multiplying it by -1
                if len(numbers)>0 : #If there is another number before the brackets, is necessary to add the + operator for the operation between the two numbers.
                    ops.append('+')
                numbers.append(-1)
                ops.append('*')


        elif operation[i] == '(':
            ops.append(operation[i])  # Adds the brackets to the ops stack.
        elif operation[i] == ')':  # If finds a closing bracket, goes through all the ops stack, until it finds the opening bracket.
            if len(ops) > 0:
                while ops[-1] != '(':
                    numbers.append(app_arith(str(ops.pop()), numbers.pop(), numbers.pop()))
                if ops[-1] == '(':
                    ops.pop()
        #If the character is one of the possible operands, checks whether is possible to perform that operation at the moment or not.
        elif operation[i] in operands:
            #Checks for possible priority order conflicts with previous operands saved in the operations queue.
            while len(ops) > 0 and check_pref(operation[i], ops[-1]):
                #At this point no conflicts were found, so the result of the operand and the 2 last saved numbers is evaluated and saved in the numbers queue.
                numbers.append(app_arith(str(ops.pop()), numbers.pop(), numbers.pop()))
            ops.append(operation[i])# The non-prioritary operand is included in the operations queue.
        i += 1
    while len(ops) != 0:
        numbers.append(app_arith(str(ops.pop()), numbers.pop(), numbers.pop()))
    return numbers.pop()


#Checks if the operator found in the operation (char1) has priority order over the last one introduced in the operator queues (char2)
def check_pref(char1, char2):
    if char2 == '(' or char1 == '^': #If the character found is a parenthesis, it means there are not enough numbers to perform any kind of operation yet.
        return False
    elif (char2 == '+') and (char1 == '*' or char1 == '/'):
        return False
    else:
        return True

#Receives an operation sign and the second number and first number of the operation, calculating its result.
def app_arith(op, num2, num1):
    if op == '+':
        return (num1 + num2)
    elif op == '/':
        return (num1 / num2)
    elif op == '*':
        return (num1 * num2)
    elif op == '^':
        return (num1 ** num2)
    else:
        return 0

variable='x'
intervals=[0,0.5,0.1]

#Insert as a method the equation to resolve.
arithmetic("4^(3*(x/-7))",variable,intervals)
