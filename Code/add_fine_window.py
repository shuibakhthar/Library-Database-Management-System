#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 18, 2020 06:05:25 PM IST  platform: Windows NT

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

import add_fine_window_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    add_fine_window_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    add_fine_window_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def add_fine(self):
        self.add_fine1(self.Fine_Range_Entry.get(), self.Fine_Amount_Entry.get())
    def add_fine1(self, fine_range, fine_amount):

        try:
            self.conn = cx_Oracle.connect('HR/root')
            self.cursor = self.conn.cursor()
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
            messagebox.showerror("Error! in connection", e)
        try:
            # if member_id == '' or member_name=='' or city=='' or date_of_register=='' or date_of_expire=='' or membership_status == '' or book_edition=='' or price=='' or rack_no=='' or supplier_id=='':
            #     messagebox.showerror("Error!","Please Enter All The Fields")
            self.cursor.execute("INSERT INTO LMS_FINE_DETAILS VALUES(:1,:2)", (fine_range, fine_amount))
            self.conn.commit()
            messagebox.showinfo("Success","Successfully Added")
        except Exception as e:
             messagebox.showerror("Error in insertion!", e)

    def update_fine(self):
        self.update_fine1(self.Fine_Range_Entry.get(), self.Fine_Amount_Entry.get())
    def update_fine1(self,fine_range,fine_amount):
        try:
            self.conn = cx_Oracle.connect('HR/root')
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
            messagebox.showerror("Error! in connection", e)

        try:
            # if member_id == '' or member_name=='' or city=='' or date_of_register=='' or date_of_expire=='' or membership_status == '' or book_edition=='' or price=='' or rack_no=='' or supplier_id=='':
            #     messagebox.showerror("Error!","Please Enter All The Fields")
            # self.cursor.execute("UPDATE INTO LMS_BOOK_DETAILS VALUES(:1,:2,:3,:4,:5,:6,:7,:8,:9,:10)", (
            # book_code, book_title, category, author, publication, publish_date, book_edition, price, rack_no,
            # supplier_id))

            if fine_amount != '':
                self.cursor.execute(("UPDATE LMS_FINE_DETAILS SET FINE_AMOUNT = :1 WHERE FINE_RANGE = :2"),(fine_amount,fine_range))
                self.conn.commit()

        except Exception as e:
            messagebox.showerror("Error in updation!", e)

    def __init__(self, Add_Fine_Window=None):

        try:
            self.conn = cx_Oracle.connect('HR/root')
            self.cursor = self.conn.cursor()
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
            messagebox.showerror("Error! in connection", e)

        def tick(time1=''):
            time2=strftime("%H:%M:%S")
            if time2!=time1:
                time1=time2
                self.Timenow_Label.configure(text = time2)
            self.Timenow_Label.after(500, tick)

        '''This class configures and populates the toplevel window.
                  Displayall_Member_window is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font11 = "-family {Times New Roman} -size 20 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font12 = "-family {Times New Roman} -size 13 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        Add_Fine_Window.geometry("1232x741+310+64")
        Add_Fine_Window.minsize(148, 1)
        Add_Fine_Window.maxsize(4112, 1055)
        Add_Fine_Window.resizable(0, 0)
        Add_Fine_Window.title("ADD FINE WINDOW")
        Add_Fine_Window.configure(background="#b42cc7")

        self.Add_Fine_Window_Frame = tk.Frame(Add_Fine_Window)
        self.Add_Fine_Window_Frame.place(relx=0.049, rely=0.063, relheight=0.884
                                         , relwidth=0.916)
        self.Add_Fine_Window_Frame.configure(relief='groove')
        self.Add_Fine_Window_Frame.configure(borderwidth="2")
        self.Add_Fine_Window_Frame.configure(relief="groove")
        self.Add_Fine_Window_Frame.configure(background="#5f86d8")

        self.Private_Label = tk.Label(self.Add_Fine_Window_Frame)
        self.Private_Label.place(relx=0.115, rely=0.061, height=126, width=912)
        self.Private_Label.configure(background="#d9d9d9")
        self.Private_Label.configure(disabledforeground="#a3a3a3")
        self.Private_Label.configure(font=font11)
        self.Private_Label.configure(foreground="#000000")
        self.Private_Label.configure(text='''Private Library''')

        self.Date_Label = tk.Label(self.Add_Fine_Window_Frame)
        self.Date_Label.place(relx=0.115, rely=0.244, height=56, width=262)
        self.Date_Label.configure(background="#d9d9d9")
        self.Date_Label.configure(disabledforeground="#a3a3a3")
        self.Date_Label.configure(font=font12)
        self.Date_Label.configure(foreground="#000000")
        self.Date_Label.configure(text='''Date:''')

        self.Datenow_Label = tk.Label(self.Add_Fine_Window_Frame)
        self.Datenow_Label.place(relx=0.345, rely=0.244, height=56, width=212)
        self.Datenow_Label.configure(background="#d9d9d9")
        self.Datenow_Label.configure(disabledforeground="#a3a3a3")
        self.Datenow_Label.configure(font=font12)
        self.Datenow_Label.configure(foreground="#000000")
        self.Datenow_Label.configure(text=date.today())

        self.Time_LAbel = tk.Label(self.Add_Fine_Window_Frame)
        self.Time_LAbel.place(relx=0.531, rely=0.244, height=56, width=213)
        self.Time_LAbel.configure(background="#d9d9d9")
        self.Time_LAbel.configure(disabledforeground="#a3a3a3")
        self.Time_LAbel.configure(font=font12)
        self.Time_LAbel.configure(foreground="#000000")
        self.Time_LAbel.configure(text='''Time:''')

        self.Timenow_Label = tk.Label(self.Add_Fine_Window_Frame)
        self.Timenow_Label.place(relx=0.717, rely=0.229, height=66, width=234)
        self.Timenow_Label.configure(background="#d9d9d9")
        self.Timenow_Label.configure(disabledforeground="#a3a3a3")
        self.Timenow_Label.configure(font=font12)
        self.Timenow_Label.configure(foreground="#000000")
        tick(self)

        self.Fine_Range_Label = tk.Label(self.Add_Fine_Window_Frame)
        self.Fine_Range_Label.place(relx=0.124, rely=0.382, height=36, width=152)
        self.Fine_Range_Label.configure(background="#d9d9d9")
        self.Fine_Range_Label.configure(disabledforeground="#a3a3a3")
        self.Fine_Range_Label.configure(font=font12)
        self.Fine_Range_Label.configure(foreground="#000000")
        self.Fine_Range_Label.configure(text='''Fine Range:''')

        self.Fine_Amount_Label = tk.Label(self.Add_Fine_Window_Frame)
        self.Fine_Amount_Label.place(relx=0.124, rely=0.458, height=36, width=152)

        self.Fine_Amount_Label.configure(background="#d9d9d9")
        self.Fine_Amount_Label.configure(disabledforeground="#a3a3a3")
        self.Fine_Amount_Label.configure(font=font12)
        self.Fine_Amount_Label.configure(foreground="#000000")
        self.Fine_Amount_Label.configure(text='''Fine Amount:''')

        self.Fine_Range_Entry = tk.Entry(self.Add_Fine_Window_Frame)
        self.Fine_Range_Entry.place(relx=0.266, rely=0.382, height=34
                                    , relwidth=0.181)
        self.Fine_Range_Entry.configure(background="white")
        self.Fine_Range_Entry.configure(disabledforeground="#a3a3a3")
        self.Fine_Range_Entry.configure(font=font12)
        self.Fine_Range_Entry.configure(foreground="#000000")
        self.Fine_Range_Entry.configure(insertbackground="black")

        self.Fine_Amount_Entry = tk.Entry(self.Add_Fine_Window_Frame)
        self.Fine_Amount_Entry.place(relx=0.266, rely=0.458, height=34
                                     , relwidth=0.181)
        self.Fine_Amount_Entry.configure(background="white")
        self.Fine_Amount_Entry.configure(disabledforeground="#a3a3a3")
        self.Fine_Amount_Entry.configure(font=font12)
        self.Fine_Amount_Entry.configure(foreground="#000000")
        self.Fine_Amount_Entry.configure(insertbackground="black")

        self.Add_Button = tk.Button(self.Add_Fine_Window_Frame)
        self.Add_Button.place(relx=0.316, rely=0.794, height=53, width=186)
        self.Add_Button.configure(activebackground="#ececec")
        self.Add_Button.configure(activeforeground="#000000")
        self.Add_Button.configure(background="#d9d9d9")
        self.Add_Button.configure(disabledforeground="#a3a3a3")
        self.Add_Button.configure(font=font12)
        self.Add_Button.configure(foreground="#000000")
        self.Add_Button.configure(highlightbackground="#d9d9d9")
        self.Add_Button.configure(highlightcolor="black")
        self.Add_Button.configure(pady="0")
        self.Add_Button.configure(command=self.add_fine, text='''ADD''')

        self.Update_Button = tk.Button(self.Add_Fine_Window_Frame)
        self.Update_Button.place(relx=0.516, rely=0.794, height=53, width=186)
        self.Update_Button.configure(activebackground="#ececec")
        self.Update_Button.configure(activeforeground="#000000")
        self.Update_Button.configure(background="#d9d9d9")
        self.Update_Button.configure(disabledforeground="#a3a3a3")
        self.Update_Button.configure(font=font12)
        self.Update_Button.configure(foreground="#000000")
        self.Update_Button.configure(highlightbackground="#d9d9d9")
        self.Update_Button.configure(highlightcolor="black")
        self.Update_Button.configure(pady="0")
        self.Update_Button.configure(command=self.update_fine, text='''UPDATE''')

        self.menubar = tk.Menu(Add_Fine_Window, font=font9, bg=_bgcolor, fg=_fgcolor)
        Add_Fine_Window.configure(menu=self.menubar)

        self.sub_menu = tk.Menu(Add_Fine_Window, tearoff=0)
        self.menubar.add_cascade(menu=self.sub_menu,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 compound="left",
                                 foreground="#000000",
                                 label="File")
        self.sub_menu.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Exit",
            command=add_fine_window_support.destroy_window)

        self.conn.commit()
        self.conn.close()

if __name__ == '__main__':
    vp_start_gui()





