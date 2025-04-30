import prompt

def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string("May to the Brain Games! ")
    print(f"Hello, {name}!")
    return name