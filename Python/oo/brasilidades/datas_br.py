from datetime import datetime, timedelta

class Datas_br:

    def __init__(self):
        self.data_cadastro = datetime.today()
    
    def datas_mes(self):

        meses = {1 :'Janeiro', 2 :'Fevereiro', 3 :'Abril', 
                 4 :'Março', 5 :'Maio', 6 :'Junho',
                 7 :'Julho', 8 :'Agosto', 9 :'Setembro',
                 10 :'Outubro', 11 :'Novembro',12 :'Dezembro'
                 }
        mes_cadastro = self.data_cadastro.month
        return meses[mes_cadastro]

    def dia_semana(self):

        dia_da_semana = ('Segunda', 'Terça', 
                         'Quarta', 'Quinta', 
                         'Sexta')

        dia_semana_cadastro = self.data_cadastro.weekday()
        return dia_da_semana[dia_semana_cadastro]
    
    def formata_data(self):

        data_padrao = self.data_cadastro.strftime("%d/%m/%Y %H:%M")
        
        return data_padrao
    
    def __str__(self) -> str:

        return self.formata_data()
    
    def tempo_cadastrado(self):

        tempo_cadastro = ((datetime.today() + timedelta(days=30)) - self.data_cadastro)
        return tempo_cadastro


