from tkinter import *
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import sqlite3





#defining function for creating GUI Layout
def Main_frame():
    #creating window
    root = Tk()
    #setting width and height for window
    root.geometry("1000x800")
    #setting title for window
    root.title("Studentdatabase")
    global tree
    global SEARCH
    global name,contact,email,rollno,branch
    SEARCH = StringVar()
    name = StringVar()
    contact = StringVar()
    email = StringVar()
    rollno = StringVar()
    branch = StringVar()

    #creating frames for layout
    #topview frame for heading
    title_frame = Frame(root, width=900, bd=4, relief=GROOVE)
    title_frame.pack(side=TOP, fill=X)
    #first left frame for registration from

    #search  frame for search form
    search_frame = Frame(root, width=900,bg="gray")
    search_frame.pack(side=BOTTOM, fill=Y)
    LFrom = Frame(root, width="800")
    LFrom.pack(side=RIGHT, fill=Y)
    #mid frame for displaying students record
    display_frame = Frame(root, width=1500,height=700)
    display_frame.pack(side=RIGHT)
    #label for heading
    lbl_text = Label(title_frame, text="Student Management System", font=('verdana', 18), width=600,bg="thistle1")
    lbl_text.pack(fill=X)
    #creating registration form in first left frame
    Label(LFrom, text="Name  ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom,font=("Arial",10,"bold"),textvariable=name).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Contact ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=contact).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Email ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=email).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Rollno ", font=("Arial", 12)).pack(side=TOP)
    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=rollno).pack(side=TOP, padx=10, fill=X)
    Label(LFrom, text="Branch ", font=("Arial", 12)).pack(side=TOP)

    Entry(LFrom, font=("Arial", 10, "bold"),textvariable=branch).pack(side=TOP, padx=10, fill=X)
    Button(LFrom,text="Submit",font=("Arial", 10, "bold"),command=register).pack(side=TOP, padx=10,pady=5, fill=X)

    # creating search label and entry in search frame
    lbl_txtsearch = Label(search_frame, text="Enter name to Search", font=('verdana', 10), bg="gray")
    lbl_txtsearch.pack()
    # creating search entry
    search = Entry(search_frame, textvariable=SEARCH, font=('verdana', 15), width=10)
    search.pack(side=LEFT, padx=10, fill=X)
    # creating search button
    btn_search = Button(search_frame, text="Search", command=SearchRecord)
    btn_search.pack(side=LEFT, padx=10, pady=10, fill=X)
    # creating view button
    btn_view = Button(search_frame, text="View All", command=DisplayData)
    btn_view.pack(side=LEFT, padx=10, pady=10, fill=X)
    # creating reset button
    btn_reset = Button(search_frame, text="Reset", command=Reset)
    btn_reset.pack(side=LEFT, padx=10, pady=10, fill=X)
    # creating delete button
    btn_delete = Button(search_frame, text="Delete", command=delete)
    btn_delete.pack(side=LEFT, padx=10, pady=10, fill=X)
    # setting scrollbar
    scrollbarx = Scrollbar(display_frame, orient=HORIZONTAL)
    scrollbary = Scrollbar(display_frame, orient=VERTICAL)
    tree = ttk.Treeview(display_frame, columns=("Student Id", "Name", "Contact", "Email", "Rollno", "Branch"),
                        selectmode="extended", height=100, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
    scrollbary.config(command=tree.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=tree.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    # setting headings for the columns
    tree.heading('Student Id', text="Student Id", anchor=W)
    tree.heading('Name', text="Name", anchor=W)
    tree.heading('Contact', text="Contact", anchor=W)
    tree.heading('Email', text="Email", anchor=W)
    tree.heading('Rollno', text="Rollno", anchor=W)
    tree.heading('Branch', text="Branch", anchor=W)

    # setting width of the columns
    tree.column('#0', stretch=NO, minwidth=0, width=0)
    tree.column('#1', stretch=NO, minwidth=0, width=100)
    tree.column('#2', stretch=NO, minwidth=0, width=150)
    tree.column('#3', stretch=NO, minwidth=0, width=80)
    tree.column('#4', stretch=NO, minwidth=0, width=120)

    tree.pack()
    DisplayData()









Main_frame()
if __name__=='__main__':
#Running Application
 mainloop()




