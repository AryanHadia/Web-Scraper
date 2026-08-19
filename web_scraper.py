from daa_get import Req

class Web_scraper:
    def menu_(self): # menu design
        print("____________________")
        print("s | Strip")
        print("l | Extracting all links")
        print("h | Finding all headers")
        print("w | Searching for a word or text")
        print("t | Testing server speed")
        print("m | Server monitoring (Unavailable)")
        print("0 | quit")
        print("____________________")
    
    def web_scraping(self):

        link = Req().get_link()
        while not link : # if the link was not intered
            print("please inter link !!")
            link = Req().get_link()
        else:
            Req().bridge(url=link , menu=self.menu_)

Web_scraper().web_scraping()
