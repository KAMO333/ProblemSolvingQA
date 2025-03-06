def response(hey_bob):
    
    remove_spaces = hey_bob.replace(" ", "")

    if remove_spaces.endswith("?"):
        return "Sure."
    
    if remove_spaces.upper():
        return "Whoa, chill out!"
    

