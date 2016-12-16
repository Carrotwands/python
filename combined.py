from urllib import urlretrieve
from progressbar import ProgressBar, Percentage, Bar

def dlProgress(count, blockSize, totalSize):
    pbar.update( int(count * blockSize * 100 / totalSize) )

n=0

file = open('test.txt', 'r')
text = file.read()
lines = text.split('\n')

while (n < len(lines)):
       
       part=lines[n].split()
       
       fileName = part[0]+".mp4"
       url = part[1]

       pbar = ProgressBar(widgets=[Percentage(), Bar()])
       urlretrieve(url, fileName, reporthook=dlProgress)

       n=n+1
       print fileName+' download finished'
