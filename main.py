from tkinter import *
import mysql.connector
from PIL import ImageTk, Image
import tkinter as tk
from tkinter import ttk

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="db_tp3dpbo"
)

dbcursor = mydb.cursor()

root = Tk()
root.title("Praktikum DPBO")

def getGender():
    global mydb
    global dbcursor

    dbcursor.execute("SELECT gender FROM mahasiswa")
    result = dbcursor.fetchall()

    return result
# Fungsi untuk mengambil data
def getMhs():
    global mydb
    global dbcursor

    dbcursor.execute("SELECT * FROM mahasiswa")
    result = dbcursor.fetchall()

    return result


# Window Input Data
def inputs():
    # Hide root window
    global root
    root.withdraw()

    top = Toplevel()
    top.title("Input")
    dframe = LabelFrame(top, text="Input Data Mahasiswa", padx=10, pady=10)
    dframe.pack(padx=10, pady=10)
    # Input 1
    label1 = Label(dframe, text="Nama Mahasiswa").grid(row=0, column=0, sticky="w")
    input_nama = Entry(dframe, width=30)
    input_nama.grid(row=0, column=1, padx=20, pady=10, sticky="w")
    # Input 2
    label2 = Label(dframe, text="NIM").grid(row=1, column=0, sticky="w")
    input_nim = Entry(dframe, width=30)
    input_nim.grid(row=1, column=1, padx=20, pady=10, sticky="w")
    # Input 3
    
    options = ["Filsafat Meme", "Sastra Mesin", "Teknik Kedokteran", "Pendidikan Gaming"]
    input_jurusan = StringVar(root)
    input_jurusan.set(options[0])
    label4 = Label(dframe, text="Jurusan").grid(row=2, column=0, sticky="w")
    input4 = OptionMenu(dframe, input_jurusan, *options)
    input4.grid(row=2, column=1, padx=20, pady=10, sticky='w')
    #input 4
    label5 = Label(dframe, text="Gender").grid(row=3, column=0, sticky="w")
    GENDEROPTION = [
    ("Laki-laki", "Laki-laki"),
    ("Perempuan", "Perempuan")
    ]
    gender = StringVar();
    gender.set("Laki-laki")
    iterasi = 0
    for text, genders, in GENDEROPTION:
        input5 = Radiobutton(dframe, text=text, variable=gender, value=genders).grid(row=3+iterasi, column=1, padx=20, pady=10, sticky='w')
        
        iterasi+=1
    # Input 5
    label6 = Label(dframe, text="Hobi").grid(row=6, column=0, sticky="w")
    n = tk.StringVar()
    hobiCombo = ttk.Combobox(dframe, width = 27, textvariable = n)
    hobiCombo['values'] = ("Bernyanyi", "Main Game", "Olah Raga", "Tidur", "Menulis")
    hobiCombo.current(2)
    hobiCombo.grid(row=6, column=1, padx=20, pady=10, sticky='w')
    
    # Button Frame
    frame2 = LabelFrame(dframe, borderwidth=0)
    frame2.grid(columnspan=2, column=0, row=10, pady=10)

    # Submit Button
    
    btn_submit = Button(frame2, text="Submit Data", anchor="s", command=lambda:[insertData(top, input_nama, input_nim, input_jurusan, gender.get(), hobiCombo.get()), top.withdraw()])
    btn_submit.grid(row=3, column=0, padx=10)

    # Cancel Button
    btn_cancel = Button(frame2, text="Gak jadi / Kembali", anchor="s", command=lambda:[top.destroy(), root.deiconify()])
    btn_cancel.grid(row=3, column=1, padx=10)

# Untuk memasukan data
def insertData(parent, nama, nim, jurusan, gender, hobi):
    top = Toplevel()
    # Get data
    nama = nama.get()
    nim = nim.get()
    
    jurusan = jurusan.get()
    gender = gender
    hobi = hobi
   
        
    if(nama == "" or nim == "" or jurusan == "" or gender == "" or hobi == ""):
        btn_ok = Button(top, text="Input field masih ada yang kosong!", anchor="s", command=lambda:[top.destroy(), parent.deiconify()])
        btn_ok.pack(padx=10, pady=10)
        # Input data disini
    else:
        dbcursor = mydb.cursor()
        sql = "INSERT INTO mahasiswa (nim, nama, jurusan, jenins_kelamin, Hobi) VALUES (%s, %s, %s, %s, %s)"
        val = (nim, nama, jurusan, gender, hobi)
        dbcursor.execute(sql, val)
        mydb.commit()
        print(dbcursor.rowcount, "Record Inserted")
        btn_ok = Button(top, text="Syap!", anchor="s", command=lambda:[top.destroy(), parent.deiconify()])
        btn_ok.pack(padx=10, pady=10)
  
