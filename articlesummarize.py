
from pathlib import Path
import sys

file_path = sys.argv[1]
#'/home/david/Documents/textrank/aih.txt'
text = Path(file_path).read_text()


from summa import summarizer
print(summarizer.summarize(text, words=75))
#print(text)