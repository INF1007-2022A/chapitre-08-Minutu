#!/usr/bin/env python
# -*- coding: utf-8 -*-

PERCENTAGE_TO_LETTER = {"A*": [95, 101], "A": [90, 95], "B+": [85, 90], "B": [80, 85], "C+": [75, 80], "C": [70, 75], "F": [0, 70]}

# TODO: Importez vos modules ici
from recettes import add_recipes, print_recipe
from os import path
import pickle

# TODO: Définissez vos fonction ici
def exercice1(file_path1, file_path2):
    with open(file_path1, 'r', enconding = 'utf-8') as f1, open(file_path2, 'r', encoding = 'utf-8') as f2:
        for count, line1 in enumerate(f1):
            line2 = f2.readline()
            if line1 != line2:
                print(f"The files are not identical. Line { count + 1} is different.")
                print(line1)
                print("is not the same as:")
                print(line2)

                return
    print("Identical files")

def exercice2(file_path1, file_path2):
    with open(file_path1, 'r', encoding = 'utf-8') as f1, open(file_path2, 'w', encoding = 'utf-8') as f2:
        for count, line in enumerate(f1):
            split_line = line.split(' ')
            for word in split_line:
                f2.write(word)
                f2.write(' ' * 3)

def exercice3(path_grades, path_marks):
    with open(path_grades, mode = 'r', encoding = 'utf-8') as f1, open(path_marks, mode = 'w', encoding = 'utf-8') as f2:
        for count, line in enumerate(f1):
            grade = line.split() # [grade]
            grade_value = float(grade[0])
            for key, value in PERCENTAGE_TO_LETTER.items():
                if grade_value > PERCENTAGE_TO_LETTER[key][0]:
                    f2.write(str(grade_value))
                    f2.write(' ')
                    f2.write(key)
                    f2.write('\n')
                else:
                    continue

def delete_recipe(dictionary):
    name = input("Entrez le nom de la recette que vous voulez supprimer.\n")

    if name in dictionary:
        del dictionary[name]
        print("La recette est supprimée!")
    else:
        print("Cette recette n'existe pas!")

    return dictionary

def exercice4(recipes_path):
    if path.exists(recipes_path):
        with open(recipes_path, 'rb') as f:
            recipes = pickle.load(f)
    else:
        recipes = dict()

    while True:
        choice = input("Choisissez une option: \n a) Ajouter une recette \n b) Modifier une recette \n c) Supprimer une recette \n d) Afficher une recette \n e) Quitter le programme\n").strip()

        if choice == 'a':
            recipes = add_recipes(recipes)
        elif choice == 'b':
            recipes = add_recipes(recipes)
        elif choice == 'c':
            recipes = delete_recipe(recipes)
        elif choice == 'd':
            print_recipe(recipes)
        elif choice == 'e':
            break
        else:
            print("L'option choisie n'est pas valide!")

def exercice5(path_file, path_file_text):
    numbers = []
    with open(path_file, mode = 'r', encoding = 'utf-8') as f1, open(path_file_text, mode = 'w', encoding = 'utf-8')as f2:
        for line in f1:
            words = line.split()
            for word in words:
                for letter in word:
                    if letter.isnumeric() == False:
                        break
                    else:
                        numbers.append(int(word))
        numbers.sort()
        for number in numbers:
            f2.write(str(number))
            f2.write('\n')

    numbers.sort()

def exercice6(example_path, write_path):
    with open(example_path, mode = 'r', encoding = 'utf-8') as f1, open(write_path, mode = 'w', encoding = 'utf-8') as f2:
        for count, line in enumerate(f1):
            if count % 2 == 0:
                f2.write(line)


if __name__ == '__main__':
    # TODO: Appelez vos fonctions ici
    # exercice2('exemple.txt', 'mina.txt')
    # exercice3('notes.txt', 'upgraded_notes.txt')
    # exercice4('./recettes.p')
    exercice5('exemple.txt', 'amogus.txt')
    exercice6('amogus.txt', 'amogus2.txt')
    pass
