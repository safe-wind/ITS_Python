#8_9 messages

# Make a list containing a series of short
# text messages. Pass the list to a function 
# called show_messages(), which prints each
# text message.

def show_messages(par:list[str]) ->str:

    for i in par:
        mess = print(i)
    
    return mess
        
    
texts:list[str] = ["ciao", "bla", "bla"]

show_messages(texts)