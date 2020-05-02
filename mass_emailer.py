import _sqlite3
import smtplib
conn = _sqlite3.connect("mydatabase.db")
c = conn.cursor()
# c.execute("CREATE TABLE EMAILS (email text)")
print("........A MASS EMAILING SCRIPT IN PYTHON....................")
print("1.TO ADD A NEW USER\n2.TO REMOVE A USER\n3.To view all users\n4.To send Emails to all\n5.Remove all Users\n6.quit")


def send():
    email = input("Enter your email password\n")
    password = input("Enter the password of this email\n")
    print("Please wait as we try to send your mail\n")
    try:
        server = smtplib.SMTP("smtp.gmail.com", 587)
        server.starttls()
        server.login(email, password)
        body = "Hello world"
        receipents = select()
        totalusers = len(receipents)
        for x in range(totalusers):
            subscribers = receipents[x]
            server.sendmail("developerpetermwaura@gmail.com", subscribers[0], body)
        print("MESSAGE SUCCESSFULLY SENT")
    except Exception as e:
        print(e)


def removeall():
    with conn:
        command = "delete from emails"
        c.execute(command)
    print("All users  were  deleted ")

def addser():
    name = input("Enter the Email of the person to add\n")
    if name == "":
        print("Invalid name press 1 to try again\n")
    else:
        with conn:
            c.execute("insert into EMAILS values (:email)", {"email": name})
            print(f"{name} was successfully added\n")


def select():
    users = c.execute("select * from emails")
    emails = users.fetchall()
    return emails



def removeuser():
    with conn:
        name_to_remove = input("Enter the name of the person you wish to Remove\n")
        c.execute("Delete from emails where email = :email", {"email": name_to_remove})
        print(f"{name_to_remove} Has been removed from your users")


def viewall():
    print("The following people have subscribed to the services")
    users = select()
    totals = len(users)
    for x in range(totals):
        each  = users[x]
        print(each[0])




while True:
    try:
        choice = int(input(" > :"))
        if choice == 1:
            addser()
        elif choice == 2:
            removeuser()
        elif choice == 3:
            viewall()
        elif choice == 4:
            send()
        elif choice == 5:
            removeall()
        elif choice == 6:
            quit
        else:
            print("The choice is not available")
    except ValueError:
        print("THAT WAS AN INVALID CHOICE PLEASE TRY AGAIN")