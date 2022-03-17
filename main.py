from scraper import scraper

print("latest value scraped from the simulator: " + str(scraper.getLatest()))

print("latest errors scraped from the simulator: " + str(scraper.getErrors()))
