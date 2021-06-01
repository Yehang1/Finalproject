def Database():
    global conn, cursor
    #creating student database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    #creating STUD_REGISTRATION table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STUD_DATAAA(STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_BRANCH TEXT)")


def register():
    Database()
    # getting form data
    name1 = name.get()
    con1 = contact.get()
    email1 = email.get()
    rol1 = rollno.get()
    branch1 = branch.get()

    # applying empty validation
    if name1 == '' or con1 == '' or email1 == '' or rol1 == '' or branch1 == '':
        tkMessageBox.showinfo("Warning", "fill the empty field!!!")
    else:
        # execute query
        conn.execute('INSERT INTO STU_DATAAA (STU_NAME,STU_CONTACT,STU_EMAIL,STU_ROLLNO,STU_BRANCH) \
                    VALUES (?,?,?,?,?)', (name1, con1, email1, rol1, branch1,));
        conn.commit()
        tkMessageBox.showinfo("Message", "Stored successfully")
        # refresh table data
        DisplayData()
        conn.close()







def Reset():
    # clear current data from table
    tree.delete(*tree.get_children())
    # refresh table data
    DisplayData()
    # clear search text
    SEARCH.set("")
    name.set("")
    contact.set("")
    email.set("")
    rollno.set("")
    branch.set("")
