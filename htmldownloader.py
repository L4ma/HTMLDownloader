import urllib2

Website=raw_input("What's the webadress you want to download? ")

fd=urllib2.urlopen(Website)
content=fd.read()
fd.close()

f = file('Website.html', 'w')
f.write(content)

print 'Thank you, for using this program! :)'





#Copyright by L4ma
