#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 20:01:51 2020

@author: alpertemel
"""
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Sep 19 16:09:44 2020

@author: alpertemel
"""

from tkinter import *
#from tkinter import messagebox
#from tkinter import filedialog
from tkinter.ttk import Combobox
#from tkinter import messagebox
#from tkinter import Canvas
#from tkinter import ttk
import pandas as pd
#import numpy as np
#import seaborn as sns
#import matplotlib.pyplot as plt
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from tkinter import Tk, Label, Frame, Entry, Button

data = pd.read_csv("/Users/alpertemel/Downloads/turkey_car_market.csv")
veri = pd.read_csv("/Users/alpertemel/Downloads/turkey_car_market.csv")

######################## MODEL BUILDING ########################


data.columns
df = data.copy()

le = LabelEncoder()

cols = ['Marka', 'Arac Tip Grubu', 'Arac Tip','Yakıt Turu', 'Vites', 'CCM', 'Beygir Gucu', 'Renk', 'Kasa Tipi',
       'Kimden', 'Durum']
for i in cols:
    df[i] = le.fit_transform(df[i])


x = df.iloc[:, 1:14]
y = df.iloc[:, 14:15]

x_train, x_test, y_train, y_test = train_test_split(x, y, test_size = 0.33,random_state = 12)

xgb = XGBRegressor(colsample_bytree = 0.7,
 learning_rate = 0.1,
 max_depth = 10,
 min_child_weight = 7,
 objective = 'reg:squarederror',
 subsample = 0.7)

xgb.fit(x_train, y_train)



######################## DATA PREPROCESSING ########################


arac_tip = data["Arac Tip"].unique()
arac_tip2 = veri["Arac Tip"].unique()
vites = data["Vites"].unique()
vites2 = veri["Vites"].unique()
marka = data["Marka"].unique()
marka2 = veri["Marka"].unique()
arac_tip_grubu = data["Arac Tip Grubu"].unique()
arac_tip_grubu2 = veri["Arac Tip Grubu"].unique()
yakıt_turu = data["Yakıt Turu"].unique()
yakıt_turu2 = veri["Yakıt Turu"].unique()
ccm = data["CCM"].unique()
ccm2 = veri["CCM"].unique()
beygir_gucu = data["Beygir Gucu"].unique()
beygir_gucu2 = veri["Beygir Gucu"].unique()
renk = data["Renk"].unique()
renk2 = veri["Renk"].unique()
kasa_tipi = data["Kasa Tipi"].unique()
kasa_tipi2 = veri["Kasa Tipi"].unique()
kimden = data["Kimden"].unique()
kimden2 = veri["Kimden"].unique()
durum = data["Durum"].unique()
durum2 = veri["Durum"].unique()


arac_tip = le.fit_transform(arac_tip)
vites = le.fit_transform(vites)
marka = le.fit_transform(marka)
arac_tip_grubu = le.fit_transform(arac_tip_grubu)
yakıt_turu = le.fit_transform(yakıt_turu)
vites = le.fit_transform(vites)
ccm = le.fit_transform(ccm)
beygir_gucu = le.fit_transform(beygir_gucu)
renk = le.fit_transform(renk)
kasa_tipi = le.fit_transform(kasa_tipi)
kimden = le.fit_transform(kimden)
durum = le.fit_transform(durum)


a = list(arac_tip) #ok
a2 = list(arac_tip2) #ok
b = list(vites) #ok
b2 = list(vites2) #ok
c = list(marka) #ok
c2 = list(marka2) #ok
d = list(arac_tip_grubu) #ok
d2 = list(arac_tip_grubu) #ok
e = list(yakıt_turu) #ok
e2 = list(yakıt_turu2) #ok
p = list(ccm) #ok
p2 = list(ccm2) #ok
h = list(beygir_gucu) #ok
h2 = list(beygir_gucu2) #ok
i = list(renk) #ok
i2 = list(renk2) #ok
j = list(kasa_tipi) #ok
j2 = list(kasa_tipi2) #ok
k = list(kimden) #ok
k2 = list(kimden2) #ok
l = list(durum) #ok
l2 = list(durum2) #ok

######################## DASHBOARD PREPARATION ########################

#from tkinter import *
#from tkinter.ttk import Combobox


anaPencere = Tk()
anaPencere.geometry("1200x900")
anaPencere.state("normal")
anaPencere.configure(bg = "#0059b3")

def marka_sec():
    global marka
    #label.destroy()
    secim = combo.get()
    
    print("=====================", secim)
    g = secenek.index(secim)
    #print(le.transform(c2[0:1]))
    marka = c[g]
    print(marka)

marka
secenek = list(veri["Marka"].unique())
combo=Combobox(anaPencere, values = secenek)
combo.place(x = 100, y = 70)
#combo.pack()
buton=Button(text="Marka Seç",command=marka_sec)
buton.place(x = 100, y = 110)
#buton.pack()
label=Label(text="")
label.pack()



