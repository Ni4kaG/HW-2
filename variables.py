# модуль 1
# выбираю описание книги:

book_name = 'Анна Каренина'     #  название
book_author = 'Лев Толстой'     #  автор
price = 537.99                  #  цена
publish_house = 'Эксмо'         #  издательство
publish_year = 2004             #  год издания
hardcover = True                #  в твердом пепеплете
pages_num = 864                 #  страниц в книге


print('Название книги:\t\t', book_name, '\t(тип:', type(book_name),')')
print('Автор:\t\t\t\t', book_author, '\t(тип:', type(book_author),')')
print('Издательство:\t\t', publish_house, '\t\t\t(тип:', type(publish_house),')')
print('Год издания:\t\t', publish_year, '\t\t\t(тип:', type(publish_year),')')
print('В твердом пепеплете:', hardcover, '\t\t\t(тип:', type(hardcover),')')
print('Число страниц:\t\t', pages_num, '\t\t\t(тип:', type(pages_num),')')
print('Цена:\t\t\t\t', price, ' руб. \t(тип:', type(price),')')
