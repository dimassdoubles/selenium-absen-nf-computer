import requests
def send_message(message):
    TOKEN = "{token}"
    chat_id = "{caht_id}"
    print(message)
    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
    requests.get(url).json()