def solve(s):
    
    #capitalized_names = []
    #for name in s.split():
        #capitalized_names.append(name.capitalize())
    #return ' '.join(capitalized_names)   
    # much better with list comprehnsion 
    return ' '.join(name.capitalize() for name in s.split())
