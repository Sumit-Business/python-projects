from tkinter import *
root = Tk()

root.title("Calculator")
root.geometry("500x400")

memory = 0

entry = Entry(root, width = 15, font = ("Arial", 20), justify = "left")
entry.grid(row=0,column=0,columnspan=4)

def press(num):     
 entry.insert(END,num)

buttons = [
 "1","2","3","+",
 "4","5","6","-",
 "7","8","9","*",
 "0","=","%","/",
 "C","M+","M-","MRC"
]

def percentage():
  val = float(entry.get())
  resul = val/100
  entry.delete(0, END)
  entry.insert(END, resul)

def memory_add():
  global memory
  if entry.get().strip() == "": 
   return
  memory += float(entry.get())
  entry.delete(0, END)

def memory_sub():
  global memory
  if entry.get().strip() == "":
    return
  memory += float(entry.get())
  entry.delete(0, END)
def memory_recall():
  entry.delete(0, END)
  entry.insert(END, memory)

def calculate(event=None):
  try:
    expression = entry.get().replace('%', '/100')
    result = eval(expression)
    entry.delete(0, END)
    entry.insert(END, result)
  except:
   entry.delete(0, END)
   entry.insert(END, "Error")   

def clear():
  entry.delete(0, END)

row=1
col=0
for text in buttons:
 if text == "=":
    btn = Button(root, text=text, command=calculate)
 elif text == "C":
    btn = Button(root, text=text, command=clear)
 elif text == "%":
    btn = Button(root,text = text, command=percentage)
 elif text == "M+":
    btn = Button(root,text = text, command=memory_add)
 elif text == "M-":
    btn = Button(root,text = text, command= memory_sub)
 elif text == "MRC":
    btn = Button(root, text = text, command=memory_recall)   
 else:
    btn = Button(root, text=text, command=lambda t=text: press(t))
 btn.grid(row=row,column=col, sticky="nsew")
 col+=1
 if col > 3:
  col = 0
  row+=1

for i in range(6):   # rows
    root.grid_rowconfigure(i, weight=1)

for j in range(5):   # columns
    root.grid_columnconfigure(j, weight=1)

root.bind("<Return>", calculate)
root.bind("<Escape>", lambda event: clear())
root.mainloop()
