
def recursivePalindrome(testo:str)-> bool:

    testo = testo.replace(" ", "")
    if len(testo) <= 1:
        return True
    
    else:
        if testo[0]!=testo[-1]:
            return False
        
        else:
            return recursivePalindrome(testo[1:-1])

            
    
print(recursivePalindrome("radar"))

