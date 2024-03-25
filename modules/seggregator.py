from .fetch import fetch

#   responce seggregation module   

def trim_title(main_string, ending_word):
    start_index=0
    for title in ['Title:','title:']:
        start_index = main_string.find(title)
        if start_index :
            break
    end_index = main_string.rfind(ending_word)
    if start_index == -1 or end_index == -1:
        return None 
    trimmed_string = main_string[start_index + 6:end_index].strip()
    return trimmed_string
def trim_desc(main_string, starting_word):
    start_index = main_string.find(starting_word)
    if start_index == -1:
        return None 
    trimmed_string = main_string[start_index + len(starting_word):-1].strip()
    return trimmed_string
def seggregate_input(comp):
    idea=str(fetch(comp))
    print(idea)
    title=trim_title(idea,"Description:")
    description=trim_desc(idea,"Description:")
    elements=[title,description]
    return elements
