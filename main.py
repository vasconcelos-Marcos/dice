from random import randint
 
class simuladorDeDados:
  def __init__(self):
    self.minimo = 1
    self.maximo = 6
    self.mensagem = 'Gostaria de rodar o dado? [s/n]: ';
    
  def start(self):
    resposta = input(self.mensagem).lower()
    try:
      if resposta == 's':
        number = self.quant()
        for n in range(number):
          print(f'Dado {n+1}: {self.rodarDado()}.')
      elif resposta == 'n':
        print('Encerrando.')
      else:
        print('Insira uma resposta válida!')
    except:
      print('Ocorreu um erro ao processar as informações.')

  def rodarDado(self):
    return randint(self.minimo, self.maximo)

  def quant(self):
    number = int(input('Quantos dados deseja rodar: '))
    return number

a = simuladorDeDados()
a.start()