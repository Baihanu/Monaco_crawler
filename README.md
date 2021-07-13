# Monaco_crawler
Desafio de desenvolvimento de uma automação para empresa Mônaco.

A consulta é feita no site: [Detran SC](http://consultas.detrannet.sc.gov.br/servicos/ConsultaPontuacaoCondutor.asp)

É utilizado o [2Captcha](https://2captcha.com/) para quebra do Normal Captcha, portanto, é necessária, chave do mesmo.

É utilizado também Chrome Versão 91.0.4472.124 (Versão oficial) 64 bits.

Por esse motivo o Chrome Webdriver está junto do repositório.

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
py -3 -m venv .venv
.venv\Scripts\activate
copy env-sample .env
pip install -r requirements.txt
```


