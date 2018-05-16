
from pathlib import Path
from summa import keywords
import sys
import pandas as pd


file_path = sys.argv[1]
wordCount = sys.argv[2]


# file_path = '/home/david/Documents/textrank/aih.txt'
# wordCount = 1

text = Path(file_path).read_text()
keyWords = keywords.keywords(text, words=wordCount).split()

df = pd.DataFrame(keyWords)
print(df)
# df.to_csv('/opt/mycroft/skills/mycroft-bitcoinprice-skill/out.csv', index=False, header=False)





#
# from summa import summarizer
# print(summarizer.summarize(text))
#print(text)aih