from tkinter import *
from PIL import ImageTk, Image
from tkinter import messagebox
import pyodbc

# bg #23222C
# fg #AC0051

m = Tk()
m.title("S.A.M Bank ")
# m.iconbitmap('address')
m.maxsize(width=2000,height=2000)
m.geometry("1200x700")

user_name = StringVar()
pass_word = StringVar()




def click(event): #FOR PLACE HOLDER
    entry_pass.config(state=NORMAL)
    entry_pass.delete(0,END)
def click_id(event):
    entry_id.config(state=NORMAL)
    entry_id.delete(0,END)


def login():   #dashboard

    #import logindashboard
    # login data is stored in these variables here
    entry_username = user_name.get()
    entry_password = pass_word.get()







    if entry_username=="" or entry_password =="":
        messagebox.showerror(" S.A.M Bank ", "All fields required*")

    else:
        try:
            conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                                  r'DBQ=E:\New folder (2)\Bank management system\database.accdb;')  # Aap apna path de gy
            cursor = conn.cursor()
            cursor.execute("select * from clients where username=? and password=? ", (entry_username, entry_password))
            row = cursor.fetchone()
            if row == None:
                messagebox.showerror(" S.A.M Bank ", "INVALID USERNAME & PASSWORD")
                # m.destroy() check it also
            else:
                messagebox.showinfo(" S.A.M Bank ", "Welcome to S.A.M Bank")

                login_win = Tk()     #dashboard
                login_win.geometry("1200x700")
                login_win.title("S.A.M Bank ")

                def log_out():
                    login_win.destroy()

                def check_balance():
                    check_win = Toplevel(login_win)
                    check_win.configure(bg = "#586887")
                    check_win.geometry("500x200")
                    conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                                          r'DBQ=E:\New folder (2)\Bank management system\database.accdb;')
                    cursor = conn.cursor()

                    # for check balance
                    cursor.execute("select balance from clients where username=? and password=? ",
                                   (entry_username, entry_password))
                    fetch_check_balance = cursor.fetchone()
                    fetch_check_balance = fetch_check_balance[0]

                    label_check1 = Label(check_win,bg = "#586887",fg="white",text="YOUR AVAILABLE BALANCE IS: ",font=("Franklin Gothic", 18, "bold"))
                    label_check1.place(x=40,y=10)

                    label_check2 = Label(check_win, bg = "#586887",fg="white", text=fetch_check_balance,font=("Franklin Gothic", 18, "bold"))
                    label_check2.place(x=80, y=60)




                def deposit():
                    deposit_win = Toplevel(login_win)
                    deposit_win.geometry("500x400")
                    deposit_win.title("S.A.M Bank ")
                    frame_deposit = Frame(deposit_win, bg="#586887", width=500, height=400)
                    frame_deposit.pack(fill=BOTH)
                    label_d_text = Label(frame_deposit, bg="#586887",fg="white",font=("Franklin Gothic",17,"bold"), text="Enter your Account No. ")
                    label_d_text.place(x=30, y=30)
                    entry_d_ac_get = StringVar()
                    # entry_d_dopt_get = StringVar()
                    entry_d_account = Entry(frame_deposit,bg="#7e8eab",fg="white",font=("Franklin Gothic", 13, "bold"))
                    entry_d_account.place(x=30, y=70)

                    label_d_text2 = Label(frame_deposit, bg="#586887", fg="white", font=("Franklin Gothic", 17, "bold"),
                                         text="Enter amount to deposit ")
                    label_d_text2.place(x=30, y=90)

                    entry_d_deposit = Entry(frame_deposit, bg="#7e8eab", fg="white",font=("Franklin Gothic", 13, "bold"),)
                    entry_d_deposit.place(x=30, y=130)
                    entry_d_ac_get = entry_d_account.get()
                    entry_d_dopt_get = entry_d_deposit.get()

                    def deposit_amount():
                        entry_d_ac_get = entry_d_account.get()
                        entry_d_dopt_get = entry_d_deposit.get()
                        entry_d_ac_get = int(entry_d_ac_get)
                        entry_d_dopt_get = int(entry_d_dopt_get)
                        s_balance = StringVar()
                        s_update_balance = StringVar()
                        # d_new_balance = int(d_new_balance)
                        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                                              r'DBQ=E:\New folder (2)\Bank management system\database.accdb;')
                        s_balance = "select balance from clients where account_num=?"
                        ac_data = (entry_d_ac_get,)
                        cursor = conn.cursor()
                        cursor.execute(s_balance, ac_data)
                        d_result = cursor.fetchone()

                        d_new_balance = d_result[0] + entry_d_dopt_get
                        s_update_balance = "update clients set balance = ? where account_num=?"
                        s_update_final = (d_new_balance, entry_d_ac_get)
                        cursor.execute(s_update_balance, s_update_final)

                        # var_msg = StringVar()
                        # var_msg= "successfully deposited " , entry_d_dopt_get , "new ",d_new_balance


                        deposit_sub_win = Toplevel(deposit_win)
                        deposit_sub_win.geometry("500x200")
                        deposit_sub_win.title("S.A.M Bank ")
                        deposit_sub_win.configure(bg="#50658c")
                        # label_d_msg = Label(deposit_sub_win,text=var_msg)
                        # label_d_msg.pack()
                        frame_d_d = Frame(deposit_sub_win,bg="#50658c",width=500,height=200)
                        frame_d_d.place(x=30,y=30)
                        label_d_d1 = Label(frame_d_d,bg="#50658c",fg="white",font=("Franklin Gothic",15,"bold"),text="You have successfully deposited")
                        label_d_d1.grid(row=1,column=1)
                        label_d_d2 = Label(frame_d_d,bg="#50658c",fg="white",font=("Franklin Gothic",15,"bold"),text=entry_d_dopt_get)
                        label_d_d2.grid(row=1,column=4)

                        label_d_d3 = Label(frame_d_d,bg="#50658c",fg="white",font=("Franklin Gothic",15,"bold"), text="Your New Balance is ")
                        label_d_d3.grid(row=4,column=1)
                        label_d_d4 = Label(frame_d_d, bg="#50658c",fg="white",font=("Franklin Gothic",15,"bold"),text=d_new_balance)
                        label_d_d4.grid(row=4,column=4)



                        def close_d():
                            deposit_sub_win.destroy()
                            deposit_win.destroy()


                        button_close = Button(deposit_sub_win,bg="#50658c",fg="white",font=("Franklin Gothic",15,"bold"),width=5,text="OK",command=close_d)
                        button_close.place(x=60,y=120)

                        #you have successfully deposited entry_d_dopt_get .
                        #and you new balance is entry_d_dopt_get



                        conn.commit()
                        conn.close()

                    deposit_button = Button(frame_deposit, text="Deposit Amount",bg="#50658c",fg="white", font=("Franklin Gothic", 14, "bold"),command=deposit_amount)
                    deposit_button.place(x=30, y=160)

                    # withdraw_button = Button(frame_deposit, text="Withdraw Amount", command=withdraw_amount)
                    # withdraw_button.place(x=30, y=120)

                def withdraw():
                    withdraw_win = Toplevel(login_win)
                    withdraw_win.geometry("500x400")
                    withdraw_win.title("S.A.M Bank ")
                    frame_withdraw = Frame(withdraw_win, bg="#586887", width=500, height=400)
                    frame_withdraw.pack(fill=BOTH)
                    label_d_text = Label(frame_withdraw, bg="#586887",fg="white", text="Enter your Account No.",font=("Franklin Gothic", 17, "bold"))
                    label_d_text.place(x=30, y=30)
                    entry_d_ac_get = StringVar()
                    # entry_d_dopt_get = StringVar()
                    entry_d_account = Entry(frame_withdraw,bg="#7e8eab", font=("Franklin Gothic", 13, "bold"),fg="white")
                    entry_d_account.place(x=30, y=70)
                    label_d_text3 = Label(frame_withdraw, bg="#586887", fg="white", font=("Franklin Gothic", 17, "bold"),
                                          text="Enter amount to withdraw ")
                    label_d_text3.place(x=30, y=90)

                    entry_d_deposit = Entry(frame_withdraw,font=("Franklin Gothic", 13, "bold"),bg="#7e8eab", fg="white")
                    entry_d_deposit.place(x=30, y=130)
                    entry_d_ac_get = entry_d_account.get()
                    entry_d_dopt_get = entry_d_deposit.get()

                    def withdraw_amount():
                        entry_d_ac_get = entry_d_account.get()
                        entry_d_dopt_get = entry_d_deposit.get()
                        entry_d_ac_get = int(entry_d_ac_get)
                        entry_d_dopt_get = int(entry_d_dopt_get)
                        s_balance = StringVar()
                        s_update_balance = StringVar()
                        # d_new_balance = int(d_new_balance)
                        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                                              r'DBQ=E:\New folder (2)\Bank management system\database.accdb;')
                        s_balance = "select balance from clients where account_num=?"
                        ac_data = (entry_d_ac_get,)
                        cursor = conn.cursor()
                        cursor.execute(s_balance, ac_data)
                        d_result = cursor.fetchone()
                        d_new_balance = d_result[0] - entry_d_dopt_get
                        s_update_balance = "update clients set balance = ? where account_num=?"
                        s_update_final = (d_new_balance, entry_d_ac_get)
                        cursor.execute(s_update_balance, s_update_final)

                        #start withdraw
                        deposit_sub_win = Toplevel(withdraw_win)
                        deposit_sub_win.geometry("500x200")
                        deposit_sub_win.title("S.A.M Bank ")
                        deposit_sub_win.configure(bg="#50658c")
                        # label_d_msg = Label(deposit_sub_win,text=var_msg)
                        # label_d_msg.pack()
                        frame_d_d = Frame(deposit_sub_win,bg="#50658c", width=500, height=200)
                        frame_d_d.place(x=30, y=30)



                        if d_new_balance >=0:
                            label_d_d1 = Label(frame_d_d,bg="#50658c", fg="white", font=("Franklin Gothic", 15, "bold"), text="You have successfully withdrawed")
                            label_d_d1.grid(row=1, column=1)
                            label_d_d2 = Label(frame_d_d, bg="#50658c", fg="white", font=("Franklin Gothic", 15, "bold"),text=entry_d_dopt_get)
                            label_d_d2.grid(row=1, column=4)
                            label_d_d3 = Label(frame_d_d,bg="#50658c", fg="white", font=("Franklin Gothic", 15, "bold"), text="Your New Balance is ")
                            label_d_d3.grid(row=4, column=1)
                            label_d_d4 = Label(frame_d_d, bg="#50658c", fg="white", font=("Franklin Gothic", 15, "bold"),text=d_new_balance)
                            label_d_d4.grid(row=4, column=4)
                        else:
                            label_d_d4 = Label(frame_d_d, text="You have insufficient amount",bg="#50658c",fg="white",font=("Franklin Gothic", 17, "bold"))
                            label_d_d4.grid(row=2, column=2)


                        def close_d():
                            deposit_sub_win.destroy()
                            withdraw_win.destroy()

                        button_close = Button(deposit_sub_win, text="OK",bg="#50658c", fg="white", font=("Franklin Gothic", 15, "bold"), width=5, command=close_d)
                        button_close.place(x=60, y=120)





                        #end withdraw
                        conn.commit()
                        conn.close()

                    withdraw_button = Button(frame_withdraw, text="Withdraw Amount",bg="#50658c", fg="white", font=("Franklin Gothic", 14, "bold"),command=withdraw_amount)
                    withdraw_button.place(x=30, y=160)
        #check above 2 lines indentation


                frame_r = Frame(login_win, bg="white", width=1200, height=700)
                frame_r.pack(fill=BOTH)
                frame_left = Frame(frame_r, bg="#41557d", width=350, height=2550   )
                frame_left.pack(side=LEFT, fill=Y)

                label_bank = Label(frame_left, text=" S.A.M BANK ", font=("Franklin Gothic", 35, "bold"),bg="#41557d", fg="white")
                label_bank.place(x=10,y=40)


                label_deposit = Button(frame_left, text="DEPOSIT AMOUNT",width=18, command=deposit, bg="#41557d", fg="white",font=("Franklin Gothic", 17, "bold"))
                label_deposit.place(x=20, y=200)
                label_with = Button(frame_left, text="WITHDRAW AMOUNT",width=18, command=withdraw, bg="#41557d", fg="white",font=("Franklin Gothic", 17, "bold"))
                label_with.place(x=20, y=300)
                label_set = Button(frame_left,command=check_balance,text="CHECK BALANCE",width=18, bg="#41557d", fg="White", font=("Franklin Gothic", 17, "bold"))
                label_set.place(x=20, y=400)
                label_log = Button(frame_left,command=log_out, text="LOG OUT", bg="#41557d",width=18, fg="White", font=("Franklin Gothic", 17, "bold"))
                label_log.place(x=20, y=500)
                frame_r_body = Frame(login_win, bg="#7e8eab", width=1500, height=1500)
                frame_r_body.place(x=340, y=1)
                # label_l_username = Label(frame_r_body,text=entry_username)
                # label_l_username.place(x=20,y=30)
                #
                # label_l_username = Label(frame_r_body,text=entry_password)
                # label_l_username.place(x=40,y=60)
                record = StringVar()
                #fetch_namef = StringVar()
                #not neccesary to define this

                conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                                      r'DBQ=E:\New folder (2)\Bank management system\database.accdb;')
                cursor = conn.cursor()

                # for first name
                cursor.execute("select first_name from clients where username=? and password=? ",
                               (entry_username, entry_password))
                fetch_namef = cursor.fetchone()
                fetch_namef = fetch_namef[0]

                # for last name
                cursor.execute("select last_name from clients where username=? and password=? ",
                               (entry_username, entry_password))
                fetch_namel = cursor.fetchone()
                fetch_namel = fetch_namel[0]

                # for cnic
                cursor.execute("select cnic from clients where username=? and password=? ",
                               (entry_username, entry_password))
                fetch_cnic = cursor.fetchone()
                fetch_cnic = fetch_cnic[0]

                # for city
                cursor.execute("select city from clients where username=? and password=? ",
                               (entry_username, entry_password))
                fetch_city = cursor.fetchone()
                fetch_city = fetch_city[0]

                # for phone
                cursor.execute("select phone from clients where username=? and password=? ",
                               (entry_username, entry_password))
                fetch_phone = cursor.fetchone()
                fetch_phone = fetch_phone[0]

                # for email
                cursor.execute("select email from clients where username=? and password=? ",
                               (entry_username, entry_password))
                fetch_email = cursor.fetchone()
                fetch_email = fetch_email[0]

                # for username
                cursor.execute("select username from clients where username=? and password=? ",
                               (entry_username, entry_password))
                fetch_username = cursor.fetchone()
                fetch_username = fetch_username[0]

                # for password
                cursor.execute("select password from clients where username=? and password=? ",
                               (entry_username, entry_password))
                fetch_password = cursor.fetchone()
                fetch_password = fetch_password[0]

                # for account_num
                cursor.execute("select account_num from clients where username=? and password=? ",
                               (entry_username, entry_password))
                fetch_account_num = cursor.fetchone()
                fetch_account_num = fetch_account_num[0]






                conn.close()


                # index 0 for first name
                # label_l_fetch = Label(frame_r_body, text=record)
                # label_l_fetch.place(x=40, y=120)

                # label_r_namef = Label(frame_r_body, text=fetch_namef)
                # label_r_namef.place(x=40, y=200)

                # label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text=fetch_namef)
                # label_r_namef.place(x=50, y=80)


                # dashboard start
                label_r_details = Label(frame_r_body,bg="#7e8eab",fg="white" ,font=("Franklin Gothic", 30, "bold"),text="PERSONAL DETAILS ")
                label_r_details.place(x=50,y=40)



                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text="FIRST NAME : ",font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=50, y=120)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text=fetch_namef,font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=250, y=120)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text="LAST NAME : ",font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=50, y=160)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text=fetch_namel,font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=250, y=160)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text="ACCOUNT NO.  : ",font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=50, y=200)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text=fetch_account_num,font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=250, y=200)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text="USERNAME : ",font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=50, y=240)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text=fetch_username,font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=250, y=240)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text="EMAIL ADDRESS : ",font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=50, y=280)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text=fetch_email,font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=250, y=280)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text="CNIC : ",font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=50, y=320)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text=fetch_cnic,font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=250, y=320)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text="CITY : ",font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=50, y=360)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text=fetch_city,font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=250, y=360)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text="PHONE NO. : ",font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=50, y=400)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text=fetch_phone,font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=250, y=400)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text="PASSWORD : ",font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=50, y=440)

                label_r_namef = Label(frame_r_body, bg="#7e8eab", fg="white", text=fetch_password,font=("Franklin Gothic", 14, "bold"))
                label_r_namef.place(x=250, y=440)


                #dashboard end
                login_win.mainloop()








            # conn.commit()
            conn.close()

        except Exception as es:
            messagebox.showerror("Error",f"Error due to {str(es)}",parent=m)





