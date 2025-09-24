from pagamento import Pagamento

class PagamentoContanti(Pagamento):


    def __init__(self, importo:float):
        super().__init__()

        self.setPagamento(importo)
    
    def dettagliPagamento(self):

        return f"Importo contanti: €{self.getPagamento():.2f}"
    

pc=PagamentoContanti(20.00)

pc.dettagliPagamento