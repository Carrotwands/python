from urllib import urlretrieve
from progressbar import ProgressBar, Percentage, Bar

def dlProgress(count, blockSize, totalSize):
    pbar.update( int(count * blockSize * 100 / totalSize) )

#url = raw_input("Irj be egy URL-t!")
#fileName = raw_input("Mi legyen a neve?")+".mp4"
#pbar = ProgressBar(widgets=[Percentage(), Bar()])
#urlretrieve(url, fileName, reporthook=dlProgress)






#--------------------------------
n=0

file = open('test.txt', 'r')
text = file.read()
lines = text.split('\n')



#print 'TITLE: '+title+' URL: '+url

while (n < len(lines)):
       
       part=lines[n].split()
       
       fileName = part[0]+".mp4"
       url = part[1]

       pbar = ProgressBar(widgets=[Percentage(), Bar()])
       urlretrieve(url, fileName, reporthook=dlProgress)

       n=n+1
       print fileName+' download finished'



       