############################################


def vites_düzenle():
    global vites
    #vites.destroy()
    vites_turu=combo2.get()
    
    print("=====================",vites_turu)
    g = secenek2.index(vites_turu)
    vites = b[g]
    print(vites)


secenek2 = list(veri["Vites"].unique())
combo2=Combobox(anaPencere,values=secenek2)
combo2.place(x = 100, y = 310)
#combo2.pack()
buton2=Button(text="Vites Turu Seç",command=vites_düzenle)
#buton2.pack()
buton2.place(x = 100, y = 350)
label2=Label(text="")
label2.pack()


############################################

def arac_tip_düzenle():
    global arac_tip
    #vites.destroy()
    tip_turu=combo3.get()
    
    print("=====================",tip_turu)
    g = secenek3.index(tip_turu)
    arac_tip = a[g]
    print(arac_tip)


secenek3 = list(veri["Arac Tip"].unique())
combo3=Combobox(anaPencere,values=secenek3)
combo3.place(x = 100, y = 230)
#combo3.pack()
buton3=Button(text="Araç Tipi Seç",command=arac_tip_düzenle)
#buton3.pack()
buton3.place(x = 100, y = 270)
label3=Label(text="")
label3.pack()



############################################



def tip_grubu_duzenle():
    
    global tip_grup
    #tip_grup.destroy()
    tip_grup_turu=combo4.get()
    
    print("=====================",tip_grup_turu)
    r = secenek4.index(tip_grup_turu)
    tip_grup = d[r]
    print(tip_grup)


secenek4 = list(veri["Arac Tip Grubu"].unique())
combo4=Combobox(anaPencere,values=secenek4)
combo4.place(x = 100, y = 150)
#combo4.pack()
buton4=Button(text="Arac Tip Grubu Seç",command=tip_grubu_duzenle)
#buton4.pack()
buton4.place(x = 100, y = 190)
label4=Label(text="")
label4.pack()




############################################

def yakıt_duzenle():
    global yakıt
    #vites.destroy()
    yakıt_turu = combo5.get()
    
    print("=====================",yakıt_turu)
    g = secenek5.index(yakıt_turu)
    yakıt = e[g]
    print(yakıt)


secenek5 = list(veri["Yakıt Turu"].unique())
combo5=Combobox(anaPencere,values=secenek5)
combo5.place(x = 100, y = 390)
#combo5.pack()
buton5=Button(text="Yakıt Turu Seç",command=yakıt_duzenle)
#buton5.pack()
buton5.place(x = 100, y = 430)
label5=Label(text="")
label5.pack()



############################################

def ccm_duzenle():
    global ccm
    #vites.destroy()
    ccm_turu = combo6.get()
    
    print("=====================",ccm_turu)
    g = secenek6.index(ccm_turu)
    ccm = p[g]
    print(ccm)


secenek6 = list(veri["CCM"].unique())
combo6=Combobox(anaPencere,values=secenek6)
combo6.place(x = 100, y = 470)
#combo6.pack()
buton6=Button(text="CCM Seç",command=ccm_duzenle)
#buton6.pack()
buton6.place(x = 100, y = 510)
label6=Label(text="")
label6.pack()



############################################

def hp_duzenle():
    global hp
    #vites.destroy()
    hp_turu = combo7.get()
    
    print("=====================",hp_turu)
    g = secenek7.index(hp_turu)
    hp = h[g]
    print(hp)


secenek7 = list(veri["Beygir Gucu"].unique())
combo7=Combobox(anaPencere,values=secenek7)
combo7.place(x = 100, y = 550)
#combo7.pack()
buton7=Button(text="HP Seç",command=hp_duzenle)
#buton7.pack()
buton7.place(x = 100, y = 590)
label7=Label(text="")
label7.pack()



############################################

def renk_duzenle():
    global renk
    #vites.destroy()
    renk_turu = combo8.get()
    
    print("=====================",renk_turu)
    g = secenek8.index(renk_turu)
    renk = i[g]
    print(renk)


secenek8 = list(veri["Renk"].unique())
combo8=Combobox(anaPencere,values=secenek8)
combo8.place(x = 400, y = 70)
#combo8.pack()
buton8=Button(text="Renk Seç",command=renk_duzenle)
buton8.pack()
buton8.place(x = 400, y = 110)
label8=Label(text="")
label8.pack()



############################################

def kasa_duzenle():
    global kasa
    #vites.destroy()
    kasa_turu = combo9.get()
    
    print("=====================",kasa_turu)
    g = secenek9.index(kasa_turu)
    kasa = j[g]
    print(kasa)


secenek9 = list(veri["Kasa Tipi"].unique())
combo9=Combobox(anaPencere,values=secenek9)
combo9.place(x = 400, y = 150)
#combo9.pack()
buton9=Button(text="Kasa Turu Seç",command=kasa_duzenle)
#buton9.pack()
buton9.place(x = 400, y = 190)
label9=Label(text="")
label9.pack()



