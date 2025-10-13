import requests, os

class WhitepaperScaper:
    """
    This Def is use to scrape CryptoCurrency whitepaper from bitscreener
    """
    def __init__(self):   
        self.HEADERS = {"User-Agent": "Mozilla/5.0"}
        os.makedirs("Data/whitepapers/", exist_ok=True)

    def CoinRetreiver(self,input:str):
        coins = []
        split = input.split(",")
        print(f"Coins Are : {split}")
        for c in split:
            coins.append(c)
        for coin in coins:
            url = f"https://files.bitscreener.com/whitepaper/{coin}-whitepaper.pdf"
            print(f"Trying {url} ...", end=" ")
            r = requests.get(url, headers=self.HEADERS)
            if r.status_code == 200 and r.content[:4] == b"%PDF":
                path = f"Data/whitepapers/{coin}.pdf"
                with open(path, "wb") as f:
                    f.write(r.content)
                print(f"saved to {path}")
            else:
                print('Oops, coin not found')

s = WhitepaperScaper()
s.CoinRetreiver("bitcoin,ethereum,tether")
