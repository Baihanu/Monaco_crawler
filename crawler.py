import os
import time
from decouple import config
from selenium import webdriver
from twocaptcha import TwoCaptcha


class MonacoCrawler:
    def __init__(self):
        self.cpf = config('CPF')
        self.registro = config('REGISTRO')
        self.chave = config('2CAPTCHA_KEY')
        self.drive = webdriver.Chrome(executable_path=r'chromewebdriver/chromedriver.exe')

    def campos(self):
        drive = self.drive
        drive.get('http://consultas.detrannet.sc.gov.br/servicos/ConsultaPontuacaoCondutor.asp')
        drive.maximize_window()

        time.sleep(1)

        captcha_photo = drive.find_element_by_xpath('//*[@id="imgDesafio"]')
        captcha_photo.screenshot('captcha.png')

        solver = TwoCaptcha(self.chave)
        result = solver.normal('captcha.png')
        result_code = result['code']

        cpf = drive.find_element_by_xpath(
            '//*[@id="principal"]/form/table[2]/tbody/tr[3]/td/fieldset/table/tbody/tr[1]/td[2]/input')

        registro = drive.find_element_by_xpath(
            '//*[@id="principal"]/form/table[2]/tbody/tr[3]/td/fieldset/table/tbody/tr[2]/td[2]/input')

        captcha = drive.find_element_by_xpath(
            '//*[@id="principal"]/form/table[2]/tbody/tr[3]/td/fieldset/table/tbody/tr[3]/td[2]/input')

        botao_consultar = drive.find_element_by_xpath(
            '//*[@id="principal"]/form/table[2]/tbody/tr[3]/td/fieldset/table/tbody/tr[6]/td/input[1]')

        cpf.send_keys(self.cpf)
        registro.send_keys(self.registro)
        captcha.send_keys(result_code)
        botao_consultar.click()

        os.remove('captcha.png')

        drive.save_screenshot('informações_condutor.png')

        cond_cpf = drive.find_element_by_xpath('//*[@id="divPontuacao"]/table[2]/tbody/tr/td[2]')
        cond_cnh = drive.find_element_by_xpath('//*[@id="divPontuacao"]/table[2]/tbody/tr/td[4]')
        cond_periodo = drive.find_element_by_xpath('//*[@id="divPontuacao"]/table[2]/tbody/tr/td[6]')
        cond_nome = drive.find_element_by_xpath('//*[@id="divDadosPontuacao"]/table[1]/tbody/tr[1]/td[1]')

        monaco_dict = {'CPF': cond_cpf.text, 'CNH': cond_cnh.text, 'Periodo': cond_periodo.text, 'Nome': cond_nome.text}
        print(monaco_dict)


bot = MonacoCrawler()
bot.campos()
