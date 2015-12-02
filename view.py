__author__ = 'Nick'

from tkinter import *
from tkinter import messagebox
# from tkinter.filedialog import askopenfilename
import os
import sys
sys.path.append( os.getcwd() )
import menu
import user
# login
def log_in():

   temp = Toplevel()
   temp.title("Log In")

   name = Label(temp, text="User Name")
   name.grid(row = 0, column = 0 )
   e1 = Entry(temp)
   e1.grid(row = 0,column = 1 )

   password = Label(temp, text="PassWord")
   password.grid(row=1,column=0)
   e2 = Entry(temp)
   e2.grid(row=1,column=1)

   global text
   # handle parameter
   def pass_para():
      global mymenu
      nonlocal e1
      nonlocal e2
      result = mymenu.login(e1.get(), e2.get())
      if( result ):
         print(result)
         text.insert(INSERT,"Login successfully!\n" )
         temp.withdraw()
      else:
         text.insert(INSERT,"Login failed! Try again or logout first!\n" )
         print(result)

   b1 = Button(temp, text="Enter", command=pass_para)
   b1.grid(row=2,column = 0)
# logout
def Log_out():
   global mymenu
   mymenu.logout()
   global text
   text.insert(INSERT, "logout successfully!\n")
# create manager
def cm():
   global mymenu
   global text
   if ( isinstance( mymenu._menu__current_user, user.manager ) ):
      temp = Toplevel()
      temp.title("Manager Account")
      # handle parameter
      def cm_pass():
         nonlocal e1
         nonlocal e2
         mymenu.account_management_create( 1,e1.get(), e2.get() )
         nonlocal temp
         temp.withdraw()

      name = Label(temp, text="New Username")
      name.grid(row = 0, column = 0 )
      e1 = Entry(temp)
      e1.grid(row = 0,column = 1 )

      password = Label(temp, text="New Password")
      password.grid(row=1,column=0)
      e2 = Entry(temp)
      e2.grid(row=1,column=1)

      b1 = Button(temp, text="Enter", command=cm_pass)
      b1.grid(row=2,column = 0)

   else:
      text.insert(INSERT, "No authorized\n")
# create employee
def ce():
   global mymenu
   global text
   if ( isinstance( mymenu._menu__current_user, user.manager ) ):
      temp = Toplevel()
      temp.title("Employee Account")

      def cm_pass():
         nonlocal e1
         nonlocal e2
         mymenu.account_management_create( 2,e1.get(), e2.get() )
         nonlocal temp
         temp.withdraw()

      name = Label(temp, text="New Username")
      name.grid(row = 0, column = 0 )
      e1 = Entry(temp)
      e1.grid(row = 0,column = 1 )

      password = Label(temp, text="New Password")
      password.grid(row=1,column=0)
      e2 = Entry(temp)
      e2.grid(row=1,column=1)

      b1 = Button(temp, text="Enter", command=cm_pass)
      b1.grid(row=2,column = 0)

   else:
      text.insert(INSERT, "No authorized\n")

# sale
def sale():
   temp = Toplevel()
   temp.title("SALE")

   name = Label(temp, text="Enter the name or barcode")
   name.grid(row = 0, column = 0 )
   e1 = Entry(temp)
   e1.grid(row = 0,column = 1 )

   global text
   # handle parameter
   def pass_para():
      global mymenu
      nonlocal e1
      #result = mymenu.store_management_sale(e1.get())
      if ( isinstance(mymenu._menu__current_user,user.manager) or isinstance(mymenu._menu__current_user, user.employee) ):
         ss = mymenu.store_management_sale(e1.get())
         text.insert(INSERT,"Sale operation successfully! {0} has been sold\n".format(e1.get()) )
         text.insert(INSERT,"{0}".format( ss ) )
      else:
         text.insert(INSERT,"Operation failed!\n")
      temp.withdraw()

   b1 = Button(temp, text="Enter", command=pass_para)
   b1.grid(row=0,column =2)

