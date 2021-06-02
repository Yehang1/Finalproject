def Database():
    global conn, cursor
    #creating student database
    conn = sqlite3.connect("student.db")
    cursor = conn.cursor()
    #creating STUD_DATAA table
    cursor.execute(
        "CREATE TABLE IF NOT EXISTS STU_DATAAA(STU_ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, STU_NAME TEXT, STU_CONTACT TEXT, STU_EMAIL TEXT, STU_ROLLNO TEXT, STU_BRANCH TEXT)")


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


def delete():
    # open database
    Database()
    if not tree.selection():
        tkMessageBox.showwarning("Warning", "Select data to delete")
    else:
        result = tkMessageBox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                          icon="warning")
        if result == 'yes':
            curItem = tree.focus()
            contents = (tree.item(curItem))
            selecteditem = contents['values']
            tree.delete(curItem)
            cursor = conn.execute("DELETE FROM STU_DATAAA WHERE STU_ID = %d" % selecteditem[0])
            conn.commit()
            cursor.close()
            conn.close()
def SearchRecord():
    #open database
    Database()
    #checking search text is empty or not
    if SEARCH.get() != "":
        #clearing current display data
        tree.delete(*tree.get_children())
        #select query with where clause
        cursor=conn.execute("SELECT * FROM STU_DATAAA WHERE STU_NAME LIKE ?", ('%' + str(SEARCH.get()) + '%',))
        #fetch all matching records
        fetch = cursor.fetchall()
        #loop for displaying all records into GUI
        for data in fetch:
            tree.insert('', 'end', values=(data))
        cursor.close()
        conn.close()



