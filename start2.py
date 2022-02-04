import requests
from bs4 import BeautifulSoup
page = requests.get('https://www.thomann.de/fr/sets_batterie_complets.html')

file = open("main.html", "w", encoding="utf-8")
file.write('''<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
    <title>Python Parsing</title>
</head>
<body>''')

data = BeautifulSoup(page.content,"html.parser")
results= data.find_all("div" , class_="fx-product-list-entry")
counter = 0

for result in results:
  name = result.find("div", class_="product__title fx-text")
  image = result.find("x", class_="fx-image")
  price = result.find("span", class_="fx-price-group__primary")
  productfile = open(f"product-{counter}.html", "w", encoding="utf-8")
  counter = counter+1

  file.write(f'''<div class="card">
  <div class="card-header">
			{name}
	</div>
	<div class="card-body">
			{image}
			<li> price :{price}</li>
	</div>
	<a href="product-{counter}.html">Voir item</a>
	</div>''')

  requestBaguetterie =requests.get(f'https://www.baguetterie.fr/catalogsearch/result/?q=drum#q=pzarl&idx=baguetterie_fr_products&p=0&hFR[categories.level0][0]=Batterie&is_v=1')
  dataBaguetterie = BeautifulSoup(requestBaguetterie.content,"html.parser")
  baguetterieResults= data.find_all("div" , class_="result-content")
  print(dataBaguetterie)
  productfile.write(f'''
    <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta http-equiv="X-UA-Compatible" content="IE=edge">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymous">
            <title>Python Parsing</title>
        </head>
        <body>
        <div class="card">
        <div class="card-header">
            {name}
        </div>
        <div class="card-body">
            {image}
            <li> price :{price}</li>
        </div>
        </div>
        <h2> Résultats sur la baguetterie<h2>
    ''')

for resultBaguetterie in baguetterieResults:
    print(resultBaguetterie)
    bagName = resultBaguetterie.find("h3", class_="result-title")
    bagImageContainer = resultBaguetterie.find("div", class_="result-thumbnail")
    bagImage = bagImageContainer.find("img")
    bagPrice = resultBaguetterie.find("span", class_="price")

    productfile.write('''
    <div class="card">
    <div class="card-header">
        {bagName}
    </div>
    <div class="card-body">
        {bagImage}
        <li> price :{bagPrice}</li>
    </div>
    </div>
    '''
    )

    productfile.write('''
    </body>
    </html>''')



file.write('''
</body>
</html>''')
