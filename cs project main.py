amount=0.0
list_seat=[]
list_item=[]
list_quantity=[]
uid=0
password="admin123"
import mysql.connector as key
def movie1():
  con=key.connect(host="localhost",user="root",passwd="tiger",database="movie1")
  def bill():
    #
    global amount
    global uid
    phone_no=int(input("Enter phone number : "))
    email_id=input("Enter Email id : ")
    print("Final Bill :")
    print("Inception  |  3:00 PM")
    print("Seats booked : ",end="")
    for i in list_seat :
      #
      print(i,end=" , ")
    print()
    print("Combos taken : ",end="")
    l=len(list_item)
    if l>0:
      #
      for j in range(0,l,1):
        #
        print(list_item[j],"×",end="")
        print(list_quantity[j],end=" , ")
    
    else:
      #
      print("None")
    print("Total amount : Rs.",amount)
    c_no=int(input("Enter Credit Card number to pay the amount : "))
    query='''Insert into User_detail(uid,emailid,phoneno,creditcardno,amount)
    Values({},'{}',{},{},{})'''.format(uid,email_id,phone_no,c_no,amount)
    cursor6=con.cursor()
    cursor6.execute(query)
    con.commit()
    print("Congo")
  def snacks_combos():
    #
    global amount
    global uid
    print("Want to add any snack combos?(Y/N)...")
    ans=input()
    if ans=="Y" :
      #
      cursor3=con.cursor()
      st="Select * from snacks_combos"
      cursor3.execute(st)
      data=cursor3.fetchall()
      print("Serial No. , Item , Price")
      for row in data :
        #
        print(row[0]," , ",row[1]," , ",row[2])
      choice="Y"
      while choice=="Y" :
        #
        sl=int(input("Enter serial number of item you wanna buy : "))
        cursor4=con.cursor()
        que="Select item,price from snacks_combos where slno={}".format(sl)
        cursor4.execute(que)
        info=cursor4.fetchone()
        p=info[1]
        quantity=int(input("Enter quantity : "))
        item_b=info[0]
        list_item.append(item_b)
        k=p*quantity
        amount = amount + k
        list_quantity.append(quantity)
        query2='''Insert into combo_bought 
        Values({},'{}',{})'''.format(item_b,quantity,uid)
        con.commit()
        choice = input("Want to add more(Y/N)...")
      bill()
    else :
      bill()
  def book_ticket():
    #
    global amount
    global uid
    cursor1=con.cursor()
    st="Select * from ticket"
    cursor1.execute(st)
    k=0
    print("Seat Arrangement :")
    print("Class Silver : ")
    for i in range(3):
      #
      for j in range(4):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          #
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          #
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    print("Class Gold : ")
    for i in range(2):
      #
      for j in range(4):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    
    print("Class diamond : ")
    for i in range(0,1,1):
     
      for j in range(4):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    print("Legend : ")
    print("E - Empty , B - Booked")
    print("Price :")
    print("Silver Class - Rs.200.00 ; Gold Class - Rs.220 ; Diamond Class - Rs.250.00")
    cursor2=con.cursor()
    print("Enter your desired seat number :")
    uid=k+1
    seat=input()
    cor="N"
    while cor=="N" :
      cir=con.cursor()
      query7="Select status from ticket where seat='{}' ".format(seat)
      cir.execute(query7)
      data_n=cir.fetchone()
      if data_n[0]=="E" :
        cor=="Y"
        break
      else :
        seat=input("Seat is already booked enter another seat number : ")
    list_seat.append(seat)
    if seat[0]=="S" :
      amount = amount + 200.00
    elif seat[0]=="G" :
      amount = amount + 220.00
    else :
      amount = amount + 250.00
    query="Update ticket set status='{}',uid={} where seat ='{}' ".format("B",uid,seat)
    cursor2.execute(query)
    con.commit()
    ans="Y"
    while ans=="Y":
      print("Want to book more seats?(Y/N)...")
      ans=input()
      if ans =="Y" :
       
        print("Enter your desired seat number :")
        seat=input()
        list_seat.append(seat)
        if seat[0]=="S" :
          amount = amount + 200.00
        elif seat[0]=="G" :
          amount = amount + 220.00
        else :
          amount = amount + 250.00
        query="Update ticket set status='{}',uid={} where seat ='{}' ".format("B",uid,seat)
        cursor2.execute(query)
        con.commit()
    
    print("Unique id - ",uid," (Store this unique id for future cancellation of your tickets)")
    snacks_combos()
  book_ticket()
