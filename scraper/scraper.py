from bs4 import BeautifulSoup
import requests


def getLatest() -> int:
    latestUrl = "http://164.92.246.227/chart.svg"
    latest = 0
    result = requests.get(latestUrl)
    doc = BeautifulSoup(result.text, 'html.parser')
    graphLineGraphVertical = doc.g
    for g in graphLineGraphVertical:
        if ("overlay" in g['class']):
            overlay = g
            for s in overlay:
                # print(s.attrs)
                if ("serie-3" in s['class']):
                    serie = s
                    for g in serie:
                        dots = g
                        for d in dots:
                            if ("value" in d['class']):
                                # print(d.attrs)
                                value = d
                                for v in value:
                                    latest = v

    return int(latest)


def getErrors() -> dict:

    data = []
    returnData = {}
    errorUrl = "http://164.92.246.227/error_chart.svg"
    result = requests.get(errorUrl)
    doc = BeautifulSoup(result.text, 'html.parser')
    graphStackedbarGraphVertical = doc.g


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


    for d in data:
        if "ReadTimeout" in d:
            returnData.setdefault("ReadTimeout", d["ReadTimeout"])
        if "register" in d:
            returnData.setdefault("register", d["register"])
        if "tweet" in d:
            returnData.setdefault("tweet", d["tweet"])
        if "follow" in d:
            returnData.setdefault("follow", d["follow"])
        if "unfollow" in d:
            returnData.setdefault("unfollow", d["unfollow"])
        if "ConnectionError" in d:
            returnData.setdefault("ConnectionError", d["ConnectionError"])

    return returnData

