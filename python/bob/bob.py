def response(hey_bob):

    clean_input = hey_bob.strip()
    
    if clean_input == "":
        return "Fine. Be that way!"
    
    if clean_input.isupper() and clean_input[-1] == "?":
        return "Calm down, I know what I'm doing!"
    
    if clean_input.isupper(): 
        return "Whoa, chill out!"
    
    if clean_input.endswith("?"):
        return "Sure."
    
    else:
        return "Whatever."