############################################

def kimden_duzenle():
    global kimden
    #vites.destroy()
    kimden_tur = combo10.get()
    
    print("=====================",kimden_tur)
    g = secenek10.index(kimden_tur)
    kimden = k[g]
    print(kimden)


secenek10 = list(veri["Kimden"].unique())
combo10=Combobox(anaPencere,values=secenek10)
combo10.place(x = 400, y = 230)
#combo10.pack()
buton10=Button(text="Satıcı Turu Seç",command=kimden_duzenle)
#buton10.pack()
buton10.place(x = 400, y = 270)
label10=Label(text="")
label10.pack()



############################################

def durum_duzenle():
    global durum
    #vites.destroy()
    durum_tur = combo11.get()
    
    print("=====================",durum_tur)
    g = secenek11.index(durum_tur)
    durum = l[g]
    print(durum)


secenek11 = list(veri["Durum"].unique())
combo11=Combobox(anaPencere,values=secenek11)
combo11.place(x = 400, y = 310)
#combo11.pack()
buton11=Button(text="Durum Turu Seç",command=durum_duzenle)
#buton11.pack()
buton11.place(x = 400, y = 350)
label11=Label(text="")
label11.pack()



############################################

def model_yıl():
    global model
    #vites.destroy()
    model = combo12.get()
    print(model)


secenek12 = list(veri["Model Yıl"].unique())
combo12=Combobox(anaPencere,values=secenek12)
combo12.place(x = 400, y = 390)
#combo12.pack()
buton12=Button(text="Model Yıl Seç",command=model_yıl)
buton12.place(x = 400, y = 430)
#buton12.pack()
label12=Label(text="")
label12.pack()



############################################

def km_duzenle():
    global km
    #vites.destroy()
    km = combo13.get()
    print(km)


secenek13 = list(veri["Km"].unique())
combo13=Combobox(anaPencere,values=secenek13)
combo13.place(x = 400, y = 470)
#combo12.pack()
buton13=Button(text="KM Seç",command=km_duzenle)
buton13.place(x = 400, y = 510)
#buton12.pack()
label13=Label(text="")
label13.pack()



######################## CALCULATING AND PRINTING ########################



def hesapla():
    
    yeni_veri = [[marka], [tip_grup], [arac_tip], [model], [yakıt], [vites], [ccm], [hp], [renk], [kasa], [kimden], [durum], [km]]
    yeni_veri = pd.DataFrame(yeni_veri).T

    df_2 = yeni_veri.rename(columns = {0: "Marka",
                                       1: "Arac Tip Grubu",
                                       2: "Arac Tip",
                                       3: "Model Yıl",
                                       4: "Yakıt Turu",
                                       5: "Vites",
                                       6: "CCM",
                                       7: "Beygir Gucu",
                                       8: "Renk",
                                       9: "Kasa Tipi",
                                       10: "Kimden",
                                       11: "Durum",
                                       12: "Km"})

    
    
    df_2["Marka"] = df_2["Marka"].astype("int64")
    df_2["Arac Tip Grubu"] = df_2["Arac Tip Grubu"].astype("int64")
    df_2["Arac Tip"] = df_2["Arac Tip"].astype("int64")
    df_2["Model Yıl"] = df_2["Model Yıl"].astype("float64")
    df_2["Yakıt Turu"] = df_2["Yakıt Turu"].astype("int64")
    df_2["Vites"] = df_2["Vites"].astype("int64")
    df_2["CCM"] = df_2["CCM"].astype("int64")
    df_2["Beygir Gucu"] = df_2["Beygir Gucu"].astype("int64")
    df_2["Renk"] = df_2["Renk"].astype("int64")
    df_2["Kasa Tipi"] = df_2["Kasa Tipi"].astype("int64")
    df_2["Kimden"] = df_2["Kimden"].astype("int64")
    df_2["Durum"] = df_2["Durum"].astype("int64")
    df_2["Km"] = df_2["Km"].astype("int64")
    
    
    print("Yeni veri: ", yeni_veri)
    print("df_2: ", df_2)
    print("********",df_2.dtypes)
    print(df_2["Marka"])
    pred = xgb.predict(df_2)
    
    
    if pred < 0:
        pred = -1 * pred

    #pred = int(pred)
    
    s2 = Label(anaPencere, text = pred, font = "helvetica 20", borderwidth = 6, padx = 100, pady = 20)
    s2.place(x = 800, y = 300)
    
    return pred



hesapla_buton = Button(anaPencere, text = "HESAPLA", command = hesapla, font = "helvetica 15", borderwidth = 60, padx = 50, pady = 20, background = "#f7fafc")
hesapla_buton.place(x = 820, y = 210)
s1 = Label(anaPencere, text = " ", font = "helvetica 12", borderwidth = 6, padx = 100, pady = 20)
s1.place(x = 800, y = 300)

mainloop()







