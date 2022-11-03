import json
from tkinter import *
import tkinter.messagebox as messagebox
import pyperclip

# To search info of name entered
def search():
    name = nameEntry.get().capitalize()

    # Checking if data.json file is present
    try:
        with open("data.json", mode="r") as dataFile:
            data = json.load(dataFile)
    except:
        data = {}

    # Checking if name is registered 
    try:
        info = data[name]
        pyperclip.copy(info["phone"])

        messagebox.showinfo("Information",f"Name: :{name}\nPhone no.: {info['phone']}\nEmail: {info['email']}\nOther: {info['other']}")
    except:
        messagebox.showerror("Not found","Not Found")

# to register new name(or update) and its info
def add():
    name = nameEntry.get().capitalize()
    phone = phoneEntry.get()
    email = emailEntry.get()
    other = otherEntry.get()

    # checking if data.json is present
    try:
        with open("data.json", mode="r") as dataFile:
            data = json.load(dataFile)
    except:
        data = {}

    # if name is not entered
    if (len(name) == 0):
        messagebox.showwarning(title="Fields are empty",
                               message="You have to write name of person.")
        return

    # if name has been already registered
    if(data.get(name)!=None):
        info=data[name]
        if(len(phone)==0):
            phone=info["phone"]
        if(len(email)==0):
            email=info["email"]
        if(len(other)==0):
            other=info["other"]
    else:
        if (len(phone) == 0):
            messagebox.showwarning(
                title="Fields are empty", message="You have to write phone number of person.")
            return

        try:
            int(phone)
        except:
            messagebox.showwarning(
                title="Fields are wrong", message="You have to write valid phone number of person.")
            return

    newData = {
        name:{
            "phone":phone,
            "email":email,
            "other":other
        }
    }

    data.update(newData)

    # checking if okay
    info = f"Name: {name}\nPhone no.: {phone}\nEmail: {email}\nOther: {other}"
    isOkay = messagebox.askyesno("You want ot save this ? ",info)

    # adding if okay
    if(isOkay):
        with open("data.json",mode="w") as df:
            json.dump(data,df,indent=4)
    else:
        return


# UI
main = Tk()
main.title("Contact Book")
main.configure(bg="#aef5be")
main.geometry("500x400")

logoImg = PhotoImage(file=r"phonebook.png")
canva = Canvas(width=100, height=100, highlightthickness=0, bg="#aef5be")
canva.create_image(50, 50, image=logoImg)
canva.place(x=200, y=10)

nameLabel = Label(master=main, text="Name:", font=(
    "bold", 15, ""), bg="#aef5be", fg="#334f3a")
nameLabel.place(x=10, y=140, width=100)

nameEntry = Entry(master=main, font=("", 12, ""))
nameEntry.place(x=100, y=140, width=280, height=32)

searchBt = Button(master=main, text="Search", font=(
    "", 15, ""), bg="#4a7ff0", fg="#fafafa", command=search)
searchBt.place(x=395, y=139, height=32, width=90)

phoneLabel = Label(master=main, text="Phone:", font=(
    "bold", 15, ""), bg="#aef5be", fg="#334f3a")
phoneLabel.place(x=10, y=192, width=100)

phoneEntry = Entry(master=main, font=("", 12, ""))
phoneEntry.place(x=100, y=192, width=380, height=32)

emailLabel = Label(master=main, text="Email:", font=(
    "bold", 15, ""), bg="#aef5be", fg="#334f3a")
emailLabel.place(x=10, y=244, width=100)

emailEntry = Entry(master=main, font=("", 12, ""))
emailEntry.place(x=100, y=244, width=380, height=32)

otherLabel = Label(master=main, text="Other:", font=(
    "bold", 15, ""), bg="#aef5be", fg="#334f3a")
otherLabel.place(x=10, y=298, width=100)

otherEntry = Entry(master=main, font=("", 12, ""))
otherEntry.place(x=100, y=298, width=380, height=32)

saveBt = Button(master=main, text="Save", font=(
    "", 15, ""), bg="#179c36", fg="#fafafa",command=add)
saveBt.place(x=200, y=350, width=100, height=40)

main.mainloop()
