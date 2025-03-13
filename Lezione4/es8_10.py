# Write a function called send_messages() that prints each text
# message and moves each message to a new list called sent_messages
# as it’s printed. After calling the function, print both of your
# lists to make sure the messages were moved correctly.

global sent_messages
sent_messages:list[str] = []

def send_messages(par:list[str], par1:list[str]) ->str:

    for i in par:

        mess = i
        par1.append(mess)
    
    return par1
        
    
texts:list[str] = ["ciao", "bla", "bla"]

send_messages(texts, sent_messages)

print(f'lista parametro: {texts}, lista sent_messages: {sent_messages}')