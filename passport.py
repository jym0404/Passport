from datetime import datetime
class Passport:
    def __init__(self, name, nat):
        now = datetime.now()
        self.doi = str(now.year)+"/"+str(now.month)+"/"+str(now.day)
        self.name = name
        self.nara = nat
        self.wg = []
    def add_nation(self, nat):
        self.wg = self.wg + [nat]
    def print_passport(self):
        print("---------------------------")
        print(" ")
        print("name:",self.name)
        print("nationality:",self.nara)
        print("date of issue:",self.doi)
        print(" ")
        print("---------------------------")
        for i in range(len(self.wg)):
            print(" ")
            print(self.wg[i])
            print(" ")
            print("---------------------------")
    def edit_owner_info(self, name, nat):
        self.name = name
        self.nara = nat
        self.wg = []
    def write_passport(self, name, po):
        f = open(po + "\\" + name, "wt")
        f.write("---------------------------\n\n")
        f.write("name:"+self.name+"\n")
        f.write("nationality:"+self.nara+"\n")
        f.write("date of issue:"+self.doi+"\n\n")
        f.write("---------------------------\n\n")
        for i in range(len(self.wg)):
            f.write(self.wg[i]+"\n\n")
            f.write("---------------------------\n")
#Ex:
#person1 = Passport("daniel", "korea")
#person1.add_nation("china")
#person1.add_nation("canada")
#person1.print_passport()
#person1.write_passport("test.txt","C:\\Users\\Public\\Documents")
#Result:
#---------------------------
# 
#name: daniel
#nationality: korea
#date of issue: 2019/7/24 <-This is the date you created the person1 variable
#
#---------------------------
# 
#china
# 
#---------------------------
# 
#canada
# 
#---------------------------
