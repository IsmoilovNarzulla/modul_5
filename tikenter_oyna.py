
# 1. Grafik interfeys (GUI) nima va foydalanuvchiga qanday qulaylik yaratadi?
# GUI (Graphical User Interface) — bu foydalanuvchi bilan dastur o‘rtasida grafik elementlar orqali o‘zaro aloqani tashkil etuvchi interfeys. Masalan:
# •	Tugma (button)
# •	Matn maydoni (textbox)
# •	Ro‘yxat (listbox)
# •	Sürgichlar, oynalar, menyular
# Qulayliklari:
# •	Buyruqlarni yozish o‘rniga sichqoncha bilan boshqarish
# •	Ko‘rinarli va interaktiv muhit yaratadi
# •	Texnik bo‘lmagan foydalanuvchi ham oson tushunadi va ishlata oladi
# •	Mobil va desktop ilovalar GUI asosida quriladi
#
# 2. Python tilida GUI yaratish uchun mashhur kutubxonalar
# Kutubxona	Afzalliklari
# Tkinter (standart)	Python bilan birga keladi. Oddiy, oson o‘rganiladi
# PyQt / PySide	Kuchli, professional darajadagi GUI yaratish, Qt Designer bilan ishlaydi
# Kivy	Mobil ilovalar yaratishda qulay, ko‘p platformali (Android, iOS, desktop)
# CustomTkinter	Tkinter'ga zamonaviy dizayn (dark mode, gradientlar) qo‘shadi
# PyGame	O‘yinlar va interaktiv ilovalar uchun mo‘ljallangan
# Tavsiya: Boshlang‘ich foydalanuvchi uchun Tkinter eng mos.
#
# 3. GUI elementlariga hodisalar (event) qanday biriktiriladi?
# Hodisa — foydalanuvchi harakati (masalan, tugmani bosish).
# Tkinter misoli:

# import tkinter as tk
#
# def tugma_bosildi():
#     print("Tugma bosildi!")
#
# oyna = tk.Tk()
# tugma = tk.Button(oyna, text="Bos!", command=tugma_bosildi)
# tugma.pack()
#
# oyna.mainloop()

# •	command=tugma_bosildi — hodisaga funksiya biriktirilgan
# •	mainloop() — GUI oynani doimiy kuzatib turadi (event loop)
#
# 4. Oyna yaratish va GUI elementlarini joylashtirish
# Tkinter’da asosiy elementlar:

import tkinter as tk

oyna = tk.Tk()                # Oyna yaratish
oyna.title("Dastur nomi")    # Oynaga sarlavha
oyna.geometry("300x200")     # Oyna o‘lchami (px)

yorliq = tk.Label(oyna, text="Salom!")
yorliq.pack()

matn_maydoni = tk.Entry(oyna)
matn_maydoni.pack()

tugma = tk.Button(oyna, text="Chiqar", command=lambda: print(matn_maydoni.get()))
tugma.pack()

oyna.mainloop()              # GUI ishga tushadi


#  Elementlarni joylashtirish usullari:
# Usul		Tavsifi
# .pack()		Elementlarni ustma-ust joylashtiradi
# .grid(row=0, column=1)		Jadval shaklida joylashtiradi
# .place(x=50, y=100)		Aniq koordinata bo‘yicha joylashtiradi

# Xulosa:
# GUI — foydalanuvchi bilan oson va interaktiv aloqa qilish vositasi.
#
# Tkinter – boshlang‘ich uchun oddiy va qulay vosita.
#
# Har bir GUI elementga command= yoki bind() orqali hodisa biriktiriladi.
#
# Oyna Tk(), elementlar esa Label, Button, Entry orqali yaratiladi.