def finish_reg():

    namef = r_namef.get()
    namel = r_namel.get()
    cnic = r_cnic.get()
    city = r_city.get()
    phone = r_phone.get()
    email = r_email.get()
    username = r_username.get()
    password = r_password.get()

    if namef =="":
        messagebox.showerror(" S.A.M Bank ","All fields required*")
        register_win.destroy()
    elif namel=="":
        messagebox.showerror(" S.A.M Bank ", "All fields required*")
        register_win.destroy()
    elif cnic =="":
        messagebox.showerror(" S.A.M Bank ", "All fields required*")
        register_win.destroy()
    elif city=="":
        messagebox.showerror(" S.A.M Bank ", "All fields required*")
        register_win.destroy()
    elif phone=="":
        messagebox.showerror(" S.A.M Bank ", "All fields required*")
        register_win.destroy()
    elif email=="":
        messagebox.showerror(" S.A.M Bank ", "All fields required*")
        register_win.destroy()
    elif username=="":
        messagebox.showerror(" S.A.M Bank ", "All fields required*")
        register_win.destroy()
    elif password=="":
        messagebox.showerror(" S.A.M Bank ", "All fields required*")
        register_win.destroy()
    else :
        conn = pyodbc.connect(r'DRIVER={Microsoft Access Driver (*.mdb, *.accdb)};'
                              r'DBQ=E:\New folder (2)\Bank management system\database.accdb;')  # Aap apna path de gy
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO clients (first_name, last_name, cnic, city, phone, email, username, password) values (?, ?, ?, ?, ?, ?, ?, ?)',
            (namef, namel, cnic, city, phone, email, username, password))
        #cursor.execute('INSERT INTO amount (username) values (?)', (username))
