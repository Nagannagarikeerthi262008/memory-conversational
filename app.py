# Memory Conversational
import ollama
user_input=[]
while True:
    p = input("ASK something:") #AI
    if p.lower()=="exit":
        print()
        break
    user_input.append({'role':'user','content':p})
    response = ollama.chat(model="llama3.2",messages=user_input)
    # get AI response
    r=response['message']['content']
    print(r)
    # store AI response
    user_input.append({'role':'assistant','content':r})
    # Print conversation history using for loop
    print("\n-- Chat History--")
    for ui in user_input:
        if ui["role"]=="user":
            print("You:",ui["content"])
        else:
            print("AI:",ui["content"])
    print("-------\n ")