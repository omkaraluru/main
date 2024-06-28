from tkinter import*
from tkinter import ttk
from PIL import Image,ImageTk 
from tkinter import messagebox

class Login_window:
    def __init__(self,root):
       self.root=root
       self.root.title('Books Management System ')
       self.root.geometry('1550x800+0+0')
       self.root.configure(bg='#fefbe9')
       self.root.resizable(False,False)
       
       self.bg=ImageTk.PhotoImage(file="ca.png")
       
       lbl_bg=Label(self.root,image=self.bg)
       lbl_bg.place(x=0,y=0,relheight=1,relwidth=1)
       
       frame=Frame(self.root,bg="#fefbe9")
       frame.place(x=450,y=400,width=650,height=300)
    #    bms
       get_bms=Label(frame,text=" Books Management System Login",font=('Times New Roman',25,'bold'),fg="black",bg="#fefbe9")
       get_bms.place(x=70,y=0)
    #    login
      #  get_str=Label(frame,text="Login",font=('Times New Roman',25,'bold'),fg="black",bg="#fefbe9")
      #  get_str.place(x=300,y=40)
    # user name 
       username=lbl=Label(frame,text="Username  :",font=('Times New Roman',25),fg="black",bg="#fefbe9")
       username.place(x=60,y=75)
       self.txtuser=Entry(frame,font=('Times New Roman',22,'bold'),border=0,bg="#fefbe9")
       self.txtuser.place(x=250,y=75)
       Frame(frame,width=295,height=2,bg='black').place(x=250,y=110)
   # password
       password=lbl=Label(frame,text="Password  :",font=('Times New Roman',25),fg="black",bg="#fefbe9")
       password.place(x=60,y=150)     
       
       self.txtpass=Entry(frame,font=('Times New Roman',22,'bold'),border=0,bg="#fefbe9",show="*")
       self.txtpass.place(x=250,y=150)
       Frame(frame,width=295,height=2,bg='black').place(x=250,y=185)
    #    sign btn
    
       loginbtn=Button(frame,command=self.login,width=26,pady=7,text='Login',bg='#E04A31',fg='white',border=0,cursor='hand2')
       loginbtn.place(x=440,y=230)
       
    #    new user btn
    
       newbtn=Button(frame,command=self.register_window,width=26,pady=7,text='New User',bg='#E04A31',fg='white',border=0,cursor='hand2')
       newbtn.place(x=240,y=230)      
   
    #    bk_btn=Button(frame,text='Available books',bg='#fefbe9',fg='#E04A31',border=0,cursor='hand2',font=('Times New Roman',16,'bold'),)
    #    bk_btn.place(x=470,y=10)
    
    def register_window(self):
       self.new_window=Toplevel(self.root)
       self.app=Register(self.new_window)
   #  after login
    def login(self):
       
           if self.txtuser.get()=="" or self.txtpass.get()=="":
              messagebox.showerror("Error","Enter all the Filds")
           
                 
         #   elif self.txtuser.get()!='admin'and self.txtpass.get()!='1234':
         #       messagebox.showerror("invaild","invalid username and password") 
           
         #   elif self.txtpass.get()!='1234':
         #       messagebox.showerror("invaild","invalid password") 
           
         #   elif self.txtuser.get()!='admin'and self.txtpass.get()=='1234':
         #       messagebox.showerror("invaild","invalid username ") 
           
           else:
                 open_main=messagebox.askyesno("YesNo","Confirm do you want to Login")
                 if open_main>0:
                    self.new_window=Toplevel(self.root)
                    self.app=Bms(self.new_window)
                 else:
                    if not open_main:
                       return
           
