def greetFreind(name,greeting,sentence):
    output = "{2},{0}!,{1}".format(greeting,name,sentence)
    return(print(output))
greeting = greetFreind("Jacob","Hello","Today is nice")

def greet_user(greeting):
    user = input("Enter Your name ")
    print("{},{}!".format(greeting,user).upper)
greet_user("Hello")