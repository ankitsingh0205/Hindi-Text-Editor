from tkinter import*
#from tkinter import messagebox
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import Label, ttk

#import console
import os,sys
import win32api
import win32print


root = Tk()
root.title(' Editor.com - Text!')
root.iconbitmap("H:\Ankit\EditorText.py")
root.geometry("1200x660")
                
#Set variable for open file name
global open_status_name
open_status_name = False

global selected
selected = False
# Create New File Function
def new_file():
    # Delete previous text
     my_text.delete("1.0",END)
     # Update status bars
     root.title('New File - Textpaid!')
     status_bar.config(text="New File      ")
     
     global open_status_name
     open_status_name = False

     
# Open Files
def open_file():
    #Delete previous text
    my_text.delete("1.0",END)


    # Grab Filename
    text_file = filedialog.askopenfilename(title = "Select file",filetypes = (("All Files","*.*"),("Text Files","*.txt"),("Python Files","*.py")))
    # Check to see if there is a file name
    if text_file:
    # Make filename global so we can access it later
      global open_status_name
      open_status_name = text_file
    # Update Status bars 
      name = text_file
      status_bar.config(text=f'Saved:{name}        ')
      name = name.replace("H:/Ankit/","")
      root.title(f'{name} -Textpad!')

    # Open the file
      text_file = open(text_file,'r')
      stuff = text_file.read()

    # Add file to textbox
      my_text.insert(END,stuff)
    # Close the opened file
      text_file.close()

# Save As File
def save_as_file():
    text_file = filedialog.asksaveasfilename(defaultextension=".*",initialdir="H:/Ankit\python.py",title="Save File",filetype=(("Text Files","*,txt"),("HTML Files","*.html"),("Python files","*.py"),("All Files","*.*")))
    if text_file:
          # Update Status Bars
          name = text_file
          status_bar.config(text=f'{name}        ')
          name = name.replace("H:/Ankit/","")
          root.title(f'{name} -Textpad!')

          # Save the file
          text_file=open(text_file,'r')
          text_file.write(my_text.get(1.0,END))
          # Close the file
          text_file.close()

# Save File
def save_file():
    global open_status_name
    if open_status_name:
        # Save the file
          text_file=open(open_status_name,'w')
          text_file.write(my_text.get(1.0,END))
          # Close the file
          text_file.close()
          
          # Put status update or popup code
          status_bar.config(text=f'Saved:{open_status_name}      ')
    else:
          save_as_file()
# Cut Text
def cut_text(e):
        global selected
        #Check to see if keyboard shortcut used
        if e:
            selected =root.clipboard_get()
        else:
            if my_text.selection_get():
            # Grab selected text from text box
             selected =my_text.selection_get()
            # Delete Selected Text from text box
            my_text.delete("sel.first","se;.last")
            # Clear the clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)
# Copy Text
def copy_text(e):
        global selected
        # Check to see if keyboard shortcut used
        if e:
             selected =root.clipboard_get()
        #else:
        if my_text.selection_get():
            # Grab selected text from text box
            selected =my_text.selection_get()
            # Clear the clipboard then append
            root.clipboard_clear()
            root.clipboard_append(selected)
            # Delete Selected Text from text box
            my_text.delete("sel.first","se;.last")
# Paste Text
def paste_text(e):
        global selected
        # Check to see if keyboard shutcut used
        if e:
            selected = root.clipboard_get()
        else:
             if selected:
                position = my_text.index(INSERT)
                my_text.insert(position,selected)
             
            # Clear the clipboard then append
             root.clipboard_clear()
             root.clipboard_append(selected)

#Bold Text
def bold_it():
    # Create our font
    bold_font = font.Font(my_text,my_text.cget("font"))
    bold_font.configure(weight="bold")

    # configure a tag
    my_text.tag_configure("bold",font=bold_font)

    # Define Current tags
    current_tags = my_text.tag_names("sel.first")
      
    # If statement to see if tag has been set
    if"bold" in current_tags:
        my_text.tag_remove("bold","sel.first","sel.last")
    else:
          my_text.tag_add("bold","sel.first","sel.last")

