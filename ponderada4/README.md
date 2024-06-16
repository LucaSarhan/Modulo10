# Ponderada 4

**Sistemas envolvidos:**

Sistema de produtos e usuarios: 
O sistema é responsável pelo gerenciamento de produtos e usuários, oferecendo funcionalidades de criação, leitura, atualização e exclusão (CRUD). Ele utiliza FastAPI para construir a API e SQLAlchemy para a interação com o banco de dados.

Sistema de ordens:
O sistema é responsável pelo gerenciamento de pedidos, permitindo a criação, leitura, atualização e exclusão (CRUD) de ordens. Ele utiliza FastAPI para desenvolver a API e SQLAlchemy para interagir com o banco de dados.

Gateway:
O  sistema atua como um redirecionador para os sistemas mencionados anteriormente. Ele possui logs integrados com filebeat, elasticsearch e kibana, que podem ser visualizados no repositorio.

# Execução da atividade
Para a execução do projeto vai ser necesário 1 terminal. 

Nesse terminal clone o repositório usando o seguinte comando:

```
git clone https://github.com/LucaSarhan/Modulo10.git
```

Posteriormente execute esse comando para entrar no projeto:

```
cd ambiente_clonado/Modulo10/ponderada4
```

Caso necessário instalar as seguintes depencias:
```
cd clientOrders
pip install requirements.txt
```

Caso necessário instalar essas dependencias:
```
cd ../prductsUser
pip install requirements.txt
```

Para executar a ponderada execute esse commando:
```
cd ..
sudo docker compose up
```


# Comprovando o funcionamento
[Link](https://drive.google.com/file/d/1x6mlhvEdhUOVIDe_25I_hV_gd9YqVHQs/view?usp=sharing)
