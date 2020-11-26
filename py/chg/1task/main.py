# this program is written in python
import sqlite3
import sys

# ................................ database part ........................

# connection from database
con = sqlite3.connect('task_list_db.sqlite')


# creating the table
def create_table(action):
    # cursor object
    cursorObj = con.cursor()
    # execute the query
    cursorObj.execute(action)
    con.commit()
    return cursorObj.lastrowid

# viewing the all pending taks
def view_task():
    # cursor object
    cursorObj = con.cursor()
    # execute the query
    cursorObj.execute("SELECT * FROM Task where IsCompleted=?",(0,))
    rows = cursorObj.fetchall()
    if rows:
        for row in rows:
            print(f'''{row[0]}. {row[1]}''')
    else:
        print ("Congrats! No Pending task available")

# fething completed tasks 
def history_task():
    # cursor object
    cursorObj = con.cursor()
    # execute the query
    cursorObj.execute("SELECT * FROM Task where IsCompleted=?",(1,))
    rows = cursorObj.fetchall()
    if rows:
        for row in rows:
            print(f'''{row[0]}. {row[1]} (Done!)''')
    else:
        print ("Sorry! You have not completed any task yet...")


# add a task
def add_task(action,params):
    # cursor object
    cursorObj = con.cursor()
    # execute the query
    cursorObj.execute(action,params)
    con.commit()
    return cursorObj.lastrowid
  
# complete a task
def complete_task(action,params):
    # cursor object
    cursorObj = con.cursor()
    # execute the query
    cursorObj.execute(action,params)
    con.commit()

# delete a task
def delete_task(action,params):
    # cursor object
    cursorObj = con.cursor()
    # execute the query
    cursorObj.execute(action,params)
    con.commit()

# creating the table if not exists...
create_table('''CREATE TABLE IF NOT EXISTS Task(TaskID INTEGER PRIMARY KEY AUTOINCREMENT, Description TEXT(20) NOT NULL, IsCompleted INTEGER);''')

        

# ................................ task part ........................

class Task:
    command = ""

    def showMenu(self):
        print(
'''
type a command from menu to perform the corresponding action.
view : View pending tasks
history : View completed tasks 
add : Add a task
complete : Complete a task
delete : Delete a task
exit : Exit program 
'''
        )
        self.command=input("your command : ")
        self.runCommand()



    def runCommand(self):
        if(self.command == "view"):
            view_task()
            self.showMenu()

        elif(self.command == "history"):
            history_task()
            self.showMenu()


        elif(self.command == "add"):
            description = input("Enter task description : ")
            params = (description,0)
            add_task("INSERT INTO Task VALUES (NULL, ?, ?)", params)
            self.showMenu()

        elif(self.command == "complete"):
            id = input("Enter the task id: ")
            params=(1,id)
            complete_task('''
            UPDATE Task
              SET IsCompleted = ? 
              WHERE TaskId = ?
            ''',params)
            self.showMenu()

        elif(self.command == "delete"):
            id = input("Enter the task id: ")
            params=(id,)
            delete_task('DELETE FROM Task WHERE TaskId=?',params)
            self.showMenu()

        elif(self.command == "exit"):
            print("Bye!")
            con.close()
            sys.exit()

        else:
            print("Invalid Command , Try again! \n")
            self.showMenu()
            
# calling the first time
Task().showMenu()











# import sys
# while True:
#     a = input("enter t")
#     print(a)
#     if(a=="exit"):
#         sys.exit()