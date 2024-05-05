import requests
from bs4 import BeautifulSoup

if __name__ == '__main__':
    simple_html = '<html><body><p>Это самый простой HTML!</p></body></html>'
    soup = BeautifulSoup(simple_html, features='html.parser')
    tag_p = soup.html.body.p
    print(tag_p)
    response = requests.get('https://docs.python.org/4/')
    # Создание "супа" из веб-страницы.
    soup = BeautifulSoup(response.text, features='lxml')
    # Печать "супа".
    print(soup)
    # Печать "супа" с отступами.
    print(soup.prettify())
    # Печать содержимого только тега <body>.
    print(soup.html.body.prettify())
    html_doc = """
    <html>
      <head><title>Сказка о трёх богатырях</title></head>
      <body>
        <p class="title"><b>Сказка о трёх богатырях</b></p>

        <p class="story">
          Давным-давно жили-были три богатыря:
          <a href="http://example.com/ilya" class="hero" id="link1">Илья Муромец</a>,
          <a href="http://example.com/alesha" class="hero" id="link2">Алёша Попович</a> и
          <a href="http://example.com/dobrynya" class="hero" id="link3">Добрыня Никитич</a>.
        </p>

        <p class="story">
          И был у них один противник
          <a href="http://example.com/dragon" class="antihero" id="link4">Змей Горыныч</a>.
        </p>

        <p class="story" name="end">
          Вот и сказке конец, а кто слушал — молодец!
        </p>
      </body>
    </html>
    """
    soup = BeautifulSoup(html_doc, 'lxml')
    # Поиск в коде всех тегов <b>.
    result = soup.find_all('b')
    print(result)
    # Будет напечатано:
    # ['<b>Сказка о трёх богатырях</b>']
    # Поиск в коде всех тегов <title> и <b>.
    result = soup.find_all(['title', 'b'])
    print(result)
    # Будет напечатано:
    # ['<title>Сказка о трёх богатырях</title>', '<b>Сказка о трёх богатырях</b>']
    # Поиск в коде всех элементов с классом 'title'.
    result = soup.find_all(attrs={'class': 'title'})
    print(result)
    # Будет напечатано:
    # ['<p class="title"><b>Сказка о трёх богатырях</b></p>']
    # Поиск в коде всех элементов <a class='hero'>.
    result = soup.find_all('a', attrs={'class': 'hero'})
    print(result)
    # Будет напечатано:
    # ['<a class="hero" href="http://example.com/ilya" id="link1">Илья Муромец</a>',
    # '<a class="hero" href="http://example.com/alesha" id="link2">Алёша Попович</a>',
    # '<a class="hero" href="http://example.com/dobrynya" id="link3">Добрыня Никитич</a>']
    # Поиск в коде всех элементов id='link2'.
    result = soup.find_all(id='link2')
    print(result)
    # Будет напечатано:
    # ['<a class="hero" href="http://example.com/alesha" id="link2">Алёша Попович</a>']
    # Поиск в коде всех элементов class_='antihero'.
    result = soup.find_all(class_='antihero')
    print(result)
    # Будет напечатано:
    # ['<a class="antihero" href="http://example.com/dragon" id="link4">Змей Горыныч</a>']
    # Поиск в HTML-коде всех тегов <p class='story'>. Найдётся три элемента.
    all_stories = soup.find_all('p', class_='story')
    # Берётся только первый тег с индексом 0.
    first_story = all_stories[0]
    # Поиск внутри найденного тега id='link2'.
    link2 = first_story.find_all(id='link2')
    print(link2)
    # Будет напечатано:
    # ['<a class="hero" href="http://example.com/alesha" id="link2">Алёша Попович</a>']
    # Поиск в коде первого элемента <a class="hero">
    result = soup.find('a', attrs={'class': 'hero'})
    print(result)
    # Будет найден только один элемент,
    # хотя под критерии поиска подходят три элемента.
    # <a class="hero" href="http://example.com/ilya" id="link1">Илья Муромец</a>
    # Поиск в коде первого элемента <p class='story'>.
    first_story = soup.find('p', class_='story')
    # Поиск внутри найденного тега элемента <id='link2'>
    link2 = first_story.find(id='link2')
    print(link2)
    # Будет напечатано:
    # <a class="hero" href="http://example.com/alesha" id="link2">Алёша Попович</a>
    first_story = soup.find('p', class_='story')
    link2 = first_story.find(id='link2')
    # Обращение к тексту тега.
    print(link2.text)
    # Будет напечатано:
    # Алёша Попович
    first_story = soup.find('p', class_='story')
    link2 = first_story.find(id='link2')
    # Обращение к атрибуту тега, в котором содержится ссылка.
    print(link2['href'])
    # Будет напечатано:
    # http://example.com/alesha
