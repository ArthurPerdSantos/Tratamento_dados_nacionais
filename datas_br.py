from datetime import datetime, timedelta

class Datas_br:

    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.format_data()

    def mes_cadastro(self):
        meses_do_ano = {
            1: "Janeiro",
            2: "Fevereiro",
            3: "Março",
            4: "Maio",
            5: "Junho",
            6: "Julho",
            7: "Agosto",
            8: "Setembro",
            9: "Outubro",
            10: "Novembro",
            11: "Dezembro"
        }
        mes = self.momento_cadastro.month
        return meses_do_ano[mes]





    def semana_cadastro(self):
        dia_da_semana = self.momento_cadastro.weekday()
        dias_semana = {
            1: "Segunda-Feira",
            2: "Terça-Feira",
            3: "Quarta-Feira",
            4: "Quinta-Feira",
            5: "Sexta-Feira",
            6: "Sábado",
            7: "Domingo"
        }
        return dias_semana[dia_da_semana+1]

    def format_data(self):
        data_formatada = self.momento_cadastro.strftime("%d/%m/%y  %H:%M")
        return data_formatada

    def tempo_cadastro(self):
        tempo = datetime.today() - self.momento_cadastro
        return tempo