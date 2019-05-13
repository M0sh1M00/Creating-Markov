import random

mydict = dict()

endwords=[]
startwords=[]
file = open("MarkovText.txt", "r")


### PART 1, GETTING THE WORDS AND THEIR LIKELYHOODS

for line in file:
  ### Splitting the spaces
  line = line.split(" ")
  if line[0] == "\n" or len(line)==1:
    pass
  else:
    ### Getting rid of \n
    line[-1]=line[-1][:-1]

    ### Checking word in line
    for word in range(len(line)):
      ### If the word is not the last word
      if line[word] == line[0]:
        startwords.append(line[word])
      if line[word]!= line[-1]:
        ### If the word is in the dictionary
        if line[word] in mydict:
          pass
        ### If its not create a dictionary for it
        else:
          mydict[line[word]]=dict()
        ### If the word in front is in the dictionary mentioned prior
        if line[word+1] in mydict[line[word]]:
          mydict[line[word]][line[word+1]] +=1
        else:
          mydict[line[word]][line[word+1]] = 1
      else:
        endwords.append(line[word])
      
###
#print(mydict)
#print(endwords)
#print(startwords)
### PART 2, CREATING THE SENTENCES
def Part2(mydict,startwords,endwords):
  random.shuffle(startwords)
  curWord = startwords[0]
  newWord = "null"
  running = True
  sentence = []
  while running:
    sentence.append(curWord)
    posWords=[]
    for word in mydict[curWord]:
      for iteration in range(mydict[curWord][word]):
        posWords.append(word)
    newWord = random.choice(posWords)
    curWord=newWord
    newWord="null"
    if curWord in endwords:
      sentence.append(curWord)
      running=False
  sentence = " ".join(sentence)
  return sentence



while True:
  print(Part2(mydict,startwords,endwords))
  input()

  



