import markup 
import numpy as np
import pylab as pl


page = markup.page()
header= "This is the header"
footer= "I am the footer"
title="Page for ex1"
page.init(title=title,header=header,footer=footer)
page.br()

text  = ["This is line1 of para1","This is line2 of para2",\
		"This is line3 of para3"];
page.p(text)

page.a("To Google",class_="external",href="http://www.google.com")
page.a("ex1.py",class_="internal",href="ex1.py")

page.br()

# Plot an image and save the link on the document
x = np.random.randn(1000)
n, bins, patches = pl.hist(x,50,normed=1, facecolor='green',\
 alpha=0.75)
pl.title('Histogram of normal with $\mu=0$')
pl.xlabel("Random points")
pl.ylabel("Counts of values")
pl.savefig('hist.png')

page.div()
page.img(width="400",height="300",alt="A histogram",src="hist.png")
page.div.close()

page.br()

# Create a table of some numbers
vals = np.arange(10).reshape((2,5))
page.table(border=1)
page.tr()
page.th(["H"+str(i) for i in range(1,6)])
page.tr()
page.tr()
page.td(vals[0])
page.tr.close()
page.tr()
page.td(vals[1])
page.tr.close()
page.table.close()
page.br()

# Create a list of values
page.ul(class_="mylist")
page.li(["item"+str(i) for i in range(5)],class_="myitem")
page.ul.close()

# Write out the document
with open("ex1.html","w") as fout : 
	fout.write(page.__str__())
