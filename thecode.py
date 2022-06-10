import csv
import os

def open_and_read_csv(file_path):
    """open and read a given csv file as a dictionnary and put the values in a given list"""
    liste = []
    with open(file_path, 'r') as file:
        csv_file = csv.DictReader(file)
        for row in csv_file:
            liste.append(row)  
    return liste

def creating_repo(li1, li2):
    """create the folders with given two lists , one containing the student's names while the order contains the subjects"""
    try:
        for i in li2:
            for j in li1:
                os.makedirs("./the_code_result/" + i["Noms"] + " " + i["Prenoms"] + "/" + j["Matieres"])
                with open("./the_code_result/" + i["Noms"] +" "+ i["Prenoms"] + "/" + j["Matieres"] + "/copy.txt", "w") as file:
                    file.write("Your text goes here")
        return 1
    except FileExistsError as e:
        print("File(s) already exist(s)")
        print()
    
def deleting_repo(li1, li2):
    for i in li2:
        for j in li1:
            os.remove("./the_code_result/" + i["Noms"] + " " + i["Prenoms"] + "/" + j["Matieres"] + "/copy.txt")
            os.rmdir("./the_code_result/" + i["Noms"] + " " + i["Prenoms"] + "/" + j["Matieres"])
        os.rmdir("./the_code_result/" + i["Noms"] + " " + i["Prenoms"])


def get_csv_files(identifier):
    while 1:
        if identifier == 1:
            csv_file_path  = input("Enter csv file absolute path for the students: ")
        elif identifier == 2:
            csv_file_path  = input("Enter csv file absolute path for the discipline: ")
        if os.path.exists(csv_file_path) == False:
            print("Path doesn't exists")
        else:
            return csv_file_path


liste_etudiants = open_and_read_csv(get_csv_files(1))
liste_filieres  = open_and_read_csv(get_csv_files(2))

if(creating_repo(liste_filieres, liste_etudiants)):
    print()
    print("THE FOLDERS HAVE BEEN CREATED !!")
    print()
