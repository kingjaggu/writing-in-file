import csv

def write_info_csv(info_list):
   with open('student_info.csv','a',newline=',') as csv_file:
      writer = csv.writer(csv_file)
      
      if csv_file.tell() == 0 :
         writer.writerow(["name", "age", "contact no", " email"])
         
      writer.window(info_list)
check = True

while(check):
   student_info = input ("Enter student data in format of (name,age, contact no, eMail)")
   print("Entered information is :"+str(student_info)
   
   #split
   student_info_list = student_info.split(,)
   print ("Entered split up information is :"+ str(student_info_list))
   
   write_into_csv(student_info_list)
   
   checking=input ("enter(yes/no) to enter new student data)
   if checking=="yes":
      check=True
   elif checking!="no":
      print ("wrong input")
   else
      check=false
   
