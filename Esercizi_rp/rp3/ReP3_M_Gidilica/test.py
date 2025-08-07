from alieno import Alieno
from mostro import *

# MAIN
if __name__ == "__main__":
    a = Alieno()
    m = Mostro("Gorthor", "GRAAAHHH", "Uuurghhh")

    print(a)
    print("Munizioni:", a.getMunizioni())
    print()
    print(m)
    print("Assalto:", m.getAssalto())
    print()
    print("Combattimento")
    vincitore = combattimento(a, m)
    print()
    if vincitore:
        if isinstance(vincitore, Alieno):
            print("Gli Alieni hanno vinto!")
        else:
            print("I Mostri hanno vinto!")
        print()
        proclamaVincitore(vincitore)