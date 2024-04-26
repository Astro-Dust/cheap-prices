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
	devices_links = soup.find_all('a', {'class':'promotion-item__link-container'})

	print(f'\x1b[6;30;42m [-- PRODUTOS DA SAMSUNG EM PROMOÇÃO --] \x1b[0m \n')

	for device, price, link in zip(devices, prices, devices_links):
		price_converted = float(price.text.replace('.', '').replace(',', '.')) # um pra tirar o ponto . e outro pra substituir o , por . pra transformar em float
		device_text = device.get_text().lower()
		devices_links = link['href']

		if 'samsung' in device_text and price_converted <= 1000:
			print(f'{device_text.title()} --- R${price_converted}')
			print(f'Buy at -> {devices_links}')
			print()

extract_prices("https://www.mercadolivre.com.br/ofertas")