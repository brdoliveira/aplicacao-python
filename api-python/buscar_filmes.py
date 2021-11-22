from credentials import key_omdb
from insert_db import insert_db
import numpy as np
import requests as rs
import json 

def adicionar_filmes() -> None:
  id_numero = str(np.random.randint(0,100000))
  while (len(id_numero) != 7):
    id_numero = "0" + id_numero
  id_filme : str = "tt" + id_numero
  consultar_site(id_filme)

def consultar_site(id_filme : str) -> None:
  api_key : str = key_omdb
  resp = rs.request('GET',f'https://www.omdbapi.com/?apikey={api_key}&i={id_filme}').text
  req = json.loads(resp)

  titulo = req['Title']
  lancamento = req['Released']
  duracao = req['Runtime']
  genero = req['Genre'] 
  diretor = req['Director']
  linguagem = req['Language']
  
  if(titulo == ''):
    adicionar_filmes()  
  else:
    insert_db(titulo,lancamento,duracao,genero,diretor,linguagem)
  
  print(f'Filme {titulo} adicionado !')

while True:
  adicionar_filmes()

