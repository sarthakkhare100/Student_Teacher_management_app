import json
import random
import string
from pathlib import Path




class Student_Teacher:
    __info=[]
    __database="school.json"

    try:
        if not Path(__database).exists():
            with open(__database,'w') as fw:
                fw.write(json.dumps(__info))
        else:
            with open(__database,'r') as fr:
                __info=json.loads(fr.read())
    except Exception as err:
        print("ERROR ",err)


    def __generateid(self):
        try:
            seq1=(random.choices(string.ascii_letters, k=3))
            seq2=(random.choices(string.digits, k=3))
            seq3=(random.choices(list("@#$*"), k=2))

            seq=seq1+seq2+seq3

            random.shuffle(seq)
            return ("".join(seq))

        except Exception as err:
            print("WRONG INPUT", err)

    # function - 1
    def create(self):
        try:
            data={}
            while True:

                data["ID"] = self.__generateid()
                data["NAME"] = input("Enter Name: ").strip()
                data["STATUS"] = input("Enter Status STUDENT OR TEACHER: ").upper().strip()
                if data["STATUS"]=="TEACHER" or data["STATUS"]=="STUDENT":
                    pass
                else:
                    return "ERROR >> INPUT DO NOT FULLFILl CRITERIA"
                    break

                try:
                    d=int(input("Enter 10 digits Contact number: ").strip())
                    if len(str(d))==10:
                        data["CONTACT"] =d
                    else:
                        print()
                        return ("input is not 10 digits")
                        break
                except Exception as err:
                    print()
                    print ("ERROR >>")
                    return err
                    break

                Student_Teacher.__info.append(data)

                with open(Student_Teacher.__database,'w') as f:
                    f.write(json.dumps(Student_Teacher.__info))
                print()
                return (f"{data['NAME']} with ID {data['ID']} and Status {data['STATUS']} REGISTERED.")

        except Exception as err:
            print("ERROR ", err)

    # FUNCTION - 2
    def read(self):
        try:
            with open("school.json") as fw:
                data1 = json.loads(fw.read())

            print()
            value = input("Enter ID to Read: ").strip()
            for i in data1:
                if i["ID"] == value:
                    return (i)
            else:
                return "ID NOT FOUND"
        except Exception as err:
            print("ERROR", err)


    # FUNCTION - 4
    def hatao(self):
        try:
            with open("school.json") as u:
                dat = json.loads(u.read())

            n1 = input("enter ID to DELETE : ").strip()
            l = []
            sta=False

            for i in dat:
                if i["ID"] == n1:
                    l.append(i)
                    sta=True
            for i in l:
                dat.remove(i)
            while sta:
                with open("school.json", 'w') as u:
                    u.write(json.dumps(dat))
                return "DELETED SUCCESSFULLY"
            return "ID NOT FOUND"
        except Exception as err:
            print("ERROR >>",err)



    # FUNCTION 3

    def update(self):
        try:
            with open("school.json") as uv:
                dat2 = json.loads(uv.read())
            en = input("Enter id to update: ").strip()
            status=False
            for i in dat2:
                if i["ID"] == en:
                    print(i)
                    l = i
                    dat2.remove(i)
                    status=True

            while status:

                print("what do you want to update: ")
                print("1. Name")
                print("2. Status")
                print("3. Contact")
                fd = int(input("enter your choice: "))
                if fd == 1:
                    name = input("Enter new name to update: ").strip()
                    l["NAME"] = name
                    dat2.append(l)

                elif fd == 2:

                    Status = input("enter NEW STATUS: ").upper().strip()
                    if Status == "TEACHER" or Status == "STUDENT":
                        l["STATUS"] = Status
                        dat2.append(l)
                    else:
                        return "ERROR >> INPUT DO NOT FULLFILl CRITERIA"

                elif fd == 3:
                    try:
                        num = int(input("Enter new contact number: "))
                        if len(str(num)) == 10:
                            l["CONTACT"] = num
                            dat2.append(l)
                        else:
                            dat2.append(l)
                            print("INVALID INPUT")

                    except Exception as err:
                        dat2.append(l)
                        print("ERROR ", err)
                else:
                    dat2.append(l)
                with open("school.json", 'w') as uv:
                    uv.write(json.dumps(dat2))
                return "Status updated"


            return "ID NOT FOUND"
        except Exception as err:
            print("ERROR ", err)




    # FUNCTION - 5

    """PAASWORD = sarthak"""

    def read_all(self):
        try:
            with open("school.json") as fr:
                pap = json.loads(fr.read())
            print("IF YOU ARE AN ADMIN")
            password = input("enter password :").upper()
            if password == "SARTHAK":
                return (pap)
            else:
                return "YOU ARE NOT AN ADMIN"
        except Exception as err:
            print("ERROR " ,err)

    def __str__(self):
        return "Sorry Cannot show Class Details."


egg=Student_Teacher()

while(True):
    print()
    print("1. Insert Student/teacher")
    print("2. Read Single.")
    print("3. Update.")
    print("4. Delete.")
    print("5. Read all Teacher/Student.")
    print("0. EXIT")


    try:
        n = int(input("Enter your choice: "))

        if n == 1:
            print(egg.create())
        elif n == 2:
            print(egg.read())
        elif n == 3:
            print(egg.update())
        elif n == 4:
            print(egg.hatao())
        elif n == 5:
            print(egg.read_all())
        elif n == 0:
            print()
            print("HELLO WORLD")
            break
        else:
            print()
            print("INVALID INPUT")
    except Exception as err:
        print("ERROR ",err)















