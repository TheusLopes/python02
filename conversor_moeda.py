real = 100
taxa_dolar = 5.2000
taxa_euro = 6.1500

conversao_dolar = real * taxa_dolar
conversao_euro = real * taxa_euro

dolar_arredondado = round(conversao_dolar, 2)
euro_arredondado = round(conversao_euro, 2)

print ("O valor do real convertido em dolar é", dolar_arredondado)
print ("O valor do real convertido em euro é", euro_arredondado)