# DataScraper

The purpose of this application is to scrape the information of current error status from http://164.92.246.227/status.html
where the two graphs exists 

![img.png](res/statusPage/Status-filer/chart.svg)

![img_1.png](res/statusPage/Status-filer/error_chart.svg)

These graphs shows what the simulator sees and this data would be nice to track and see if we have an error, or we introduce a new error.

The idea is to make a prometheus /metrics endpoint that with this data could be visualized.