#start



#end
        conn.commit()
        conn.close()

        messagebox.showinfo(" S.A.M Bank ", "SUCCESSFULL REGISTRATION")
        register_win.destroy()


def registration():
    global register_win
    register_win = Toplevel(m)
    register_win.geometry("1200x700")
    register_win.configure(bg="#7e8eab")


#######
    frame_top = Frame(register_win, bg="#586887", height=150)
    frame_top.pack(side=TOP, fill=X)
    label_bankname = Label(frame_top, text="S.A.M BANK", bg="#586887", fg="white", font=("Franklin Gothic", 43, "bold"))
    label_bankname.place(x=450, y=40)
    # btn_home = Button(frame_top, text="ABOUT US", pady=8, font=("Franklin Gothic", 12, "bold"), fg="white",
    #                   bg="#586887", width=10)
    # btn_home.place(x=200, y=90)

    img1 = Image.open("background1.png")
    img_body = img1.resize((1600, 1200))
    img_body = ImageTk.PhotoImage(img_body)

    # img2 = Image.open("S.A.M BANK.png")
    # img_top = img2.resize((1,1))
    # img_top = ImageTk.PhotoImage(img_top)

    frame_body = Frame(m, height=700, bg="#7e8eab")
    frame_body.pack(fill=X, side=BOTTOM)

    label_body_img = Label(frame_body, image=img_body)
    label_body_img.pack(fill=BOTH)
    #
    # label_top_img = Label(frame_top,image=img_top)
    # label_body_img.place(x=10,y=1)

    # label_body= Label(frame_body,text="YOUR BANK IS YOUR FINGERPRINT",fg="black",bg="grey",font=("cablri",28))
    # label_body.place(x=350,y=10)

    ##########


    frame_r_body= Frame(register_win,bg="pink",width=950,height=450)
    frame_r_body.place(x=150,y=180)
    frame_r_text = Frame(frame_r_body,bg="#465573",width=350,height=450)
    frame_r_text.place(x=0.0001,y=0.0001)
    frame_r_reg = Frame(frame_r_body,bg="#586887",width=600,height=450)
    frame_r_reg.place(x=350,height=450)
    label_r_text = Label(frame_r_text,bg="#465573",fg="white",text="SOCIAL IMPACT",font=("arial",25,"bold"))
    label_r_text.place(x=50,y=100)
    label_r_text2 = Label(frame_r_text,width=25,height=7,fg="white",bg="#465573",text="Our reach ,scale & \n commitment has given millions \n a merit based access to life \n changing opportunities.",font=("arial",18) )
    label_r_text2.place(x=3,y=170)
    label_r_reg = Label(frame_r_reg,text="REGISTER HERE",fg="white",bg="#586887",font=("airal",25,"bold"))
    label_r_reg.place(x=60,y=20)

    global r_namef
    global r_namel
    global r_cnic
    global r_city
    global r_phone
    global r_email
    global r_username
    global r_password

    r_namef = StringVar()
    r_namel = StringVar()
    r_cnic = StringVar()
    r_city = StringVar()
    r_phone = StringVar()
    r_email = StringVar()
    r_username = StringVar()
    r_password = StringVar()



    label_r_namef = Label(frame_r_reg,text="FIRST NAME",font=("arial",12,"bold"),fg="white",bg="#586887")
    label_r_namef.place(x=40,y=93)

    entry_r_namef = Entry(frame_r_reg,textvariable=r_namef,fg="white",bg="#60708f",font=("arial",16),width=15)
    entry_r_namef.place(x=40,y=120)

    label_r_namel = Label(frame_r_reg, text="LAST NAME",font=("arial",12,"bold"),fg="white",bg="#586887")
    label_r_namel.place(x=350, y=93)

    entry_r_namel = Entry(frame_r_reg,textvariable=r_namel,fg="white",bg="#60708f", font=("arial", 16),width=15)
    entry_r_namel.place(x=350, y=120)

    label_r_cnic = Label(frame_r_reg,text="CNIC NO.",font=("arial",12,"bold"),fg="white",bg="#586887")
    label_r_cnic.place(x=40,y=158)

    entry_r_cnic = Entry(frame_r_reg,textvariable=r_cnic,fg="white",bg="#60708f",font=("arial",16),width=15)
    entry_r_cnic.place(x=40,y=185)

    label_r_city = Label(frame_r_reg, text="CITY",font=("arial",12,"bold"),fg="white",bg="#586887")
    label_r_city.place(x=350, y=158)

    entry_r_city = Entry(frame_r_reg,textvariable=r_city,fg="white", bg="#60708f",font=("arial", 16),width=15)
    entry_r_city.place(x=350, y=185)


    label_r_phone = Label(frame_r_reg,text="PHONE NO.",font=("arial",12,"bold"),fg="white",bg="#586887")
    label_r_phone.place(x=40,y=223)

    entry_r_phone = Entry(frame_r_reg,textvariable=r_phone,fg="white",bg="#60708f",font=("arial",16),width=15)
    entry_r_phone.place(x=40,y=250)

    label_r_email = Label(frame_r_reg, text="EMAIL ADDRESS",font=("arial",12,"bold"),fg="white",bg="#586887")
    label_r_email.place(x=350, y=223)

    entry_r_email = Entry(frame_r_reg,textvariable=r_email,fg="white",bg="#60708f", font=("arial", 16),width=15)
    entry_r_email.place(x=350, y=250)

    label_r_username = Label(frame_r_reg,text="USERNAME",font=("arial",12,"bold"),fg="white",bg="#586887")
    label_r_username.place(x=40,y=288)

    entry_r_username = Entry(frame_r_reg,textvariable=r_username,fg="white",bg="#60708f",font=("arial",16),width=15)
    entry_r_username.place(x=40,y=320)

    label_r_password = Label(frame_r_reg, text="PASSWORD",font=("arial",12,"bold"),fg="white",bg="#586887")
    label_r_password.place(x=350, y=288)

    entry_r_password = Entry(frame_r_reg,show="*",fg="white",textvariable=r_password,bg="#60708f", font=("arial", 16),width=15)
    entry_r_password.place(x=350, y=320)

    button_finish = Button(frame_r_reg,text="FINISH",font=("arial",15,"bold"),bg="#586887",width=10,fg="white",command=finish_reg)
    button_finish.place(x=220,y=370)




