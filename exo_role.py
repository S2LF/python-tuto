from random import randint

me = 50
enemy = 50
nb_pot = 3
choice_list = ["1", "2"]

while me > 0 and enemy > 0:
    choice = input("Souhaitez-vous attaquer ⚔ (1) ou utiliser une potion 🧪 (2) ? ")

    if choice in choice_list:
        if int(choice) == 1:
            my_damage = randint(5, 10)
            enemy -= my_damage
            print(f"Vous avez infligé {my_damage} points de dégâts à l'ennemi ⚔ . Il lui reste {'0' if enemy < 0 else enemy} points de vie ❤ .")
            if enemy <= 0:
                break
            enemy_damage = randint(5, 15)
            me -= enemy_damage
            print(f"L'ennemi a infligé {enemy_damage} points de dégâts à vous ⚔ . Il vous reste {'0' if me < 0 else me} points de vie ❤ .")
            if me <= 0:
                break
        elif int(choice) == 2:
            if nb_pot > 0:
                nb_pot -= 1
                heal = randint(15, 50)
                me += heal
                print(f"Vous avez récupéré {heal} points de vie ❤{'❤' if heal > 25 else ''}{'❤' if heal > 35 else ''}. Vous avez maintenant {me} points de vie ❤ .")
                print(f"{'Il ne vous reste que '+str(nb_pot) if nb_pot >= 1 else 'Il ne vous reste plus de'} 🧪 potion{'s' if nb_pot > 1 else ''}.")
                enemy_damage = randint(5, 15)
                me -= enemy_damage
                print('Vous passez votre tour...')
                print(f"L'ennemi vous a infligé {enemy_damage} points de dégâts ⚔ . Il vous reste {'0' if me < 0 else me} points de vie ❤ .")
                if me <= 0:
                    break
                enemy_damage = randint(5, 15)
                me -= enemy_damage
                print(f"L'ennemi a infligé {enemy_damage} points de dégâts à vous ⚔ . Il vous reste {'0' if me < 0 else me} points de vie ❤ .") 
                if me <= 0:
                    break
            else :
                print('Vous n\'avez plus de potion 🧪 😥.')
    else :
        print("Veuillez entrer un choix valide. 😉")
        continue
    print('-' * 50)

if me <= 0:
    print("Vous avez perdu ! 😥")
elif enemy <= 0:
    print("Vous avez gagné ! 🎉🎉🎉")

