from bs4 import BeautifulSoup
import lxml

markup = "<b><!--Hey, buddy. Want to buy a used parser?--></b>"
soup = BeautifulSoup(markup, 'lxml')
comment = soup.b.string
print(type(comment))
print(comment)
print(soup.b.prettify())