# funcões 

def desafio001():
  return "olá prof ihhu"

def desafio002():
  
  nome = input("digite seu nome:")
  print("seja bem-vindo", nome)

def desafio003():
  
  n1 = int(input("digite um valor:"))
  n2 = int(input("digite outro valor:"))
  s = n1+n2
  print("a soma entre {} e {} é igual a {}".format(n1, n2, s))

def desafio004():
  
  a = input("digite algo:")
  print("tipo primitivo:", type(a))
  print("só tem espaço", a.isspace())
  print("é um número:", a.isnumeric())
  print("é alfabético:", a.isalpha())
  print("é afanúmerico:", a.isalnum())
  print("maiusculas:", a.isupper())
  print("minuscula:", a.islower())
  print("capitalizado:", a.istitle())

def desafio005():
  
  n = int(input("digite um número:"))
  a = n - 1
  s = n + 1
  print("o número {} tem como seu antecessor {} e seu sucessor {}".format(n, a, s))

def desafio006():
  
  n = int(input("digite um número:"))
  d = n * 2
  t = n * 3
  r = n ** (1/2)
  print("o dobro de {} é {}".format(n, d))
  print("o tripo de {} é {}".format(n, t))
  print("a raiz de {} é {}".format(n, r))

def desafio007():
  
  n1 = float(input("primeiro bimestre:"))
  n2 = float(input("segundo bimentre:"))
  m = (n1 + n2) /2
  print("a média entre {} e {} é igual a {}".format(n1, n2, m ))

def desafio008():
  
  medidas = float(input("distencia em metros:"))
  cm = medidas * 100
  mm = medidas * 1000
  print("a medida de {}m corresponte a {}cm e {}mm".format(medidas, cm, mm))

def desafio009():
  
  n = int(input("número:"))
  print("{} . {} = {}".format(n, 1, n*1))
  print("{} . {} = {}".format(n, 2, n*2))
  print("{} . {} = {}".format(n, 3, n*3))
  print("{} . {} = {}".format(n, 4, n*4))
  print("{} . {} = {}".format(n, 5, n*5))
  print("{} . {} = {}".format(n, 6, n*6))
  print("{} . {} = {}".format(n, 7, n*7))
  print("{} . {} = {}".format(n, 8, n*8))
  print("{} . {} = {}".format(n, 9, n*9))
  print("{} . {} = {}".format(n, 10, n*10))

def desafio010():
  
  moneybr = float(input("dinheiro disponível:"))
  dolar = moneybr / 5.11
  print("com essa quantidade de R${} você consegue US${}".format(moneybr, dolar))

def desafio011():
  
  l = float(input("a largura da parede:"))
  a = float(input("a altura da parede:"))
  ar = l * a
  print("a dimensão da parede é {}x{} e sua area é de {}m²".format(l, a, ar))
  t = ar / 2
  print("para pintar a parede precisará de {}l de tinta".format(t))

def desafio012():
  
  p = float(input("preço: R$"))
  n = p - ( p * 5 / 100)
  print("o preço custava R${} com desconto de 5% ficou R${}".format(p, n))

def desafio013():
  
  s = float(input("salario: R$")) 
  n = s + ( s * 15 / 100 )
  print("o funcionário ganhava R${} com 15% de aumento passou a ganhar R${}".format(s, n))

def desafio014():
  
  c = float(input("digite a temperatura ´c:"))
  f = (( 9 * c ) / 5) + 32
  print("a temperatura em {}´c é igual a {}´f".format(c, f))

def desafio015():
  
  d = int(input("quantos dias alugado:"))
  km = float(input("quantos km rodado:"))
  p = (d * 60) + (km * 0.15)
  print("valor a pagar R${}".format(p))

def desafio016():
  
  n = float(input("valor:"))
  print("o valor informado foi de {} e sua parte interia é {}".format(n, int(n)))

def desafio017():
  
  co = float(input("comprimento do cateto oposto:"))
  ca = float(input("comprimento do cateto adjcente:"))
  h = (co ** 2 + ca ** 2) ** (1/2)
  print("a hipotenusa é {}".format(h))

def desafio018():
  
  from math import radians, sin, cos, tan

  an = float(input("digite o angulo:"))
  se = sin(radians(an))
  co = cos(radians(an))
  ta = tan(radians(an))
  print("o angulo {} tem como seno {}".format(an, se))
  print("o angulo {} tem como cosseno {}".format(an, co))
  print("o angulo {} tem como tangente {}".format(an, ta))

