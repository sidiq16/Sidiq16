#!/usr/bin/env python
# coding: utf-8

# ## Soal 1

# In[14]:


nama = str(input("Masukan Nama : "))
Umur = int(input("Masukan umur : ")) # 17 tapi boong
Tinggi = float(input("Masukan tinggi badan : "))


print("Nama saya " + nama + " , umur saya " + f'{Umur}' + " tahun, dan tinggi saya " + f'{Tinggi}'  + " cm")


# In[15]:


print(type(nama))
print(type(Umur))
print(type(Tinggi))


# ## Soal 2

# In[23]:


r = float(input("Masukan Jari-jari Lingkaran : "))
luas_lingkaran = round((22/7)*(r*r),2)
print("Luas lingkar dengan jari :" + f'{r}' + "cm, adalah luas lingkaran :", f'{luas_lingkaran}' + "cm\u00b2")

    


# In[24]:


r = float(input("Masukan Jari-jari Lingkaran : "))
luas_lingkaran = round((22/7)*(r*r),2)
print("Luas lingkar dengan jari :" + f'{r}' + "cm, adalah luas lingkaran :", f'{luas_lingkaran}' + "cm\u00b2")


# ## Soal 3

# In[26]:


ujian_teori = float(input("Nilai Ujian Teori : "))
ujian_praktek = float(input("Nilai Ujian Praktek : "))

if ujian_teori >= 70 and  ujian_praktek >=70:
    print("Selamat anda lulus")
elif ujian_teori >= 70 and  ujian_praktek <=70:
    print("Anda harus mengulangi ujian praktek")
elif ujian_teori <= 70 and  ujian_praktek >=70:
    print("Anda harus mengulangi ujian teori")
else:
    print("Anda harus mengulangi ujian teori dan praktek")


# In[39]:


no = -1
deret = int(input("Masukkan Jumlah Piramida Segitiga :"))
for x in range(-1,deret):
    no = no + 1
    print(" " *(deret - x),"*" *no)
    


# In[ ]:





# In[ ]:




