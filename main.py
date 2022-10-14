# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import random


def hello(name):
    # Use a breakpoint in the code line below to debug your script.
    mot = ["es gentil", "es méchant", "pues", "bois du coca"]  # Press Ctrl+F8 to toggle the breakpoint.
    print(f"salut, {name}, tu {mot[random.randint(0, len(mot) - 1)]}")

def change(a,b):
    print('a:',a);
    print('b:', b);
    a, b = b, a
    print('a:', a);
    print('b:', b);
def get_length_sentence(sentence):
    cpt = 0;
    for x in sentence:
        if(x != " "):
            cpt +=1;
    return cpt
def trouve_longueur(chaine):
    return len(chaine);
# Press the green button in the gutter to run the script.
def test_var():
    x = float(1);
    y = int(2.8);
    z = complex(1);

    print(x);
    print(y);
    print(z);

    a = float(x);
    b = int(y);
    c = complex(1);

    print(type(a));
    print(type(b));
    print(type(c));
def find_word(sentence,word_to_find):
    if word_to_find in sentence:
        return "Trouvé !";
    if word_to_find not in sentence:
        return "Pas trouvé ...";
def slicing(sentence):
    return (sentence[2:4]);
if __name__ == '__main__':
    slt = "Salut les dev"
    slt = slt.replace("les","la")
    print(slt);
#prenom = "Pierre";
#    age = 20;
#    majeur = True;
#    compte_en_banque = 20135, 384;
#    amis = ["Marie", "Julien", "Adrien"];
#    parents = ("Marc", "Caroline");
#Corriger les erreurs
#site_web="google''
#correction : site_web="google"

#Exercice 3
#nombre = 17
#print("Le nombre est"+str(nombre)

#Exerice 5
#Exercice 6
#liste = range(3);
# listDeux = range(5);
#print(list(listDeux));

#Exercice 7
#prenom = "Vincent";
#    print(prenom)
#    if type(prenom) is str:
#        print("vrai");
#        prenom = 0
#    if type(prenom) is int:
#        print("vrai");

#Exercice 8
# slt = "Salut les dev"
#    slt = slt.replace("les","la")
#    print(slt);