import requests
import os.path

save_path = 'inf/'

def get_info():
   responce = requests.get(url='https://yobit.net/api/3/info')
   
   with open(os.path.join(save_path,'info.txt'),'w') as file:            #save in derictory with the "os"
      file.write(responce.text)
      
   return responce.text


def get_ticker(coin1='btc', coin2='usd'):
   #responce = requests.get(url='https://yobit.net/api/3/ticker/eth_btc-xpr_btc?ignore_invalid=1')
   responce = requests.get(url=f'https://yobit.net/api/3/ticker/{coin1}_{coin2}?ignore_invalid=1')
   
   with open(os.path.join(save_path,'ticker.txt'), 'w') as file:
      file.write(responce.text)
   
   return responce.text


def get_depth(coin1='btc', coin2='usd', limit=150):
   responce = requests.get(url=f'https://yobit.net/api/3/depth/{coin1}_{coin2}?limit={limit}&ignore_invalid=1')
   
   with open(os.path.join(save_path,'depth.txt'), 'w') as file:
      file.write(responce.text)
   
   bids = responce.json()[f'{coin1}_usd']['bids']
   
   total_bids_amount = 0
   for item in bids:
      price = item[0]
      coin_amount = item[1]
      
      total_bids_amount += price * coin_amount
   
   return f'Total bids: {total_bids_amount} $'


def trades(coin1='btc', coin2='usd', limit=150):
   responce = requests.get(url=f'https://yobit.net/api/3/trades/{coin1}_{coin2}?limit={limit}&ignore_invalid=1')
   
   with open(os.path.join(save_path,'trades.txt'), 'w') as file:
      file.write(responce.text)
   
   return responce.text
