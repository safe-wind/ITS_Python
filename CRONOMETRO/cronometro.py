

def cronometro(fun):

    def wrapper(*args):
        import time
        start = time.time()
        fun(*args)
        print(time.time()-start)
    
    return wrapper

@cronometro
def prova():
    for i in range(1000000):
        pass
# equivale a scrivere -> prova = conometro(prova)

