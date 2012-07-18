"""
This shows how to use string templates
"""


s1 = """\
Hello There Mr %(YOU)s
It's been almost %(n_days)d days since we last spoke
I believe I still owe you $%(beer).2f for the beer that you paid for me
"""

print("The template string looks like")
print(s1)

print
print("The template string substituted with values looks like")
print(s1%{'YOU':'Foo','n_days':1000,'beer':4.56})
