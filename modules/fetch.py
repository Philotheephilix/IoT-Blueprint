from .chat import chat

##Prompt designer for accurate output

##change as per users requirment
#change max_token from chat module according to the length of the response needed

def fetch(components):
    prompt_base='give an innovative project idea which can be done with the components given '
    prompt_component=""
    for i in components:
        prompt_component +=i
        prompt_component+=", "
    prompt_end='give the output in the form of title at first and then the description of the project dont give smart irrigation system also give description 150 words'
    prompt=prompt_base+prompt_component+prompt_end
    result=chat(prompt)
    return result