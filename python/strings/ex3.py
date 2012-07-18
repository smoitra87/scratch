"""
Explore some string functions in python 

"""

# You don't need + for concatenating python strings
x = "/usr/bin" "/mycmd" " -zxvf" " filename.awesome"
print x

# To print warning statements
print("warning".upper().center(40,'*'))

# Demonstrate the use of str.endswith
assert 'www.google.com'.endswith('.com')

# The connection between tabs and white spaces
print 'foo\tbar'.expandtabs()
print 'food\tbar'.expandtabs()
print 'foodie\tbar'.expandtabs()
print 'foodies\tbar'.expandtabs()

print repr("1	12	123	1234	12345	123456	1234567	12345678	")
print "1	12	123	1234	12345	123456	1234567	12345678	123456789"
x = map(lambda i : chr(ord('a')+i), range(9))
print  "\t".join("".join(x[0:i+1]) for i in range(len(x)))


# Justification statements 
print('left'.ljust(20,'<'))
print('center'.center(20,'^'))
print('right'.rjust(20,'>'))

# Partition
print('a/b/c'.partition('/'))
print('a/b/c'.rpartition('/'))

# Zfill # Pads number string with 0
print('123'.zfill(5))


