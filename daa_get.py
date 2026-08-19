import requests
from bs4 import BeautifulSoup
import time
import re

class Req:
    def get_link(self): # getting link
        link = input("please inter your link: ") # link input
        return link

    def connect(self , url):
        try:
            # trying to connect
            t_s = time.time() # timer start
            self.Respond = requests.get(url , timeout=3) # make a request
            t_e = time.time() # timer stop
            self.Respond_text = self.Respond.text
            self.delay = t_e - t_s # calculating server connection delay
            st = self.Respond.status_code # status codes (2XX \ 3XX \ 4XX \ 5XX)
            
            # if there was a successful connection
            if st == 200: # a Successful request
                print("connection was successful!!")
                return True

            elif st != 200: # an Unsuccessful connection
                if st > 300 and st < 399: # Redirects
                    self.new_URL = self.Respond.url # finding new url
                    print("this URL is Redirected !!")
                    print(f"valid link: {self.new_URL}") # show correct link

                elif st > 400 and st < 499: # user fault
                    print(f"error {st} !!")
                    if st == 400: # if it is a bad request
                        print("bad request| The reason for a 400 response is typically due to malformed request syntax, invalid request message framing, or deceptive request routing.")
                    
                    elif st == 401: # Unauthorized
                        print("Unauthorized | you need to log in with an api key or ...")

                    elif st == 403: # forbbiden
                        print("forbidden | it means your not Allowed to enter (ip block , antibot , ...)")
                    
                    elif st == 404: # Not found
                        print("Not found | Invalid link")

                    elif st == 405: # Method not allowed
                        self.Respond = requests.POST(url)

                    elif st == 408: # timeout
                        print(("timeout | connecting was to long!! it gonna be your Internet or ... "))

                    elif st == 429: # Too Many Requests
                        print("Too Many Requests | too many request please wait !!!")
                        for x in range(10,0,-1): # cooldown timer
                            time.sleep(1)
                            print(x)

                elif st > 500 and st < 599: # Server errors
                    print(f"there was an error from server. error{st}")

                else: # another code
                    print(f"Unknown error: {st}")
                
                print("wrong link !! (did you Forget (https://)?")
                

            return False

        except requests.exceptions.Timeout: # if request is imeout
            print("Request timeout!")
        except requests.exceptions.RequestException as e: # if request failed
            print("Request failed:", e)
        except requests.exceptions.InvalidProxyURL  as ef: 
            print("Request failed:", ef)
        except requests.exceptions.ProxyError as pe: # if there was a proxy error
            print("Request failed:", pe )

        
    def bridge(self , url , menu):
        result = self.connect(url) # if it get connected
        if result == True:
            self.search(text_=self.Respond_text , connecion_speed=self.delay , menu_=menu)
        else:
            exite1 = False
            while result == False: # if not get connected
                e = input("exit? (y/n)") # if user want to exit
                link = self.get_link()
                result2 = self.connect(link)
                if result2 == True:
                    self.search(text_=self.Respond_text , connecion_speed=self.delay , menu_=menu)
                else:
                    print("there was a problem this program start shuting down!!")
                    for t in range(10 , 0 , -1):
                        print(t)
                        time.sleep(1) # 1 second delay

    
    def search(self,text_, connecion_speed , menu_):
        self.exite = False
        while self.exite == False:
            try:
                soup = BeautifulSoup(text_ , "html.parser")
                menu_() # showing menu
                option = input("so how can i help you ?").lower() # user option input
            except: # failed to extracing data
                print("there was a problem with extracting data")

            
            if option == "s": # extracing text
                for tag in soup(["script", "style"]):
                    tag.decompose()

                text = soup.get_text(separator=" ", strip=True)
                print(text)

            elif option == "c": # show he html code
                print(text_)

            elif option == "h": # looking for headers
                # functions
                def search_h (tag_name): # searching function
                    header = soup.find_all(tag_name) # search for option
                    for h in header:
                        print(h.text)
                        print("_____________________")
                
                # menu
                print("_______________________")
                print("1 | show all h1 headers")
                print("2 | show all h2 headers")
                print("3 | show all h3 headers")
                print("4 | show all h4 headers")
                print("5 | show all h5 headers")
                print("6 | show all h6 headers")
                print("A | show all headers")
                print("_______________________")
                h_selection = input("please select one:").lower()

                # options
                if h_selection == "1":
                    search_h("h1")
                elif h_selection == "2":
                    search_h("h2")
                elif h_selection == "3":
                    search_h("h3")
                elif h_selection == "4":
                    search_h("h4")
                elif h_selection == "5":
                    search_h("h5")
                elif h_selection == "6":
                    search_h("h6")
                elif h_selection == "a":
                    search_h(["h1" , "h2" , "h3" , "h4" , "h5" , "h6"])
                else:
                    print(f"please inter a valid option ({h_selection}) is not Defined !!")
    
            elif option == "hf": # search in headers
                pass

            elif option == "l": # extracting link from code
                links = soup.find_all("a") # finding all links
                for l in links:
                    print(f"name: {l.text}|link: {l.get("href")}")
                    print("_______________________________________")

            elif option == "w": # searching for a word
                name_input = input("inter a name to start searching: ") # getting word from user
                name = soup.find_all(string=re.compile(name_input , re.IGNORECASE)) # find all words
                for n in name:
                    print(f"text:{n.text}| tag:{n.parent.name}") 
                    print("__________________________________")

            elif option == "t": # testing server speed
                print(f"({connecion_speed}) second")

                # Explanation to the Connection 
                if connecion_speed <= 1:
                    print("the connection was (Perfect)")
                elif connecion_speed > 1 and connecion_speed <= 2:
                    print("the connection was (good)")
                elif connecion_speed > 2 and connecion_speed <= 4:
                    print("the connection was (weak)")
                elif connecion_speed > 4 :
                    print("the connection was (poor)")


            elif option == "m": # monitoring a server
                print("is option is Unable")

            elif option == "n": # finding link by name
                link_name = input("please import link name:") # getting a nam from user
                link_search = soup.find_all("a", link_name) # searching for that link
                for n in link_search:
                    print(f"name: {n.text} |link: {n}")

            elif option == "p": # looking for a tag
                tag_name = input("please input tag name (a , p , h1 , h2 , h3 , h4 , h5 , h6): ").lower()
                if tag_name != "a" and tag_name != "h" and  tag_name != "p": # unvalied tag
                    print("please import valied name")
                else: # valied tag
                    tag_search = soup.find_all(tag_name)
                    for t in tag_search:
                        print(t)
                        print("_________________")

            elif option == "i": # extract all numbers
                numb = soup.find_all("p" , limit=int)
                for n in numb:
                    print(n)
                    print("__________________")

            elif option == "c": # show code
                print(soup)

            elif option == "0": # exiting the program
                self.exite = True
            else:
                print("eplease enter a valid option from menu")