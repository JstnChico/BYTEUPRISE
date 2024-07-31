import customtkinter
from tkinter import *
from tkinter import messagebox
import re

#Tkinter Window
app = customtkinter.CTk()
app.title('Chio Password Checker')
app.geometry('400x350+480+200')
app.config(bg='#000')
app.resizable(False, False)

#Fonts
title_font = ('Arial',20,'bold')
subtitle_font = ('Arial',17,'bold')
button_font = ('Arial',18,'bold')

#Suggestion
suggestion = ' '

#Password Function Conditions
def is_strong_password(password):
    global suggestion
    if len(password) < 8:
        suggestion = '*Password should be at least 8 characters long'
        return False
    
    if not re.search(r'[A-Z]', password):
        suggestion = '*Password should contain at least one uppercase letter'
        return False
    
    if not re.search(r'[a-z]', password):
        suggestion = '*Password should contain at least one lowercase letter'
        return False
    
    if not re.search(r'[0-9]', password):
        suggestion = '*Password should contain at least one digit'
        return False
    
    if not re.search(r'[!@#$%^&*()<>,.?":;{}_-]', password):
        suggestion = '*Password should contain at least one special character'
        return False
        
    suggestion = ' '
    return True
    

#Display Result Function
def display_password_result():
    password = password_text_box.get()
    if password:
        result_text_box.configure(state='normal')
        result_text_box.delete(0,END)

        if is_strong_password(password):
            result_text_box.insert(0, "Strong")
            result_text_box.configure(fg_color="#069602")
        else:
            result_text_box.insert(0, "Weak")
            result_text_box.configure(fg_color="#F00")

        result_text_box.configure(state='disabled')
        suggestion_label.configure(text=suggestion)
    
    else:
        messagebox.showerror(title='Error', message='Enter a Password to check.')

#Title Label
title_label = customtkinter.CTkLabel(app, text='CHIO PASSWORD CHECKER',font=title_font,text_color='#FFFFFF',bg_color='#000')
title_label.place(x=65,y=20)

#Password Entry Box
password_text_box = customtkinter.CTkEntry(app, font=subtitle_font,text_color='#fff', fg_color='#000',bg_color='#000',border_color='#00FF00',width=300,height=50)
password_text_box.place(x=50,y=60)

#Check Button
check_button = customtkinter.CTkButton(app,command=display_password_result, text='Check Password',font=button_font,text_color='#000000',fg_color='#00FF00', bg_color='#000',hover_color='#008000',cursor='hand2',corner_radius=20,width=150,height=40)
check_button.place(x=105,y=130)

#Strength Result Label
password_strength_label = customtkinter.CTkLabel(app, text='Your Password Strength',font=title_font,text_color='#FFFFFF',bg_color='#000')
password_strength_label.place(x=80,y=200)

#Strength Result
result_text_box = customtkinter.CTkEntry(app, state='disabled', font=subtitle_font,text_color='#FFF',fg_color='#000',bg_color='#000',border_color='#FFF',justify='center',width=200,height=30)
result_text_box.place(x=100,y=240)

#Suggestion Label
suggestion_label_frame = Frame(app, bg='#000')
suggestion_label_frame.place(x=0, y=300, width=400)
suggestion_label = customtkinter.CTkLabel(suggestion_label_frame, text=suggestion, font=('Arial', 15, 'bold'), text_color='#F00', bg_color='#000')
suggestion_label.pack(fill=BOTH, expand=True)

app.mainloop()