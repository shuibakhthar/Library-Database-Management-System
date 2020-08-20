#! /usr/bin/env python
#  -*- coding: utf-8 -*-
#
# GUI module generated by PAGE version 4.26
#  in conjunction with Tcl version 8.6
#    Feb 17, 2020 04:35:32 PM IST  platform: Windows NT

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

import displayall_borrowedbook_window_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = Toplevel1 (root)
    displayall_borrowedbook_window_support.init(root, top)
    root.mainloop()

w = None
def create_Toplevel1(root, *args, **kwargs):
    '''Starting point when module is imported by another program.'''
    global w, w_win, rt
    rt = root
    w = tk.Toplevel (root)
    top = Toplevel1 (w)
    displayall_borrowedbook_window_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_Toplevel1():
    global w
    w.destroy()
    w = None

class Toplevel1:

    def add_borrower(self):
        try:
            add_bookissue_window.create_Toplevel1(root)
        except:
            add_bookissue_window.create_Toplevel1(rt)

    def delete_borrower(self):
        try:
            delete_bookissue_window.create_Toplevel1(root)
        except:
            delete_bookissue_window.create_Toplevel1(rt)

    def show_all(self):
        try:
            self.conn = cx_Oracle.connect('HR/root')
            self.cursor = self.conn.cursor()
            self.cursor.execute('select * from LMS_BOOK_ISSUE order by BOOK_ISSUE_NO')
            row = self.cursor.fetchall()
            table_array = []
            table_array = np.asarray(row)

            try:
                for i in range(0, len(table_array)):
                    self.Displayall_Borrowedbook_Scrolledlistbox.insert("", 'end', text="#", values=row[i])
            except:
                print("hi")
        except Exception as e:
            messagebox.showerror("Error!", e)

    def refresh(self):
        self.Displayall_Borrowedbook_Scrolledlistbox.delete(*self.Displayall_Borrowedbook_Scrolledlistbox.get_children())
        self.show_all()

    def __init__(self, Displayall_Borrowedbook_Window=None):

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
            messagebox.showerror("Error! while connecting", e)


        def tick(time1=''):
            time2 = strftime("%H:%M:%S")
            if time2 != time1:
                time1 = time2
                self.Timenow_Label.configure(text=time2)
            self.Timenow_Label.after(500, tick)

        '''This class configures and populates the toplevel window.
                           Displayall_Member_window is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9'  # X11 color: 'gray85'
        _ana1color = '#d9d9d9'  # X11 color: 'gray85'
        _ana2color = '#ececec'  # Closest X11 color: 'gray92'
        font10 = "-family {Times New Roman} -size 15 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font11 = "-family {Times New Roman} -size 13 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font12 = "-family {Times New Roman} -size 20 -weight normal " \
                 "-slant roman -underline 0 -overstrike 0"
        font9 = "-family {Segoe UI} -size 9 -weight normal -slant " \
                "roman -underline 0 -overstrike 0"

        Displayall_Borrowedbook_Window.geometry("1232x741+310+64")
        Displayall_Borrowedbook_Window.minsize(148, 1)
        Displayall_Borrowedbook_Window.maxsize(4112, 1055)
        Displayall_Borrowedbook_Window.resizable(1, 1)
        Displayall_Borrowedbook_Window.title("BORROWER - ALL BORROWER WINDOW")
        Displayall_Borrowedbook_Window.configure(background="#b42cc7")

        self.Displayall_Borrowedbook_Window_Frame = tk.Frame(Displayall_Borrowedbook_Window)
        self.Displayall_Borrowedbook_Window_Frame.place(relx=0.049, rely=0.061
                                                        , relheight=0.884, relwidth=0.91)
        self.Displayall_Borrowedbook_Window_Frame.configure(relief='groove')
        self.Displayall_Borrowedbook_Window_Frame.configure(borderwidth="2")
        self.Displayall_Borrowedbook_Window_Frame.configure(relief="groove")
        self.Displayall_Borrowedbook_Window_Frame.configure(background="#5f86d8")

        self.Private_Label = tk.Label(self.Displayall_Borrowedbook_Window_Frame)
        self.Private_Label.place(relx=0.115, rely=0.061, height=126, width=912)
        self.Private_Label.configure(background="#d9d9d9")
        self.Private_Label.configure(disabledforeground="#a3a3a3")
        self.Private_Label.configure(font=font12)
        self.Private_Label.configure(foreground="#000000")
        self.Private_Label.configure(text='''Private Library''')

        self.Date_Label = tk.Label(self.Displayall_Borrowedbook_Window_Frame)
        self.Date_Label.place(relx=0.115, rely=0.244, height=56, width=262)
        self.Date_Label.configure(background="#d9d9d9")
        self.Date_Label.configure(disabledforeground="#a3a3a3")
        self.Date_Label.configure(font=font11)
        self.Date_Label.configure(foreground="#000000")
        self.Date_Label.configure(text='''Date:''')

        self.Datenow_Label = tk.Label(self.Displayall_Borrowedbook_Window_Frame)
        self.Datenow_Label.place(relx=0.345, rely=0.244, height=56, width=212)
        self.Datenow_Label.configure(background="#d9d9d9")
        self.Datenow_Label.configure(disabledforeground="#a3a3a3")
        self.Datenow_Label.configure(font=font11)
        self.Datenow_Label.configure(foreground="#000000")
        self.Datenow_Label.configure(text=date.today())

        self.Time_Label = tk.Label(self.Displayall_Borrowedbook_Window_Frame)
        self.Time_Label.place(relx=0.531, rely=0.244, height=56, width=212)
        self.Time_Label.configure(background="#d9d9d9")
        self.Time_Label.configure(disabledforeground="#a3a3a3")
        self.Time_Label.configure(font=font11)
        self.Time_Label.configure(foreground="#000000")
        self.Time_Label.configure(text='''Time:''')

        self.Timenow_Label = tk.Label(self.Displayall_Borrowedbook_Window_Frame)
        self.Timenow_Label.place(relx=0.717, rely=0.229, height=66, width=239)
        self.Timenow_Label.configure(background="#d9d9d9")
        self.Timenow_Label.configure(disabledforeground="#a3a3a3")
        self.Timenow_Label.configure(font=font11)
        self.Timenow_Label.configure(foreground="#000000")
        tick()

        self.Refresh_Button = tk.Button(self.Displayall_Borrowedbook_Window_Frame)
        self.Refresh_Button.place(relx=0.025, rely=0.343, height=50, width=200)
        self.Refresh_Button.configure(activebackground="#f9f9f9")
        self.Refresh_Button.configure(activeforeground="black")
        self.Refresh_Button.configure(background="#d9d9d9")
        self.Refresh_Button.configure(disabledforeground="#a3a3a3")
        self.Refresh_Button.configure(font="-family {Times New Roman} -size 13")
        self.Refresh_Button.configure(foreground="#000000")
        self.Refresh_Button.configure(highlightbackground="#d9d9d9")
        self.Refresh_Button.configure(highlightcolor="black")
        self.Refresh_Button.configure(text="Refresh", command=self.refresh)

        self.Displayall_Borrowedbook_Scrolledlistbox = ScrolledTreeView(Displayall_Borrowedbook_Window)
        self.Displayall_Borrowedbook_Scrolledlistbox.place(relx=0.075, rely=0.443
                                              , relheight=0.477, relwidth=0.876)
        style = ttk.Style()
        style.configure("Treeview.Heading", font=("Helvatica", 15))
        style.configure("Treeview", font=("Helvatica", 12, "normal"))
        self.Displayall_Borrowedbook_Scrolledlistbox.configure(columns=(
        "Book_Issue_No", "Member_ID", "Book_Code", "Date_Issue", "Date_Return", "Date_Returned", "Book_Issue_status", "Fine_Range"))
        # self.Displayall_Borrowedbook_Scrolledlistbox.configure(font="-family {Helvatica} -size 15 -weight normal -slant"  \
        #     " roman -underline 0 -overstrike 0")
        # build_treeview_support starting.
        self.Displayall_Borrowedbook_Scrolledlistbox.heading("#0", text="#")
        self.Displayall_Borrowedbook_Scrolledlistbox.heading("#0", anchor="center")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("#0", width="0")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("#0", minwidth="0")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("#0", stretch="0")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("#0", anchor="center")

        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Book_Issue_No", text="Book Issue NO")
        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Book_Issue_No", anchor="center")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Issue_No", width="150")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Issue_No", minwidth="20")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Issue_No", stretch="1")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Issue_No", anchor="center")

        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Member_ID", text="Member ID")
        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Member_ID", anchor="center")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Member_ID", width="200")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Member_ID", minwidth="20")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Member_ID", stretch="1")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Member_ID", anchor="center")

        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Book_Code", text="Book Code")
        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Book_Code", anchor="center")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Code", width="150")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Code", minwidth="20")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Code", stretch="1")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Code", anchor="center")

        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Date_Issue", text="Date Of Issue")
        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Date_Issue", anchor="center")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Issue", width="200")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Issue", minwidth="20")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Issue", stretch="1")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Issue", anchor="center")

        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Date_Return", text="Date Of Return")
        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Date_Return", anchor="center")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Return", width="150")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Return", minwidth="20")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Return", stretch="1")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Return", anchor="center")

        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Date_Returned", text="Date Returned")
        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Date_Returned", anchor="center")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Returned", width="200")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Returned", minwidth="20")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Returned", stretch="1")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Date_Returned", anchor="center")

        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Book_Issue_status", text="Book Issue Status")
        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Book_Issue_status", anchor="center")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Issue_status", width="200")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Issue_status", minwidth="20")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Issue_status", stretch="1")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Book_Issue_status", anchor="center")

        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Fine_Range", text="Fine Range")
        self.Displayall_Borrowedbook_Scrolledlistbox.heading("Fine_Range", anchor="center")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Fine_Range", width="150")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Fine_Range", minwidth="20")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Fine_Range", stretch="1")
        self.Displayall_Borrowedbook_Scrolledlistbox.column("Fine_Range", anchor="center")

        # self.Displayall_Borrowedbook_Scrolledlistbox = ScrolledListBox(self.Displayall_Borrowedbook_Window_Frame)
        # self.Displayall_Borrowedbook_Scrolledlistbox.place(relx=0.116, rely=0.382, relheight=0.53
        #                                                    , relwidth=0.807)
        # self.Displayall_Borrowedbook_Scrolledlistbox.configure(background="white")
        # self.Displayall_Borrowedbook_Scrolledlistbox.configure(disabledforeground="#a3a3a3")
        # self.Displayall_Borrowedbook_Scrolledlistbox.configure(font=font10)
        # self.Displayall_Borrowedbook_Scrolledlistbox.configure(foreground="black")
        # self.Displayall_Borrowedbook_Scrolledlistbox.configure(highlightbackground="#d9d9d9")
        # self.Displayall_Borrowedbook_Scrolledlistbox.configure(highlightcolor="#d9d9d9")
        # self.Displayall_Borrowedbook_Scrolledlistbox.configure(selectbackground="#c4c4c4")
        # self.Displayall_Borrowedbook_Scrolledlistbox.configure(selectforeground="black")
        # # self.Displayall_Borrowedbook_Scrolledlistbox.insert(0,"hi")
        self.show_all()

        self.menubar = tk.Menu(Displayall_Borrowedbook_Window, font=font9, bg=_bgcolor, fg=_fgcolor)
        Displayall_Borrowedbook_Window.configure(menu=self.menubar)

        self.File = tk.Menu(Displayall_Borrowedbook_Window, tearoff=0)
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
            command=displayall_borrowedbook_window_support.destroy_window)
        self.Edit = tk.Menu(Displayall_Borrowedbook_Window, tearoff=0)
        self.menubar.add_cascade(menu=self.Edit,
                                 activebackground="#ececec",
                                 activeforeground="#000000",
                                 background="#d9d9d9",
                                 compound="left",
                                 foreground="#000000",
                                 label="Edit")
        self.Edit.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Add Borrower",
            command=self.add_borrower)
        self.Edit.add_command(
            activebackground="#ececec",
            activeforeground="#000000",
            background="#d9d9d9",
            foreground="#000000",
            label="Delete Borrower",
            command=self.delete_borrower)

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





