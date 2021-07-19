import os

if os.environ.get('TOKEN'):
    token = os.environ['TOKEN']
    chatid = os.environ['CHATID']
    delay = int(os.environ['DELAY'])
else:
    token = "X"
    chatid = "X"
    delay = 120

if os.environ.get('MANAGER') and os.environ['MANAGER'] != 'X':
    manager = os.environ['MANAGER']
else:
    manager = chatid

if os.environ.get('T_PROXY') and os.environ['T_PROXY'] != 'X':
    telegram_proxy = os.environ['T_PROXY']
else:
    telegram_proxy = ''

if os.environ.get('R_PROXY') and os.environ['R_PROXY'] != 'X':
    requests_proxies = {
        'all': os.environ['R_PROXY']
    }
else:
    requests_proxies = {}

if token == "X":
    print("Token not set!")