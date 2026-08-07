def caixa_registradora():
  print("--- Caixa Registradora ---")
  total = 0.0

while True:
  preco = float(input("Digite o preço do produto (ou 0 para encerrar): R$ "))
  if preco == 0:
    break
  total += preco
  print(f"Subtotal atual: R$ {total:.2f}")

print(f"\nValor total da compra: R$ {total:.2f}")

dinheiro = float(input("Digite o valor pago pelo cliente: R$ "))

if dinheiro>=total:
  troco = dinheiro - total
  print(f"Troco a devolver: R$ {troco:.2f}")
else:
  faltando = total - dinheiro
  print(f"Valor insuficiente! Faltam R$ {faltando:.2f}")

if__name__=="__main__":
  caixa registradora()
