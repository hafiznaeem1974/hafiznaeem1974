from email.mime import image
from tkinter import*
from tkinter import ttk,messagebox
from PIL import Image ,ImageTk  # pip install pillow
from category_5 import categoryClass
from employee_2 import employeeClass
from supplier_4 import supplierClass
from product_6 import productClass
from sales_7 import salesClass
import os
import time
import pyodbc
class IMS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1950x1000+0+0")
        self.root.title("Inventory Management System")
        self.root.config(bg="white")
        ####title###
        self.Icon_title=PhotoImage(file="images/logo1.png")
        title=Label(self.root,text="Inventory Management System",image=self.Icon_title,compound=LEFT,font=("time new roman",40,"bold"),bg="#010c48",fg="white",anchor="w",padx=20).place(x=0,y=0,relwidth=1,height=70)
        #######  Button_logout
        btn_logout=Button(self.root,text="Logout",command=self.logout,font=("time new roman",15,"bold"),bg="yellow",cursor="hand2").place(x=1700,y=10,height=50,width=150)
        ######## Clock
        self.lbl_clock=Label(self.root,text="Welcome to Inventory Management System\t\t Date: DD-MM-YYYY\t\t Time: HH:MM:SS",font=("time new roman",15),bg="#4d636d",fg="white")
        self.lbl_clock.place(x=0,y=70,relwidth=1,height=30)
        ##########Left Menu
        self.MenuLogo=Image.open("images/menu_im.png")
        self.MenuLogo=self.MenuLogo.resize((200,200),Image.ANTIALIAS)
        self.MenuLogo=ImageTk.PhotoImage(self.MenuLogo)

        LEFTMenu=Frame(self.root,bd=2,relief=RIDGE,bg="white")
        LEFTMenu.place(x=0,y=102,width=200,height=900)

        lbl_menuLogo = Label(LEFTMenu,image=self.MenuLogo)
        lbl_menuLogo.pack(side=TOP,fill=X)

        self.Icon_side=PhotoImage(file="images/side.png")
        ######Label
        lbl_menu=Label(LEFTMenu,text="Menu",font=("time new roman",20),bg="#009688").pack(side=TOP,fill=X)
        ######### Button
        btn_employee=Button(LEFTMenu,text="Employee",command=self.employee,image=self.Icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",19,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_supplier=Button(LEFTMenu,text="supplier",command=self.supplier,image=self.Icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",19,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_category=Button(LEFTMenu,text="category",command=self.category,image=self.Icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",19,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_product=Button(LEFTMenu,text="product",command=self.product,image=self.Icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",19,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_sales=Button(LEFTMenu,text="sales",command=self.sales,image=self.Icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",19,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        btn_exit=Button(LEFTMenu,text="exit",image=self.Icon_side,compound=LEFT,padx=5,anchor="w",font=("time new roman",19,"bold"),bg="white",bd=3,cursor="hand2").pack(side=TOP,fill=X)
        ### Contents #####
        self.lbl_employee = Label(self.root,text="Total Employee\n[ 0 ]",bd=5,relief=RIDGE,bg="#33bb59",font=("goudy old style",20,"bold")) 
        self.lbl_employee.place(x=300,y=120,height=150,width=300)

        self.lbl_supplier = Label(self.root,text="Total Supplier\n[ 0 ]",bd=5,relief=RIDGE,bg="#ff5722",font=("goudy old style",20,"bold")) 
        self.lbl_supplier.place(x=650,y=120,height=150,width=300)

        self.lbl_category = Label(self.root,text="Total Category\n[ 0 ]",bd=5,relief=RIDGE,bg="#009688",font=("goudy old style",20,"bold")) 
        self.lbl_category.place(x=1000,y=120,height=150,width=300)

        self.lbl_product = Label(self.root,text="Total Product\n[ 0 ]",bd=5,relief=RIDGE,bg="#607d8b",font=("goudy old style",20,"bold")) 
        self.lbl_product.place(x=300,y=300,height=150,width=300)

        self.lbl_sales = Label(self.root,text="Total Sales\n[ 0 ]",bd=5,relief=RIDGE,bg="#ffc107",font=("goudy old style",20,"bold")) 
        self.lbl_sales.place(x=650,y=300,height=150,width=300)
        
        ############# footer
        lbl_footer=Label(self.root,text="IMS-Inventory Management System | Developed By HMN US CORP\nFor Contact: 0015189772970",font=("time new roman",15),bg="#4d636d",fg="white").pack(side=BOTTOM,fill=X)
        self.update_content()
    ################################
    def employee(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=employeeClass(self.new_window)

    def supplier(self):
        self.new_window=Toplevel(self.root)
        self.new_obj=supplierClass(self.new_window)

    def category(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=categoryClass(self.new_win)

    def product(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=productClass(self.new_win)

    def sales(self):
        self.new_win=Toplevel(self.root)
        self.new_obj=salesClass(self.new_win)

    def update_content(self):
        con=pyodbc.connect(DRIVER="{ODBC driver 17 for sql server}",host="localhost",user="superuser",password="T722707@cd",database="ims")
        cur=con.cursor()
        try:
            cur.execute("select * from product")
            product=cur.fetchall()
            self.lbl_product.config(text=f'Total Products\n[ {str(len(product))} ]')
            
            cur.execute("select * from supplier")
            supplier=cur.fetchall()
            self.lbl_supplier.config(text=f'Total Suppliers\n[ {str(len(supplier))} ]')
            
            cur.execute("select * from category")
            category=cur.fetchall()
            self.lbl_category.config(text=f'Total Categories\n[ {str(len(category))} ]')
            
            cur.execute("select * from employee")
            employee=cur.fetchall()
            self.lbl_employee.config(text=f'Total Categories\n[ {str(len(employee))} ]')
            bill=len(os.listdir('bill'))
            self.lbl_sales.config(text=f'Total Sales\n [{str(bill)}]')

            time_=time.strftime("%H:%M:%S")
            date_=time.strftime("%d-%m-%Y")
            self.lbl_clock.config(text=f"Welcome to Inventory Management System\t\t Date: {str(date_)}\t\t Time: {str(time_)}")
            self.lbl_clock.after(200,self.update_content)
        
        except Exception as es:
            messagebox.showerror("Error",f"Error due to :{str(es)}",parent=self.root)

    def logout(self):
        self.root.destroy()
        os.system("python login.py")



if __name__ == "__main__":
    root=Tk()
    obj=IMS(root)
    root.mainloop()