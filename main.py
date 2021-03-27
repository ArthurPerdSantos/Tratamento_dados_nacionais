from datas_br import Datas_br
from datetime import datetime
from acesso_cep import Busca_endereco
import requests


cep = 96610000
obj_cep = Busca_endereco(cep)
bairro, cidade, uf = obj_cep.acessa_via_cep()

print(bairro, cidade, uf)
