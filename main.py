import os
n1 = 0
n2 = 1
div =0

while( n2 > 0):
  
  n1 = int(input("Digite o primeiro valor: "))
  n2 = int(input("Digite o segundo valor: "))

  if ( n2 == 0 ):
    os.system('clear')
    print("**Atenção valor tem que ser maior que zero**")
    n2 = int(input("Digite o segundo valor: "))
  else:
    div = n1 / n2
    print(f"Calculo de Divisão: {div:.2f}")
   
  