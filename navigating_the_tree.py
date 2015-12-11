html_doc = """
<html><head><title>The Dormouse's story</title></head>
<body>
<p class="title"><b>The Dormouse's story</b></p>

<p class="story">Once upon a time there were three little sisters; and their names were
<a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
<a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
<a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
and they lived at the bottom of a well.</p>

<p class="story">...</p>
"""

from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

print(soup.head)

print(soup.title)

print(soup.body.b)

print(soup.a)

print(soup.find_all('a'))

print("HEAD TAG")
head_tag = soup.head
print(head_tag)
print("HEAD TAG CONTENTS")
print(head_tag.contents)

title_tag = head_tag.contents[0]
print(title_tag)
print(title_tag.contents)

print(len(soup.contents))
print(soup.contents[1].name)

print("SOUP CHILDREN:-")
for child in soup.children:
	print(child)

print("SOUP CHILDREN LENGTH")
print(len(list(soup.children)))
print("SOUP DESCENDANTS LENGTH")
print(len(list(soup.descendants)))

print("PRINTING STRINGS")
for string in soup.strings:
    print(repr(string))

print("PRINTING STRIPPED STRINGS")
for string in soup.stripped_strings:
    print(repr(string))

print("\n\n GOING UP")
title_tag = soup.title
print(title_tag.parent)
html_tag = soup.html
print(type(html_tag.parent))

link = soup.a
for parent in link.parents:
    if parent is None:
        print(parent)
    else:
        print(parent.name)

print("\n\nGOING SIDEWAYS")
for sibling in soup.a.next_siblings:
    print(repr(sibling))