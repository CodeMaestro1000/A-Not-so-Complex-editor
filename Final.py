from test import *
import tkinter as tk
import os
import tkinter.messagebox
from tkinter import filedialog
from image import CreateToolTip


photo = None
photo1 = None
photo2 = None
photo3 = None
photo4 = None
photo5 = None
photo6 = None
photo7 = None
photo8 = None
photo9 = None
photo10 = None
photo11 = None
photo12 = None
photo13 = None
photo14 = None
photo15 = None
photo16 = None
photo17 = None
photo18 = None
photo19 = None
photo_x = None
photo_xx = None


class Editor(tk.Frame):
    def __init__(self, *args, **kwargs):
        tk.Frame.__init__(self, *args, **kwargs)
        root.title("Untitled - TXTeditor")
        root.geometry('700x600+200+60')
        root.iconbitmap(r'C:\Users\Ojotule\Downloads\logo.ico')
        self.text = CustomText(self)
        self.text.config(undo=tk.TRUE)
        self.text.config(wrap='none')
        self.vsb = tk.Scrollbar(orient="vertical", command=self.text.yview)
        self.hsb = tk.Scrollbar(self.text, orient="horizontal", command=self.text.xview)
        self.text.configure(yscrollcommand=self.vsb.set)
        self.text.configure(xscrollcommand=self.hsb.set)
        self.text.tag_configure("bigfont", font=("Helvetica", "24", "bold"))
        self.linenumbers = TextLineNumbers(self, width=30)
        self.linenumbers.config(background='lavender')
        self.linenumbers.attach(self.text)
        self.popup = tk.Menu(root, tearoff=0)
        self.vsb.pack(side="right", fill="y")
        self.hsb.pack(side=tk.BOTTOM, fill=tk.X)
        self.text.pack(side="right", fill="both", expand=True)
        self.status_frame = tk.Frame(root)
        self.status_frame.pack(side=tk.BOTTOM, fill=tk.X)
        self.status_bar1 = tk.Label(self.status_frame, text='Unsaved ', padx=2, anchor=tk.W)
        self.status_bar2 = tk.Label(self.status_frame, padx=2, anchor=tk.W)

        self.text.bind("<<Change>>", self._on_change)
        self.text.bind("<Configure>", self._on_change)
        self.text.bind("<Any-KeyPress>", self.content_update)
        self.text.bind("<Control-f>", self.create_search_window)
        self.text.bind("<Control-F>", self.create_search_window)
        self.text.bind("<Control-n>", lambda event: self.new_command())
        self.text.bind("<Control-N>", lambda event: self.new_command())
        self.text.bind("<Control-s>", lambda event: self.save_command())
        self.text.bind("<Control-S>", lambda event: self.save_command())
        self.text.bind("<Control-o>", lambda event: self.open_command())
        self.text.bind("<Control-O>", lambda event: self.open_command())
        self.text.bind("<Control-G>", lambda event: self.find_and_replace_window())
        self.text.bind("<Control-g>", lambda event: self.find_and_replace_window())
        self.text.bind("<Button-3>", self.do_pop_up)
        self.bind('<Alt-Key-F4>', self.exit_command)
        self.show_number = tk.IntVar()
        self.status_num = tk.IntVar()
        self.highlight = tk.IntVar()

        self.menu_bar()
        self.toolbar()

        self.file_name = ''
        self.save = 0
        self.a_file = None
        self.data = ''
        self.search_entry_id = tk.StringVar()
        self.find_var = tk.StringVar()
        self.replace_var = tk.StringVar()
        root.protocol('WM_DELETE_WINDOW', self.exit_command)

    def menu_bar(self):
        global photo, photo1, photo2, photo3, photo4, photo5, photo6, photo7, photo8, photo9, photo_x, photo_xx
        photo = tk.PhotoImage(file="Icons/newIcon.gif")
        photo1 = tk.PhotoImage(file="Icons/Save_24x24.png")
        photo2 = tk.PhotoImage(file='Icons/Open_24x24.png')
        photo3 = tk.PhotoImage(file='Icons/Delete_24x24.png')
        photo4 = tk.PhotoImage(file='Icons/Copy v2_24x24.png')
        photo5 = tk.PhotoImage(file='Icons/Cut_24x24.png')
        photo6 = tk.PhotoImage(file='Icons/Paste_24x24.png')
        photo7 = tk.PhotoImage(file='Icons/Undo_24x24.png')
        photo8 = tk.PhotoImage(file='Icons/Redo_24x24.png')
        photo9 = tk.PhotoImage(file='Icons/Information_24x24.png')
        photo_x = tk.PhotoImage(file='Icons/Find_24x24.png')
        photo_xx = tk.PhotoImage(file='Icons/replace.png')
        the_menu = tk.Menu()
        root.config(menu=the_menu)
        file_menu = tk.Menu(the_menu, tearoff=0)
        the_menu.add_cascade(label="File", menu=file_menu)
        file_menu.add_command(label="New", accelerator="Ctrl+N", compound='left', image=photo, command=self.new_command)
        file_menu.add_command(label="Open...", accelerator='Ctrl+O', compound='left', image=photo2, command=self.open_command)
        file_menu.add_command(label="Save", accelerator="Ctrl+S", compound='left', image=photo1, command=self.save_command)
        file_menu.add_command(label="Save As", compound='left', image=photo1, command=self.save_as_command)
        file_menu.add_separator()
        file_menu.add_command(label="Exit", compound='left', image=photo3, accelerator="Alt+F4", command=self.exit_command)

        edit_menu = tk.Menu(the_menu, tearoff=0)
        the_menu.add_cascade(label="Edit", menu=edit_menu)
        edit_menu.add_command(label="Copy", accelerator="Ctrl+C", compound='left', image=photo4, command=self.copy_command)
        edit_menu.add_command(label="Cut", accelerator="Ctrl+X", compound='left', image=photo5, command=self.cut_command)
        edit_menu.add_command(label="Paste", accelerator="Ctrl+V", compound='left', image=photo6, command=self.paste_command)
        edit_menu.add_separator()
        edit_menu.add_command(label="Undo", accelerator="Ctrl+Z", compound='left', image=photo7, command=self.undo_command)
        edit_menu.add_command(label="Redo", accelerator="Ctrl+Y", compound='left', image=photo8, command=self.redo_command)
        edit_menu.add_separator()
        edit_menu.add_command(label="Search", accelerator="Ctrl+F", compound='left', image=photo_x, command=self.create_search_window)
        edit_menu.add_command(label="Find and Replace", accelerator="Ctrl+G", compound='left', image=photo_xx, command=self.find_and_replace_window)
        view_menu = tk.Menu(the_menu, tearoff=0)
        the_menu.add_cascade(label="View", menu=view_menu)
        view_menu.add_checkbutton(label="Show Line Number", variable=self.show_number, command=self.show_line_numbers)
        view_menu.add_checkbutton(label="Show Status bar", variable=self.status_num, command=self.show_status_bar)
        view_menu.add_checkbutton(label="Highlight Current Line", variable=self.highlight, command=self.toggle_highlight)
        help_menu = tk.Menu(the_menu, tearoff=0)
        the_menu.add_cascade(label="Help", menu=help_menu)
        help_menu.add_command(label="About", command=self.gui_info, compound='left', image=photo9)
        self.popup.add_command(label="New", compound=tk.LEFT, accelerator="Ctrl+N", command=self.new_command, image=photo)
        self.popup.add_command(label="Save", compound=tk.LEFT, accelerator="Ctrl+S", command=self.save_command, image=photo1)
        self.popup.add_command(label="Open", compound=tk.LEFT, accelerator="Ctrl+O", command=self.open_command, image=photo2)
        self.popup.add_separator()
        self.popup.add_command(label="Copy", compound=tk.LEFT, accelerator="Ctrl+C", command=self.copy_command, image=photo4)
        self.popup.add_command(label="Cut", compound=tk.LEFT, accelerator="Ctrl+X", command=self.cut_command, image=photo5)
        self.popup.add_command(label="Paste", compound=tk.LEFT, accelerator="Ctrl+V", command=self.paste_command, image=photo6)
        self.popup.add_command(label="Undo", compound=tk.LEFT, accelerator="Ctrl+Z", command=self.undo_command, image=photo7)
        self.popup.add_command(label="Redo", compound=tk.LEFT, accelerator="Ctrl+Y", command=self.redo_command, image=photo8)
        self.popup.add_command(label="Search", compound=tk.LEFT, accelerator="Ctrl+F", command=self.create_search_window, image=photo_x)
        self.popup.add_command(label="Find and Replace", compound=tk.LEFT, accelerator="Ctrl+G",
                               command=self.find_and_replace_window, image=photo_xx)
        self.popup.add_separator()
        self.popup.add_command(label="About", compound=tk.LEFT, command=self.gui_info, image=photo9)
        self.popup.add_separator()
        self.popup.add_command(label="Exit", compound=tk.LEFT, accelerator="Alt+F4", command=self.exit_command, image=photo3)

    def toolbar(self):
        global photo10, photo11, photo12, photo13, photo14, photo15, photo16, photo17, photo18, photo19
        frame = tk.Frame(root, height=30, bg='white', bd=1, relief=tk.FLAT, background='AntiqueWhite1')
        photo10 = tk.PhotoImage(file="Icons/New_24x24.png")
        button = tk.Button(frame, image=photo10, command=self.new_command)
        photo11 = tk.PhotoImage(file="Icons/Open_24x24.png")
        button1 = tk.Button(frame, image=photo11, command=self.open_command)
        photo12 = tk.PhotoImage(file="Icons/Save_24x24.png")
        button2 = tk.Button(frame, image=photo12, command=self.save_command)
        photo13 = tk.PhotoImage(file="Icons/Copy v2_24x24.png")
        button3 = tk.Button(frame, image=photo13, command=self.copy_command)
        photo14 = tk.PhotoImage(file="Icons/Cut_24x24.png")
        button4 = tk.Button(frame, image=photo14, command=self.cut_command)
        photo15 = tk.PhotoImage(file="Icons/Paste_24x24.png")
        button5 = tk.Button(frame, image=photo15, command=self.paste_command)
        photo16 = tk.PhotoImage(file="Icons/Undo_24x24.png")
        button6 = tk.Button(frame, image=photo16, command=self.undo_command)
        photo17 = tk.PhotoImage(file="Icons/Redo_24x24.png")
        button7 = tk.Button(frame, image=photo17, command=self.redo_command)
        photo18 = tk.PhotoImage(file='Icons/Find_24x24.png')
        button8 = tk.Button(frame, image=photo18, command=self.create_search_window)
        photo19 = tk.PhotoImage(file='Icons/high.png')
        button9 = tk.Button(frame, image=photo19, command=self.toggle_highlight_button)
        frame.pack(side=tk.TOP, expand=tk.FALSE, fill=tk.X)
        button.pack(side=tk.LEFT, padx=5)
        button1.pack(side=tk.LEFT, padx=5)
        button2.pack(side=tk.LEFT, padx=5)
        button3.pack(side=tk.LEFT, padx=5)
        button4.pack(side=tk.LEFT, padx=5)
        button5.pack(side=tk.LEFT, padx=5)
        button6.pack(side=tk.LEFT, padx=5)
        button7.pack(side=tk.LEFT, padx=5)
        button8.pack(side=tk.LEFT, padx=5)
        button9.pack(side=tk.LEFT, padx=5)
        CreateToolTip(button, "New File")
        CreateToolTip(button1, "Open")
        CreateToolTip(button2, "Save")
        CreateToolTip(button3, "Copy")
        CreateToolTip(button4, "Cut")
        CreateToolTip(button5, "Paste")
        CreateToolTip(button6, "Undo")
        CreateToolTip(button7, "Redo")
        CreateToolTip(button8, "Find Text")
        CreateToolTip(button9, "Toggle Highlight")

    def get_text_data(self):
        data = self.text.get('1.0', tk.END + '-1c')
        return data

    def content_update(self, event=None):
        self.update_cursor_info()

    def _on_change(self, event):
        self.linenumbers.redraw()

    def show_line_numbers(self):
        line_info = self.show_number.get()
        if line_info:
            self.linenumbers.pack(side="left", fill="y")

        else:
            self.linenumbers.pack_forget()

    def open_command(self):
        a_file = filedialog.askopenfile(parent=root, mode="r", title="Select a file to open",
                                        filetype=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if a_file is not None:
            file_content = a_file.read()
            self.text.insert(1.0, file_content)
            a_file.close()
            full_path = os.path.basename(str(a_file))
            num = full_path.find(".")
            text = full_path[0:num]
            root.title(str(text) + "-TXTeditor")
            root.title(os.path.basename(text) + " -TXTeditor")

    def save_command(self):
        save_text = self.file_name + '.txt'
        if self.save == 1:
            self.a_file = open(save_text, 'w')
            self.data = self.get_text_data()
            self.a_file.write(self.data)
            self.a_file.close()
            self.data = ''
            self.show_status_bar()
        else:
            self.save_as_command()

    def save_as_command(self):
        self.a_file = filedialog.asksaveasfile(parent=root, mode="w", title="Save file", initialfile='Untitled'
                                                                                                     '.txt',
                                               defaultextension=".txt",
                                               filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt"), ("HTML file", "*.html")])

        if self.a_file:
            self.data = self.get_text_data()
            self.a_file.write(self.data)
            self.a_file.close()
            self.save = 1
            full_path = os.path.basename(str(self.a_file))
            num = full_path.find(".")
            self.file_name = full_path[0:num]
            root.title(str(self.file_name) + "-TXTeditor")
            self.show_status_bar()

    def show_status_bar(self):
        status_info = self.status_num.get()
        if status_info:
            if self.save > 0:
                self.status_bar1.config(text='Saved')
                self.status_bar1.pack(side=tk.LEFT, fill=tk.X)
            else:
                self.status_bar1.pack(side=tk.LEFT, fill=tk.X)

            self.status_bar2.pack(side=tk.RIGHT)
            self.update_cursor_info()
        else:
            self.status_frame.pack_forget()

    def update_cursor_info(self):
        row, col = self.text.index(tk.INSERT).split('.')
        line_num, col_num = str(int(row)), str(int(col) + 1)
        cursor_info = 'Line: {} | Column: {}'.format(line_num, col_num)
        self.status_bar2.config(text=cursor_info)

    def new_command(self):
        old_data = self.get_text_data()
        if old_data != '':
            exit_ask = tkinter.messagebox.askyesnocancel('Quit', 'Do you want to save changes?')
            if exit_ask is True:
                self.save_command()
            else:
                if exit_ask is None:
                    pass
                else:
                    a_file = None
                    self.text.delete(1.0, tk.END)

        else:
            a_file = None
            self.text.delete(1.0, tk.END)
        root.title("Untitled - TXTeditor")
        self.save = 0

    def exit_command(self):
        if self.save == 0:
            if tkinter.messagebox.askyesno('Quit', 'The Current file has not been saved \n Do you want to Exit'):
                root.destroy()
        else:
            self.save_changes()

    def save_changes(self):
        temp_data = self.get_text_data()
        if self.data != temp_data:
            exit_ask = tkinter.messagebox.askyesnocancel('Quit', 'Do you want to save changes?')
            if exit_ask is True:
                self.save_command()
            else:
                if exit_ask is None:
                    pass
                else:
                    root.destroy()
        else:
            root.destroy()

    def cut_command(self):
        self.text.event_generate("<<Cut>>")
        self.content_update()
        return "break"

    def copy_command(self):
        self.text.event_generate("<<Copy>>")
        self.content_update()
        return "break"

    def paste_command(self, event=None):
        paste_text = self.selection_get(selection="CLIPBOARD")
        self.text.insert('insert', paste_text)

    def undo_command(self):
        self.text.event_generate("<<Undo>>")
        self.content_update()
        return "break"

    def redo_command(self, event=None):
        self.text.event_generate("<<Redo>>")
        self.content_update()
        return "break"

    def create_search_window(self, event=None):
        self.search_window = tk.Toplevel(root)
        self.search_window.geometry('250x70+300+300')
        self.search_window.title('Find Text')
        self.search_window.transient(root)
        label = tk.Label(self.search_window, text='Find All: ')
        label.pack(side=tk.LEFT)
        search_entry = tk.Entry(self.search_window, textvariable=self.search_entry_id, width=25)
        search_entry.pack(side=tk.LEFT)
        search_button = tk.Button(self.search_window, text='Find')
        search_button.pack(side=tk.LEFT, padx=2)
        search_button.bind('<Button-1>', self.search_command)
        self.search_window.protocol('WM_DELETE_WINDOW', self.close_search_window)

    def search_command(self, event=None):
        self.text.tag_remove('highlight', '1.0', tk.END)
        self.a_string = self.search_entry_id.get()
        matches = 0
        if self.a_string:
            start_pos = '1.0'
            while True:
                search_var = self.text.search(self.a_string, start_pos, stopindex=tk.END)
                if not search_var:
                    break
                end_pos = '{}+{}c'.format(search_var, len(self.a_string))
                self.text.tag_add('highlight', search_var, end_pos)
                start_pos = end_pos
                matches += 1
                search_var = self.text.search(self.a_string, start_pos, stopindex=tk.END)
            self.text.tag_config('highlight', foreground='red', background='yellow')
        self.search_window.title('{} matches found'.format(matches))
        matches = 0

    def close_search_window(self):
        self.text.tag_remove('highlight', '1.0', tk.END)
        self.search_window.destroy()
        return 'break'

    def find_and_replace_window(self):
        self.replace_window = tk.Toplevel(root)
        self.replace_window.geometry('250x76+300+300')
        self.replace_window.title('Find and replace')
        self.replace_window.transient(root)

        label = tk.Label(self.replace_window, text='Replace: ', anchor=tk.E)
        label.grid(row=0, column=0)
        search_entry = tk.Entry(self.replace_window, textvariable=self.find_var, width=25)
        search_entry.grid(row=0, column=1, padx=2)
        label = tk.Label(self.replace_window, text='With: ', pady=2)
        label.grid(row=1, column=0)
        search_entry1 = tk.Entry(self.replace_window, textvariable=self.replace_var, width=25)
        search_entry1.grid(row=1, column=1, pady=2)
        search_button = tk.Button(self.replace_window, text='Replace')
        search_button.grid(row=3, column=1, pady=2)
        search_button.bind('<Button-1>', self.replace_command)

    def replace_command(self, event=None):
        text = self.text.get('1.0', tk.END)
        og_string = self.find_var.get()
        rep_string = self.replace_var.get()
        self.text.tag_config('highlight', foreground='white', background='blue')
        self.text.delete("1.0", tk.END)
        self.text.insert(tk.END, text.replace(og_string, rep_string))
        start_pos = '1.0'
        while True:
            search_var = self.text.search(rep_string, start_pos, stopindex=tk.END)
            if not search_var:
                break
            end_pos = '{}+{}c'.format(search_var, len(rep_string))
            self.text.tag_add('highlight', search_var, end_pos)
            start_pos = end_pos

    def do_pop_up(self, event):
        try:
            self.popup.tk_popup(event.x_root, event.y_root, 0)
        finally:
            self.popup.grab_release()

    def highlight_line(self, interval=1000):
        self.text.tag_remove("active_line", 1.0, "end")
        self.text.tag_add("active_line", "insert linestart", "insert lineend + 1c")
        self.text.tag_configure("active_line", background="ivory2")
        self.text.after(interval, self.toggle_highlight)

    def toggle_highlight(self, event=None):
        val = self.highlight.get()
        self.undo_highlight() if not val else self.highlight_line()

    def toggle_highlight_button(self, event=None):
        self.highlight_line()
        self.highlight.set(1)

    def undo_highlight(self):
        self.text.tag_remove("active_line", 1.0, "end")

    @staticmethod
    def gui_info():
        tkinter.messagebox.showinfo("About TXTeditor", "The Very First GUI \n Created in 2019 \n By Akoji Timothy")


if __name__ == "__main__":
    root = tk.Tk()
    Editor(root).pack(side="top", fill="both", expand=True)
    root.mainloop()
