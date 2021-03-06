#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 15, 2020 11:09:51 PM IST  platform: Windows NT

import sys
from datetime import date
from time import strftime
from tkinter import messagebox

import first_window_support
import search_window
import search_window_support
import member_window
import member_window_support


import displayall_book_window
import displayall_book_window_support
import displayall_member_window
import displayall_member_window_support
import displayall_supplier_window
import displayall_supplier_window_support
import displayall_fine_window
import displayall_supplier_window_support
import displayall_borrowedbook_window
import displayall_borrowedbook_window_support
import add_book_window
import add_book_window_support
import add_member_window
import add_member_window_support
import add_supplier_window
import add_supplier_window_support
import add_fine_window
import add_fine_window_support
import add_bookissue_window
import add_bookissue_window_support
import delete_book_window
import delete_book_window_support
import delete_fine_window
import delete_fine_window_support
import delete_member_window
import delete_member_window_support
import delete_supplier_window
import delete_supplier_window_support
import delete_bookissue_window
import delete_bookissue_window_support

import numpy as np
import cx_Oracle



try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3 = False
except ImportError:
    import tkinter.ttk as ttk
    py3 = True



def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = search_window (root)
    search_window_support.init(root, top)
    root.mainloop()

w = None
def create_search_window(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = search_window (w)
    search_window_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_search_window():
    global w
    w.destroy()
    w = None

class search_window:

    def search(self):
        self.search1(self.Bookname_Entry.get(),self.Authorname_Entry.get())
    def search1(self,bookname,author):
        try:
            self.conn = cx_Oracle.connect("HR/root")
            self.cursor = self.conn.cursor()
            try:
                self.cursor.execute(
                    "declare nCount NUMBER; begin SELECT count(*) into nCount FROM user_tables where table_name = 'LMS_MEMBERS'; IF(nCount <= 0) THEN execute immediate ('Create table LMS_MEMBERS(MEMBER_ID Varchar2(10), MEMBER_NAME Varchar2(30) NOT NULL, CITY Varchar2(20), DATE_REGISTER date NOT NULL, DATE_EXPIRE date , MEMBERSHIP_STATUS Varchar2(15) NOT NULL, Constraint LMS_cts1 PRIMARY KEY(MEMBER_ID))'); END IF; end;")
            except Exception as e:
                messagebox.showerror("member table", e)
            try:
                self.cursor.execute(
                    "declare nCount NUMBER; begin SELECT count(*) into nCount FROM user_tables where table_name = 'LMS_SUPPLIERS_DETAILS'; IF(nCount <= 0) THEN execute immediate ('Create table LMS_SUPPLIERS_DETAILS(SUPPLIER_ID Varchar2(3),  SUPPLIER_NAME Varchar2(30) NOT NULL, ADDRESS Varchar2(50),	CONTACT number(10) NOT NULL, EMAIL Varchar2(15) NOT NULL, Constraint LMS_cts2 PRIMARY KEY(SUPPLIER_ID))'); END IF; end;")
            except Exception as e:
                messagebox.showerror("supplier table", e)
            try:
                self.cursor.execute(
                    "declare nCount NUMBER; begin SELECT count(*) into nCount FROM user_tables where table_name = 'LMS_FINE_DETAILS'; IF(nCount <= 0) THEN execute immediate ('Create table LMS_FINE_DETAILS(FINE_RANGE Varchar2(3), FINE_AMOUNT number(10,2) NOT NULL, Constraint LMS_cts3 PRIMARY KEY(FINE_RANGE))'); END IF; end;")
            except Exception as e:
                messagebox.showerror("finedetails table", e)
            try:
                self.cursor.execute(
                    "declare nCount NUMBER; begin SELECT count(*) into nCount FROM user_tables where table_name = 'LMS_BOOK_DETAILS'; IF(nCount <= 0) THEN execute immediate ('Create table LMS_BOOK_DETAILS(BOOK_CODE Varchar2(10), BOOK_TITLE Varchar2(50) NOT NULL, CATEGORY Varchar2(15) NOT NULL, AUTHOR Varchar2(30) NOT NULL, PUBLICATION Varchar2(30), PUBLISH_DATE date, BOOK_EDITION int, PRICE number(8,2) NOT NULL, RACK_NUM Varchar2(3), DATE_ARRIVAL date NOT NULL, SUPPLIER_ID Varchar2(3) NOT NULL, Constraint LMS_cts4 PRIMARY KEY(BOOK_CODE), Constraint LMS_cts41 FOREIGN KEY(SUPPLIER_ID) References LMS_SUPPLIERS_DETAILS(SUPPLIER_ID))'); END IF; end;")
            except Exception as e:
                messagebox.showerror("bookdetails table", e)
            try:
                self.cursor.execute(
                    "declare nCount NUMBER; begin SELECT count(*) into nCount FROM user_tables where table_name = 'LMS_BOOK_ISSUE'; IF(nCount <= 0) THEN execute immediate ('Create table LMS_BOOK_ISSUE(BOOK_ISSUE_NO int,MEMBER_ID Varchar2(10) NOT NULL, BOOK_CODE Varchar2(10) NOT NULL, DATE_ISSUE date NOT NULL, DATE_RETURN date NOT NULL, DATE_RETURNED date NULL,BOOK_ISSUE_STATUS varchar2(20), FINE_RANGE Varchar2(3), Constraint LMS_cts5 PRIMARY KEY(BOOK_ISSUE_NO), Constraint LMS_Mem FOREIGN KEY(MEMBER_ID) References LMS_MEMBERS(MEMBER_ID), Constraint LMS_BookDetail FOREIGN KEY(BOOK_CODE) References LMS_BOOK_DETAILS(BOOK_CODE), Constraint LMS_FineDetail FOREIGN KEY(FINE_RANGE) References LMS_FINE_DETAILS(FINE_RANGE))'); END IF; end;")
            except Exception as e:
                messagebox.showerror("book issue table", e)
            self.conn.commit()

        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Error!,while connecting", e)

        try:
            try:
                statement='select * from LMS_BOOK_DETAILS where BOOK_TITLE = :1 or AUTHOR = :2 '
                self.cursor.execute(statement,{'1' :bookname ,'2':author})
            except Exception as e:
                print("hi",e)
            row = self.cursor.fetchall()
            table_array = []
            table_array = np.asarray(row)

            try:
                for i in range(0, len( table_array)):
                    self.Search_Book_Scolledlistbox.insert("", 'end', text="#", values=row[i])
            except Exception as e:
                print("Hi", e)
        except Exception as e:
            messagebox.showerror("Error!", e)

    def display_all(self):
        try:
            displayall_book_window.create_displayall_window(root)
        except:
            displayall_book_window.create_displayall_window(rt)

    def add_book(self):
        try:
            add_book_window.create_Add_Book_Window(root)
        except:
            add_book_window.create_Add_Book_Window(rt)

    def delete_book(self):
        try:
            delete_book_window.create_Toplevel1(root)
        except:
            delete_book_window.create_Toplevel1(rt)

    def __init__(self, Search_Window=None):

        try:
            self.conn= cx_Oracle.connect("HR/root")
            self.cursor=self.conn.cursor()
            try:
                self.cursor.execute("declare nCount NUMBER; begin SELECT count(*) into nCount FROM user_tables where table_name = 'LMS_MEMBERS'; IF(nCount <= 0) THEN execute immediate ('Create table LMS_MEMBERS(MEMBER_ID Varchar2(10), MEMBER_NAME Varchar2(30) NOT NULL, CITY Varchar2(20), DATE_REGISTER date NOT NULL, DATE_EXPIRE date , MEMBERSHIP_STATUS Varchar2(15) NOT NULL, Constraint LMS_cts1 PRIMARY KEY(MEMBER_ID))'); END IF; end;")
            except Exception as e:
                messagebox.showerror("member table", e)
            try:
                self.cursor.execute("declare nCount NUMBER; begin SELECT count(*) into nCount FROM user_tables where table_name = 'LMS_SUPPLIERS_DETAILS'; IF(nCount <= 0) THEN execute immediate ('Create table LMS_SUPPLIERS_DETAILS(SUPPLIER_ID Varchar2(3),  SUPPLIER_NAME Varchar2(30) NOT NULL, ADDRESS Varchar2(50),	CONTACT number(10) NOT NULL, EMAIL Varchar2(15) NOT NULL, Constraint LMS_cts2 PRIMARY KEY(SUPPLIER_ID))'); END IF; end;")
            except Exception as e:
                messagebox.showerror("supplier table", e)
            try:
                self.cursor.execute("declare nCount NUMBER; begin SELECT count(*) into nCount FROM user_tables where table_name = 'LMS_FINE_DETAILS'; IF(nCount <= 0) THEN execute immediate ('Create table LMS_FINE_DETAILS(FINE_RANGE Varchar2(3), FINE_AMOUNT number(10,2) NOT NULL, Constraint LMS_cts3 PRIMARY KEY(FINE_RANGE))'); END IF; end;")
            except Exception as e:
                messagebox.showerror("finedetails table", e)
            try:
                self.cursor.execute("declare nCount NUMBER; begin SELECT count(*) into nCount FROM user_tables where table_name = 'LMS_BOOK_DETAILS'; IF(nCount <= 0) THEN execute immediate ('Create table LMS_BOOK_DETAILS(BOOK_CODE Varchar2(10), BOOK_TITLE Varchar2(50) NOT NULL, CATEGORY Varchar2(15) NOT NULL, AUTHOR Varchar2(30) NOT NULL, PUBLICATION Varchar2(30), PUBLISH_DATE date, BOOK_EDITION int, PRICE number(8,2) NOT NULL, RACK_NUM Varchar2(3), DATE_ARRIVAL date NOT NULL, SUPPLIER_ID Varchar2(3) NOT NULL, Constraint LMS_cts4 PRIMARY KEY(BOOK_CODE), Constraint LMS_cts41 FOREIGN KEY(SUPPLIER_ID) References LMS_SUPPLIERS_DETAILS(SUPPLIER_ID))'); END IF; end;")
            except Exception as e:
                messagebox.showerror("bookdetails table", e)
            try:
                self.cursor.execute("declare nCount NUMBER; begin SELECT count(*) into nCount FROM user_tables where table_name = 'LMS_BOOK_ISSUE'; IF(nCount <= 0) THEN execute immediate ('Create table LMS_BOOK_ISSUE(BOOK_ISSUE_NO int,MEMBER_ID Varchar2(10) NOT NULL, BOOK_CODE Varchar2(10) NOT NULL, DATE_ISSUE date NOT NULL, DATE_RETURN date NOT NULL, DATE_RETURNED date NULL,BOOK_ISSUE_STATUS varchar2(20), FINE_RANGE Varchar2(3), Constraint LMS_cts5 PRIMARY KEY(BOOK_ISSUE_NO), Constraint LMS_Mem FOREIGN KEY(MEMBER_ID) References LMS_MEMBERS(MEMBER_ID), Constraint LMS_BookDetail FOREIGN KEY(BOOK_CODE) References LMS_BOOK_DETAILS(BOOK_CODE), Constraint LMS_FineDetail FOREIGN KEY(FINE_RANGE) References LMS_FINE_DETAILS(FINE_RANGE))'); END IF; end;")
            except Exception as e:
                messagebox.showerror("book issue table", e)
            self.conn.commit()

        except cx_Oracle.DatabaseError as e:
            messagebox.showerror("Error!,while connecting",e)

        def tick(time1=''):
            time2=strftime("%H:%M:%S")
            if time2!=time1:
                time1=time2
                self.Timenow_Label.configure(text = time2)
            self.Timenow_Label.after(500, tick)

        '''This class configures and populates the toplevel window.
            Search_Window is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font11 = "-family {Times New Roman} -size 13 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font10 = "-family {Times New Roman} -size 15 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        Search_Window.geometry("1232x741+310+64")
        Search_Window.minsize(148, 1)
        Search_Window.maxsize(4112, 1055)
        Search_Window.resizable(0, 0)
        Search_Window.title("SEARCH WINDOW")
        Search_Window.configure(background="#b42cc7")
        Search_Window.configure(highlightbackground="#d9d9d9")
        Search_Window.configure(highlightcolor="black")

        self.Search_Window_Frame = tk.Frame(Search_Window)
        self.Search_Window_Frame.place(relx=0.049, rely=0.067, relheight=0.884
                                       , relwidth=0.916)
        self.Search_Window_Frame.configure(relief='groove')
        self.Search_Window_Frame.configure(borderwidth="2")
        self.Search_Window_Frame.configure(relief="groove")
        self.Search_Window_Frame.configure(background="#5f86d8")
        self.Search_Window_Frame.configure(highlightbackground="#d9d9d9")
        self.Search_Window_Frame.configure(highlightcolor="black")

        self.Private_Label = tk.Label(self.Search_Window_Frame)
        self.Private_Label.place(relx=0.115, rely=0.061, height=126, width=912)
        self.Private_Label.configure(activebackground="#f9f9f9")
        self.Private_Label.configure(activeforeground="black")
        self.Private_Label.configure(background="#d9d9d9")
        self.Private_Label.configure(disabledforeground="#a3a3a3")
        self.Private_Label.configure(font="-family {Times New Roman} -size 20")
        self.Private_Label.configure(foreground="#000000")
        self.Private_Label.configure(highlightbackground="#d9d9d9")
        self.Private_Label.configure(highlightcolor="black")
        self.Private_Label.configure(text='''Private Library''')

        self.Date_Label = tk.Label(self.Search_Window_Frame)
        self.Date_Label.place(relx=0.115, rely=0.244, height=56, width=262)
        self.Date_Label.configure(activebackground="#f9f9f9")
        self.Date_Label.configure(activeforeground="black")
        self.Date_Label.configure(background="#d9d9d9")
        self.Date_Label.configure(disabledforeground="#a3a3a3")
        self.Date_Label.configure(font="-family {Times New Roman} -size 13")
        self.Date_Label.configure(foreground="#000000")
        self.Date_Label.configure(highlightbackground="#d9d9d9")
        self.Date_Label.configure(highlightcolor="black")
        self.Date_Label.configure(text='''Date:''')

        self.Datenow_Label = tk.Label(self.Search_Window_Frame)
        self.Datenow_Label.place(relx=0.345, rely=0.244, height=56, width=212)
        self.Datenow_Label.configure(activebackground="#f9f9f9")
        self.Datenow_Label.configure(activeforeground="black")
        self.Datenow_Label.configure(background="#d9d9d9")
        self.Datenow_Label.configure(disabledforeground="#a3a3a3")
        self.Datenow_Label.configure(font="-family {Times New Roman} -size 13")
        self.Datenow_Label.configure(foreground="#000000")
        self.Datenow_Label.configure(highlightbackground="#d9d9d9")
        self.Datenow_Label.configure(highlightcolor="black")
        self.Datenow_Label.configure(text=date.today())

        self.Time_Label = tk.Label(self.Search_Window_Frame)
        self.Time_Label.place(relx=0.531, rely=0.244, height=56, width=212)
        self.Time_Label.configure(activebackground="#f9f9f9")
        self.Time_Label.configure(activeforeground="black")
        self.Time_Label.configure(background="#d9d9d9")
        self.Time_Label.configure(disabledforeground="#a3a3a3")
        self.Time_Label.configure(font="-family {Times New Roman} -size 13")
        self.Time_Label.configure(foreground="#000000")
        self.Time_Label.configure(highlightbackground="#d9d9d9")
        self.Time_Label.configure(highlightcolor="black")
        self.Time_Label.configure(text='''Time:''')

        self.Timenow_Label = tk.Label(self.Search_Window_Frame)
        self.Timenow_Label.place(relx=0.717, rely=0.229, height=66, width=234)
        self.Timenow_Label.configure(activebackground="#f9f9f9")
        self.Timenow_Label.configure(activeforeground="black")
        self.Timenow_Label.configure(background="#d9d9d9")
        self.Timenow_Label.configure(disabledforeground="#a3a3a3")
        self.Timenow_Label.configure(font="-family {Times New Roman} -size 13")
        self.Timenow_Label.configure(foreground="#000000")
        self.Timenow_Label.configure(highlightbackground="#d9d9d9")
        self.Timenow_Label.configure(highlightcolor="black")
        tick()

        self.Bookname_Label = tk.Label(self.Search_Window_Frame)
        self.Bookname_Label.place(relx=0.124, rely=0.382, height=46, width=202)
        self.Bookname_Label.configure(activebackground="#f9f9f9")
        self.Bookname_Label.configure(activeforeground="black")
        self.Bookname_Label.configure(background="#d9d9d9")
        self.Bookname_Label.configure(disabledforeground="#a3a3a3")
        self.Bookname_Label.configure(font="-family {Times New Roman} -size 13")
        self.Bookname_Label.configure(foreground="#000000")
        self.Bookname_Label.configure(highlightbackground="#d9d9d9")
        self.Bookname_Label.configure(highlightcolor="black")
        self.Bookname_Label.configure(text='''Book Title:''')

        self.Authorname_Label = tk.Label(self.Search_Window_Frame)
        self.Authorname_Label.place(relx=0.124, rely=0.489, height=46, width=202)
        self.Authorname_Label.configure(activebackground="#f9f9f9")
        self.Authorname_Label.configure(activeforeground="black")
        self.Authorname_Label.configure(background="#d9d9d9")
        self.Authorname_Label.configure(disabledforeground="#a3a3a3")
        self.Authorname_Label.configure(font="-family {Times New Roman} -size 13")
        self.Authorname_Label.configure(foreground="#000000")
        self.Authorname_Label.configure(highlightbackground="#d9d9d9")
        self.Authorname_Label.configure(highlightcolor="black")
        self.Authorname_Label.configure(text='''Author:''')

        self.Publication_label = tk.Label(self.Search_Window_Frame)
        self.Publication_label.place(relx=0.124, rely=0.595, height=36, width=202)
        self.Publication_label.configure(activebackground="#f9f9f9")
        self.Publication_label.configure(activeforeground="black")
        self.Publication_label.configure(background="#d9d9d9")
        self.Publication_label.configure(disabledforeground="#a3a3a3")
        self.Publication_label.configure(font="-family {Times New Roman} -size 13")
        self.Publication_label.configure(foreground="#000000")
        self.Publication_label.configure(highlightbackground="#d9d9d9")
        self.Publication_label.configure(highlightcolor="black")
        self.Publication_label.configure(text='''Publication:''')

        self.Bookname_Entry = tk.Entry(self.Search_Window_Frame)
        self.Bookname_Entry.place(relx=0.328, rely=0.382, height=44, relwidth=0.305)
        self.Bookname_Entry.configure(background="white")
        self.Bookname_Entry.configure(disabledforeground="#a3a3a3")
        self.Bookname_Entry.configure(font="-family {Times New Roman} -size 13")
        self.Bookname_Entry.configure(foreground="#000000")
        self.Bookname_Entry.configure(highlightbackground="#d9d9d9")
        self.Bookname_Entry.configure(highlightcolor="black")
        self.Bookname_Entry.configure(insertbackground="black")
        self.Bookname_Entry.configure(selectbackground="#c4c4c4")
        self.Bookname_Entry.configure(selectforeground="black")

        self.Authorname_Entry = tk.Entry(self.Search_Window_Frame)
        self.Authorname_Entry.place(relx=0.328, rely=0.489, height=44, relwidth=0.305)
        self.Authorname_Entry.configure(background="white")
        self.Authorname_Entry.configure(disabledforeground="#a3a3a3")
        self.Authorname_Entry.configure(font="-family {Times New Roman} -size 13")
        self.Authorname_Entry.configure(foreground="#000000")
        self.Authorname_Entry.configure(highlightbackground="#d9d9d9")
        self.Authorname_Entry.configure(highlightcolor="black")
        self.Authorname_Entry.configure(insertbackground="black")
        self.Authorname_Entry.configure(selectbackground="#c4c4c4")
        self.Authorname_Entry.configure(selectforeground="black")

        self.Publication_Entry = tk.Entry(self.Search_Window_Frame)
        self.Publication_Entry.place(relx=0.328, rely=0.595, height=44, relwidth=0.305)
        self.Publication_Entry.configure(background="white")
        self.Publication_Entry.configure(disabledforeground="#a3a3a3")
        self.Publication_Entry.configure(font="-family {Times New Roman} -size 13")
        self.Publication_Entry.configure(foreground="#000000")
        self.Publication_Entry.configure(highlightbackground="#d9d9d9")
        self.Publication_Entry.configure(highlightcolor="black")
        self.Publication_Entry.configure(insertbackground="black")
        self.Publication_Entry.configure(selectbackground="#c4c4c4")
        self.Publication_Entry.configure(selectforeground="black")

        self.Searchavail_Button = tk.Button(self.Search_Window_Frame)
        self.Searchavail_Button.place(relx=0.248, rely=0.733, height=53, width=176)
        self.Searchavail_Button.configure(activebackground="#ececec")
        self.Searchavail_Button.configure(activeforeground="#000000")
        self.Searchavail_Button.configure(background="#d9d9d9")
        self.Searchavail_Button.configure(disabledforeground="#a3a3a3")
        self.Searchavail_Button.configure(font="-family {Times New Roman} -size 13")
        self.Searchavail_Button.configure(foreground="#000000")
        self.Searchavail_Button.configure(highlightbackground="#d9d9d9")
        self.Searchavail_Button.configure(highlightcolor="black")
        self.Searchavail_Button.configure(pady="0")
        self.Searchavail_Button.configure(command=self.search,text='''Search''')

        self.Searchall_Button = tk.Button(self.Search_Window_Frame)
        self.Searchall_Button.place(relx=0.762, rely=0.443, height=83, width=176)
        self.Searchall_Button.configure(activebackground="#ececec")
        self.Searchall_Button.configure(activeforeground="#000000")
        self.Searchall_Button.configure(background="#d9d9d9")
        self.Searchall_Button.configure(disabledforeground="#a3a3a3")
        self.Searchall_Button.configure(font="-family {Times New Roman} -size 13")
        self.Searchall_Button.configure(foreground="#000000")
        self.Searchall_Button.configure(highlightbackground="#d9d9d9")
        self.Searchall_Button.configure(highlightcolor="black")
        self.Searchall_Button.configure(pady="0")
        self.Searchall_Button.configure(command=self.display_all,text='''SHOW ALL''')

        self.Search_Book_Scolledlistbox = ScrolledTreeView(Search_Window)
        self.Search_Book_Scolledlistbox.place(relx=0.452, rely=0.727, relheight=0.198, relwidth=0.50)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvatica", 15))
        style.configure("Treeview", font=("Helvatica", 12, "normal"))
        self.Search_Book_Scolledlistbox.configure(columns=(
        "Book_Code", "Book_Title", "Category", "Author", "Publication", "Publish_Date", "Book_Edition", "Price",
        "Rack_Num", "Supplier_Id"))
        # self.Search_Book_Scolledlistbox.configure(font="-family {Helvatica} -size 15 -weight normal -slant"  \
        #     " roman -underline 0 -overstrike 0")
        # build_treeview_support starting.
        self.Search_Book_Scolledlistbox.heading("#0", text="#")
        self.Search_Book_Scolledlistbox.heading("#0", anchor="center")
        self.Search_Book_Scolledlistbox.column("#0", width="0")
        self.Search_Book_Scolledlistbox.column("#0", minwidth="0")
        self.Search_Book_Scolledlistbox.column("#0", stretch="0")
        self.Search_Book_Scolledlistbox.column("#0", anchor="center")

        self.Search_Book_Scolledlistbox.heading("Book_Code", text="Book Code")
        self.Search_Book_Scolledlistbox.heading("Book_Code", anchor="center")
        self.Search_Book_Scolledlistbox.column("Book_Code", width="100")
        self.Search_Book_Scolledlistbox.column("Book_Code", minwidth="20")
        self.Search_Book_Scolledlistbox.column("Book_Code", stretch="1")
        self.Search_Book_Scolledlistbox.column("Book_Code", anchor="center")

        self.Search_Book_Scolledlistbox.heading("Book_Title", text="Book Title")
        self.Search_Book_Scolledlistbox.heading("Book_Title", anchor="center")
        self.Search_Book_Scolledlistbox.column("Book_Title", width="200")
        self.Search_Book_Scolledlistbox.column("Book_Title", minwidth="20")
        self.Search_Book_Scolledlistbox.column("Book_Title", stretch="1")
        self.Search_Book_Scolledlistbox.column("Book_Title", anchor="center")

        self.Search_Book_Scolledlistbox.heading("Category", text="Category")
        self.Search_Book_Scolledlistbox.heading("Category", anchor="center")
        self.Search_Book_Scolledlistbox.column("Category", width="150")
        self.Search_Book_Scolledlistbox.column("Category", minwidth="20")
        self.Search_Book_Scolledlistbox.column("Category", stretch="1")
        self.Search_Book_Scolledlistbox.column("Category", anchor="center")

        self.Search_Book_Scolledlistbox.heading("Author", text="Author")
        self.Search_Book_Scolledlistbox.heading("Author", anchor="center")
        self.Search_Book_Scolledlistbox.column("Author", width="200")
        self.Search_Book_Scolledlistbox.column("Author", minwidth="20")
        self.Search_Book_Scolledlistbox.column("Author", stretch="1")
        self.Search_Book_Scolledlistbox.column("Author", anchor="center")

        self.Search_Book_Scolledlistbox.heading("Publication", text="Publication")
        self.Search_Book_Scolledlistbox.heading("Publication", anchor="center")
        self.Search_Book_Scolledlistbox.column("Publication", width="150")
        self.Search_Book_Scolledlistbox.column("Publication", minwidth="20")
        self.Search_Book_Scolledlistbox.column("Publication", stretch="1")
        self.Search_Book_Scolledlistbox.column("Publication", anchor="center")

        self.Search_Book_Scolledlistbox.heading("Publish_Date", text="Publish Date")
        self.Search_Book_Scolledlistbox.heading("Publish_Date", anchor="center")
        self.Search_Book_Scolledlistbox.column("Publish_Date", width="200")
        self.Search_Book_Scolledlistbox.column("Publish_Date", minwidth="20")
        self.Search_Book_Scolledlistbox.column("Publish_Date", stretch="1")
        self.Search_Book_Scolledlistbox.column("Publish_Date", anchor="center")

        self.Search_Book_Scolledlistbox.heading("Book_Edition", text="Book Edition")
        self.Search_Book_Scolledlistbox.heading("Book_Edition", anchor="center")
        self.Search_Book_Scolledlistbox.column("Book_Edition", width="90")
        self.Search_Book_Scolledlistbox.column("Book_Edition", minwidth="20")
        self.Search_Book_Scolledlistbox.column("Book_Edition", stretch="1")
        self.Search_Book_Scolledlistbox.column("Book_Edition", anchor="center")

        self.Search_Book_Scolledlistbox.heading("Price", text="Price")
        self.Search_Book_Scolledlistbox.heading("Price", anchor="center")
        self.Search_Book_Scolledlistbox.column("Price", width="70")
        self.Search_Book_Scolledlistbox.column("Price", minwidth="20")
        self.Search_Book_Scolledlistbox.column("Price", stretch="1")
        self.Search_Book_Scolledlistbox.column("Price", anchor="center")

        self.Search_Book_Scolledlistbox.heading("Rack_Num", text="Rack Num")
        self.Search_Book_Scolledlistbox.heading("Rack_Num", anchor="center")
        self.Search_Book_Scolledlistbox.column("Rack_Num", width="150")
        self.Search_Book_Scolledlistbox.column("Rack_Num", minwidth="20")
        self.Search_Book_Scolledlistbox.column("Rack_Num", stretch="1")
        self.Search_Book_Scolledlistbox.column("Rack_Num", anchor="center")

        self.Search_Book_Scolledlistbox.heading("Supplier_Id", text="Supplier Id")
        self.Search_Book_Scolledlistbox.heading("Supplier_Id", anchor="center")
        self.Search_Book_Scolledlistbox.column("Supplier_Id", width="150")
        self.Search_Book_Scolledlistbox.column("Supplier_Id", minwidth="20")
        self.Search_Book_Scolledlistbox.column("Supplier_Id", stretch="1")
        self.Search_Book_Scolledlistbox.column("Supplier_Id", anchor="center")

        # self.Search_Book_Scolledlistbox = ScrolledListBox(self.Search_Window_Frame)
        #
        # self.Search_Book_Scolledlistbox.place(relx=0.452, rely=0.727, relheight=0.248, relwidth = 0.518)
        #
        # self.Search_Book_Scolledlistbox.configure(background="white")
        # self.Search_Book_Scolledlistbox.configure(disabledforeground="#a3a3a3")
        #
        # self.Search_Book_Scolledlistbox.configure(font=font10)
        #
        # self.Search_Book_Scolledlistbox.configure(foreground="black")
        #
        # self.Search_Book_Scolledlistbox.configure(highlightbackground="#d9d9d9")
        #
        # self.Search_Book_Scolledlistbox.configure(highlightcolor="#d9d9d9")
        # self.Search_Book_Scolledlistbox.configure(selectbackground="#c4c4c4")
        #
        # self.Search_Book_Scolledlistbox.configure(selectforeground="black")

        self.menubar = tk.Menu(Search_Window, font=font9, bg=_bgcolor, fg=_fgcolor)
        Search_Window.configure(menu = self.menubar)

        self.File = tk.Menu(Search_Window, tearoff=0)
        self.menubar.add_cascade(menu=self.File,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 compound="left",
                                 foreground="#000000",
                                 label="File")
        self.File.add_command(
                activebackground="#ececec",
                activeforeground="#000000",
                background="#d9d9d9",
                foreground="#000000",
                label="Exit",
                command=search_window_support.destroy_window)
        self.Edit_Menu = tk.Menu(Search_Window, tearoff=0)
        self.menubar.add_cascade(menu=self.Edit_Menu,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 compound="left",
                                 foreground="#000000",
                                 label="Edit")
        self.Edit_Menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Add Book",
            command=self.add_book)

        self.Edit_Menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Delete Book",
            command=self.delete_book)

        self.conn.commit()
        self.conn.close()

# The following code is added to facilitate the Scrolled widgets you specified.
class AutoScroll(object):
    '''Configure the scrollbars for a widget.'''

    def __init__(self, master):
        #  Rozen. Added the try-except clauses so that this class
        #  could be used for scrolled entry widget for which vertical
        #  scrolling is not supported. 5/7/14.
        try:
            vsb = ttk.Scrollbar(master, orient='vertical', command=self.yview)
        except:
            pass
        hsb = ttk.Scrollbar(master, orient='horizontal', command=self.xview)

        #self.configure(yscrollcommand=_autoscroll(vsb),
        #    xscrollcommand=_autoscroll(hsb))
        try:
            self.configure(yscrollcommand=self._autoscroll(vsb))
        except:
            pass
        self.configure(xscrollcommand=self._autoscroll(hsb))

        self.grid(column=0, row=0, sticky='nsew')
        try:
            vsb.grid(column=1, row=0, sticky='ns')
        except:
            pass
        hsb.grid(column=0, row=1, sticky='ew')

        master.grid_columnconfigure(0, weight=1)
        master.grid_rowconfigure(0, weight=1)

        # Copy geometry methods of master  (taken from ScrolledText.py)
        if py3:
            methods = tk.Pack.__dict__.keys() | tk.Grid.__dict__.keys() \
                  | tk.Place.__dict__.keys()
        else:
            methods = tk.Pack.__dict__.keys() + tk.Grid.__dict__.keys() \
                  + tk.Place.__dict__.keys()

        for meth in methods:
            if meth[0] != '_' and meth not in ('config', 'configure'):
                setattr(self, meth, getattr(master, meth))

    @staticmethod
    def _autoscroll(sbar):
        '''Hide and show scrollbar as needed.'''
        def wrapped(first, last):
            first, last = float(first), float(last)
            if first <= 0 and last >= 1:
                sbar.grid_remove()
            else:
                sbar.grid()
            sbar.set(first, last)
        return wrapped

    def __str__(self):
        return str(self.master)

def _create_container(func):
    '''Creates a ttk Frame with a given master, and use this new frame to
    place the scrollbars and the widget.'''
    def wrapped(cls, master, **kw):
        container = ttk.Frame(master)
        container.bind('<Enter>', lambda e: _bound_to_mousewheel(e, container))
        container.bind('<Leave>', lambda e: _unbound_to_mousewheel(e, container))
        return func(cls, container, **kw)
    return wrapped

class ScrolledTreeView(AutoScroll, ttk.Treeview):
    '''A standard ttk Treeview widget with scrollbars that will
    automatically show/hide as needed.'''
    @_create_container
    def __init__(self, master, **kw):
        ttk.Treeview.__init__(self, master, **kw)
        AutoScroll.__init__(self, master)

import platform
def _bound_to_mousewheel(event, widget):
    child = widget.winfo_children()[0]
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        child.bind_all('<MouseWheel>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-MouseWheel>', lambda e: _on_shiftmouse(e, child))
    else:
        child.bind_all('<Button-4>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Button-5>', lambda e: _on_mousewheel(e, child))
        child.bind_all('<Shift-Button-4>', lambda e: _on_shiftmouse(e, child))
        child.bind_all('<Shift-Button-5>', lambda e: _on_shiftmouse(e, child))

def _unbound_to_mousewheel(event, widget):
    if platform.system() == 'Windows' or platform.system() == 'Darwin':
        widget.unbind_all('<MouseWheel>')
        widget.unbind_all('<Shift-MouseWheel>')
    else:
        widget.unbind_all('<Button-4>')
        widget.unbind_all('<Button-5>')
        widget.unbind_all('<Shift-Button-4>')
        widget.unbind_all('<Shift-Button-5>')

def _on_mousewheel(event, widget):
    if platform.system() == 'Windows':
        widget.yview_scroll(-1*int(event.delta/120),'units')
    elif platform.system() == 'Darwin':
        widget.yview_scroll(-1*int(event.delta),'units')
    else:
        if event.num == 4:
            widget.yview_scroll(-1, 'units')
        elif event.num == 5:
            widget.yview_scroll(1, 'units')

def _on_shiftmouse(event, widget):
    if platform.system() == 'Windows':
        widget.xview_scroll(-1*int(event.delta/120), 'units')
    elif platform.system() == 'Darwin':
        widget.xview_scroll(-1*int(event.delta), 'units')
    else:
        if event.num == 4:
            widget.xview_scroll(-1, 'units')
        elif event.num == 5:
            widget.xview_scroll(1, 'units')

if __name__ == '__main__':
    vp_start_gui()