def movie2():
  con=key.connect(host="localhost",user="root",passwd="tiger",database="movie2")
  def bill():
    #
    global amount
    global uid
    phone_no=int(input("Enter phone number : "))
    email_id=input("Enter Email id : ")
    print("Final Bill :")
    print("Inception  |  3:00 PM")
    print("Seats booked : ",end="")
    for i in list_seat :
      #
      print(i,end=" , ")
    print()
    print("Combos taken : ",end="")
    l=len(list_item)
    if l>0:
      #
      for j in range(0,l,1):
        #
        print(list_item[j],"×",end="")
        print(list_quantity[j],end=" , ")
    
    else:
      #
      print("None")
    print("Total amount : Rs.",amount)
    c_no=int(input("Enter Credit Card number to pay the amount : "))
    query='''Insert into User_detail(uid,emailid,phoneno,creditcardno,amount)
    Values({},'{}',{},{},{})'''.format(uid,email_id,phone_no,c_no,amount)
    cursor6=con.cursor()
    cursor6.execute(query)
    con.commit()
    print("Congo")
  def snacks_combos():
    #
    global amount
    global uid
    print("Want to add any snack combos?(Y/N)...")
    ans=input()
    if ans=="Y" :
      #
      cursor3=con.cursor()
      st="Select * from snacks_combos"
      cursor3.execute(st)
      data=cursor3.fetchall()
      print("Serial No. , Item , Price")
      for row in data :
        #
        print(row[0]," , ",row[1]," , ",row[2])
      choice="Y"
      while choice=="Y" :
        #
        sl=int(input("Enter serial number of item you wanna buy : "))
        cursor4=con.cursor()
        que="Select item,price from snacks_combos where slno={}".format(sl)
        cursor4.execute(que)
        info=cursor4.fetchone()
        p=info[1]
        quantity=int(input("Enter quantity : "))
        item_b=info[0]
        list_item.append(item_b)
        k=p*quantity
        amount = amount + k
        list_quantity.append(quantity)
        query2='''Insert into combo_bought 
        Values({},'{}',{})'''.format(item_b,quantity,uid)
        con.commit()
        choice = input("Want to add more(Y/N)...")
      bill()
    else :
      bill()
  def book_ticket():
    #
    global amount
    global uid
    cursor1=con.cursor()
    st="Select * from ticket"
    cursor1.execute(st)
    k=0
    print("Seat Arrangement :")
    print("Class Silver : ")
    for i in range(3):
      #
      for j in range(4):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          #
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          #
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    print("Class Gold : ")
    for i in range(2):
      #
      for j in range(4):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    
	
    print("Class diamond : ")
    for i in range(0,1,1):
      
      for j in range(4):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    print("Legend : ")
    print("E - Empty , B - Booked")
    print("Price :")
    print("Silver Class - Rs.200.00 ; Gold Class - Rs.220 ; Diamond Class - Rs.250.00")
    cursor2=con.cursor()
    print("Enter your desired seat number :")
    uid=k+1
    seat=input()
    cor="N"
    while cor=="N" :
      cir=con.cursor()
      query7="Select status from ticket where seat='{}' ".format(seat)
      cir.execute(query7)
      data_n=cir.fetchone()
      if data_n[0]=="E" :
        cor=="Y"
        break
      else :
        seat=input("Seat is already booked enter another seat number : ")
    list_seat.append(seat)
    if seat[0]=="S" :
      amount = amount + 200.00
    elif seat[0]=="G" :
      amount = amount + 220.00
    else :
      amount = amount + 250.00
    query="Update ticket set status='{}',uid={} where seat ='{}' ".format("B",uid,seat)
    cursor2.execute(query)
    con.commit()
    ans="Y"
    while ans=="Y":
      print("Want to book more seats?(Y/N)...")
      ans=input()
      if ans =="Y" :
        
        print("Enter your desired seat number :")
        seat=input()
        list_seat.append(seat)
        if seat[0]=="S" :
          amount = amount + 200.00
        elif seat[0]=="G" :
          amount = amount + 220.00
        else :
          amount = amount + 250.00
        query="Update ticket set status='{}',uid={} where seat ='{}' ".format("B",uid,seat)
        cursor2.execute(query)
        con.commit()
    
    print("Unique id - ",uid," (Store this unique id for future cancellation of your tickets)")
    snacks_combos()
  book_ticket()
