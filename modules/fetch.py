from .chat import chat

def fetch():
    components=["arduino uno" ,"ultrasonic sensor",
 "ir sensor","servo motors"]
    prompt_base='give an innovative project idea which can be done with the components given '
    prompt_component=""
    for i in components:
        prompt_component +=i
        prompt_component+=", "
    prompt_end='give the output in the form of title at first and then the description of the project'
    prompt=prompt_base+prompt_component+prompt_end
    result=chat(prompt)
    return result