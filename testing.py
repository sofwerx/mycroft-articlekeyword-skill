
import subprocess

proc = subprocess.Popen(['python3', 'articlekeywords.py',  'aih.txt' , '5'], stdout=subprocess.PIPE )
#print(type(proc.communicate()[0]))

# path = '/opt/mycroft/skills/mycroft-bitcoinprice-skill/'

text = proc.stdout.read()
rows = text.splitlines()


#print(text.splitlines())

count = 0
s = ""
for row in rows:
    divide = row.split()
    wordCount = len(divide)
    if wordCount > 1:
        count = count + 1

        s += str(count)
        s += " "
        s += str(divide[1])
        s += " "


print(s)

# with open(path + 'out.csv', 'r') as content_file:
#     text = content_file.read()
# self.speak_dialog("bitcoin.price", data={'price': str(text)})

#file_path = '/opt/mycroft/skills/mycroft-bitcoinprice-skill/out.csv'
#wordCount = 10
#
# text = Path(file_path).read_text()
# #print(exit_code)