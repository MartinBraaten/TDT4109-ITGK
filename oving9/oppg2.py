__author__ = 'Martinskole'
# -*- coding: utf-8 -*-

#Bursdagsdatabasen

birthdays = {
"22 nov ": ["Lars", "Mathias"],
"10 des ": " Elle ",
"30 okt ": ["Veronica", "Rune"],
"12 jan ": "Silje",
"31 okt ": "Willy",
"8 jul ": ["Brage", "Øystein"],
"1 mar ": "Nina"
}


def add_birthday_to_date(date , name):

    try:
        birthdays[date].append(name)
 #   except AttributeError:
        print("asd")
    except KeyError:
        birthdays["date"]=date
        birthdays[date].append(name)





add_birthday_to_date("30.okt" , "martin")