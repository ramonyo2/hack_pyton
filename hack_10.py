"""
text: "fooziman" output => ["F","0","0","Z","1","M","@","N"]
"""

def fn_hack_10():
    result = "fooziman"

    transformed = []
    
    for char in result:
        if char == 'f':
            transformed.append('F')
        elif char == 'o' or char == 'z':
            transformed.append('0')
        elif char == 'i':
            transformed.append('1')
        elif char == 'm':
            transformed.append('M')
        elif char == 'a':
            transformed.append('@')
        elif char == 'n':
            transformed.append('N')
        else:
            transformed.append(char)  
        
    return transformed