# search
def search():
   temp = Toplevel()
   temp.title("Search")

   name = Label(temp, text="Enter the name or barcode")
   name.grid(row = 0, column = 0 )
   e1 = Entry(temp)
   e1.grid(row = 0,column = 1 )

   global text
   # handle parameter
   def pass_para():
      global mymenu
      nonlocal e1
      #result = mymenu.store_management_sale(e1.get())
      if ( isinstance(mymenu._menu__current_user,user.manager) or isinstance(mymenu._menu__current_user, user.employee) ):
         ss = mymenu.store_management_search(e1.get())
         text.insert(INSERT,"Search operation successfully! {0} has been found\n".format(e1.get()) )
         text.insert(INSERT,"{0}\n".format( ss ) )
      else:
         text.insert(INSERT,"Operation failed!\n")
      temp.withdraw()

   b1 = Button(temp, text="Enter", command=pass_para)
   b1.grid(row=0,column =2)

# delete
def delete():
   temp = Toplevel()
   temp.title("Delete")

   name = Label(temp, text="Enter the name or barcode")
   name.grid(row = 0, column = 0 )
   e1 = Entry(temp)
   e1.grid(row = 0,column = 1 )

   global text
   # handle parameter
   def pass_para():
      global mymenu
      nonlocal e1
      #result = mymenu.store_management_sale(e1.get())
      if ( isinstance(mymenu._menu__current_user,user.manager) or isinstance(mymenu._menu__current_user, user.employee) ):
         ss = mymenu.store_management_delete(e1.get())
         text.insert(INSERT,"Delete operation successfully! {0} has been deleted\n".format(e1.get()) )
         text.insert(INSERT,"{0}\n".format( ss ) )
      else:
         text.insert(INSERT,"Operation failed!\n")
      temp.withdraw()

   b1 = Button(temp, text="Enter", command=pass_para)
   b1.grid(row=0,column =2)
# show all item in inventory
def show_all():
   global text
   global mymenu
   #result = mymenu.store_management_sale(e1.get())
   if ( isinstance(mymenu._menu__current_user,user.manager) or isinstance(mymenu._menu__current_user, user.employee) ):
      ss = mymenu.report()
      text.insert(INSERT,"Report operation successfully!\n" )
      for temp in ss.keys():
         text.insert(INSERT,"{0}\n".format( ss[temp] ) )
   else:
      text.insert(INSERT,"Operation failed!\n")

def about():
   messagebox.showinfo( "About", "This is a final project in OOAD course.")
def building():
   messagebox.showinfo("Building","Not finished yet!")

mymenu = menu.menu()

root = Tk()
root.title("Inventory Manager System")
root.geometry("800x600")
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
# text
text = Text(root)
text.grid(row=0, column=0, sticky='nesw')
vertical_scroller = Scrollbar(root, orient='vertical')
vertical_scroller.grid(row=0, column=1, sticky='ns')
horizontal_scroller = Scrollbar(root, orient='horizontal')
horizontal_scroller.grid(row=1, column=0, sticky='ew')
# add menu
menu = Menu(root,tearoff = 0)
root.config(menu=menu)
# file menu
filemenu = Menu(menu)
menu.add_cascade(label="Menu", menu=filemenu)
filemenu.add_command(label="Log In", command = log_in )
filemenu.add_command(label="Log Out", command=Log_out )
filemenu.add_separator()
filemenu.add_command(label="Create Manager", command = cm )
filemenu.add_command(label="Create Employee", command = ce )
filemenu.add_command(label="Modify")
filemenu.add_separator()
filemenu.add_command(label="Exit", command=root.quit)
# store menu
storemenu = Menu(menu)
menu.add_cascade( label="Store",menu = storemenu )
storemenu.add_command(label="Sale",command = sale )
storemenu.add_command(label="Search",command = search )
storemenu.add_command(label="Delete",command = delete )
storemenu.add_command(label="Modify", command = building )
#report menu
reportmenu = Menu(menu)
menu.add_cascade(label="Report", menu=reportmenu )
reportmenu.add_command(label="Show all", command = show_all)
#reportmenu.add_command("")
# help menu
helpmenu = Menu(menu)
menu.add_cascade(label="Help", menu=helpmenu)
helpmenu.add_command(label="About...", command=about)

mainloop()