frame_top = Frame(m,bg="#586887",height=150,highlightbackground="#586887",highlightthickness=10)
frame_top.pack(side=TOP,fill=X)
label_bankname = Label(frame_top,text="S.A.M BANK",bg="#586887",fg="white",font=("Franklin Gothic",43,"bold"))
label_bankname.place(x=450,y=30)
# btn_home = Button(frame_top,text="ABOUT US",pady=8,font=("Franklin Gothic",12,"bold"),fg="white",bg="#586887",width=10)
# btn_home.place(x=200,y=90)

img1 = Image.open("background1.png")
img_body = img1.resize((1600,1200))
img_body = ImageTk.PhotoImage(img_body)

# img2 = Image.open("S.A.M BANK.png")
# img_top = img2.resize((1,1))
# img_top = ImageTk.PhotoImage(img_top)

frame_body = Frame(m,height=700,bg="dark slate gray")
frame_body.pack(fill=X,side=BOTTOM)

label_body_img = Label(frame_body,image=img_body)
label_body_img.pack(fill=BOTH)
#
# label_top_img = Label(frame_top,image=img_top)
# label_body_img.place(x=10,y=1)

# label_body= Label(frame_body,text="YOUR BANK IS YOUR FINGERPRINT",fg="black",bg="grey",font=("cablri",28))
# label_body.place(x=350,y=10)


