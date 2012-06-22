"""
Opens up a bowser and then createsa ands gets thwe contenst of the page   
"""


import mechanize
b = mechanize.Browser()
page = b.open("http://www.cs.cmu.edu/~subhodee")

# Initial Print of page
print(repr(page.read()))


print("This does not print anything")
print(repr(page.read()))

print("This prints the page again")
page.seek(0)
print(repr(page.read()))

print("This prints the whole page by doing the seeking for you")
print(repr(page.get_data()))

page.close()


