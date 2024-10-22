import requests

url = input('Insert the URL')

plugins_encontrados = []

def buscarPluginsEnWp(plugin):
    respuesta = requests.get(url + plugin)
    print('buscando plugin', plugin)
    if respuesta.status_code == 403:
        plugins_encontrados.append(plugin)

with open('plugins.txt', 'r') as file:
    plugins = [line.strip() for line in file if line.strip()]

for plugin in plugins:
    buscarPluginsEnWp(plugin)

print('La web', url.split('/wp-content')[0], 'tiene los siguientes plugins:', plugins_encontrados)
