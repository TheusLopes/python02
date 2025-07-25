produto = "camiseta"
preco_original = 50.00
desconto = 20

valor_desconto = preco_original * (desconto / 100)
preco_final = preco_original - desconto

print(f"Produto: {produto}")
print(f"Preço original: R$ {preco_original:.2f}")
print(f"Desconto: {desconto}%")
print(f"Valor do desconto: R$ {valor_desconto:.2f}")
print(f"Preço com desconto: R$ {preco_final:.2f}")