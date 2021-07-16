def comun_div(num):
  #result = 0
  valores = []
  vueltas = 7
  while num != 1.0:
    print('esta vuelta vale: ', num)
    vueltas -= 1
    if num%2 == 0:
      num = num/2
      valores.append(2)
      continue
    if num%3 == 0:
      num = num/3
      valores.append(3)
      continue
    if num%5 == 0:
      num = num/5
      valores.append(5)
      continue
    if num%7 == 0:
      num = num/7
      valores.append(7)
      continue
    if num%11 == 0:
      num = num/11
      valores.append(7)
      continue
    if num%13 == 0:
      num = num/13
      valores.append(7)
      continue
    if num%num == 0:
      valores.append(num)
      num = num/num
      continue
  return valores
def buscar_Comun(lista1, lista2):
  lista_comun = []
  for num in lista1:
    if num in lista2:
      lista_comun.append(num)
      lista2.remove(num)
  print("lista_comun", lista_comun)
  return lista_comun
def valor_maximo(lista):
  resultado = 1
  for num in lista:
    resultado = resultado * num
  return resultado

def mcd(num,n2):
  result1 = []
  result2 = []
  result1 = comun_div(num)
  result2 = comun_div(n2)
  res = buscar_Comun(result1, result2)
  val_maximo = valor_maximo(res)
  return val_maximo

print('valor Maximo: ',mcd(225,300))