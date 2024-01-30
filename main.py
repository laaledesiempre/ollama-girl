import ollama

emotions= ["Happy","kind","protective","curious","empathic","creative","responsible","independent","dependent","boring","psichotic","sad","egoist","friendly","prideful","fearless","lonely","shameful","angry","violent"]

while True:
    print("Welcome to the ollama-girl creator, a chat game with AI models!")
    print("""
    1. Play
    Q. Quit
""")
    response=input("Option: ")
    if response=="1":
        print("DEBUG BLOCK")
        print(ollama.list())
        print("game started")
        print("Select at least three from this list, beware, if your selections have no sense, probably the chat ai will not be the best")
        for x in emotions:
            print(x)
        print("You can also add your own, but this ones work pretty well")
        emotions_selections= input("write three of them, try to not adding lot more!")
        print("now lets add some background to your new friend:")
        background=input("tell me a little about your friend things, like age, likes, family etc.")
        print("Now tell us what kind of relation you want:")
        relation_kind=input("Short description of your future relation")
        print("generating model")
        modelfile=f"""
FROM tinydolphin
SYSTEM you are a girl, your emotions are: {emotions_selections}, your background story is {background} and you want to develop this kind of relation with the user {relation_kind}
"""
        print("Name your new friend:")
        name=input("Name: ")
        ollama.create(model="ollama-girl/"+name, modelfile=modelfile)
        while True:
            message=input(">>> ")
            if message == "q":
                break
            ollama.chat(model="ollama-girl/+name", messages=[{'content': message}])
    elif response.lower() == "q":
        break
    break