def desafio019():
  
  from random import choice

  a1 = input("primeiro aluno:")
  a2 = input("segundo aluno:")
  a3 = input("terceiro aluno:")
  a4 = input("quarto aulno:")
  l = [a1, a2, a3, a4]
  e = choice(l)

  print("o aluno sorteado foi {}".format(e))

def desafio020():

  from random import shuffle

  a1 = input("primeiro aluno:")
  a2 = input("segundo aluno:")
  a3 = input("terceiro aluno:")
  a4 = input("quarto aulno:")
  l = [a1, a2, a3, a4]
  shuffle(l)
  print("ordem de apresentação será ")
  print(l)  

# dasafio021 

def desafio022():
  
  n = input("seu nome:").strip()
  print("analisando...")
  print("nome em maiúsculo: {}".format(n.upper()))
  print("nome em minúsculo: {}".format(n.lower()))
  print("nome tem {} letras".format(len(n) - n.count(" ")))
  s = n.split()
  print("o primeiro nome é {} e ele possui {} letras".format(s[0], len(s[0])))

def desafio023():
  
  n = int(input("numero:"))
  u = n // 1 % 10
  d = n // 10 % 10
  c = n // 100 % 10
  m = n // 1000 % 10
  print("anisando o numero {}".format(n))
  print("unidade {}".format(u))
  print("dezena {}".format(d))
  print("centena {}".format(c))
  print("milhar {}".format(m))

def desafio024():
  
  c = input("qual cidade você nasceu?:").strip()
  print(c[:5].upper() == "SANTOS")

def desafio025():
  
  n = input("nome completo:").strip()
  print("esse nome tem silva? {}".format("silva" in n.lower()))

def desafio026():
  
  f = str(input("digite uma frase:")).upper().strip()
  print("quantidades de vezes que aparece a letra 'A' {}".format(f.count('A')))
  print("a primeira letra 'A' apareceu nessa posição {}".format(f.find('A') +1 ))
  print("a ultima letra 'A' apareceu nessa posição {}".format(f.rfind('A') +1 ))

def desafio027():

  n = str(input("nome completo:")).strip()
  name = n.split()
  print("é um prazer te conhecer")
  print("primeiro nome: {}".format(name[0]))
  print("ultimo nome: {}".format(name[len(name) -1]))

def desafio028():

  from random import randint

  comp = randint(0,5)
  print("=====================")
  print("adivinhe o numero 'dica: é um numero entre 0 e 5'")
  print("====================")

  jog = int(input("bora adivinha ai:"))

  if jog == comp:
    print("PARABÉNS!!!")

  else:
    print("ERROU!!")

def desafio029():

  v = float(input("velocidade atual do seu automóvel:"))

  if v > 80:
    print("MULTADO! você passou do limite de velocidade")

    m = (v - 80) * 7

    print("sua multa é de R${}".format(m))

def desafio030():

  num = int(input("número:"))
  r = num % 2

  if r == 0:
    print("o numero {} é PAR".format(num))

  else:
    print("o numero é {} é IMPAR".format(num))

def desafio031():

  d = float(input("qual a distancia da sua viagem?:"))
  print("você vai comecar sua viagem de {}km".format(d))
  p = d * 0.05  if d <= 200  else d * 0.45
  print("sua passagem custará R${}".format(p))

def desafio032():

  from datetime import date

  a = int(input("qual ano quer que seja analizado? caso queria analisar o ano atual digite 0 :"))

  if a == 0:
    a = date.today().year

  if a % 4 == 0 and a % 100 != 0 or a % 400 == 0:
    print("o ano {} é bissexto".format(a))

  else:
    print("o ano {} não é bissexto".format(a))

def desafio033():

  p = int(input("primeiro valor:"))
  s = int(input("segundo valor:"))
  t = int(input("terceiro valor:"))
  #menor 
  m = p 
  if s < p and s < t:
    m = s

  if t < p and t < s:
    m = t

  #maior
  ma = p
  if s > p and s > t:
    ma = s

  if t > p and t > b:
    ma = t 

  print("menor valor digitado {}".format(m))
  print("maior valor digitado {}".format(ma))

def desafio034():

  s = float(input("qual o salario do funcionario?: R$"))

  if s <= 1250:
    n = s + (s * 15 / 100)

  else:
    n = s + (s * 10 / 100)

  print("quem ganhava R${} passou a ganhar R${}".format(s, n))

def desafio035():

  print("analisando o triangulo...")

  r1 = float(input("primeiro comprimento:"))
  r2 = float(input("segundo comprimento:"))
  r3 = float(input("terceiro comprimento:"))

  if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print("pode ser feito um triangulo")

  else:
    print("não pode ser um triangulo")