def movie3():
  con=key.connect(host="localhost",user="root",passwd="tiger",database="movie3")
  def bill():
    #
    global amount
    global uid
    phone_no=int(input("Enter phone number : "))
    email_id=input("Enter Email id : ")
    print("Final Bill :")
    print("Inception  |  3:00 PM")
    print("Seats booked : ",end="")
    for i in list_seat :
      #
      print(i,end=" , ")
    print()
    print("Combos taken : ",end="")
    l=len(list_item)
    if l>0:
      #
      for j in range(0,l,1):
        #
        print(list_item[j],"×",end="")
        print(list_quantity[j],end=" , ")
    
    else:
      #
      print("None")
    print("Total amount : Rs.",amount)
    c_no=int(input("Enter Credit Card number to pay the amount : "))
    query='''Insert into User_detail(uid,emailid,phoneno,creditcardno,amount)
    Values({},'{}',{},{},{})'''.format(uid,email_id,phone_no,c_no,amount)
    cursor6=con.cursor()
    cursor6.execute(query)
    con.commit()
    print("Congo")
  def snacks_combos():
    #
    global amount
    global uid
    print("Want to add any snack combos?(Y/N)...")
    ans=input()
    if ans=="Y" :
      #
      cursor3=con.cursor()
      st="Select * from snacks_combos"
      cursor3.execute(st)
      data=cursor3.fetchall()
      print("Serial No. , Item , Price")
      for row in data :
        #
        print(row[0]," , ",row[1]," , ",row[2])
      choice="Y"
      while choice=="Y" :
        #
        sl=int(input("Enter serial number of item you wanna buy : "))
        cursor4=con.cursor()
        que="Select item,price from snacks_combos where slno={}".format(sl)
        cursor4.execute(que)
        info=cursor4.fetchone()
        p=info[1]
        quantity=int(input("Enter quantity : "))
        item_b=info[0]
        list_item.append(item_b)
        k=p*quantity
        amount = amount + k
        list_quantity.append(quantity)
        query2='''Insert into combo_bought 
        Values({},'{}',{})'''.format(item_b,quantity,uid)
        con.commit()
        choice = input("Want to add more(Y/N)...")
      bill()
    else :
      bill()
  def book_ticket():
    #
    global amount
    global uid
    cursor1=con.cursor()
    st="Select * from ticket"
    cursor1.execute(st)
    k=0
    print("Seat Arrangement :")
    print("Class Silver : ")
    for i in range(3):
      #
      for j in range(4):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          #
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          #
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    print("Class Gold : ")
    for i in range(2):
      #
      for j in range(4):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    
	
    print("Class diamond : ")
    for i in range(0,1,1):
      for j in range(4):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    print("Legend : ")
    print("E - Empty , B - Booked")
    print("Price :")
    print("Silver Class - Rs.200.00 ; Gold Class - Rs.220 ; Diamond Class - Rs.250.00")
    cursor2=con.cursor()
    print("Enter your desired seat number :")
    uid=k+1
    seat=input()
    cor="N"
    while cor=="N" :
      cir=con.cursor()
      query7="Select status from ticket where seat='{}' ".format(seat)
      cir.execute(query7)
      data_n=cir.fetchone()
      if data_n[0]=="E" :
        cor=="Y"
        break
      else :
        seat=input("Seat is already booked enter another seat number : ")
    list_seat.append(seat)
    if seat[0]=="S" :
      amount = amount + 200.00
    elif seat[0]=="G" :
      amount = amount + 220.00
    else :
      amount = amount + 250.00
    query="Update ticket set status='{}',uid={} where seat ='{}' ".format("B",uid,seat)
    cursor2.execute(query)
    con.commit()
    ans="Y"
    while ans=="Y":
      print("Want to book more seats?(Y/N)...")
      ans=input()
      if ans =="Y" :
       
        print("Enter your desired seat number :")
        seat=input()
        list_seat.append(seat)
        if seat[0]=="S" :
          amount = amount + 200.00
        elif seat[0]=="G" :
          amount = amount + 220.00
        else :
          amount = amount + 250.00
        query="Update ticket set status='{}',uid={} where seat ='{}' ".format("B",uid,seat)
        cursor2.execute(query)
        con.commit()
    
    print("Unique id - ",uid," (Store this unique id for future cancellation of your tickets)")
    snacks_combos()
  book_ticket()
