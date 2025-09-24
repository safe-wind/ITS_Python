class Pagamento:

    imp_pagamento:float

def setPagamento(self, imp_pagamento:float):
    self.pagamento = imp_pagamento

def getPagamento(self):
    return self.pagamento

def dettagliPagamento(self, imp_pagamento)->str:
    return f"Importo del pagamento: €{self.getPagamento():.2f}"

