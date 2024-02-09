import tkinter as tk
from tkinter import ttk
from tkinter.tix import IMAGETEXT
from animals import *
from tkinter import *
import tkinter 


class InfoAnimals(tk.Frame):

    def __init__(self, root):   
        super().__init__(root)
        self.animal_shelter()
        self.btn()
        self.tree_view()
        self.db = Shelter()
        self.output()

    def animal_shelter(self):
        self.fr = ttk.Frame().pack(padx=0, pady=26)

    def btn(self):
        ttk.Button(self.fr, text="Ввод данных", command=DataAnimals)\
            .place(x=37, y=650)
        ttk.Button(self.fr, text="Удаление", command=self.delete_animal)\
            .place(x=140, y=650)
        ttk.Button(self.fr, text="Выход", command=root.destroy)\
            .place(x=1175, y=650)

    def tree_view(self):
        list_animals = ["id", "animals", "name", "bread", "age", "gender", "commands", "packani", "date_1", "date_2", "vaccine", "date_vac"]
        list_head = ["ID", "Животное", "Кличка", "Порода", "Возраст", "Пол", "Знает команды", "Класс животного", "Дата рождения", "Дата поступления в приют", "Вакцинирован", "Дата вакцинации"]
        dict_list = dict(zip(list_animals, list_head))
        self.tree = ttk.Treeview(self, columns=(list_animals),\
                                height=26, show="headings")
        self.tree.column("id", width=30, anchor=tk.CENTER)
        for i in list_animals[1:]:
            self.tree.column(i, width=110, anchor=tk.CENTER)
        for k, v in dict_list.items():
            self.tree.heading(k, text=v)

        self.tree.pack(expand=True, fill="both")

    def output(self):        
        self.db.cur.execute("SELECT * FROM animals_table")
        for i in self.tree.get_children():
            self.tree.delete(i)
        for i in self.db.cur.fetchall():
            self.tree.insert("", "end", values=i)

    def delete_animal(self):
        for j in self.tree.selection():
            self.db.cur.execute("""DELETE FROM animals_table WHERE
                                id==?""", (self.tree.set(j, "#1"),))
            self.db.db.commit()
            self.tree.delete(j) 
    

