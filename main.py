import pandas as pd
import matplotlib.pyplot as plt

dados = pd.read_csv("USD_BRL_hist.csv")

plt.figure(figsize=(10, 5))

plt.plot(dados['Data'], dados['USD_BRL'])

plt.title("Evolução do Dólar")
plt.xlabel("Data")
plt.ylabel("Cotação USD/BRL")
plt.savefig("grafico1.png")
plt.show()

plt.figure(figsize=(10, 5))
plt.hist(dados["USD_BRL"], bins=20)

plt.title("Distribuição da Cotação do Dólar")
plt.xlabel("Cotação")
plt.ylabel("Frequência")
plt.savefig("grafico2.png")
plt.show()

plt.figure(figsize=(10, 5))
plt.boxplot(dados["USD_BRL"])

plt.title("Boxplot da Cotação do Dólar")
plt.ylabel("USD/BRL")
plt.savefig("grafico3.png")
plt.show()