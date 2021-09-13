import requests

def main():
    buscar_dados()

def buscar_dados():
    request = requests.get("https://apisidra.ibge.gov.br/values/t/1612/n6/3101607")
    print(request.content)