class DataAnimals(tk.Toplevel):    
    
    def __init__(self):
        super().__init__()
        self.info_animals()
        self.str_var()
        self.label()
        self.entry()
        self.animal_list()
        self.radio_button()
        self.radio_button_1()
        self.radio_button_2()
        self.btn()
        self.sh = Shelter()
        self.app = app        

    def info_animals(self):
        self.title("Ввод данных")
        self.geometry("650x490+420+220")
        self.resizable(False, False)
        self.grab_set()
        self.focus_set()

    def str_var(self):        
        self.animals_result = tk.StringVar(value=" ")
        self.name_al = tk.StringVar()
        self.breed_al = tk.StringVar()
        self.age_al = tk.StringVar()
        self.gender_als = tk.StringVar()
        self.commands_al = tk.StringVar()
        self.packani_als = tk.StringVar()
        self.date_1_al = tk.StringVar()
        self.date_2_al = tk.StringVar()
        self.vaccine_als = tk.StringVar()
        self.date_vac_al = tk.StringVar()

    def label(self):        
        ttk.Label(self, text="Внесенные данные:",\
                  font=title_font).place(x=400, y=60)

        ttk.Label(self, text="Животные", font=title_font).place(x=130, y=10)
        ttk.Label(self, textvariable=self.animals_result).place(x=460, y=100)
        ttk.Label(self, text="Животное:").place(x=340, y=100)
        
        ttk.Label(self, text="Кличка:").place(x=20, y=100)
        ttk.Label(self, textvariable=self.name_al).place(x=460, y=120)
        ttk.Label(self, text="Кличка:").place(x=340, y=120)

        ttk.Label(self, text="Порода:").place(x=20, y=130)
        ttk.Label(self, textvariable=self.breed_al).place(x=460, y=140)
        ttk.Label(self, text="Порода:").place(x=340, y=140)

        ttk.Label(self, text="Возраст:").place(x=20, y=160)
        ttk.Label(self, textvariable=self.age_al).place(x=460, y=160)
        ttk.Label(self, text="Возраст:").place(x=340, y=160)

        ttk.Label(self, text="Пол:").place(x=20, y=190)
        ttk.Label(self, textvariable=self.gender_als).place(x=460, y=180)
        ttk.Label(self, text="Пол:").place(x=340, y=180)
        
        ttk.Label(self, text="Знает команды:").place(x=20, y=220)
        ttk.Label(self, textvariable=self.commands_al).place(x=460, y=200)
        ttk.Label(self, text="Знает команды:").place(x=340, y=200)

        ttk.Label(self, text="Класс животных:").place(x=20, y=250)
        ttk.Label(self, textvariable=self.packani_als).place(x=460, y=220)
        ttk.Label(self, text="Класс животного:").place(x=340, y=220)

        ttk.Label(self, text="Дата рождения:").place(x=20, y=280)
        ttk.Label(self, textvariable=self.date_1_al).place(x=460, y=240)
        ttk.Label(self, text="Дата рождения:").place(x=340, y=240)

        ttk.Label(self, text="Дата поступления:").place(x=20, y=310)
        ttk.Label(self, textvariable=self.date_2_al).place(x=460, y=260)
        ttk.Label(self, text="Дата поступления:").place(x=340, y=260)

        ttk.Label(self, text="Вакцинирован:").place(x=20, y=340)
        ttk.Label(self, textvariable=self.vaccine_als).place(x=460, y=280)
        ttk.Label(self, text="Вакцинирован:").place(x=340, y=280)

        ttk.Label(self, text="Дата вакцинации:").place(x=20, y=370)
        ttk.Label(self, textvariable=self.date_vac_al).place(x=460, y=300)
        ttk.Label(self, text="Дата вакцинации:").place(x=340, y=300)

    def entry(self):
        ttk.Entry(self, width=25, textvariable=self.name_al,\
            font=_font).place(x=130, y=100)        
        ttk.Entry(self, width=25, textvariable=self.breed_al,\
            font=_font).place(x=130, y=130)
        ttk.Entry(self, width=25, textvariable=self.age_al,\
            font=_font).place(x=130, y=160)
        ttk.Entry(self, width=25, textvariable=self.commands_al,\
            font=_font).place(x=130, y=220)
        ttk.Entry(self, width=25, textvariable=self.date_1_al,\
            font=_font).place(x=130, y=280)
        ttk.Entry(self, width=25, textvariable=self.date_2_al,\
            font=_font).place(x=130, y=310)
        ttk.Entry(self, width=25, textvariable=self.date_vac_al,\
            font=_font).place(x=130, y=370)
    
    def radio_button(self):
        ttk.Radiobutton(self, text="муж.", value="мужской",\
            variable=self.gender_als,\
            command=self.gender_animals).place(x=130, y=190)
        ttk.Radiobutton(self, text="жен.", value="женский",\
            variable=self.gender_als,\
            command=self.gender_animals).place(x=220, y=190)
    
    def radio_button_1(self):
        ttk.Radiobutton(self, text="Домашнее", value="Домашнее животное",\
            variable=self.packani_als,\
            command=self.pack_animals).place(x=130, y=250)
        ttk.Radiobutton(self, text="Вьючное", value="Вьючное животное",\
            variable=self.packani_als,\
            command=self.pack_animals).place(x=220, y=250)
    
    def radio_button_2(self):
        ttk.Radiobutton(self, text="Да", value="Да",\
            variable=self.vaccine_als,\
            command=self.vaccine).place(x=130, y=340)
        ttk.Radiobutton(self, text="Нет", value="Нет",\
            variable=self.vaccine_als,\
            command=self.vaccine).place(x=220, y=340)

    def btn(self):
        ttk.Button(self, text="Готово",\
                   command=self.data_animals).place(x=395, y=415)
        ttk.Button(self, text="Закрыть",\
                   command=self.destroy).place(x=495, y=415)

    def gender_animals(self):
        gender_al = self.gender_als.get()
        if gender_al == "мужской":
            return "мужской"
        else:
            gender_al == "женский"
            return "женский"
    
    def pack_animals(self):
        pack_al = self.packani_als.get()
        if pack_al == "Домашнее":
            return "Домашнее животное"
        else:
            pack_al == "Вьючное"
            return "Вьючное животное"
    
    def vaccine(self):
        pack_al = self.packani_als.get()
        if pack_al == "Да":
            return "Вакцинирован"
        else:
            pack_al == "Нет"
            return "Не вакцинорован"
        
    def animal_list(self):
        self.animal = ["Собака", "Кот", "Хомяк", "Лошадь", "Верблюд", "Осел"]
        ttk.Combobox(self, font=_font, values=self.animal,\
                    textvariable=self.animals_result,\
                    state="readonly").place(x=90, y=35)

                    
    def data_animals(self):
        anim = self.animals_result.get()
        if anim == "Кот":
            self.sh.main(animal=anim, name=self.name_al.get(),\
                         breed=self.breed_al.get(),\
                         age=self.age_al.get(), gender=self.gender_animals(),\
                         commands=self.commands_al.get(),\
                         packani=self.packani_als.get(),\
                         date_1=self.date_1_al.get(),\
                         date_2=self.date_2_al.get(),\
                         vaccine=self.vaccine_als.get(),\
                         date_vac=self.date_vac_al.get())            
        elif anim == "Собака":
            self.sh.main(animal=anim, name=self.name_al.get(),\
                         breed=self.breed_al.get(),\
                         age=self.age_al.get(), gender=self.gender_animals(),\
                         commands=self.commands_al.get(),\
                         packani=self.packani_als.get(),\
                         date_1=self.date_1_al.get(),\
                         date_2=self.date_2_al.get(),\
                         vaccine=self.vaccine_als.get(),\
                         date_vac=self.date_vac_al.get())
        elif anim == "Хомяк":
            self.sh.main(animal=anim, name=self.name_al.get(),\
                         breed=self.breed_al.get(),\
                         age=self.age_al.get(), gender=self.gender_animals(),\
                         commands=self.commands_al.get(),\
                         packani=self.packani_als.get(),\
                         date_1=self.date_1_al.get(),\
                         date_2=self.date_2_al.get(),\
                         vaccine=self.vaccine_als.get(),\
                         date_vac=self.date_vac_al.get())
        elif anim == "Лошадь":
            self.sh.main(animal=anim, name=self.name_al.get(),\
                         breed=self.breed_al.get(),\
                         age=self.age_al.get(), gender=self.gender_animals(),\
                         commands=self.commands_al.get(),\
                         packani=self.packani_als.get(),\
                         date_1=self.date_1_al.get(),\
                         date_2=self.date_2_al.get(),\
                         vaccine=self.vaccine_als.get(),\
                         date_vac=self.date_vac_al.get())
        elif anim == "Верблюд":
            self.sh.main(animal=anim, name=self.name_al.get(),\
                         breed=self.breed_al.get(),\
                         age=self.age_al.get(), gender=self.gender_animals(),\
                         commands=self.commands_al.get(),\
                         packani=self.packani_als.get(),\
                         date_1=self.date_1_al.get(),\
                         date_2=self.date_2_al.get(),\
                         vaccine=self.vaccine_als.get(),\
                         date_vac=self.date_vac_al.get())
        elif anim == "Осел":
            self.sh.main(animal=anim, name=self.name_al.get(),\
                         breed=self.breed_al.get(),\
                         age=self.age_al.get(), gender=self.gender_animals(),\
                         commands=self.commands_al.get(),\
                         packani=self.packani_als.get(),\
                         date_1=self.date_1_al.get(),\
                         date_2=self.date_2_al.get(),\
                         vaccine=self.vaccine_als.get(),\
                         date_vac=self.date_vac_al.get())                      
        self.app.output()

    
if __name__ == "__main__":
    root = tk.Tk() 
    app = InfoAnimals(root)
    app.pack()
    root.title("Приют для животных")
    root.geometry("1280x720+100+30")
    root.configure(background='DodgerBlue')
    root.resizable(False, False)
    title_font = ("Pobeda Bold", "10", "bold")
    _font = ("Pobeda Bold", "10")
    style = ttk.Style()
    style.configure(root, font=_font, foreground="#000000")
    root.mainloop()

