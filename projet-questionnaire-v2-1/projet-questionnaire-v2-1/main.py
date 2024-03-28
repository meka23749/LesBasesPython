# LES FONCTIONS : PROJET QUESTIONNAIRE
#
# Question : Quelle est la capitale de la France ?
# (a) Marseille
# (b) Nice
# (c) Paris
# (d) Nantes
#
# Votre réponse :
# Bonne réponse / Mauvaise réponse

# ...
# Question : Quelle est la capitale de l'Italie ?
# ...
#
# 4 questions

def poser_question(question):
    global score
    print(question[0])
    #print("  " + question)
    for i in range (0, len(question[1])):
        print(i+1, question[1][i])
    #print("  (b)", question[1][1])
    #print("  (c)", question[1][2])
    #print("  (d)", question[1][3])
    print()
    reponse = input("Votre réponse ( 1 entre et " + str(len(question[1])) + ") : ")
    reponse_int = int(reponse)
    if reponse.lower()  == question[2].lower() or question[1][reponse_int-1] == question[2]:
        print("Bonne réponse")
        score += 1
    else:
        print("Mauvaise réponse")   
    print()


score = 0

'''
    questionnaire[]
        question
            titre = "Quelle est la capitale de la France ?"
            reponses = ("Marseille", "Nice", "Paris", "Nantes")
            bonne_reponse = "Paris"

'''

question1 = ("Quelle est la capitale de la France ?", ("Marseille", "Nice", "Paris", "Nantes"), "Paris")
question2 = ("Quelle est la capitale de la l'Italie ?", ("Rome", "Venise", "Pise", "Florence"), "Rome")

poser_question(question1)
poser_question(question2)
# poser_question("Quelle est la capitale de la France ?", "Marseille", "Nice", "Paris", "Nantes", "c")
#poser_question("Quelle est la capitale de l'Italie ?", "Rome", "Venise", "Pise", "Florence", "a")

print("Score final :", score)
