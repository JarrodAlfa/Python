import random
x = 0
groepje = 0
groepjes = int(input("Hoeveel groepen wil je?: "))
personen = int(input("Hoeveel personen wil je?: "))
huidigeNaam = 0
namen = ["Daan A.", "Abdul", "Yaroslav", "Beam", "Luo Xi", "Dima", "Damiën", "Matthew", "Ahmed", "Winay", "Jarrod", "Mohammad", "Jaimy", "Maurizio", "Jay-Quan", "Safa", "Kiyara", "Marouf", "Annemare", "Semen", "Ajay", "Bert", "Rogier", "Daan V.", "Kateryna"]

for i in range(groepjes):
    groepje += 1
    print("___________")
    print(f"groep {groepje}:")
    print("___________")
    for i in range(personen):
        huidigeNaam = random.choice(namen)
        print(huidigeNaam)
        namen.remove(huidigeNaam)
        i += 1