# for the new user registration form
class Register:
    def __init__(self,root):
       self.root=root
       self.root.title('Books Management System-Register')
       self.root.geometry("1550x800+0+0")
       
    #   varables 
       self.var_name=StringVar()
       self.var_address=StringVar()
       self.var_gender=StringVar()
       self.var_mobile=StringVar()
       self.var_email=StringVar()
       self.var_pasw=StringVar()
       
    #    frame
       frame=Frame(self.root,bg="white")
       frame.place(x=570,y=100,width=400,height=620)
    #    registration lable
       register_lbl=Label(frame,text="Register Here",font=("times new roman",15,"bold"),bg="white")
       register_lbl.place(x=10,y=10)
       
       name=Label(frame,text="Name*",font=('Times New Roman',20,'bold'),bg="white")   
       name.place(x=40,y=60)              
       self.name_entry=ttk.Entry(frame,textvariable=self.var_name,font=('Tite',18))
       self.name_entry.place(x=40,y=100,width=325)
       
       address=Label(frame,text="Address*",font=('Times New Roman',20,'bold'),bg="white")   
       address.place(x=40,y=150)           
       self.address_entry=ttk.Entry(frame,textvariable=self.var_address,font=('Tite',18))
       self.address_entry.place(x=40,y=190,width=325)
       
       gender=Label(frame,text="Gender",font=('Times New Roman',20,'bold'),bg="white")
       gender.place(x=40,y=240)
       gen=StringVar()
       g1 = Radiobutton(frame, text="Male",variable=gen,value="Male",font=('Times New Roman',18),bg="white")
       g1.place(x=40,y=280)
       
       g2 = Radiobutton(frame, text="Female",variable=gen,value="Female",font=('Times New Roman',18),bg="white")
       g2.place(x=140,y=280)
       
       mobile=Label(frame,text="Mobile",font=('Times New Roman',20,'bold'),bg="white")   
       mobile.place(x=40,y=330)       
       self.mobile=ttk.Entry(frame,textvariable=self.var_mobile,font=('Title',18))
       self.mobile.place(x=40,y=370,width=325)
       
       pasw=Label(frame,text="Password",font=('Times New Roman',20,'bold'),bg="white")   
       pasw.place(x=40,y=410)       
       self.pasw=ttk.Entry(frame,textvariable=self.var_pasw,font=('title',18))
       self.pasw.place(x=40,y=450,width=325)
       
    #    login
       sign_up= Button(frame,command=root.destroy,width=12,height=1,text='<Back to Login',border=0,fg='blue',cursor='hand2',bg='white',)
       sign_up.place(x=40,y=500)
             

    #    button
       loginbtn=Button(frame,command=self.Register_data,width=26,pady=7,text='Submit',bg='#E04A31',fg='white',border=0,cursor='hand2')
       loginbtn.place(x=40,y=550,width=325)      
    
       
    def Register_data(self):
        if self.var_name.get()=="" or self.var_email.get()=="" or self.var_mobile()=="" or self.var_pasw.get()=="":
            messagebox.showinfo("Success","Registered Successfully Go Back And Login",parent=self.root)
        else:
            messagebox.showinfo("Success","Registered Successfully Go Back And Login",parent=self.root)
    
class Bms:
   def __init__(self,root):
       self.root=root
       self.root.title('main')
       self.root.geometry("1200x725+0+0")
       self.img=ImageTk.PhotoImage(file="lib.jpg")       
       lbl_img=Label(self.root,image=self.img)
       lbl_img.place(x=0,y=48)
       frame=Frame(self.root,bg="#f68121")
       frame.place(x=4,y=2,width=1520,height=50)
      
       bms=lbl=Label(frame,text="Book Management System",font=('Times New Roman',25,'bold'),fg="black",bg="#f68121")
       bms.place(x=0,y=4)
       
