import requests
from bs4 import BeautifulSoup

def extract_prices(url):
	
	response = requests.get(url) # requisiçao http com header, código de status, conteúdo (html), etc.

	if response.status_code != 200:
		print('Failed to request data: ', response.status_code)
		return
	
	soup = BeautifulSoup(response.text, "html.parser") # para reconhecer como texto html

	devices = soup.find_all('p', {'class':'promotion-item__title'})
	prices = soup.find_all('span', {'class':'andes-money-amount__fraction'})

	print(f'\x1b[6;30;42m [-- PRODUTOS DA SAMSUNG EM PROMOÇÃO --] \x1b[0m \n')

	for device, price in zip(devices, prices):

		if 'samsung' in device_text and price_converted <= 1000:
			print(f'{device_text.title()} --- R${price_converted}')

extract_prices("https://www.mercadolivre.com.br/ofertas")