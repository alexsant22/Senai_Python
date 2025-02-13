import datetime

data_hora_atual = datetime.datetime.now()
print(data_hora_atual)

hora_data_atual = datetime.datetime.now()

ano = hora_data_atual.year
mes = hora_data_atual.month
dia = hora_data_atual.day
hora = hora_data_atual.hour
minuto = hora_data_atual.minute
segundo = hora_data_atual.second

print(f"Ano: {ano}, Mês: {mes}, Dia: {dia}, Hora: {hora}, Minuto: {minuto}, Segundo: {segundo}")