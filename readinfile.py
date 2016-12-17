#file = open("newfile.txt", "w")

#file.write("hello world in the new file")

#file.write("and another line")

#________________________________

#file = open('test.txt', 'r')

#print file.read()

#print file.readline()

#file.close()

#________________________________________

#with open('test.txt', 'r') as f:
 #   data = f.readlines()

  #  for line in data:
   #     words = line.split()

#print data

n=0

file = open('test.txt', 'r')
text = file.read()
lines = text.split('\n')

part=lines[n].split()

title = part[0]
url = part[1]

print 'TITLE: '+title+' URL: '+url

print len(lines)





