from bs4 import BeautifulSoup
import lxml

soup = BeautifulSoup('<b class="boldest">Extremely bold</b>', 'lxml')
tag = soup.b
print(type(tag))
print(tag.name)
print(tag['class'])
print(tag.attrs)
print(tag.string)
print(type(tag.string))
unicode_string = unicode(tag.string)
unicode_string
print(type(unicode_string))
tag.string.replace_with("No longer bold")
print(tag)