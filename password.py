
from tkinter import *
from tkinter import messagebox
import pandas
from json import *
import random
import pyperclip
from pymongo import MongoClient
# ----------------------------------------- CONSTANTS ------------------------------------------------- #

web_ent=None
user_email_ent=None
pass_ent=None
g_pass=0000
dataBase = "Password_unite"
collectionName = "password"
Client=MongoClient("mongodb://localhost:27017/")
db=Client[dataBase]
collection=db[collectionName]

# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def passgenerator():
    """ No paramertres are required.
        This function gives gives the password (mixture of symbols, numbers, characters).
        Also prefered for on time use. 
    """
    global g_pass
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
    t=True
    lis=[]
    c1,c2,c3=0,0,0
    while t==True:
        i=random.randint(1,200)
        if i%3==0 and c3!=3:
            s1=random.randint(0,8)
            lis.append(symbols[s1])
            c3+=1
        elif i%2==0 and c2!=2 :
            n1=random.randint(0,9)
            lis.append(numbers[n1])
            c2+=1
        elif i%1==0 and c1!=6 :         
            l1=random.randint(0,51)
            lis.append(letters[l1])
            c1+=1
        if c1==6 and c2==2 and c3==3 :
            t=False        
    g_pass="".join(lis)
    pass_entry.insert(0, g_pass)
    # copy the password to clipboard for on time use.
    pyperclip.copy(g_pass)
    # paster the password to powershell window of compiler
    #pyperclip.paste(g_pass)

# ---------------------------- SEARCH PASSWORD ------------------------------- #

def search():
    """ No paramertres are required.
    searches the website name from the file. This is function is only avaliable for json format.  
    """
    
    
    global web_ent, user_email_ent, pass_ent
    web_ent=web_entry.get()
    see=web_ent
    email_add=None
    email_add=None
    
    result=collection.find_one({"Name":web_ent})
    print(result)
    if result==None:
        print(f" Entered website {see} isn't in repository ") 
    else:
        messagebox.showinfo(title=f" Detail of Website{see}" , message=f" Email/Username : {result["Email"]} \n Password : {result["password"]}")    
    
    # try :
    #     with open("./29 passwordsaver/passdata.json", mode="r") as json_obj:
    #         dic2=load(json_obj)    
            
    # except FileNotFoundError as error:
    #          messagebox.showerror(title=" Error", message=" No Password folder in Json format is avaliable")
            
    # else:
    #     try:
    #         flag=0
    #         for i in dic2:
            
    #             if see==i:
            
    #                 email_add=dic2[i]["email"]
    #                 email_pass=dic2[i]["password"]
    #                 flag=1
    #                 break
    #         if flag==0:
    #             raise ValueError
    #     except ValueError:
    #         print(f" Entered website {see} isn't in repository ")
    #     else:
    #         messagebox.showinfo(title=f" Detail of Website{see}" , message=f" Email/Username : {email_add} \n Password : {email_pass}") 
    # finally:
    #     # clearing the entry box after the search as been completed.
    #     web_entry.delete(0, END)
                                
# ---------------------------- SAVE PASSWORD ------------------------------- #

def add():
    
    """ No paramertres are required.
        This function add the Entry boxes details to file.
    """
    
    global web_ent, user_email_ent, pass_ent
    
    """
    #storing the data in the normal txt file format.
    
    with open("./29 passwordsaver/passdata.txt", mode="a") as addfile:
        addfile.writelines(f"{web_ent} | {user_email_ent} | {pass_ent} \n")
    
    """
    """
    #for storing in csv
    
    with open("./29 passwordsaver/passdata.csv", mode="a") as filecsv:
        flag=1
        with open("./29 passwordsaver/passdata.csv", mode="r") as test:
            pos=test.tell()
            if pos==0:
                flag=0           
        if flag==0:
            filecsv.write(" website , username , password \n") 
                  
        filecsv.write(f"{web_ent},{user_email_ent},{pass_ent}\n")
    
    """
    """
    # storing the data in json format for search purpose.
    
    new_dic={web_ent:
               { 
                "email":user_email_ent, "password":pass_ent
                }
            }
    
    with open("/Users/raman/Documents/python program/pythonProject/File_handling/Basic/29 passwordsaver/passdata.json", mode="r") as json_obj:
            dic=load(json_obj)    
            dic.update(new_dic)
            
    with open("/Users/raman/Documents/python program/pythonProject/File_handling/Basic/29 passwordsaver/passdata.json", mode="w") as j_obj:
            dump(dic, j_obj, indent=4)
    """
    
    #mongo db Client save
    collection.insert_one({
        "Name":web_ent,
        "email":user_email_entry,
        "password":pass_ent
    })        
                         