#Italic Text
def Italics_it():
     # Create our font
    Italics_font = font.Font(my_text,my_text.cget("font"))
    Italics_font.configure(slant="italic")

    # configure a tag
    my_text.tag_configure("italic",font=Italics_font)
    # Define Current tags
    current_tags = my_text.tag_names("sel.first")

# If statement to see if tag has been set
    if"italic" in current_tags:
        my_text.tag_remove("italic","sel.first","sel.last")
    else:
          my_text.tag_add("italic","sel.first","sel.last")

# Change Selected  Text Color
def text_color():
     # Pick a color
     my_color = colorchooser.askcolor()
     status_bar.config(text=my_color)
    # Create our font
     color_font = font.Font(my_text, my_text.cget("font"))
     color_font.cofigure(slant="italic")

    # configure a tag
     my_text.tag_configure("colored",font=color_font,foreground=my_color)

    # Define Current tags
     current_tags = my_text.tag_names("sel.first")

   # If statement to see if tag has been set
     if"colored" in current_tags:
        my_text.tag_remove("colored","sel.first","sel.last")
     else:
      my_text.tag_add("colored","sel.first","sel.last")

def find_func(self):
     def tk_toplevel(master):
        findandreplace = tk.Toplevel(master)
        findandreplace.title('Find & Replace')

        find_label = tk.Label(findandreplace, text='Find')
        find_label.pack(side = tk.LEFT) 
        find_words = tk.StringVar()
        find_entry = tk.Entry(findandreplace, textvariable=find_words)
        find_entry.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)

        find_button = tk.Button(findandreplace, text='Find', command=self.find)
        find_button.pack(side = tk.LEFT)

        replace_label = tk.Label(findandreplace, text='Replace')
        replace_label.pack(side = tk.LEFT) 
        replace_words = tk.StringVar()
        replace_entry = tk.Entry(findandreplace, textvariable=replace_words)
        replace_entry.pack(side = tk.LEFT, fill = tk.BOTH, expand = 1)
        
        replace_button = tk.Button(findandreplace, text='Replace', command=self.replace)
        replace_button.pack(side = tk.LEFT)

        find_string = find_words.get()
        replace_string = replace_words.get()

        return find_string, replace_string

def find(self):
        self.textarea.tag_remove('found', '1.0', tk.END)
        find_word = self.find_and_replace()[0]
        if find_word:
            idx = '1.0'
            while True:
                idx = self.textarea.search(find_word, idx, nocase=1,
                                            stopindex=tk.END)

                if not idx:
                    break

                lastidx = '% s+% dc' % (idx, len(find_word))
                idx = lastidx
            self.textarea.tag_config('found', foreground='red')
    
def replace(self):
        self.textarea.tag_remove('found', '1.0', tk.END)
        find_word = self.find_and_replace()[0]
        replace_word = self.find_and_replace()[1]

        if find_word and replace_word:
            idx = '1.0'
            while True:
                idx = self.textarea.search(find_word, idx, nocase=1,
                                            stopindex=tk.END)
                if not idx:
                    break

                lastidx = '% s+% dc' % (idx, len(find_word))
                self.textarea.delete(idx, lastidx)
                self.textarea.insert(idx, replace_word)

                lastidx = '% s+% dc' % (idx, len(replace_word))
                idx = lastidx
            self.textarea.tag_config('found', foreground='green', background='yellow')



# Change bg color
def bg_color():
       my_color = colorchooser.askcolor()[1]
       if my_color:
           my_text.config(bg=my_color)
# Change All Text Color
def all_text_color():
     my_color = colorchooser.askcolor()[1]
     if my_color:
           my_text.config(fg=my_color)

# Print File Function
def print_file():
     printer_name = win32print.GetDefaultPrinter()
     status_bar.config(text=printer_name)
     # Grab Filename
     file_to_print = filedialog.askopenfilename(initialdir="H:/Ankit/",title=("open File"),filetypes=(("Text Files", "*.txt"),("HTML Files","*.html"),("Python Files","*.py"),("All files","*.*")))

     if file_to_print:
        win32api.ShellExecute(0,"print",file_to_print,None,".",0)
     

#Create a toolbar Frame
toolbar_frame = Frame(root)
toolbar_frame.pack(fill=X)

