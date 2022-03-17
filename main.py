from scraper import scraper
from prometheus_client import start_http_server, Gauge
import time
import os

PORT = os.environ.get('PORT')
if (PORT == None):
    PORT = 8080

if __name__ == '__main__':

    start_http_server(PORT)

    latest = Gauge('latest', 'Latest value from the simulator')
    connectionError = Gauge('group_d_connection_error', 'Current ConnectionError value from the simulator')
    follow = Gauge('group_d_follow', 'Current Follow error value from the simulator')
    tweet = Gauge('group_d_tweet', 'Current Tweet error value from the simulator')
    unfollow = Gauge('group_d_unfollow', 'Current Unfollow error value from the simulator')
    readTimeout = Gauge('group_d_readTimeout', 'Current ReadTimeout error value from the simulator')
    register = Gauge('group_d_register', 'Current Register error value from the simulator')

    while True:
        latest.set(scraper.getLatest())
        errors = scraper.getErrors()
        connectionError.set(errors['ConnectionError'])
        follow.set(errors['follow'])
        tweet.set(errors['tweet'])
        unfollow.set(errors['unfollow'])
        readTimeout.set(errors['ReadTimeout'])
        register.set(errors['register'])

        time.sleep(10)
