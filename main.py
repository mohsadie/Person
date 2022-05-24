import datetime
import re

class PERSON:
    Fname=""
    Mname=""
    Lname=""
    Dob= "00-00-0000"
    Gender=""
    id = 0
    MobileNo = "000-000-0000"

    def __init__(self , fn , mn , ln , dob , gen , ID , mno):
        self.Fname = fn
        self.Mname = mn
        self.Lname = ln
        self.Dob = dob
        self.Gender = gen
        self.id = ID
        self.MobileNo = mno


    def getage(self):

        if self.Dob == "00-00-0000" :
                return "Invalid Birth date , can calculate your age . . ."


        else:
            birthdate = datetime.datetime.strptime( self.Dob , "%d-%m-%Y").date()
            today = datetime.date.today();
            days = today - birthdate ;
            return  days.days // 365



if __name__ == '__main__':
    x1 = input("Enter first name : ")
    x2 = input("Enter middle name : ")
    x3 = input("Enter last name : ")
    x4 = input("Enter your  B'day Date (in DD-MM-YYYY) : ")
    matched = re.match("[0-9][0-9]-[0-9][0-9]-[0-9][0-9][0-9][0-9]", x4)
    is_match = bool(matched)
    if is_match == False :
         x4 ="00-00-0000"


    x5 = input("Enter gender : ")
    x6 = input("Enter identity NO : ")
    x7 = input("Enter your  Mobile NO  (in 000-000-0000) : ")
    print ("\n ----------------------RESULT ------------------------\n")
    matched = re.match("[0-9][0-9][0-9]-[0-9][0-9][0-9]-[0-9][0-9][0-9][0-9]", x7)
    is_match = bool(matched)
    if is_match == False :
        x7 ="000-000-0000"
        print("this phone NO is nor correct , [ not saved ] ...")


    obj = PERSON(x1 ,x2 ,x3 ,x4,x5,x6,x7)
    print( obj.getage())







