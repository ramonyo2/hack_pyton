"""
loop: while [1,2,3] ouput => [1,'@',2,'@',3,'@']
"""

def fn_hack_9():
    result = [1,2,3]
    i = 1
    
    while i < len(result):
        result.insert(i,"@")
        i+= 2
        result.append("@")
        
    return result  