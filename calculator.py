from add import add_
def calculator(user_operator):
    if user_operator=="+":
        print(add_(int(input("enter your first number: ")),int(input("enter your second number: "))))
calculator(input("enter your operator: "))