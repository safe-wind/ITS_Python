from pagamento import Pagamento

class PagamentoContanti(Pagamento):


    def __init__(self, importo):
        super().__init__()

        self.setImporto(importo)

    def setImporto(self,importo:float):
        self.importo = importo
        
    def getImporto(self):
        return self.importo
    
    def dettagliImporto(self):

        return f"Importo contanti: €{self.getPagamento():.2f}"
    

pc=PagamentoContanti(20.00)

pc.dettagliPagamento