# Monaco_crawler
Desafio de desenvolvimento de uma automação para empresa Mônaco.

A consulta é feita no site: [Detran SC](http://consultas.detrannet.sc.gov.br/servicos/ConsultaPontuacaoCondutor.asp)

É utilizado o [2Captcha](https://2captcha.com/) para quebra do Normal Captcha, portanto, é necessária, chave do mesmo.

É utilizado também Chrome Versão 91.0.4472.124 (Versão oficial) 64 bits.

Por esse motivo o Chrome Webdriver está junto do repositório.

Assim que o script terminar de rodar, a imagem solicitada estará na raiz do projeto, com o nome "dados_pessoais.png"
## Para Desenvolver:

1. Clone o repositório.
2. Crie um virtualenv com Python 3.9.
3. Ative o virtualenv.
4. Instale as dependências.
5. Adicione as variáveis de ambiente referentes à sua realidade.

### Ambientes Linux:
```
python3 -m venv .venv
source .venv/bin/activate
cp env-sample .env
pip install -r requirements.txt
```
### Ambientes Windows:
```
Set-ExecutionPolicy Unrestricted -Scope Process
py -3 -m venv .venv
.venv\Scripts\activate
copy env-sample .env
pip install -r requirements.txt
```
### Caso queira liberar os scripts como Admnistrador no Ambiente Windows:
[Clique aqui](https://docs.vmware.com/en/vRealize-Automation/7.6/com.vmware.vra.iaas.hp.doc/GUID-9670AFC5-76B8-4321-822A-BCE05800DB5B.html)

Para quem usa Windows:

Crie o arquivo: 
```nome_do_projeto\.venv\Scripts\mng.bat```

No conteúdo do arquivo: 
```@python "%VIRTUAL_ENV%\..\manage.py" %*```

O comando equivalente ao alias no Windows é:

```doskey mng=@python "%VIRTUAL_ENV%\..\manage.py" $*```


# Scripts para trabalhar com postgres

```
#!/bin/bash

# Update
sudo apt update

# Install postgres
sudo apt install -y postgresql postgresql-contrib

# Create database
sudo -u postgres createdb <_project_name_>

# sudo su - postgres
# psql
# CREATE USER postgres;
# ALTER USER postgres WITH PASSWORD 'postgres';
# ALTER DATABASE <_project_name_> OWNER TO postgres;
```
