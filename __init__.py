from os.path import dirname

from adapt.intent import IntentBuilder
from mycroft.skills.core import MycroftSkill
from mycroft.util.log import getLogger
from pathlib import Path
import subprocess
import time




path = '/opt/mycroft/skills/mycroft-articlekeyword-skill/'



__author__ = 'dmp1ce'
LOGGER = getLogger(__name__)

class ArticleKeyword(MycroftSkill):
    def __init__(self):
        super(ArticleKeyword, self).__init__(name="ArticleKeyword")

    def initialize(self):
        self.load_data_files(dirname(__file__))

        intent = IntentBuilder("ArticleKeywordIntent").require("ArticleKeyword").build()
        self.register_intent(intent, self.handle_intent)

    def handle_intent(self, message):
        try:

            proc = subprocess.Popen(['python3', path + 'articlekeywords.py', path +  'aih.txt', '5'], stdout=subprocess.PIPE)
            # print(type(proc.communicate()[0]))


            text = proc.stdout.read()
            rows = text.splitlines()
            # print(text.splitlines())
            #
            count = 0
            s = ""
            for row in rows:
                divide = row.split()
                wordCount = len(divide)
                if wordCount > 1:
                    count = count + 1

                    s += "number "

                    s += str(count)
                    s += ": "
                    #time.sleep(3)

                    s += str(divide[1])

                    s += " "
                    #time.sleep(1)

            firstPart = "The top 5 keywords for this article are: "
            time.sleep(3)
            both = firstPart + s
            self.speak(both)

            # with open(path + 'out.csv', 'r') as content_file:
            #     text = content_file.read()

            
        except:
            self.speak_dialog("not.found")

    def stop(self):
        pass

def create_skill():
    return ArticleKeyword()
