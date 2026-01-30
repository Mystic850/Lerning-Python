

# <--- Ist ein kommentar man kann rein schreiben was man will und es wir am ende nicht angezeigt


# print ist eine function die dem computer sagt das man etwas in die console rein schreiben will.
# Und aufpassen das man print IMMER klein schreibt sonst ist es ein syntax Fehler und wir vom computer nicht erkannt.

print("Hello World")

# Wen man diesen code jetzt ausführt wird in der console Hello World stehen.

# Mit python kann man auch rechnen und das ist der einfachste teil.
# Wir haben hier die zwei variablen A und B mit dem wert 10 und 15 und dan sagen wir das c gleich a plus b ist und dan nurnoch mehr printen damit das ergebnis auch in der console steht und das geht wen man print(C) macht
# Und nicht vergessen die variablen richtig zu schreiben weil wen man print(c) macht wird das nicht gehen weil das c klein ist und wir die Variable als grosses C gemacht haben.
A = 10
B = 15

C = A + B 
print(C)


# Jetzt haben wir die gleichen variablen wie vorher nur das wir jetzt eine neue Function namens IF haben und das sagt WEN A kleiner als B ist dan print A ist kleiner als B.
# Dan haben wir noch eine neue Function names ELSE und das sagt wen das erste also print("A ist kleiner als B") nicht stimmt dann print("A ist größer als B")

A = 10
B = 15 

if A < B:
    print("A ist kleiner als B")
else:
    print("A ist größer als B")



# Hier ist eine liste von mehreren sachen und die lise kann man mit egal welchen variablen kenzeichnen ich habe mylist genommen.
# Um sachen in die liste zu packen benutzen wir [ ] und der inhalt kann zahlen buchstaben und alles was man will haben aber man muss jedes ding mit " " beschriften.

mylist = ["Alex", "Jerome", "Nadija", "Marijan"]

print(mylist)



#  Hier haben wir ein dictionary auf deutsch Wörterbuch und hier geben wir wieder eine variable deiner wahl ein und machen eine offene klammer und dan geben wir die variablen ein die wir einen wert geben.
# Zum beispiel ich habe bei Name den wert jerome gegeben und wen wir alle variablen eingegeben haben die wir wollten schliesen wir die klammer und geben  print(VARIABLE[VARIABLEN die wir printen wollen]) 
thisdict = {
    "Name": "Jerome",
    "Age" : "15",
    "Language": "German & English",
}
print(thisdict["Name"])


# Man kann auch eine neue variable machen und sagen das x den wert von einer variable von thisdict2 hat zb. Age und dan nur noch mehr print(x)
thisdict2 = {
    "Name" : "Marijan",
    "Age"  : "15",
}

x = thisdict2.get("Age")
print(x)


# Mit thisdict3.update kann man sachen in sein dictionary hinzügen.

thisdict3 = {
    "Name" : "Marijan",
    "Age"  : "15",
}
thisdict3.update({"Country" : "Austria"})
print(thisdict3)



# Mit del .... kann man sachen aus seinem dictionary raus machen.
thisdict4 ={
    "Name" : "Ertan",
    "Age"  : "14",
}

del thisdict4["Name"]
print(thisdict4)

# Und wen man nichts mehr drin haben will muss man nur thisdict4.clear machen

