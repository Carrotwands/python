#import urllib.request as urllib
from urllib import urlretrieve
from progressbar import ProgressBar, Percentage, Bar

def dlProgress(count, blockSize, totalSize):
    pbar.update( int(count * blockSize * 100 / totalSize) )

url = "http://50.7.164.202:8182/v2oriwtwwwu4tqukwyflnb3wjhqurcwwkymsph5nsb2rjuu3cw7g33ruoy/video.mp4"
fileName = "example.mp4"
pbar = ProgressBar(widgets=[Percentage(), Bar()])
urlretrieve(url, fileName, reporthook=dlProgress)


