import characters as char

def main():
    
    while True:
        char_pick = input(f"pilih character yg ingin dijadikan main hero\n1. {char.kalue.name} ({char.kalue.role})\n2. {char.grogle.name} ({char.grogle.role})\n3. {char.cytia.name} ({char.cytia.role})\n4. {char.halusina.name} ({char.halusina.role})\n(input number only)\n>")
        char_pick = int(char_pick)
        
        if char_pick == 1:
            main_hero = char.kalue.name
            input(f"youre choosing {main_hero} as your main hero ...\n")
            break
        elif char_pick == 2:
            main_hero = char.grogle.name
            input(f"youre choosing {main_hero} as your main hero ...\n")
            break
        elif char_pick == 3:
            main_hero = char.cytia.name
            input(f"youre choosing {main_hero} as your main hero ...\n")
            break
        elif char_pick == 4:
            main_hero = char.halusina.name
            input(f"youre choosing {main_hero} as your main hero ...\n")
            break
        else:
            print("input appropriate answer only ...\n")
            continue

    def main_game():
        if main_hero == 'Kalue':
            input(f"Anda bersama tiga rekan guild anda, Halusina, Grogle, dan Cytia memasuki dungeon ...\n(tekan enter)\n")
        elif main_hero == 'Grogle':
            input(f"Anda bersama tiga rekan guild anda, Halusina, Kalue, dan Cytia memasuki dungeon ...\n(tekan enter)\n")
        elif main_hero == 'Cytia':
            input(f"Anda bersama tiga rekan guild anda, Halusina, Kalue, dan Grogle memasuki dungeon ...\n(tekan enter)\n")
        elif main_hero == 'Halusina':
            input(f"Anda bersama tiga rekan guild anda, Cytia, Kalue, dan Grogle memasuki dungeon ...\n(tekan enter)\n")

        input(f"Didalam dungeon, kalian dicegat oleh dua monster yang berbentuk ular jadi-jadian, dan satu lagi bagai alien berlendir.\nJangan takut dan lawan mereka!\n(tekan enter)\n")
        print("FIGHTING START!\n")

        while True:
            print('pilih hero untuk menyerang lawan tertentu:\n')
            print("   your team      |  dungeon monters  \n"
                "1. Kalue        |  1. Oray          \n"
                "2. Grogle       |  2. Jurig         \n"
                "3. Cytia        |                   \n"
                "4. Halusina     |                   \n")
            print("cara/format memilihnya yaitu adalah dengan mengetik nomor\nsalah satu hero di tim anda, dan kemudian salah satu nomor dari musuhnya.\n")
            
            while True:
                hero_penyerang = input("pilih nomor dari salah satu hero anda (masukan nomor saja)\n> ")
                hero_penyerang = int(hero_penyerang)
                if hero_penyerang == 1 or hero_penyerang == 2 or hero_penyerang == 3 or hero_penyerang == 4:
                    break
                else:
                    print("masukan angka yg tepat saja\n")
            
            while True:
                musuh_yg_diserang = input("pilih nomor dari salah satu musuh anda (masukan nomor saja)\n> ")
                musuh_yg_diserang = int(musuh_yg_diserang)
                if musuh_yg_diserang == 1 or musuh_yg_diserang == 2:
                    break
                else:
                    print("masukan angka yg tepat saja\n")

            if hero_penyerang == 1:
                if musuh_yg_diserang == 1:
                    musuh_yg_diserang = char.oray.name
                elif musuh_yg_diserang == 2:
                    musuh_yg_diserang = char.jurig.name
                
                damage_point, hit_obj = char.kalue.attack(hit_obj=musuh_yg_diserang)
                
                if hit_obj == char.oray.name:
                    char.oray.take_damage(external_damage=damage_point)
                elif hit_obj == char.jurig.name:
                    char.jurig.take_damage(external_damage=damage_point)
            
            elif hero_penyerang == 2:
                if musuh_yg_diserang == 1:
                    musuh_yg_diserang = char.oray.name
                elif musuh_yg_diserang == 2:
                    musuh_yg_diserang = char.jurig.name
                
                damage_point, hit_obj = char.grogle.attack(hit_obj=musuh_yg_diserang)
                
                if hit_obj == char.oray.name:
                    char.oray.take_damage(external_damage=damage_point)
                elif hit_obj == char.jurig.name:
                    char.jurig.take_damage(external_damage=damage_point)

            elif hero_penyerang == 3:
                if musuh_yg_diserang == 1:
                    musuh_yg_diserang = char.oray.name
                elif musuh_yg_diserang == 2:
                    musuh_yg_diserang = char.jurig.name
                
                damage_point, hit_obj = char.cytia.attack(hit_obj=musuh_yg_diserang)
                
                if hit_obj == char.oray.name:
                    char.oray.take_damage(external_damage=damage_point)
                elif hit_obj == char.jurig.name:
                    char.jurig.take_damage(external_damage=damage_point)

            elif hero_penyerang == 4:
                if musuh_yg_diserang == 1:
                    musuh_yg_diserang = char.oray.name
                elif musuh_yg_diserang == 2:
                    musuh_yg_diserang = char.jurig.name
                
                damage_point, hit_obj = char.halusina.attack(hit_obj=musuh_yg_diserang)
                
                if hit_obj == char.oray.name:
                    char.oray.take_damage(external_damage=damage_point)
                elif hit_obj == char.jurig.name:
                    char.jurig.take_damage(external_damage=damage_point)  

            input(" . . . \n")
            print("")
    
    # todo: gak jelas, masih kocak, gak lengkap, musuhnya juga diem aja dan gak nyerang
    main_game()

main()
