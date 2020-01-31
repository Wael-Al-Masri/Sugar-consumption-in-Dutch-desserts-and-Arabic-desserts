from bs4 import BeautifulSoup
import requests
import xlsxwriter

page_nr = 1
recipe_urls = []

while page_nr < 116:
    try:
        #here you can change the link by adding the link to the website that you would like to scrap
        source = requests.get(f"https://kitchen.sayidaty.net/recipes/index/category/2811/cuisine/2405/?page={page_nr}").text

        soup = BeautifulSoup(source, 'lxml')
        for recipe in soup.find_all('div', class_="article-item-title"):
            a = recipe.find('a')
            recipe_urls.append(a['href'])
        page_nr += 1

    except:
        pages = False
    #if len(recipe_urls) > 20:
        #break


exCounter = 0
workbook = xlsxwriter.Workbook('databases\database.xlsx')
worksheet = workbook.add_worksheet()
for url in recipe_urls:
    exCounter += 1
    titleexc = 'A' + str(exCounter)
    ingredientsexc = 'B' + str(exCounter)
    peopleExc = 'C' + str(exCounter)
    urlExc = 'D' + str(exCounter)
    source = requests.get(url).text
    soup = BeautifulSoup(source, 'lxml')
    ingredients = soup.find('div', class_="ingredients-area")
    title = soup.find('div', class_="entry-title")
    people = soup.find('div', class_="recipe-meta")
    if people.text[people.text.index("أشخاص") - 3] != '/n':
        next_word = people.text[people.text.index("أشخاص") - 3] + people.text[people.text.index("أشخاص") - 2]
    else:
        next_word = people.text[people.text.index("أشخاص") - 2]
    if title != None and ingredients != None and people!= None :
        worksheet.write(titleexc, title.text)
        worksheet.write(ingredientsexc, ingredients.text)
        worksheet.write(peopleExc, next_word)
        worksheet.write(urlExc, url)
    if exCounter == 17:
        workbook.close()
        break


