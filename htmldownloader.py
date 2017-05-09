import urllib2

Homepage=raw_input("Welche Adresse wollen sie downloaden? ")

fd=urllib2.urlopen(Homepage)
content=fd.read()
fd.close()
print content

f = file('website.html', 'w')
f.write(content)
