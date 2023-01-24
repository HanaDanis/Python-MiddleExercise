import os
from dotenv import load_dotenv

class log:  
    #file = None
    def __init__(self):
        self.path = os.getenv('PATH')

    load_dotenv()

    def write(self, mes):
        os.chdir(r'C:\\Users\\Hana Danis\\Documents')
        self.file = open('Log.txt', 'a')
        self.file.write(mes)
        self.file.flush()
        self.file.close()