def movie4():
  con=key.connect(host="localhost",user="root",passwd="tiger",database="movie4")
  def bill():
    #
    global amount
    global uid
    phone_no=int(input("Enter phone number : "))
    email_id=input("Enter Email id : ")
    print("Final Bill :")
    print("Inception  |  3:00 PM")
    print("Seats booked : ",end="")
    for i in list_seat :
      #
      print(i,end=" , ")
    print()
    print("Combos taken : ",end="")
    l=len(list_item)
    if l>0:
      #
      for j in range(0,l,1):
        #
        print(list_item[j],"×",end="")
        print(list_quantity[j],end=" , ")
    
    else:
      #
      print("None")
    print("Total amount : Rs.",amount)
    c_no=int(input("Enter Credit Card number to pay the amount : "))
    query='''Insert into User_detail(uid,emailid,phoneno,creditcardno,amount)
    Values({},'{}',{},{},{})'''.format(uid,email_id,phone_no,c_no,amount)
    cursor6=con.cursor()
    cursor6.execute(query)
    con.commit()
    print("Congo")
  def snacks_combos():
    #
    global amount
    global uid
    print("Want to add any snack combos?(Y/N)...")
    ans=input()
    if ans=="Y" :
      #
      cursor3=con.cursor()
      st="Select * from snacks_combos"
      cursor3.execute(st)
      data=cursor3.fetchall()
      print("Serial No. , Item , Price")
      for row in data :
        #
        print(row[0]," , ",row[1]," , ",row[2])
      choice="Y"
      while choice=="Y" :
        #
        sl=int(input("Enter serial number of item you wanna buy : "))
        cursor4=con.cursor()
        que="Select item,price from snacks_combos where slno={}".format(sl)
        cursor4.execute(que)
        info=cursor4.fetchone()
        p=info[1]
        quantity=int(input("Enter quantity : "))
        item_b=info[0]
        list_item.append(item_b)
        k=p*quantity
        amount = amount + k
        list_quantity.append(quantity)
        query2='''Insert into combo_bought 
        Values({},'{}',{})'''.format(item_b,quantity,uid)
        con.commit()
        choice = input("Want to add more(Y/N)...")
      bill()
    else :
      bill()
  def book_ticket():
    #
    global amount
    global uid
    cursor1=con.cursor()
    st="Select * from ticket"
    cursor1.execute(st)
    k=0
    print("Seat Arrangement :")
    print("Class Silver : ")
    for i in range(3):
      #
      for j in range(4):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          #
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          #
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    print("Class Gold : ")
    for i in range(2):
      #
      for j in range(4):
        #
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    
	
    print("Class diamond : ")
    for i in range(0,1,1):
      
      for j in range(4):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print("     ",end=" ")
      for m in range(5):
        data=cursor1.fetchone()
        if data[0]>k :
          k=data[0]
        print(data[1],"(",data[2],")",end=" ")
      print()
    print("Legend : ")
    print("E - Empty , B - Booked")
    print("Price :")
    print("Silver Class - Rs.200.00 ; Gold Class - Rs.220 ; Diamond Class - Rs.250.00")
    cursor2=con.cursor()
    print("Enter your desired seat number :")
    uid=k+1
    seat=input()
    cor="N"
    while cor=="N" :
      cir=con.cursor()
      query7="Select status from ticket where seat='{}' ".format(seat)
      cir.execute(query7)
      data_n=cir.fetchone()
      if data_n[0]=="E" :
        cor=="Y"
        break
      else :
        seat=input("Seat is already booked enter another seat number : ")
    list_seat.append(seat)
    if seat[0]=="S" :
      amount = amount + 200.00
    elif seat[0]=="G" :
      amount = amount + 220.00
    else :
      amount = amount + 250.00
    query="Update ticket set status='{}',uid={} where seat ='{}' ".format("B",uid,seat)
    cursor2.execute(query)
    con.commit()
    ans="Y"
    while ans=="Y":
      print("Want to book more seats?(Y/N)...")
      ans=input()
      if ans =="Y" :
        
        print("Enter your desired seat number :")
        seat=input()
        list_seat.append(seat)
        if seat[0]=="S" :
          amount = amount + 200.00
        elif seat[0]=="G" :
          amount = amount + 220.00
        else :
          amount = amount + 250.00
        query="Update ticket set status='{}',uid={} where seat ='{}' ".format("B",uid,seat)
        cursor2.execute(query)
        con.commit()
    
    print("Unique id - ",uid," (Store this unique id for future cancellation of your tickets)")
    snacks_combos()
  book_ticket()
