def solve(s):
    
    #capitalized_names = []
    #for name in re.split(r'(\s+)):
        #capitalized_names.append(name.capitalize())
    #return ''.join(capitalized_names)   
    # much better with list comprehnsion 
    # re.split(r'(\s+) preserve original withespaces
    return ''.join(name.capitalize() for name in re.split(r'(\s+)', s))
