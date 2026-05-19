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




#For website





# from flask import Flask, request, render_template_string

# app = Flask(__name__)

# memory = 0

# @app.route("/", methods=["GET", "POST"])
# def home():
#     global memory
#     result = ""
#     expression = ""

#     if request.method == "POST":
#         expression = request.form.get("expression")
#         action = request.form.get("action")

#         try:
#             if action == "=":
#                 expression = expression.replace('%', '/100')
#                 result = eval(expression)

#             elif action == "C":
#                 result = ""

#             elif action == "%":
#                 result = float(expression) / 100

#             elif action == "M+":
#                 if expression.strip() != "":
#                     memory += float(expression)
#                 result = expression

#             elif action == "M-":
#                 if expression.strip() != "":
#                     memory -= float(expression)
#                 result = expression

#             elif action == "MRC":
#                 result = memory

#             else:
#                 result = expression

#         except:
#             result = "Error"

#     return render_template_string("""
#     <html>
#     <head>
#         <title>Calculator</title>
#     </head>
#     <body>
#         <h2>Calculator </h2>
#         <form method="POST">
#             <input type="text" name="expression" value="{{result}}" style="width:200px;height:40px;font-size:20px;"><br><br>
            
#             {% for row in buttons %}
#                 {% for btn in row %}
#                     <button name="action" value="{{btn}}" style="width:50px;height:50px;font-size:18px;">{{btn}}</button>
#                 {% endfor %}
#                 <br>
#             {% endfor %}
#         </form>
#     </body>
#     </html>
#     """, result=result, buttons=[
#         ["1","2","3","+"],
#         ["4","5","6","-"],
#         ["7","8","9","*"],
#         ["0","=","%","/"],
#         ["C","M+","M-","MRC"]
#     ])

# if __name__ == "__main__":
#     app.run(debug=True)