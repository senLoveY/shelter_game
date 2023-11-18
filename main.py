import random
from tkinter import *
from tkinter import ttk
import tkinter.messagebox as mb
from subprocess import call
import shutil
import os
from PIL import Image, ImageFont, ImageDraw


def delete_everything_in_folder():
    shutil.rmtree('/Users/pavel_arsenovich/Documents/Files/Бункер/bunker_py/players')
    os.mkdir('/Users/pavel_arsenovich/Documents/Files/Бункер/bunker_py/players')


def distribute_roles():
    delete_everything_in_folder()
    world = []
    with open("roles/world.txt") as f:  # prof
        for line in f:
            world.append([x for x in line.split()])
    random.shuffle(world)
    with open("players/world.txt", "w+") as my_file:
        my_file.write(" ".join(world[0]) + "\n")

    prof = []
    sex = []
    age = []
    bagage = []
    fact = []
    health = []
    hobby = []
    fobia = []

    n = int(number_of_pl.get())

    if n < 6:
        msg = "Минимальное количество игроков – 6! Попробуйте еще раз!"
        mb.showwarning("Предупреждение", msg)

    elif n > 16:
        msg = "Максимальное количество игроков – 16! Попробуйте еще раз!"
        mb.showwarning("Предупреждение", msg)
    else:

        with open("roles/prof.txt") as f:                                 # prof
            for line in f:
                prof.append([x for x in line.split()])

        with open("roles/sex.txt") as f:                                  # sex
            for line in f:
                sex.append([x for x in line.split()])

        with open("roles/age.txt") as f:                                  # age
            for line in f:
                age.append([x for x in line.split()])

        with open("roles/bagage.txt") as f:                               # bagage
            for line in f:
                bagage.append([x for x in line.split()])

        with open("roles/fact.txt") as f:                                 # fact
            for line in f:
                fact.append([x for x in line.split()])

        with open("roles/health.txt") as f:                               # health
            for line in f:
                health.append([x for x in line.split()])

        with open("roles/hobby.txt") as f:                                # hobby
            for line in f:
                hobby.append([x for x in line.split()])

        with open("roles/fobia.txt") as f:                                # fobia
            for line in f:
                fobia.append([x for x in line.split()])

        random.shuffle(prof)
        random.shuffle(sex)
        random.shuffle(age)
        random.shuffle(bagage)
        random.shuffle(fact)
        random.shuffle(health)
        random.shuffle(hobby)
        random.shuffle(fobia)

        for i in range(n):
            with open("players/player"+str(i+1)+".txt", "w+") as my_file:

                my_file.write("Профессия: "+" ".join(prof[i])+"\n")
                my_file.write("Возраст:   "+" ".join(age[i])+"\n")
                my_file.write("Пол:       "+" ".join(sex[i])+"\n")
                my_file.write("Багаж:     "+" ".join(bagage[i])+"\n")
                my_file.write("Факт:      "+" ".join(fact[i])+"\n")
                my_file.write("Здоровье:  "+" ".join(health[i])+"\n")
                my_file.write("Хобби:     "+" ".join(hobby[i])+"\n")
                my_file.write("Фобия:     "+" ".join(fobia[i])+"\n")

        targetdirectory = "/Users/pavel_arsenovich/Documents/Files/Бункер/bunker_py/players"
        call(["open", targetdirectory])

        for i in range(n):
            image = Image.open("image1.png")
            font = ImageFont.truetype("Arial", 25)
            drawer = ImageDraw.Draw(image)

            drawer.text((270 - (len(" ".join(prof[i])) * 5 / 2), 200), " ".join(prof[i]), font=font, fill='white')
            drawer.text((270 - (len(" ".join(age[i])) * 5 / 2), 278), " ".join(age[i]), font=font, fill='white')
            drawer.text((270 - (len(" ".join(sex[i])) * 5 / 2), 356), " ".join(sex[i]), font=font, fill='white')
            drawer.text((270 - (len(" ".join(bagage[i])) * 5 / 2), 434), " ".join(bagage[i]), font=font, fill='white')
            drawer.text((270 - (len(" ".join(fact[i])) * 5 / 2), 512), " ".join(fact[i]), font=font, fill='white')
            drawer.text((270 - (len(" ".join(health[i])) * 5 / 2), 590), " ".join(health[i]), font=font, fill='white')
            drawer.text((270 - (len(" ".join(hobby[i])) * 5 / 2), 668), " ".join(hobby[i]), font=font, fill='white')
            drawer.text((270 - (len(" ".join(fobia[i])) * 5 / 2), 746), " ".join(fobia[i]), font=font, fill='white')
            image.save('players/player'+str(i+1)+'.png')
            image.show()


root = Tk()
root.geometry("600x150+450+250")
root.title("Бункер")
root["bg"] = "gray22"

label = ttk.Label(text="Введите количество игроков", font="Arial 30")
label.pack(anchor="center")

number_of_pl = ttk.Entry()
number_of_pl.pack(anchor="center", padx=20, pady=20)

button_image = PhotoImage(file="images/button1.png")
btn = Button(image=button_image, command=distribute_roles)  # создаем кнопку из пакета ttk
btn["border"] = "0"
btn.pack(anchor="center")    # размещаем кнопку в окне

root.mainloop()
