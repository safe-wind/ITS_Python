
# Start with your work from Exercise 8-10. Call the function 
# send_messages() with a copy of the list of messages. After 
# calling the function, print both of your lists to show that 
# the original list has retained its messages.

global sent_messages
sent_messages:list[str] = []

def send_messages(par:list[str], par1:list[str]) ->str:

    for i in par:

        mess = i
        par1.append(mess)
    
    return par1
    
texts:list[str] = ["ciao", "bla", "bla"]
texts_copy:list[str] = texts.copy()

send_messages(texts_copy, sent_messages)

print(f'Copia di lista: {texts_copy}, lista di origine: {texts}')