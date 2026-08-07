Python

def calcular_imc():
  print("--- Calculadora de IMC ---")
  peso = float(input("Digite seu peso em kg: "))
  altura = float(input("Digite sua altura em metros: "))

  imc = peso / (altura ** 2)
  print(f"Seu IMC é: {imc:.2f}")

if__name__==__main__":
  calcular imc()