#  search book entery 
       ser=lbl=Label(frame,text="Search ",font=('Times New Roman',18),fg="black",bg="#f68121")
       ser.place(x=895,y=8)        
       self.txtpass=Entry(frame,text="search",font=('Times New Roman',22,'bold'),border=0,bg="white")
       self.txtpass.place(x=975,y=8,width=210)    
    #    saparate frame for elements
       box=Frame(self.root,bg="#f68121")
       box.place(x=785,y=85,height=600,width=400)

       username=lbl=Label(box,text="Username   :Omkar",font=('Times New Roman',22),fg="black",bg="#f68121")
       username.place(x=20,y=150)       
       id=lbl=Label(box,text="Id Numbeer :12113791",font=('Times New Roman',20),fg="black",bg="#f68121")
       id.place(x=20,y=190)                                                                                       
       Frame(box,width=405,height=2,bg='black').place(x=0,y=240)
       
       ser_btn=Button(box,command=self.search,width=26,pady=7,text='Avalable Book',bg='white',fg='#f68121',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       ser_btn.place(x=5,y=300,width=390)
       
       req_btn=Button(box,command=self.request,width=26,pady=7,text='Request Book',bg='white',fg='#f68121',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       req_btn.place(x=5,y=375,width=390)
       
       sub_btn=Button(box,command=self.submit,width=26,pady=7,text='Submit Book',bg='white',fg='#f68121',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       sub_btn.place(x=5,y=450,width=390)
       
       back_btn= Button(box,command=root.destroy,width=12,height=1,text='<Back to Login',border=0,fg='blue',cursor='hand2',bg='#f68121',)
       back_btn.place(x=5,y=550)
    
   #  subimt book page call
   def submit(self):      
        
         self.new_window=Toplevel(self.root)
         self.app=submit_page(self.new_window)        
   
# request page call
   def request(self):      
               
         self.new_window=Toplevel(self.root)
         self.app=request_page(self.new_window)
         
   def search(self):
         
         self.new_window=Toplevel(self.root)
         self.app=search_page(self.new_window)


         
# submit page created
class submit_page:
   def __init__(self,root):
       self.root=root
       self.root.title('Books Management System -Submit Book')
       self.root.geometry("1200x725+0+0")
       self.img=ImageTk.PhotoImage(file="lib.jpg")       
       lbl_img=Label(self.root,image=self.img)
       lbl_img.place(x=0,y=48)
       frame=Frame(self.root,bg="#f68121")
       frame.place(x=4,y=2,width=1520,height=50)
      
       bms=lbl=Label(frame,text="Book Management System",font=('Times New Roman',25,'bold'),fg="black",bg="#f68121")
       bms.place(x=0,y=4)
        
       ser=lbl=Label(frame,text="Search ",font=('Times New Roman',18),fg="black",bg="#f68121")
       ser.place(x=895,y=8)        
       self.txtpass=Entry(frame,text="search",font=('Times New Roman',22,'bold'),border=0,bg="white")
       self.txtpass.place(x=975,y=8,width=210)    
    #    saparate frame for login
       box=Frame(self.root,bg="#f68121")
       box.place(x=785,y=85,height=600,width=400)
       
       sub=Label(box,text="Submit Book",fg="black",bg="#f68121",font=('Times New Roman',20))
       sub.place(x=115,y=20)      
       Frame(box,width=405,height=2,bg='black').place(x=0,y=65)
       
       username=lbl=Label(box,text="Username   :Praneeth",font=('Times New Roman',22),fg="black",bg="#f68121")
       username.place(x=20,y=80)       
       id=lbl=Label(box,text="Id Numbeer :12112110",font=('Times New Roman',20),fg="black",bg="#f68121")
       id.place(x=20,y=120) 
       Frame(box,width=405,height=2,bg='black').place(x=0,y=170)
       
       ur_name=Label(box,text="User Name :",font=('Times New Roman',22),fg="black",bg="#f68121").place(x=20,y=190)
       user = Entry(box,width=25,fg='black',border=0,bg='white',font=('Times New Roman',22))
       user.place(x=20,y=230)
       
       bk_name=Label(box,text="Book Name :",font=('Times New Roman',22),fg="black",bg="#f68121").place(x=20,y=280)
       book = Entry(box,width=25,fg='black',border=0,bg='white',font=('Times New Roman',22))
       book.place(x=20,y=320)
       
       pr=Label(box,text="Price:",font=('Times New Roman',22),fg="black",bg="#f68121").place(x=20,y=370)
       price = Entry(box,width=25,fg='black',border=0,bg='white',font=('Times New Roman',22))
       price.place(x=20,y=410)

       back_btn= Button(box,command=root.destroy,width=16,height=1,text='<Back to main page',border=0,fg='blue',cursor='hand2',bg='#f68121',)
       back_btn.place(x=5,y=460)
                      
       sub_btn=Button(box,command=self.submitted ,width=26,pady=7,text='Submit Book',bg='white',fg='#f68121',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       sub_btn.place(x=5,y=500,width=390)
   
   def submitted(self):
      open_main=messagebox.askyesno("YesNo","Confirm do you want to submit",parent=self.root)      
      if open_main>0:
         messagebox.showinfo("Success","Submited successfully",parent=self.root)
      else:
         messagebox.showerror("Error","not submited",parent=self.root)

class request_page:
   def __init__(self,root):
       self.root=root
       self.root.title('Request Book')
       self.root.geometry("1200x725+0+0")
       self.img=ImageTk.PhotoImage(file="lib.jpg")       
       lbl_img=Label(self.root,image=self.img)
       lbl_img.place(x=0,y=48)
       frame=Frame(self.root,bg="#f68121")
       frame.place(x=4,y=2,width=1520,height=50)
      
       bms=lbl=Label(frame,text="Book Management System",font=('Times New Roman',25,'bold'),fg="black",bg="#f68121")
       bms.place(x=0,y=4)       
 
       ser=lbl=Label(frame,text="Search ",font=('Times New Roman',18),fg="black",bg="#f68121")
       ser.place(x=895,y=8)        
       self.txtpass=Entry(frame,text="search",font=('Times New Roman',22,'bold'),border=0,bg="white")
       self.txtpass.place(x=975,y=8,width=210)    
    #    saparate frame for login
       box=Frame(self.root,bg="#f68121")
       box.place(x=785,y=85,height=600,width=400)
       
       sub=Label(box,text="Request Book",fg="black",bg="#f68121",font=('Times New Roman',20,"bold"))
       sub.place(x=110,y=20)      
       Frame(box,width=405,height=2,bg='black').place(x=0,y=65)
       
       username=lbl=Label(box,text="Username   :Praneeth",font=('Times New Roman',22),fg="black",bg="#f68121")
       username.place(x=20,y=80)       
       id=lbl=Label(box,text="Id Numbeer :12112110",font=('Times New Roman',20),fg="black",bg="#f68121")
       id.place(x=20,y=120) 
       Frame(box,width=405,height=2,bg='black').place(x=0,y=170)
       
       ur_name=Label(box,text="User Name :",font=('Times New Roman',22),fg="black",bg="#f68121").place(x=20,y=190)
       user = Entry(box,width=25,fg='black',border=0,bg='white',font=('Times New Roman',22))
       user.place(x=20,y=230)
       
       bk_name=Label(box,text="Avalable Books :",font=('Times New Roman',22),fg="black",bg="#f68121").place(x=20,y=280)
       clicked= StringVar()
       drop = OptionMenu(box, clicked,"Absalom, Absalom","A Time to Kill by John Grisham","The House of Mirth by Edith Wharton","East of Eden by John Steinbeck","Absalom","Vile Bodies by Evelyn Waugh","he House of Mirth","A Scanner Darkly by Philip ","Moab is my Washpot by Stephen Fry","East of Eden by John Steinbeck 1","A Time to Kill by John Grisham 2","book 3","he House of Mirth 4","he House of Mirth 5","Absalom 6","A Time to Kill by John Grisham 7","Absalom 8","lorem 9","c++ 10","python 11","radio 12","good man  13","power of the house 14","good you language","heelo world","he House of Mirth 17","Absalom 18","A Time to Kill by John Grisham 19","he House of Mirth 20","rooosd star 21","A Time to Kill by John Grisham 22")
       drop.pack()
       drop.place(x=20,y=320,width=350,height=35)
       
       pr=Label(box,text="Price:",font=('Times New Roman',22),fg="black",bg="#f68121").place(x=20,y=370)
       price = Entry(box,width=25,fg='black',border=0,bg='white',font=('Times New Roman',22))
       price.place(x=20,y=410)

       back_btn= Button(box,command=root.destroy,width=12,height=1,text='<Back to Main page',border=0,fg='blue',cursor='hand2',bg='#f68121',)
       back_btn.place(x=5,y=460,width=120)
                      
       sub_btn=Button(box,command=self.submitted ,width=26,pady=7,text='Order Book',bg='white',fg='#f68121',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       sub_btn.place(x=5,y=500,width=390)
   
   def submitted(self):
      open_main=messagebox.askyesno("YesNo","Confirm do you want to Order",parent=self.root)      
      if open_main>0:
         messagebox.showinfo("Success","Orderded successfully",parent=self.root)
      else:
         messagebox.showerror("Error","not Orderded",parent=self.root)
    
class search_page:
   def __init__(self,root):
       self.root=root
       self.root.title('Books Management System -Available Book')
       self.root.geometry("1200x725+0+0")
       self.img=ImageTk.PhotoImage(file="lib.jpg")       
       lbl_img=Label(self.root,image=self.img)
       lbl_img.place(x=0,y=48)
       frame=Frame(self.root,bg="#f68121")
       frame.place(x=4,y=2,width=1520,height=50)
      
       bms=lbl=Label(frame,text="Book Management System",font=('Times New Roman',25,'bold'),fg="black",bg="#f68121")
       bms.place(x=0,y=4)       
 
       ser=lbl=Label(frame,text="Search ",font=('Times New Roman',18),fg="black",bg="#f68121")
       ser.place(x=895,y=8)        
       self.txtpass=Entry(frame,text="search",font=('Times New Roman',22,'bold'),border=0,bg="white")
       self.txtpass.place(x=975,y=8,width=210)    
    #    saparate frame for login
       box=Frame(self.root,bg="#f68121")
       box.place(x=785,y=85,height=600,width=400)
       
       sub=Label(box,text="Available Book",fg="black",bg="#f68121",font=('Times New Roman',20,"bold"))
       sub.place(x=110,y=20)      
       Frame(box,width=405,height=2,bg='black').place(x=0,y=65)
       
       username=lbl=Label(box,text="Username   :Praneeth",font=('Times New Roman',22),fg="black",bg="#f68121")
       username.place(x=20,y=80)       
       id=lbl=Label(box,text="Id Numbeer :12112110",font=('Times New Roman',20),fg="black",bg="#f68121")
       id.place(x=20,y=120) 
       Frame(box,width=405,height=2,bg='black').place(x=0,y=170)       
       
       bk_name=Label(box,text="Avalable Books :",font=('Times New Roman',22),fg="black",bg="#f68121").place(x=20,y=190)
       clicked= StringVar()
       drop = OptionMenu(box, clicked,"Absalom, Absalom","A Time to Kill by John Grisham","The House of Mirth by Edith Wharton","East of Eden by John Steinbeck","Absalom","Vile Bodies by Evelyn Waugh","he House of Mirth","A Scanner Darkly by Philip ","Moab is my Washpot by Stephen Fry","East of Eden by John Steinbeck 1","A Time to Kill by John Grisham 2","book 3","he House of Mirth 4","he House of Mirth 5","Absalom 6","A Time to Kill by John Grisham 7","Absalom 8","lorem 9","c++ 10","python 11","radio 12","good man  13","power of the house 14","good you language","heelo world","he House of Mirth 17","Absalom 18","A Time to Kill by John Grisham 19","he House of Mirth 20","rooosd star 21","A Time to Kill by John Grisham 22")
       drop.pack()
       drop.place(x=20,y=230,width=350,height=35)             

       back_btn= Button(box,command=root.destroy,width=16,height=2,text='<Back to main page',border=0,fg='blue',cursor='hand2',bg='#f68121',font=('Times New Roman',22))
       back_btn.place(x=5,y=460)

       sub_btn=Button(box,command=self.submitted ,width=26,pady=7,text='Add to Cart',bg='white',fg='#f68121',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       sub_btn.place(x=5,y=300,width=390)
       
       buy_btn=Button(box,command=self.buy ,width=26,pady=7,text='Buy Now',bg='white',fg='#f68121',border=0,cursor='hand2',font=('Times New Roman',16,'bold'))
       buy_btn.place(x=5,y=375,width=390)
   
   def submitted(self): 

         messagebox.showinfo("Success","Book added to Cart",parent=self.root)
            
   def buy(self):
      open_main=messagebox.askyesno("YesNo","Confirm do you want to Buy",parent=self.root)      
      if open_main>0:
         messagebox.showinfo("Success","Orderded successfully",parent=self.root)
      else:
         messagebox.showerror("Error","not Orderded",parent=self.root)                      
         
if __name__=="__main__":
    root=Tk()
    app=Login_window(root)
    root.mainloop()
    