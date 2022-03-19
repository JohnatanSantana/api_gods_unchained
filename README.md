# Gods Unchained 

# incluir sumario
 1. [Requeriments do Projeto](#requeriments)
 2. [Como usar](#howto)
 3. [Stack](#stack)
 
### Requeriments para executar o projeto <a name="requeriments"></a>
Você vai precisar ter instalado na sua maquina:
- Docker version 20.10.8.
- Docker Compose version 1.29.2.

### Como usar <a name="howto"></a>
Baixar repositorio

```
    git clone https://github.com/JohnatanSantana/api_gods_unchained.git
```

Acessar o diretorio onde foi feito o comando acima e execute (provavel pytest)

``` 
    docker-compose up
```

Acesse pelo navegador o link abaixo

>  http://localhost:8000/docs



![alt](/images/api_image.png)


Visualizar quais dados existem no Database:

>  http://localhost:8081/db/godsUnchained/cards

![alt](/images/mongodbui.png)

## Stack <a name="stack"> </a>

Nesse Projeto estamos utilizando:
- [FastAPI](https://fastapi.tiangolo.com/)
- [MongoDB](https://www.mongodb.com/)
- [Docker](https://www.docker.com/)


#### FastAPI
Decidi utilizar o FastAPI pela facilidade, ele cria documentação e também tem uma documentação muito boa. 

#### MongoDB
Banco de Documentos para armazenar os dados já existentes, também poderia ser utilizado o Redis.

#### Docker
Facilidade de criar Container e reproduzir localmente em qualquer maquina.

### To Do
- [ ] - Diminuir tamanho da imagem do docker
- [ ] - criar sh
- [ ] - Testes
- [ ] - k8s
- [ ] - async para o mongo
- [ ] - Router para incluir novos cards
- [ ] - Container com MLFlow