def cancel_ticket() :
  #
  print("Which movie ticket you want to cancel ?")
  print("Enter 1 for The Dark Knight")
  print("Enter 2 for Inception")
  n=int(input())
  if n==2 :
    #
    print("Choose the timing of the show")
    print("Enter 1 for 4:00 PM - 6:30 PM show")
    print("Enter 2 for 6:30 PM - 9:30 PM show")
    m=int(input())
    if m ==1 :
      con2 =key.connect(host="localhost",user="root",passwd="tiger",database="movie1")
      ud=int(input("Enter your unique id : "))
      cursor=con2.cursor()
      query1="Update  ticket set status='{}' where uid={}".format("E",ud)
      cursor.execute(query1)
      con2.commit()
      query2="Delete from combo_bought where uid={}".format(ud)
      cursor.execute(query2)
      con2.commit()
      query3="Delete from user_detail where uid={}".format(ud)
      cursor.execute(query3)
      con2.commit()
    else :
      #
      con2 =key.connect(host="localhost",user="root",passwd="tiger",database="movie2")
      ud=int(input("Enter your unique id : "))
      cursor1=con2.cursor()
      query1="Update ticket set status='{}' where uid={}".format("E",ud)
      cursor1.execute(query1)
      con2.commit()
      query2="Delete from combo_bought where uid={}".format(ud)
      cursor1.execute(query2)
      con2.commit()
      query3="Delete from user_detail where uid={}".format(ud)
      cursor1.execute(query3)
      con2.commit()  
  else :
    #
    
    print("Choose the timing of the show")
    print("Enter 1 for 3:00 PM - 5:30 PM show")
    print("Enter 2 for 4:30 PM - 7:00 PM show")
    m=int(input())
    if m==1 :
      con2 =key.connect(host="localhost",user="root",passwd="tiger",database="movie3")
      ud=int(input("Enter your unique id : "))
      cursor=con2.cursor()
      query1="Update  ticket set status='{}' where uid={}".format("E",ud)
      cursor.execute(query1)
      con2.commit()
      query2="Delete from combo_bought where uid={}".format(ud)
      cursor.execute(query2)
      con2.commit()
      query3="Delete from user_detail where uid={}".format(ud)
      cursor.execute(query3)
      con2.commit()
  
    else :
      #
      #copypastedone
      con2 =key.connect(host="localhost",user="root",passwd="tiger",database="movie4")
      ud=int(input("Enter your unique id : "))
      cursor=con2.cursor()
      query1="Update  ticket set status='{}' where uid={}".format("E",ud)
      cursor.execute(query1)
      con2.commit()
      query2="Delete from combo_bought where uid={}".format(ud)
      cursor.execute(query2)
      con2.commit()
      query3="Delete from user_detail where uid={}".format(ud)
      cursor.execute(query3)
      con2.commit()
  print("Ticket successfully cancelled")
