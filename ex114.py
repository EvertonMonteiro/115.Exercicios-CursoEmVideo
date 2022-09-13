import urllib.request
try:
    site = urllib.request.urlopen('http://www.pudim.com.br')
except urllib.error.URLError:
    print('O site Pudim não esta disponível no momento.')
else:
    print('Consegui acessar o site pudim!')
    print(site.read())