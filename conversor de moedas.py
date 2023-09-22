import requests


dados = requests.get("http://economia.awesomeapi.com.br/json/last/USD-BRL,EUR-BRL,BTC-BRL")
dadosjson = dados.json()
dolar = dadosjson['USDBRL']['bid']
euro = dadosjson['EURBRL']['bid']
bitcoin = dadosjson['BTCBRL']['bid']

print("=== CONVERSOR DE MOEDAS ===")
print("Moedas disponiveis: USD, EUR, BTC")

valor = float(input("valor: "))

print('''Escolha uma opção:
[1] Dólar
[2] Euro
[3] Bitcoin
''')

escolha = int(input('QUAL OPÇÃO IRÁ ESCOLHER '))
if escolha == 1:
   conve1 = valor / float(dolar)
   print(f"O valor do === DÓLAR === em relação ao === REAL === está US${dolar}. convertendo R${valor} você ficará com US${conve1}!")
elif escolha == 2:
   conve2 = valor / float(euro)
   print(f"O valor do === EURO === em relação ao === REAL === está US${euro}. convertendo R${valor} você ficará com US${conve2}!")
elif escolha == 3:
   conve3 = valor / float(bitcoin)
   print(f"O valor do === BITCOIN === em relação ao === REAL === está US${bitcoin}. convertendo R${valor} você ficará com US${conve3}!")
else:
   print("Essa opção não existe. por favor, reinicie o programa e escolha outra!")
print("FIM DO PROGRAMA")