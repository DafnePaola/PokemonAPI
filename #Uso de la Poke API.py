#Uso de la Poke API
import requests
import matplotlib.pyplot as plt 
import matplotlib.image as img 

pokemon = input("Introduce el nombre de un pokemon: ")
url = "https://pokeapi.co/api/v2/pokemon/" + pokemon
res = requests.get(url)

if res.status_code != 200 :
    print("Pokemon no encontrado")
    exit()

imagen = img.imread(res.json()['sprites']['front_default'])
plt.title(res.json()['name'])
imgplot = plt.imshow(imagen)
plt.show()