frame_login =Frame(m,bd=4,width=500,height=350,bg="#586887")
frame_login.place(x=400,y=250)
label_welcome= Label(frame_login,anchor=CENTER,text="WELCOME",font=("Franklin Gothic",25,"bold"),fg="white",bg="#586887")
label_welcome.place(x=150,y=10)
entry_id =Entry(frame_login,textvariable=user_name,fg="white",bg="#60708f",width=35,font=("Arial",18))
entry_id.place(x=20,y=100)
entry_id.insert(0,"USERNAME")
entry_id.config(state=DISABLED)
entry_id.bind("<Button-1>",click_id)
entry_pass =Entry(frame_login,textvariable=pass_word,fg="white",bg="#60708f",show="*",width=35,font=("Arial",18))
entry_pass.place(x=20,y=180)
entry_pass.insert(0,"PASSWORD")
entry_pass.config(state=DISABLED)
entry_pass.bind("<Button-1>",click)
btn_login = Button(frame_login,text="LOGIN",font=("Franklin Gothic",14,"bold"),pady=8,command=login,fg="white",width=15,bg="#8696b5")
btn_login.place(x=20,y=250)
btn_register = Button(frame_login,command=registration,text="REGISTER",pady=8,font=("Franklin Gothic",14,"bold"),fg="white",width=15,bg="#8696b5")
btn_register.place(x=289,y=250)

m.mainloop()