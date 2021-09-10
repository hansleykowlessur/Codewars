def abbrev_name(name):
    """
    Write a function to convert a name into initials. This kata strictly takes two words with one space in between them.
    The output should be two capital letters with a dot separating them.
    """
    
    abbreviate = ""
    
    try:
        # Split string into list 
        li_of_name = name.split(" ")
        
        # Concatenate string together while taking first character from each word
        abbreivate = (li_of_name[0][0] + "." + li_of_name[len(li_of_name) - 1][0]).upper()
        
    finally:
        return abbreivate