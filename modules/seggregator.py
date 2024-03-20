from .fetch import fetch
def trim_title(main_string, starting_word, ending_word):
    start_index = main_string.find(starting_word)
    end_index = main_string.rfind(ending_word)
    if start_index == -1 or end_index == -1:
        return None 
    trimmed_string = main_string[start_index + len(starting_word):end_index].strip()
    return trimmed_string
def trim_desc(main_string, starting_word):
    start_index = main_string.find(starting_word)
    if start_index == -1:
        return None 
    trimmed_string = main_string[start_index + len(starting_word):-1].strip()
    return trimmed_string
def seggregate_input(comp):
    idea=str(fetch(comp))
    title=trim_title(idea,"Title:","Description:")
    description=trim_desc(idea,"Description:")
    elements=[title,description]
    return elements
