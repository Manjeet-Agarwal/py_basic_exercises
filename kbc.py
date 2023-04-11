# let's try to create a basic KBC software

questions = [
    ["What is the output of the following code snippet? \nprint(2+2*2)",
     "4",
     "6",
     "8",
     "10",
     2],
    ["What is the keyword used to define a function in Python?",
     "method",
     "function",
     "define",
     "def",
     4],
    ["Which of the following operators is used to perform exponentiation in Python?",
     "**",
     "^",
     "*",
     "//",
     1],
    ["What is the default value of a boolean variable in Python?",
     "True",
     "False",
     "0",
     "1",
     2],
    ["Which of the following is not a valid comparison operator in Python?",
     "==",
     "!=",
     "<>",
     "<",
     3],
    ["which of the following is the  correct python file extension",
     ".p", ".python", ".pyt", ".py", 4],

    ["Which of the following is not a valid programming paradigm?",
     "Object-Oriented Programming",
     "Declarative Programming",
     "Imperative Programming",
     "Interpreted Programming",
     3],
    ["Which of the following data structures is implemented using a Last-In-First-Out (LIFO) approach?",
     "Stack",
     "Queue",
     "Linked List",
     "Binary Tree",
     1],
    ["Which of the following is not a type of loop in programming?",
     "For Loop",
     "While Loop",
     "Do-While Loop",
     "Next Loop",
     4],
    ["Which of the following is not a primitive data type in Python?",
     "String",
     "Float",
     "Tuple",
     "Boolean",
     3],
    ["What is the output of the following code snippet? \n\nx = 3 \nif x > 2: \n    print('Hello, World!')",
     "Hello, World!",
     "3",
     "Error",
     "None of the above",
     1],
    ["Which of the following is not a reserved keyword in Python?",
        "global",
        "final",
        "assert",
        "pass",
        2],
    ["What is the result of the following code? \n\na = [1, 2, 3, 4] \nb = a[1:3] \nprint(b)",
        "[1, 2]",
        "[2, 3, 4]",
        "[2, 3]",
        "[1, 3]",
        3],
    ["Which built-in function in Python can be used to sort a list?",
        "sort()",
        "sorted()",
        "order()",
        "arrange()",
        2],
    ["Which of the following is not a valid way to open a file in Python?",
        "open('file.txt')",
        "open('file.txt', 'w')",
        "open('file.txt', 'r')",
        "open('file.txt', 'execute')",
        4]


]
levels = [1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000,
          160000, 320000, 640000, 1250000, 2500000, 5000000, 10000000]
money = 0
for i in range(0, len(questions)):
    question = questions[i]
    print(f"your question for Rs. {levels[i]}\n")
    print(f"{question[0]}")
    print(f" 1. {question[1]}        2. {question[2]}")
    print(f" 3. {question[3]}        4. {question[4]}")
    try:
        answer = int(input('choose the value from 1 to 4 :'))
    except:
        print("enter a interger value from 1-4 ")
        break
    if answer == question[-1]:
        print(
            f"\ncongrats! it's the correct answer and you have won Rs.{levels[i]}\n")
        if (i == 4):
            money = levels[i]
        elif (i == 9):
            money = levels[i]
        elif (i == 14):
            money = levels[i]
    else:
        print("It's the wrong answer!")
        break
    
print(f"your take home money is {money}\n")