# Window Semua Mahasiswa
def viewAll():
    global root
    root.withdraw()

    top = Toplevel()
    top.title("Semua Mahasiswa")
    frame = LabelFrame(top, borderwidth=0)
    frame.pack()
    # Cancel Button
    btn_cancel = Button(frame, text="Kembali", anchor="w", command=lambda:[top.destroy(), root.deiconify()])
    btn_cancel.grid(row=0, column=0, padx=10, pady=10, sticky="w")
    # Head title
    head = Label(frame, text="Data Mahasiswa")
    head.grid(row=0, column=1, padx=10, pady=10, sticky="w")

    tableFrame = LabelFrame(frame)
    tableFrame.grid(row=1, column = 0, columnspan=2)

    # Get All Data
    result = getMhs()

    # Title
    title1 = Label(tableFrame, text="No.", borderwidth=1, relief="solid", width=3, padx=5).grid(row=0, column=0)
    title2 = Label(tableFrame, text="NIM", borderwidth=1, relief="solid", width=15, padx=5).grid(row=0, column=1)
    title3 = Label(tableFrame, text="Nama", borderwidth=1, relief="solid", width=20, padx=5).grid(row=0, column=2)
    title4 = Label(tableFrame, text="Jurusan", borderwidth=1, relief="solid", width=20, padx=5).grid(row=0, column=3)
    title5 = Label(tableFrame, text="Gender", borderwidth=1, relief="solid", width=15, padx=5).grid(row=0, column=4)
    title6 = Label(tableFrame, text="Hobi", borderwidth=1, relief="solid", width=15, padx=5).grid(row=0, column=5)

    # Print content
    i = 0
    for data in result:
        label1 = Label(tableFrame, text=str(i+1), borderwidth=1, relief="solid", height=2, width=3, padx=5).grid(row=i+1, column=0)
        label2 = Label(tableFrame, text=data[1], borderwidth=1, relief="solid", height=2, width=15, padx=5).grid(row=i+1, column=1)
        label3 = Label(tableFrame, text=data[2], borderwidth=1, relief="solid", height=2, width=20, padx=5).grid(row=i+1, column=2)
        label4 = Label(tableFrame, text=data[3], borderwidth=1, relief="solid", height=2, width=20, padx=5).grid(row=i+1, column=3)
        label5 = Label(tableFrame, text=data[4], borderwidth=1, relief="solid", height=2, width=15, padx=5).grid(row=i+1, column=4)
        label6 = Label(tableFrame, text=data[5], borderwidth=1, relief="solid", height=2, width=15, padx=5).grid(row=i+1, column=5)
        i += 1

# Dialog konfirmasi hapus semua data
def clearAll():
    top = Toplevel()
    lbl = Label(top, text="Yakin mau hapus semua data?")
    lbl.pack(padx=20, pady=20)
    btnframe = LabelFrame(top, borderwidth=0)
    btnframe.pack(padx=20, pady=20)
    # Yes
    btn_yes = Button(btnframe, text="Gass", bg="green", fg="white", command=lambda:[top.destroy(), delAll()])
    btn_yes.grid(row=0, column=0, padx=10)
    # No
    btn_no = Button(btnframe, text="Tapi boong", bg="red", fg="white", command=top.destroy)
    btn_no.grid(row=0, column=1, padx=10)

# Dialog konfirmasi keluar GUI
def exitDialog():
    global root
    root.withdraw()
    top = Toplevel()
    lbl = Label(top, text="Yakin mau keluar?")
    lbl.pack(padx=20, pady=20)
    btnframe = LabelFrame(top, borderwidth=0)
    btnframe.pack(padx=20, pady=20)
    # Yes
    btn_yes = Button(btnframe, text="Gass", bg="green", fg="white", command=lambda:[top.destroy(), root.destroy()])
    btn_yes.grid(row=0, column=0, padx=10)
    # No
    btn_no = Button(btnframe, text="Tapi boong", bg="red", fg="white", command=lambda:[top.destroy(), root.deiconify()])
    btn_no.grid(row=0, column=1, padx=10)

