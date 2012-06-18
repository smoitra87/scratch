"""
Goes to a HTML forms demo page and tries to submit some data to it
using the mechanize browser

"""

import mechanize
import re

page_link= "http://www.w3schools.com/html/html_forms.asp"

# Start the brower
b = mechanize.Browser()
b.open(page_link)
assert(b.viewing_html())

# Find the HTML 5 tutorial link and goto it
response1 = b.follow_link(text="HTML5 Tutorial")
assert(b.viewing_html())
print(b.title())
print(response1.geturl())
print(response1.info())
print(response1.read())

# Go back to the form page
response2 = b.back()
b.select_form(name="input0")
b["user"] = "Super Man"
response3 = b.submit()

# Print the currently selected form
print("Currently selected form is")
print(b.form)

# Print the resuls of what sumbitting the previous form returned
assert(b.viewing_html())
print(response3.geturl())
print(response3.info())
print(response3.get_data())

# Go back to the forms page. Find all the forms and print their names
b.back()
page = b.response()

for form in b.forms() : 
	print(form.name)

