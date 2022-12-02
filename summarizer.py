import requests
from bs4 import BeautifulSoup
import re 
import string 
import operator
class Summarizer:
    def cleanInput(self,input):
        input = re.sub("\n+","",input)
        input = re.sub('\[[0-9]*\]','',input)
        input = re.sub(" +"," ",input)
        input = bytes(input,'UTF-8')
        input = input.decode("ascii",'ignore')
        cleanInput = []
        input = input.split(" ")
        for item in input:
            item.strip(string.punctuation)
            if len(item) > 1 or (item.lower() == 'a' or item.lower() == 'i'):
                cleanInput.append(item)
        return cleanInput
    def ngrams(self,input,n):
        input = self.cleanInput(input)
        output = {}
        for i in range(len(input)-n+1):
            ngramsTemp = " ".join(input[i:i+n])
            if ngramsTemp not in output:
                output[ngramsTemp] = 0
            output[ngramsTemp] += 1
        return output
    def run(self):
        bs_obj = BeautifulSoup(requests.get("https://tolonews.com/index.php/afghanistan-180992").content,"html.parser").find("div",{"id",re.compile("wrapper")}).get_text()
        ngrams = self.ngrams(bs_obj,2)
        sortedNGrams = sorted(ngrams.items(),key= operator.itemgetter(1),reverse=True)
        print(sortedNGrams)
if __name__ == "__main__":
    bot = Summarizer()
    bot.run()