def delAll():
    top = Toplevel()
    # Delete data disini
    dbcursor = mydb.cursor()
    sql = "TRUNCATE mahasiswa"
    dbcursor.execute(sql)
    mydb.commit()
    print(dbcursor, "Table has been reset")
    btn_ok = Button(top, text="Zeeb", command=top.destroy)
    btn_ok.pack(pady=20)
def galery():
    global root
    root.withdraw()
    
    top = Toplevel()
    top.title("Daftar Fasilitas Kampus")
    dframe = LabelFrame(top, text="Daftar Fasilitas Kampus", padx=10, pady=10)
    dframe.pack(padx=10, pady=10)
    my_img1 = ImageTk.PhotoImage(Image.open('image/gambar1.jpg'))
    my_img2 = ImageTk.PhotoImage(Image.open('image/gambar2.jpg'))
    my_img3 = ImageTk.PhotoImage(Image.open('image/gambar3.jpg'))
    my_img4 = ImageTk.PhotoImage(Image.open('image/gambar4.jpg'))
    my_img5 = ImageTk.PhotoImage(Image.open('image/gambar5.jpg'))

    image_list = [my_img1, my_img2, my_img3, my_img4, my_img5]

    my_label = Label(dframe, image=my_img1)
    my_label.grid(row=0, column=0, columnspan=3)
    frame2 = LabelFrame(dframe, borderwidth=0)
    frame2.grid(columnspan=2, column=0, row=10, pady=10)
    def forward(image_number, my_label):
        
        global button_forward
        global button_back

        my_label.grid_forget()
        my_label = Label(dframe, image=image_list[image_number - 1])
        button_forward = Button(dframe, text=">>", command=lambda: forward(image_number + 1, my_label))
        button_back = Button(dframe, text="<<", command=lambda: back(image_number - 1, my_label))

        if image_number == 5:
            button_forward = Button(dframe, text=">>", state=DISABLED)

        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)


    def back(image_number, my_label):
        global button_forward
        global button_back

        my_label.grid_forget()
        my_label = Label(dframe, image=image_list[image_number - 1])
        button_forward = Button(dframe, text=">>", command=lambda: forward(image_number + 1, my_label))
        button_back = Button(dframe, text="<<", command=lambda: back(image_number - 1, my_label))

        if image_number == 1:
            button_back = Button(dframe, text="<<", state=DISABLED)

        my_label.grid(row=0, column=0, columnspan=3)
        button_back.grid(row=1, column=0)
        button_forward.grid(row=1, column=2)
   
    button_back = Button(dframe, text="<<", command=lambda: back(), state=DISABLED)
    btn_cancel = Button(dframe, text="Kembali", anchor="w", command=lambda:[top.destroy(), root.deiconify()])
    button_forward = Button(dframe, text=">>", command=lambda: forward(2, my_label))

    button_back.grid(row=1, column=0)
    btn_cancel.grid(row=1, column=1)
    button_forward.grid(row=1, column=2)

# Title Frame
frame = LabelFrame(root, text="Praktikum DPBO", padx=10, pady=10)
frame.pack(padx=10, pady=10)

# ButtonGroup Frame
buttonGroup = LabelFrame(root, padx=10, pady=10)
buttonGroup.pack(padx=10, pady=10)

# Title
label1 = Label(frame, text="Data Mahasiswa", font=(30))
label1.pack()

# Description
label2 = Label(frame, text="Ceritanya ini database mahasiswa ngab")
label2.pack()

# Input btn
b_add = Button(buttonGroup, text="Input Data Mahasiswa", command=inputs, width=30)
b_add.grid(row=0, column=0, pady=5)

# All data btn
b_add = Button(buttonGroup, text="Semua Data Mahasiswa", command=viewAll, width=30)
b_add.grid(row=1, column=0, pady=5)

# Clear all btn
b_clear = Button(buttonGroup, text="Hapus Semua Data Mahasiswa", command=clearAll, width=30)
b_clear.grid(row=2, column=0, pady=5)

# Galery buttom
b_galery = Button(buttonGroup, text="Daftar Fasilitas Kampus", command=galery, width=30)
b_galery.grid(row=3, column=0, pady=5)
# Exit btn
b_exit = Button(buttonGroup, text="Exit", command=exitDialog, width=30)
b_exit.grid(row=4, column=0, pady=5)

root.mainloop()