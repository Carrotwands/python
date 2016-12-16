# coding: utf-8
import requests, sys
link = "http://50.7.164.202:8182/v2oriwtwwwu4tqukwyflnb3wjhqurcwwkymsph5nsb2rjuu3cw7g33ruoy/video.mp4"
file_name = "proba.mp4"
with open(file_name, "wb") as f:
        print ("Downloading %s" % file_name)
        response = requests.get(link, stream=True)
        total_length = response.headers.get('content-length')

        if total_length is None: # no content length header
            f.write(response.content)
        else:
            dl = 0
            total_length = int(total_length)
            for data in response.iter_content(chunk_size=4096):
                dl += len(data)
                f.write(data)
                done = int(50 * dl / total_length)
                sys.stdout.write("\r[%s%s]" % ('=' * done, ' ' * (50-done)) )    
                sys.stdout.flush()
