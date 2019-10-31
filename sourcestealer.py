#-*-coding:utf-8-*-
#shitty code,lmao

from bs4 import BeautifulSoup
import requests
import os
import random
import webbrowser

while True:
    os.system("color a")

    print("""

     ██╗    ██╗███████╗ ██████╗███████╗
     ██║    ██║██╔════╝██╔════╝██╔════╝
     ██║ █╗ ██║███████╗██║     ███████╗
     ██║███╗██║╚════██║██║     ╚════██║
     ╚███╔███╔╝███████║╚██████╗███████║
      ╚══╝╚══╝ ╚══════╝ ╚═════╝╚══════╝
    # Written by Scarlet | github.com/scarletdev | discord.me/scarlet
    # Disclaimer: Please add "http://" or "https://" to the beginning of the url.
    """)
    print("█"*90)
    url = str(input("URL: "))
    #url = "https://www.google.com/"

    r = requests.get(url)

    soup = BeautifulSoup(r.content,"lxml")

    x = soup.find("head")
    xxx = str(input("""
    0)Exit
    1)View Source Code Here
    2)Save to Desktop
    3)Find
    4)Subscribe to Creator's Channel
    """))

    desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')

    if xxx == "0":
        print("Quitting...")
        raise SystemExit

    elif xxx == "1":
        print("Viewing...")
        print(soup.prettify())

    elif xxx == "2":
        print("Saving...")
        desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
        a = str(random.randrange(1,696969))
        #file = open(desktop + "\\" + a + ".txt","w")
        file = open(desktop + "\\" + a + ".html","w")
        file.write(soup.prettify())
        file.close()

    elif xxx == "3":
        ask = str(input("What do you want to find(?):"))
        soup1 = BeautifulSoup(r.content,"lxml")
        result = str(soup1.find_all(ask))
        #result = str(soup1.find(ask))
        options = str(input("""Done.
        (1)View
        (2)Save to Desktop :
        """))

        if options == "1":
            print("\n",result)

        elif options == "2":
            desktop = os.path.join(os.path.join(os.environ['USERPROFILE']), 'Desktop')
            with open(desktop + "\\" + str(random.randrange(1,60000)) + ".html","w") as ff:
                fWrite = ff.write(result)

    elif xxx == "4":
        webbrowser.open("https://www.youtube.com/channel/UCyxPTPhPcu6FDfliEgc76fQ?sub_confirmation=1")
