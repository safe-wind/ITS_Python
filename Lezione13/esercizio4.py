
def recursiveCounter(n:int) -> int:

    if abs(n) < 10: #tutti i casi di n = 1 cifra -9 --- 9
        return 1    #recCount(9) -> 1
    else:
        return abs( 1 + recursiveCounter(n / 10)) # step1. n = 100
                                                   # funzione eseguita, n!=10                               n = 100
                                                   # |==> else return *(1)+recCount(n/10) (*)1 il caso dove n = 100
                                                   # si richiama la funzione ^^^^^^^^      |n = 1 cifra che
                                                   # step2. si esegue                      |aggiunge 1      n = 100
                                                   # (1+)100/10 = (1+)10 -> no return 1+ at step2              n=100/10 -> n=10
                                                   # step3. (1+)10/10 = 1+1 -> return 2 at step3            n=1
                                                   # step4. return 3
    
print(recursiveCounter(120))
print(recursiveCounter(-9000))