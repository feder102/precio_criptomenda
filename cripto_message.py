import requests
import telegram
import time
from config import CHAT_ID, TOKEN

# Bot Token para Telegram
bot = telegram.Bot(token=TOKEN)

# CoinMarketCap API URL
url = 'https://pro-api.coinmarketcap.com/v1/cryptocurrency/quotes/latest'

# Parámetros para la API
params = {
  'symbol': 'BTC,BNB,ETH',
  'convert': 'USD'
}

# Cabecera con la API Key
headers = {
  "Accepts": "application/json",
  "X-CMC_Pro_API_Key": "cfc81648-b9a2-45c8-9424-10db79de99d7"
}

# Bucle infinito para enviar el precio cada 6 Horas
while True:
  # Hacer una solicitud a la API
  response = requests.get(url, headers=headers, params=params)

  # Obtener la respuesta en formato JSON
  data = response.json()

  # Crear un mensaje con los precios de las criptomonedas
  message =  'Precios de criptomonedas:\n'
  message += 'Bitcoin (BTC): $' + str(round(data['data']['BTC']['quote']['USD']['price'],2)) + '\n'
  message += 'Binance Coin (BNB): $' + str(round(data['data']['BNB']['quote']['USD']['price'],2)) + '\n'
  message += 'Ethereum (ETH): $' + str(round(data['data']['ETH']['quote']['USD']['price'],2)) + '\n'

  # Enviar el mensaje a Telegram
  bot.send_message(chat_id=CHAT_ID, text=message)

  # Esperar 6 horas
  time.sleep(6 * 60 * 60)