def admin():
  #
  pass1=input("Enter the admin password to access details : ")
  b="N"
  while b == "N" :
      if pass1 == password :
          b="Y"
      else :
          print("Enter password again : ")
          pass1=input()
  print("Which movie ticket you want to see details ?")
  print("Enter 1 for The Dark Knight")
  print("Enter 2 for Inception")
  n=int(input())
  if n==1 :
    #
    print("Choose the timing of the show")
    print("Enter 1 for 4:00 PM - 6:30 PM show")
    print("Enter 2 for 7:00 PM - 9:30 PM show")
    m=int(input())
    if m ==1 :
      #
      con3 =key.connect(host="localhost",user="root",passwd="tiger",database="movie1")
      print("Enter seat number for deatils :")
      seat=input()
      cursor7=con3.cursor()
      query1="Select uid from ticket where seat='{}' ".format(seat)
      cursor7.execute(query1)
      data=cursor7.fetchone()
      ui=data[0]
      query2="Select * from user_detail where uid={} ".format(ui)
      cursor7.execute(query2)
      dataf=cursor7.fetchone()
      print("Seat booked by unique id : ",dataf[0])
      print("Email - id : ",dataf[1])
      print("Phone number : ",dataf[2])
      print("Credit Card number : ",dataf[3])
      print("Total Amount paid : Rs.",dataf[4])
    else :
      con3 =key.connect(host="localhost",user="root",passwd="tiger",database="movie2")
      print("Enter seat number for deatils :")
      seat=input()
      cursor7=con3.cursor()
      query1="Select uid from ticket where seat='{}' ".format(seat)
      cursor7.execute(query1)
      data=cursor7.fetchone()
      ui=data[0]
      query2="Select * from user_detail where uid={} ".format(ui)
      cursor7.execute(query2)
      dataf=cursor7.fetchone()
      print("Seat booked by unique id : ",dataf[0])
      print("Email - id : ",dataf[1])
      print("Phone number : ",dataf[2])
      print("Credit Card number : ",dataf[3])
      print("Total Amount paid : Rs.",dataf[4])
      
  else :
    #
    print("Choose the timing of the show")
    print("Enter 1 for 3:00 PM - 5:30 PM show")
    print("Enter 2 for 4:30 PM - 7:00 PM show")
    m=int(input())    
    if m ==2 :
      #
      con3 =key.connect(host="localhost",user="root",passwd="tiger",database="movie3")
      #copypastefromcancelticket
      print("Enter seat number for deatils :")
      seat=input()
      cursor7=con3.cursor()
      query1="Select uid from ticket where seat='{}' ".format(seat)
      cursor7.execute(query1)
      data=cursor7.fetchone()
      ui=data[0]
      query2="Select * from user_detail where uid={} ".format(ui)
      cursor7.execute(query2)
      dataf=cursor7.fetchone()
      print("Seat booked by unique id : ",dataf[0])
      print("Email - id : ",dataf[1])
      print("Phone number : ",dataf[2])
      print("Credit Card number : ",dataf[3])
      print("Total Amount paid : Rs.",dataf[4])
    else :
      con3 =key.connect(host="localhost",user="root",passwd="tiger",database="movie4")
      print("Enter seat number for deatils :")
      seat=input()
      cursor7=con3.cursor()
      query1="Select uid from ticket where seat='{}' ".format(seat)
      cursor7.execute(query1)
      data=cursor7.fetchone()
      ui=data[0]
      query2="Select * from user_detail where uid={} ".format(ui)
      cursor7.execute(query2)
      dataf=cursor7.fetchone()
      print("Seat booked by unique id : ",dataf[0])
      print("Email - id : ",dataf[1])
      print("Phone number : ",dataf[2])
      print("Credit Card number : ",dataf[3])
      print("Total Amount paid : Rs.",dataf[4])

print("Press 1 to book tickets")
print("Press 2 to cancel booked tickets")
print("Press 3 to access administrative details")
ch=int(input("Enter your choice(1/2/3): "))
if ch==1:
  print("Running movies")
  print("Press 1 for The Dark Knight")
  print("Press 2 for Inception")
  ch2=int(input("Enter the no. for movie of your choice :"))
  if ch2==1:
    print("The Dark Knight")
    print('''Premise : After Gordon, Dent and Batman begin an assault on Gotham's organised crime,
the mobs hire the Joker, a psychopathic criminal mastermind who offers
to kill Batman and bring the city to its knees''')
    print("Press 1 for 4:00 pm-6:30 pm show(Language : English, Available in 2D)")
    print("Press 2 for 7:00 pm-9:30 pm show(language : English, Available in 3D)")
    ch3=int(input())
    if ch3==1:
      movie1()
    if ch3==2 :
      movie2()
  if ch2==2:
    print("Inception")
    print('''Premise : Cobb steals information from his targets by entering their dreams.
Saito offers to wipe clean Cobb's criminal history as payment
for performing an inception on his sick competitor's son''')
    print("Running shows :")
    print("Press 1 for 3:00 pm-5:30 pm show(Language : Hindi , Available in 2D)")
    print("Press 2 for 4:30 pm-7:00 pm show(Language : English, Available in 3D)")
    ch3=int(input())
    if ch3==1:
      movie3()
    if ch3==2 :
      movie4()
    
if ch==2:
  cancel_ticket()
if ch==3:
  admin()
else :
  print("Invalid choice")
              
  
