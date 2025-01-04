from requests import get;

allwords = get("https://random-word-api.herokuapp.com/all")

def WordGenerator():
   randomword = get("https://random-word-api.herokuapp.com/word");
   return randomword.json();

lessThanFiveCharacters = list(filter(lambda x: len(x)<3, allwords.json()));
fiveTotenCharacters = list(filter(lambda x: len(x)>=5 and len(x)<=10, allwords.json()));
greaterthanTenCharacters = list(filter(lambda x: len(x)>10, allwords.json()));