import string



class Reader:  
    
    def __init__(self, filename):
        self.filename = filename
    
    #Convierte la informacion del archivo a una lista
    def filetolist(self):
        
        with open(self.filename, "r", encoding="utf8") as file:
            word = ""
            Words = list(string.ascii_letters)
            Words.extend(['ñ','Ñ','á','é','í','ó','ú'])
            self.info = []

            for i in file.read():
                if i in Words:
                    word += i

                #else:
                    #self.info.append(word.lower())
                    #word = "" 
                else:
                    if word!='':
                        self.info.append(word.lower())
                    word = "" 
        print(self.info)
        return self.info

    #Retorna la informacion de la palabra con todas sus repeticiones
    def InfoToDict(self):

        self.filetolist()

        self.info_update = dict()

        for i in self.info:
            self.info_update[i] = 0

        for i in self.info:
            self.info_update[i] += 1

        #if self.info_update[""]:
         #   del self.info_update[""]
        
        print(self.info_update)
        return self.info_update
        



def WordPrediction(sel_input):

    r = Reader("test.txt")
    r.InfoToDict()
    indexes = []

    if sel_input in r.info_update.keys():

        for i in range(len(r.info)):
            if sel_input == r.info[i] and i+1 < len(r.info):
                indexes.append(i+1)

        if len(indexes) > 0:
            repeat = dict()
            for i in indexes:
                posible = r.info[i]
                cont = 0
                for x in range(len(r.info)):
                    if posible == r.info[x] and sel_input == r.info[x-1]:
                        cont += 1 

                repeat[(sel_input, posible)] = cont

            for i in repeat:
                index1, index2 = i
                if index1 == '':
                    repeat[i] = 0
                if index2 == '':
                    repeat[i] = 0
                

        for i in range(0, 3):
            key_max = max(repeat.keys(), key=(lambda k: repeat[k]))
            print(key_max, repeat[key_max])
            del repeat[key_max]
             


WordPrediction("is")








