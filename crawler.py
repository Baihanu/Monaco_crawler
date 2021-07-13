import os
import time
from decouple import config
from selenium import webdriver
from twocaptcha import TwoCaptcha


class MonacoCrawler:
    """    Inicia definindo as variáveis de sistema    """
    def __init__(self):
        self.cpf = config('CPF')
        self.registro = config('REGISTRO')
        self.chave = config('2CAPTCHA_KEY')
        self.drive = webdriver.Chrome(executable_path=r'chromewebdriver/chromedriver.exe')

    def campos(self):

        """Requisita a url e adentra na mesma."""
        drive = self.drive
        drive.get('http://consultas.detrannet.sc.gov.br/servicos/ConsultaPontuacaoCondutor.asp')

        """Deixa a janela em full screen para que não hajam erros durante capturas de tela."""
        drive.maximize_window()

        """Coloca um tempo de espera de um segundo, para que se tenha certeza que o código do Captcha carregará."""
        time.sleep(1)

        """Tira um print do Captcha."""
        captcha_photo = drive.find_element_by_xpath('//*[@id="imgDesafio"]')
        captcha_photo.screenshot('captcha.png')

        """ Envia a foto para a API do 2Captcha junto com a chave. """

        solver = TwoCaptcha(self.chave)
        result = solver.normal('captcha.png')

        """ Recebe a resposta do Captcha """

        result_code = result['code']

        """ Localiza na página os elementos que serão preenchidos com as variáveis"""

        cpf = drive.find_element_by_xpath(
            '//*[@id="principal"]/form/table[2]/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td[2]/input')

        registro = drive.find_element_by_xpath(
            '//*[@id="principal"]/form/table[2]/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td[2]/input')

        captcha = drive.find_element_by_xpath(
            '//*[@id="principal"]/form/table[2]/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td[2]/input')

        botao_consultar = drive.find_element_by_xpath(
            '//*[@id="principal"]/form/table[2]/tbody/tr[3]/td/fieldset/table/tbody/tr[6]/td/input[1]')

        """ Envia as variáveis de forma automática. """

        cpf.send_keys(self.cpf)
        registro.send_keys(self.registro)
        captcha.send_keys(result_code)
        botao_consultar.click()

        """ Tendo o submit sido feito, reduzo o tamanho da tela para 80%, scrollo até embaixo e tira um print. """
        drive.execute_script("document.body.style.zoom='80%'")
        drive.execute_script("window.scrollTo(0, document.body.scrollHeight);")

        drive.save_screenshot('dados_pessoais.png')

        """ Apaga a imagem do Captcha que não será mais necessária """
        os.remove('captcha.png')

        """ Define as variáveis que serão os valores para o dicionário """

        cond_cpf = drive.find_element_by_xpath('//*[@id="divPontuacao"]/table[2]/tbody/tr/td[2]')
        cond_cnh = drive.find_element_by_xpath('//*[@id="divPontuacao"]/table[2]/tbody/tr/td[4]')
        cond_periodo = drive.find_element_by_xpath('//*[@id="divPontuacao"]/table[2]/tbody/tr/td[6]')
        cond_nome = drive.find_element_by_xpath('//*[@id="divDadosPontuacao"]/table[1]/tbody/tr[1]/td[1]')

        """ Coleto somente o nome do condutor """
        nome = cond_nome.text[18:34]

        monaco_dict = {'CPF': cond_cpf.text, 'CNH': cond_cnh.text, 'Periodo': cond_periodo.text, 'Nome': nome}
        print(monaco_dict)

        """ Fecho a automação """
        drive.quit()


try:
    bot = MonacoCrawler()
    bot.campos()

except:
    print('Estamos com problemas em nossos servidores, por favor, tente novamente em alguns segundos')
