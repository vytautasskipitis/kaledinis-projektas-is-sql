from tkinter import *
from employee_class import *
from pagrindines_funkcijos import *


# lenteleje esancios funkcijos
def surask():
    ivesta1_0 = laukas1_0.get()
    status["text"] = get_emps_by_name(ivesta1_0)


def ivesk():
    ivesta2_0 = laukas2_0.get()
    ivesta2_1 = laukas2_1.get()
    ivesta2_2 = laukas2_2.get()
    insert_emp(Employee(ivesta2_0, ivesta2_1, ivesta2_2))
    status["text"] = "zmogus irasytas"


def pakeisk():
    ivesta3_0 = laukas3_0.get()
    ivesta3_1 = laukas3_1.get()
    ivesta3_2 = laukas3_2.get()
    if get_emps_by_name(ivesta3_1):
        remove_emp(ivesta3_0, ivesta3_1)
    insert_emp(Employee(ivesta3_0, ivesta3_1, ivesta3_2))
    status["text"] = "alga pakeista"


def pasalink():
    ivesta4_0 = laukas4_0.get()
    ivesta4_1 = laukas4_1.get()
    remove_emp(ivesta4_0, ivesta4_1)
    status["text"] = "istrintas"


def visi_zmones():
    c.execute("SELECT * FROM employees")
    items1_0 = c.fetchall()
    status["text"] = items1_0


def algu_suma():
    c.execute("SELECT * FROM employees")
    items1_0 = c.fetchall()
    list1 = [
        item[2]
        for item in items1_0
    ]
    status["text"] = "daubuotoju algu suma : ", sum(list1)


def menu_1():
    status["text"] = "veikia 1"


def menu_2():
    status["text"] = "veikia 2"


if __name__ == "__main__":
    print("mainas veikia ")


# cia pati lentele
langas = Tk()

meniu = Menu(langas)
langas.config(menu=meniu)
submeniu = Menu(meniu, tearoff=0)
submeniu2 = Menu(meniu, tearoff=0)

meniu.add_cascade(label="File", menu=submeniu)
submeniu.add_command(label="paraso 1", command=menu_1)
submeniu.add_command(label="paraso 2", command=menu_2)

meniu.add_cascade(label="Options", menu=submeniu2)
submeniu2.add_command(label="paraso 1", command=menu_1)
submeniu2.add_command(label="paraso 2", command=menu_2)

mygtukas1 = Button(langas, text="zmogaus info ->", command=surask)
mygtukas2 = Button(langas, text="ikelt zmogu i duomenu baze ->", command=ivesk)
mygtukas3 = Button(langas, text="pakeisti zmogaus alga ->", command=pakeisk)
mygtukas4 = Button(langas, text="istrinti zmogu pagal pavarde ->", command=pasalink)
mygtukas5 = Button(langas, text="visi zmones", command=visi_zmones)
mygtukas6 = Button(langas, text="darbuotoju algu suma", command=algu_suma)
laukas1_0 = Entry(langas)
laukas2_0 = Entry(langas)
laukas2_1 = Entry(langas)
laukas2_2 = Entry(langas)
laukas3_0 = Entry(langas)
laukas3_1 = Entry(langas)
laukas3_2 = Entry(langas)
laukas4_0 = Entry(langas)
laukas4_1 = Entry(langas)

status = Label(langas, text="cia bus info", bd=1, relief=SUNKEN, anchor=W)
status.grid(row=5, columnspan=4)

mygtukas1.grid(row=0, column=0, sticky=E)
mygtukas2.grid(row=1, column=0, sticky=E)
mygtukas3.grid(row=2, column=0, sticky=E)
mygtukas4.grid(row=3, column=0, sticky=E)
mygtukas5.grid(row=4, column=0, sticky=E)
mygtukas6.grid(row=4, column=1, sticky=E)
laukas1_0.grid(row=0, column=1)
laukas2_0.grid(row=1, column=1)
laukas2_1.grid(row=1, column=2)
laukas2_2.grid(row=1, column=3)
laukas3_0.grid(row=2, column=1)
laukas3_1.grid(row=2, column=2)
laukas3_2.grid(row=2, column=3)
laukas4_0.grid(row=3, column=1)
laukas4_1.grid(row=3, column=2)

langas.mainloop()