#create main Frame
my_frame = Frame(root)
my_frame.pack(pady=20)

# Create our scrollbar For the Text Box
text_scroll = Scrollbar(my_frame)
text_scroll.pack(side=RIGHT,fill=Y)

#Horizontal Scrollbar
hor_scroll = Scrollbar(my_frame,orient='horizontal')
hor_scroll.pack(side=BOTTOM,fill=X)

#Create Text Box
my_text = Text(my_frame,width=125,height=30,font=("Regular",15),selectbackground="yellow",selectforeground="black",undo=True,yscrollcommand=text_scroll.set,wrap="none",xscrollcommand=hor_scroll.set)
my_text.pack()

#configure our Scrollbar
text_scroll.config(command=my_text.yview)
hor_scroll.config(command=my_text.xview)
# Create Menu
my_menu = Menu(root)
root.config(menu=my_menu)

#Add File Menu
file_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="File",menu=file_menu)
file_menu.add_command(label="New",command=new_file)
file_menu.add_command(label="Open",command=open_file)
file_menu.add_command(label="Save",command=save_file)
file_menu.add_command(label="Save As",command=save_as_file)
file_menu.add_separator()
file_menu.add_command(label="Print File",command=print_file)
file_menu.add_separator()
file_menu.add_command(label="Exit",command=root.quit)

# Add Edit Meu                      
edit_menu = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Edit",menu=edit_menu)
edit_menu.add_command(label="Cut",command=lambda: cut_text(False),accelerator="(Ctrl+x)")
edit_menu.add_command(label="Copy" ,command=lambda: copy_text(False),accelerator="(Ctrl+c)")
edit_menu.add_command(label="Paste"        ,command=lambda: paste_text(False),accelerator="(Ctrl+V)")
edit_menu.add_separator()
edit_menu.add_command(label="Undo",command=my_text.edit_undo ,accelerator="(Ctrl+z)")
edit_menu.add_command(label="Redo",command=my_text.edit_redo,accelerator="(Ctrl+y)")
edit_menu.add_separator()
edit_menu.add_command(label="Find",command=find_func)     
edit_menu.add_command(label="Replace",command=find_func)
# Add Find Menu
find_func_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Find",menu=find_func_menu)
find_func_menu.add_command(label="Find... ",command=find_func)
find_func_menu.add_command(label="Find Next ",command=find_func)
find_func_menu.add_command(label="Find Previous ",command=find_func)
find_func_menu.add_command(label="Replace",command=find_func)

# Add Colour Menu
color_menu = Menu(my_menu,tearoff=False)
my_menu.add_cascade(label="Colors",menu=color_menu)
color_menu.add_command(label="Selected Text",command=text_color)
color_menu.add_command(label="All Text",command= all_text_color)
color_menu.add_command(label="Background",command=bg_color)

# Add Status Bar To Bottom Of App
status_bar = Label(root,text='Ready        ',anchor=E)
status_bar.pack(fill=X,side=BOTTOM,ipady=5)

# Edit Binding
root.bind('<Control-Key-x>',cut_text)
root.bind('<Control-Key-c>',copy_text)
root.bind('<Control-Key-v>',paste_text)
root.bind('<Control-Key-F>',find_func)

fee ="AnkitSingh"
my_label = Label(root,text=fee[:-1]).pack()


# Create Button

# Bold Button
bold_button = Button(toolbar_frame,text="Bold",command=bold_it)
bold_button.grid(row=0,column=0,sticky=W,padx=5)

# Italic Button
Italics_button = Button(toolbar_frame,text="Italics",command=Italics_it)
Italics_button.grid(row=0,column=1,padx=5)

# Undo /Redo Buttoms
Undo_button = Button(toolbar_frame,text="Undo",command=my_text.edit_undo)
Undo_button.grid(row=0,column=2,padx=5)
Redo_button = Button(toolbar_frame,text="Redo",command=my_text.edit_redo)
Redo_button.grid(row=0,column=3,padx=5)

# Text Color
color_text_button = Button(toolbar_frame,text="Text Color",command=text_color)
color_text_button.grid(row=0,column=4,padx=5)


root.mainloop()
                      