def save():
    """ No paramertres are required.
    This function saves the Entered data in the file and clears all the data entry from the entry boxes. 
    """
    global web_ent, user_email_ent, pass_ent, g_pass
    web_ent=web_entry.get()    
    user_email_ent=user_email_entry.get()
    pass_ent=pass_entry.get()
    
    p_l=len(pass_ent)
    w_l=len(web_ent)
    u_l=len(user_email_ent)
    
    is_length=True
    if p_l<1 or w_l<1 or u_l<1:
        is_length=False
        messagebox.showerror(title="Error", message=" You haven't filled up some details!!")        
    is_ok= messagebox.askokcancel(title={web_ent}, message=f"Are the entered details coreect:\n Username: {user_email_ent} \n password: {pass_ent}")
    if is_ok and is_length:
        messagebox.showinfo(title=" update ", message=" Data Added")
        
    collection.insert_one({
        "Name":web_ent,
        "email":user_email_ent,
        "password":pass_ent
    })
    
    # new_dic={web_ent:
    #            { 
    #             "email":user_email_ent, "password":pass_ent
    #            }
    #         }
    # try:
    #     with open("/Users/raman/Documents/python program/pythonProject/File_handling/Basic/29 passwordsaver/passdata.json", mode="r") as json_obj:
    #         dic=load(json_obj)    
    #         # the problem with load method is that if file is empty it show error
    #         dic.update(new_dic)
            
    #     with open("/Users/raman/Documents/python program/pythonProject/File_handling/Basic/29 passwordsaver/passdata.json", mode="w") as j_obj:
    #             dump(dic, j_obj, indent=4)
    # except FileNotFoundError: 
    #     with open("/Users/raman/Documents/python program/pythonProject/File_handling/Basic/29 passwordsaver/passdata.json", mode="w") as j_obj:
    #             dump(new_dic, j_obj, indent=4)
    
    
                   
    web_entry.delete(0, END)
    # user_email_entry.delete(0, END)
    pass_entry.delete(0, END)
    g_pass=0000
# ---------------------------- UI SETUP ------------------------------- #


window = Tk()
window.title("Password Saver")
window.config(padx=20, pady=20, bg="lightblue")

# Canvas for logo
image_name = PhotoImage(file="/Users/raman/Documents/python program/pythonProject/File_handling/Basic/29 passwordsaver/logo.png")
canvas = Canvas(height=200, width=240, bg="lightblue", highlightthickness=0)
canvas.create_image(120, 120, image=image_name)
canvas.grid(column=1, row=0, pady=10)

# Labels
website_label = Label(text="Website:", width=20, anchor="e", bg="lightblue", fg="black", font=("Arial", 12))
website_label.grid(column=0, row=1, padx=5, pady=5)

user_email_label = Label(text="Email/User Name:", width=20, anchor="e", bg="lightblue", fg="black", font=("Arial", 12))
user_email_label.grid(column=0, row=2, padx=5, pady=5)

pass_label = Label(text="Password:", width=20, anchor="e", bg="lightblue", fg="black", font=("Arial", 12))
pass_label.grid(column=0, row=3, padx=5, pady=5)

# Entries
web_entry = Entry(width=35)
web_entry.focus()
web_entry.grid(column=1, row=1, columnspan=2, sticky="ew", padx=5, pady=5)

user_email_entry = Entry(width=35)
user_email_entry.grid(column=1, row=2, columnspan=2, sticky="ew", padx=5, pady=5)
user_email_entry.insert(0, string="ramanred@gmail.com")

pass_entry = Entry(width=35, show="*")
pass_entry.grid(column=1, row=3, columnspan=2, sticky="ew", padx=5, pady=5)

# Buttons
search_button = Button(text="Search", command=lambda: print("Search clicked"), width=10, bg="gray", fg="white", font=("Arial", 10))
search_button.grid(column=2, row=1, sticky="e", padx=5)

generate_button = Button(text="Generate Password", command=lambda: print("Generate clicked"), bg="gray", fg="white", font=("Arial", 10))
generate_button.grid(column=2, row=3, sticky="ew", padx=5)

add_button = Button(text="ADD", width=35, command=lambda: print("Add clicked"), bg="green", fg="white", font=("Arial", 12, "bold"))
add_button.grid(column=1, row=4, columnspan=2, pady=10)

# Run the application
window.mainloop()




# window=Tk()
# window.config( padx=40, pady=40, bg="gray")
# # window.configure(width=240,  height=240)

# """ creating the GUI window components. """
                                                                                                                                                                                                                               
# image_name=PhotoImage(file="/Users/raman/Documents/python program/pythonProject/File_handling/Basic/29 passwordsaver/logo.png")
# canvas=Canvas( height=200, width=240, bg="gray", highlightthickness=0)
# canvas.create_image( 120, 120, image=image_name)
# canvas.grid(column=1, row=0)

# website_label=Label(text="WebSite :", width=20)
# website_label.grid(column=0, row=1)

# user_email_label=Label(text="Email/ User name :"  , width=20 ,  highlightthickness=1, fg="black" )
# user_email_label.grid(column=0, row=2)

# pass_label=Label(text="Password :", width=20)
# pass_label.grid(column=0, row=3)

# web_entry=Entry(width=47)
# web_entry.focus()
# web_entry.grid(column=1, row=1, columnspan=2)

# user_email_entry=Entry(width=45)
# user_email_entry.grid(column=1, row=2, columnspan=2, sticky="ew")
# user_email_entry.insert(0, string="ramanred@gmail.com")

# search_button=Button(text="Search", command=search, width= 6)
# search_button.grid(column=2, row=1, columnspan=1)

# pass_entry=Entry(width=48, textvariable=" enter your password", show="*")
# pass_entry.grid(column=1, row=3, columnspan=2)

# generate_button=Button(text="generate password", command=passgenerator)
# generate_button.grid(column=2, row=3, sticky="ew")

# add_button=Button( text="ADD", width=38, command=save)
# add_button.grid(column=1, row=4, columnspan=2, sticky="ew")

# #mainloop to main the GUI window. 

# window.mainloop()