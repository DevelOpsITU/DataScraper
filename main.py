from bs4 import BeautifulSoup
import requests

latest = 0
readTimeout = 0
register = 0
tweet = 0
unfollow = 0
connectionError = 0
follow = 0


readTimeoutIndex = 0
registerIndex = 0
tweetIndex = 0
unfollowIndex = 0
connectionErrorIndex = 0
followIndex = 0

latestUrl = "http://164.92.246.227/chart.svg"
errorUrl = "http://164.92.246.227/error_chart.svg"


result = requests.get(latestUrl)
doc = BeautifulSoup(result.text, 'html.parser')
graphLineGraphVertical = doc.g
for g in graphLineGraphVertical:
    if("overlay" in g['class']):
        overlay = g
        for s in overlay:
            #print(s.attrs)
            if("serie-3" in s['class']):
                serie = s
                for g in serie:
                    dots = g
                    for d in dots:
                        if( "value" in d['class']):
                            #print(d.attrs)
                            value = d
                            for v in value:
                                latest = v

print("latest value scraped from the simulator: " + str(latest))



result = requests.get(errorUrl)
doc = BeautifulSoup(result.text, 'html.parser')
graphStackedbarGraphVertical = doc.g

data = []

for g in graphStackedbarGraphVertical:
    if ("legends" in g['class']) and (len(g['class']) == 1):
        legends = g
        for g in legends:
            data.append({g.text: 0})

i = 0
for g in graphStackedbarGraphVertical:
    if ("plot" in g['class']) and (len(g['class']) == 1):
        plot = g
        for g in plot:
            if("series" in g['class']): # ReadTimeout
               bar = g.g.g
               for obj in bar:
                   if("value" in obj['class']):
                       keys = data[i].keys()
                       data[i].update({list(keys)[0]: int(obj.text)})
                       i = i + 1


print(data)

for d in data:
    if "ReadTimeout" in d:
        readTimeout = d["ReadTimeout"]
    if "register" in d:
        register = d["register"]
    if "tweet" in d:
        tweet = d["tweet"]
    if "follow" in d:
        follow = d["follow"]
    if "unfollow" in d:
        unfollow = d["unfollow"]
    if "ConnectionError" in d:
        connectionError = d["ConnectionError"]


print("ReadTimeout value scraped from the simulator: " + str(readTimeout))
print("register value scraped from the simulator: " + str(register))
print("tweet value scraped from the simulator: " + str(tweet))
print("unfollow value scraped from the simulator: " + str(unfollow))
print("connectionError value scraped from the simulator: " + str(connectionError))
print("follow value scraped from the simulator: " + str(follow))

