from bs4 import BeautifulSoup
import requests
class Dimage:
    def __init__(self,url):
        self.url = str(url)
        self.page = self.getPage()
        self.i = 0
        self.main()
    def getPage(self):
        web = requests.get(self.url).text
        return BeautifulSoup(web,"html.parser")
    def getImage(self,img):
        imgSrc = img.get("data-src")
        imgNanme = img.get("alt")
        try:
            fic = open(imgNanme+".jpg","wb")
            fic.write(requests.get(imgSrc).content)
            print(f"file write: {imgNanme} ? {self.i} ")
            self.i = 0
        except:
            print("error")
            exit(1)
    def main(self):
        self.imgs = self.page.findAll("img")
        for img in self.imgs:
            self.getImage(img)
url = input("entrer une url:")
Dimage(url)