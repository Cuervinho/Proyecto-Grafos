import string
import json


class Reader:  
    
    def __init__(self, filename):
        self.filename = filename
    
    #Convierte la informacion del archivo a una lista
    def filetolist(self):
        
        with open(self.filename, "r", encoding="utf8") as file:
            word = ""
            Words = list(string.ascii_letters)
            Words.extend(['á','é','í','ó','ú','ñ','Ñ'])
            self.info = []

            for i in file.read():
                if i in Words:
                    word += i

                else:
                    self.info.append(word.lower())
                    word = "" 

        with open("info.txt", "w") as outFile:
            json.dump(self.info, outFile)

        return self.info

    #Retorna la informacion de la palabra con todas sus repeticiones
    def InfoToDict(self):

        self.filetolist()

        self.info_update = dict()

        for i in self.info:
            self.info_update[i] = 0

        for i in self.info:
            self.info_update[i] += 1

        if self.info_update[""]:
            del self.info_update[""]


        info = json.dumps(self.info_update)
        with open("info_update.json", "w") as outFile:
            outFile.write(info)

        return self.info_update


if __name__ == "__main__":
    r = Reader("español.txt")
    r.InfoToDict()
