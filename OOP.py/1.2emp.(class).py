class emp:

    def __init__(self,id,name1,sal1)
        self.id=id
        self.name1 = name1
        self.sal1=sal1

    def getId(self):
        return self.id

    def setId(self,newId):
        self.id = newId

    def getName(self):
        return self.name1

    def setName(self,newName):
        self.name1 = newName

    def getSal(self):
        return self.name1

    def setSal(self,newSal):
        self.sal1=newSal

    def display(self):
        print(f'Id:{self.id}\tNAME:{self.name1}\tSAL:{self.sal}')

        