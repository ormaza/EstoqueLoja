class item:  
    def __init__(self, nome, qtd, cat):  
        self.nome = nome  
        self.qtd = qtd 
        self.cat = cat

list_categoria = [];
list_estoque = [];

def addCategoria():
  print('Digite o nome da categoria')
  cat = input()
  list_categoria.append(cat)
  print(cat, 'é a categoria numero', len(list_categoria))

def addItem(item):
  if(len(list_estoque) == 0):
    list_estoque.append(item)
  else:
    for i in list_estoque:
      if(i.nome == item.nome):
        i.qtd = int(i.qtd) + int(item.qtd)
        return -1
    list_estoque.append(item)

def removeItem(item):
  for i in list_estoque:
      if(i.nome == item.nome):
        if(int(i.qtd) - int(item.qtd) < 0):
          print('ERRO: o estoque ficará abaixo de zero!')
        else:
          i.qtd = int(i.qtd) - int(item.qtd)

def gerenciarItem(isAdd):
  print('Nome do item:')
  nome = input()
  print('Quantidade do item:')
  qtd = input()
  if(isAdd):
    print('Categoria do item:')
    cat = input()
  if(isAdd):
    addItem(item(nome, qtd, cat))
  else:
    removeItem(item(nome, qtd, 0))

def listarItens():
  posItem = 1
  for i in list_estoque:
    print(i.nome,' - ', i.qtd,' - ', list_categoria[int(i.cat)-1])
    posItem = posItem + 1

def verificarEstoque():
  for i in list_estoque:
    if(int(i.qtd) < 1):
      print('ALERTA', i.nome, 'está em falta!')

while(1):
  print('')
  verificarEstoque()
  print('GERENCIA DE ESTOQUE')
  print('Digite uma opção:')
  print('1: Listar produtos')
  print('2: Adicionar produtos')
  print('3: Adicionar categorias')
  print('4: Retirar produtos')
  
  op = int(input())

  if op == 1:
    listarItens()
  elif op == 2:
    gerenciarItem(True)
  elif op == 3:
    addCategoria()
  elif op == 4:
    gerenciarItem(False)