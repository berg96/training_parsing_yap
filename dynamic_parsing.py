from bs4 import BeautifulSoup
from requests_html import HTMLSession


if __name__ == '__main__':
    # Создание сессии, все запросы будут отправляться через неё.
    session = HTMLSession()
    # Делаем запрос
    response = session.get('https://httpbin.org/')
    response.html.render(sleep=3)
    soup = BeautifulSoup(response.html.html, 'lxml')
    swagger = soup.find(id='swagger-ui')
    print(swagger.prettify())
