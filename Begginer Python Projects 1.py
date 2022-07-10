# Welcome to the my begginer python projects


import random

# random_integer=random.randint(1,10)
# x=input("Sayi gir.")
# if x==random_integer:
#     print("U are wizard.")
# else:
#     print("Try again.")

#LOVE SCORE PROGRAM
# print(f"bilgisayarın tuttuğu sayı {random_integer}")
# random_float= random.random()*10
# print(random_float)
# love_score=random.randint(1,100)
# print(f"Your love score is {love_score}")
# END LOVE SCORE PROGRAM

# HEAD OR TAİL PROGRAM
# print("Welcome to the head or tail program.")
# secim=input("Head or Tail.").lower()
# head_tail=random.randint(0,1)
# if head_tail==0:
#     head_tail="tail"
# else:
#     head_tail="head"
# if secim==head_tail:
#     print(f"You are win come a {head_tail}.")
# else:
#     print(f"You are lose come a {head_tail}.")
# LIST EXERCISES
# states_turkey=["Bursa","Istanbul","Ankara"]
# print(states_turkey[1])
# states_turkey.append("Mevlutland")
# print(states_turkey)
# states_turkey.extend("First")
# states_turkey.insert(2,3)
# states_turkey.remove(3)
# print(states_turkey)

# WHO PAY THE BİLL PROGRAM
# name1=input("Name 1").lower()
# name2=input("Name 2").lower()
# name3=input("Name 3").lower()
# name4=input("Name 4").lower()
# name5=input("Name 5").lower()
# paylist=[name1,name2,name3,name4,name5]
# bill=random.choice(paylist)
# print(f"{bill} pay the bill.")
# option2
# names=input("isimleri virgül kullanarak yaz.")
# name_list=names.split(",")
# num_items=len(name_list)
# x=random.randint(0,int(num_items))
# y=name_list[x]
# print(f"{y} pay the bill")
# END THE

# OPEN THE CHOOSING PIECE PROGRAM**
# piece1=["🎱","🎱","🎱"]
# piece2=["🎱","🎱","🎱"]
# piece3=["🎱","🎱","🎱"]
# maps=[piece1,piece2,piece3]
# print(f"{piece1}\n{piece2}\n{piece3}")
# position=input("Hangisini acmak istiyorsan sayı gir.")
# yatay=int(position[0])
# dikey=int(position[1])
# maps[yatay-1][dikey-1]="X"
# print(f"{piece1}\n{piece2}\n{piece3}")
    # END THE

    # ROCK PAPER SCİSSORS PROGRAM
# print("Welcome to the Rock,Paper,Scissors game! ")
# rockpapersc=['''
#    _______
# ---'   ____)
#       (_____)
#       (_____)
#       (____)
# ---.__(___)
# ''', '''
# _______
# ---'   ____)____
#           ______)
#           _______)
#          _______)
# ---.__________)]
# ''','''
#     _______
# ---'   ____)____
#           ______)
#        __________)
#       (____)
# ---.__(___)
# ''']
# tas=rockpapersc[0]
# kagit=rockpapersc[1]
# makas=rockpapersc[2]
# secim=input("Choose a one tas kagit makas").lower()
# rastgele=random.choice(rockpapersc)
# if secim==tas and rastgele==kagit:
#     print("You are Lose\n.")
#     print(f"{secim}\n")
#     print(f"{rastgele}\n")
# else:
#     print(f"You are win. \n")
#     print(f"{secim}\n")
#     print(f"{rastgele}\n")

# END

# FIND AVERAGE HEIGHT PROGRAM
# boylar=input("boyları gir bosluk bırakarak ").split( )
# sayi=len(boylar)
# toplam=0
# for n in range(0,sayi):
#     boylar[n]=int(boylar[n])
# for x in boylar:
#     toplam=toplam+x
#
# print(toplam/sayi)

# HIGH SCORE FINDING PROGRAM
# notlar=input("notları girin bosluk birakarak.").split( )
# sayi=len(notlar)
# sayac=0
# for n in range(0,sayi):
#     notlar[n]=int(notlar[n])
# print(max(notlar))
# for skor in notlar:
#     if skor>sayac:
#         sayac=skor
# print(sayac)

# PRİNT SUMME EVEN NUMBERS PROGRAM
# print("Welcome to the gauß even numbers summe.")
# toplam=0
# for n in range(0,101,2):
#     toplam=n+toplam
# print(f"Even numbers summe {toplam}")
# STOP

# Fizz Buzz Game
# print("Welcome to the FizzBuzz game.")
# Çözümü otomatik olarak FizzBuzz oyununa yazdıran bir program yazacaksınız.
#
# Programınız sırayla 1'den 100'e kadar her sayıyı yazdırmalıdır.
#
# Sayı 3'e bölündüğünde, sayıyı yazdırmak yerine "Fizz" yazmalıdır.
#
# `Sayı 5'e bölünebiliyorsa, sayıyı yazdırmak yerine "Buzz" yazmalıdır.`
# `Ve eğer sayı hem 3'e hem de 5'e bölünebiliyorsa, ör. 15 numara yerine "FizzBuzz" yazmalıdır.
# Örneğin. şöyle başlayabilir:
# for n in range(1,101):
#     if n%3==0 and n%5==0:
#         print("FizzBuzz")
#     elif n%5==0:
#         print("Buzz")
#     elif n%3==0:
#         print("Fizz")
#     else:
#         print(n)
# else kullanmamızın sebebi normal print yazınca direkt hepsini yazdırır ama else kullanınca fizz ve buzz yazmadıklarını
# normal olarak diğerlerini fizz buz zolarak yazdırır çünkü else e geçmez

# PASSWORD GENERATOR
# print("Welcome to the password generator.")
# kackarakter=int(input("How many letters would you like in your password. "))
# symbols=["!","'",".",",","!","^","+","%","&","/","(",")","*","-","_","<",">"]
# numbers=["1","2","3","4","5","6","7","8","9","0"]
# harf=['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
# kacsembol=int(input("How many symbols would you like? "))
# kacsayi=int(input("How many numbers would you like? "))
# password=""
# for n in range(1,kackarakter+1):
#     password=password+random.choice(harf)
# for char in range(1, kacsembol+1):
#     password=password+random.choice(symbols)
# for char in range(1,kacsayi+1):
#     password=password+random.choice(numbers)
# print(f"Your password is generated: {password}")

# end













