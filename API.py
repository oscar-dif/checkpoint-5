import requests

def get_phone(r):
    r = requests.get('http://localhost:5000/api?action=phone&name=Urban')
    return r.text
def get_name(r):
    r = requests.get('http://localhost:5000/api?action=name&phone=0435-4355438')
    return r.text
