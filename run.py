from main import get_info, get_depth, get_ticker, trades


def main():
   print(get_info())
   print(get_ticker(coin1='eth'))
   print(trades())
   print(get_depth())

if __name__=='__main__':
   main()