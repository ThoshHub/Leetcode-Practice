# given this json document url
feed_url = 'https://s3.amazonaws.com/zumper.interviews/feed.json'
    
# 1) fetch the file over https (requests is available for import)

# 2) count the total number of keys 
#    correct answer: 15

# 3) find the _key_ name for the str value with the most characters i.e. len(value)
#    e.g. {'content_html': '<a>long value</a>', 'wrong_long_key': 'a'} == 'content_html'
#    correct answer: content_html

import requests

allvals = []
maxval = ''

def countkeys(r):
    count = 0
    count += len(r.keys())
    # print(r.keys())
    longkeyval = ''
    lenlongkeyval = 0
    
    global allvals
    
    for i in r:
        val = r.get(i)
        if type(val) is dict:
            count += countkeys(val)
        elif type(val) is list:
            for j in val:
                count += countkeys(j)
        else:
            # print(len(val))
            # allvals.append(i)
            if len(val) > lenlongkeyval
            
            
    # return count
    return count
    

r = requests.get(url=feed_url)
s = countkeys(r.json())
# print(s)

print(allvals)

# print(r.json())


# print(r.json().get('version'))
# for i in r.json():
  #  print(i.json().get('content_html'))

# print(type(r.json()))
# print()


        
    