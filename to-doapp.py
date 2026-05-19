from tkinter import *
from tkinter import messagebox
root = Tk()
root.title("To-Do App")

root.geometry("500x500")

entry = Entry(root)
entry.pack()
    
listbox = Listbox(root)
listbox.pack()

def add_task(event=None):
    get = entry.get()
    if get.strip() == "":
     messagebox.showwarning("Worng input","please enter your task")
    else:
     listbox.insert(END, get)
     entry.delete(0, END)

def del_task():
    selected = listbox.curselection()
    if selected == ():
      messagebox.showerror("Wrong input", "Select something to delete")
    else:
      listbox.delete(selected[0])


def mark_compl():
   select = listbox.curselection() 
   if select == ():
      messagebox.showerror("Wrong input", "Select something first")
   else:
      task = listbox.get(select[0])
      
      if task.startswith("✔"):
         return
   
      listbox.delete(select[0])
      listbox.insert(select[0], "✔" + task)


button = Button(root, text="Add", command=add_task)
button.pack()
button1 = Button(root,text = "Delete", command = del_task)
button2 = Button(root,text = "done", command = mark_compl)
button1.pack()
button2.pack()
root.bind("<Return>", add_task)
root.mainloop()

