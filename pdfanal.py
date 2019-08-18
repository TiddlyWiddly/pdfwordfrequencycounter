import pdftotext
from nltk.tokenize import word_tokenize
from collections import Counter
import codecs

# creating an object 
myfile = open('1.pdf', 'rb')
outfile = codecs.open("out.html", "w", "utf-8")

# creating a pdf reader object
mypdf = pdftotext.PDF(myfile)

mylist = []
for page in mypdf:
   tokenized = word_tokenize(page)
   i = 0
   while i < len(tokenized):
      #print tokenized[i]
      #fix hyphenated words
      if tokenized[i].endswith('-'):
         try:
            mylist += [tokenized[i].replace("-","") + tokenized[i+1]]
            i = i + 2
         except:
            i = i + 1
         next
      elif tokenized[i].encode('utf-8').lower() in ["ο","το","η","οι","τα","τις","τους","της","του","τον","την", "των"]:
         try:
            #print tokenized[i] + " " + tokenized[i+1]
            mylist += [tokenized[i] + " " + tokenized[i+1]]
            i = i + 2
         except:
            i = i + 1
         next
      #ignore punctuations
      elif tokenized[i].encode('utf-8') in ["(",")",".","...",",","«","»",";",":","!","'"]:
          i = i + 1
          next
      else:
         mylist += [tokenized[i]]
         #print tokenized[i]
      i = i + 1

#convert to lowercase
mylist = [x.lower() for x in mylist]

counted = Counter(mylist).most_common(750)
total = Counter(mylist)

#for i in counted:
#   print str(i[1]) + "\t" + i[0]
#print str(len(total)) + " total unique words, sort of."
num = 1
outfile.write("<html><meta charset=\"utf-8\"/>")
for i in (sorted(total.items(), key= lambda t: (t[1], t[0]), reverse=True)):
   outfile.write(str(num) + ">\t\t" + str(i[1]) + "\t\t" + i[0] + "<br>\n")
   num += 1
   #print str(str(i[1]) + "\t" + str(i[0])).encode('utf-8')
outfile.write("</html>")
