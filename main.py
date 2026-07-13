import random
import time

inventory = []
hp = 100
rooms_passed = 0

while True:
    action = input("Что делаешь? (искать / лечиться / ворота / сдаться): ").lower()
    
    if action == "сдаться":
        print("Ты сдался и умер в одиночестве..")
        break
        
    elif action == "искать":
        rooms_passed += 1
        hp_lost = random.randint(10, 25)
        hp -= hp_lost
        print(f"Осталось здоровья: {hp} | Инвентарь: {inventory}")
        
        if hp <= 0:
            print("Провалено.. Здоровье закончилось.")
            break
        else:
            print("Обыскиваешь комнату...")
            time.sleep(2)
            item_found = random.randint(1, 3)
            if item_found == 1:
                print("Ты нашел чип!")
                inventory.append("чип")
            elif item_found == 2:
                print("Ого, среди хлама нашлась аптечка! (+30 HP)")
                inventory.append("аптечка")
            else:
                print("Ничего интересного, только старый хлам.")
                
    elif action == "лечиться":
        if "аптечка" in inventory:
            inventory.remove("аптечка")
            hp += 30
            if hp > 100: 
                hp = 100
            print(f"Ты использовал аптечку. Здоровье восстановлено до {hp}!")
        else:
            print("У тебя нет аптечек! Ищи внимательнее в комнатах.")

    elif action == "ворота":
        chips_amount = inventory.count("чип")
        print(f"Чипов: {chips_amount}")
        if chips_amount >= 3:
            print("\n========================================")
            print(" ДВЕРИ ОТКРЫВАЮТСЯ... СВЕЖИЙ ВОЗДУХ!")
            print(f" ТЫ УСПЕШНО СБЕЖАЛ ЗА {rooms_passed} КОМНАТ(Ы)!")
            print("========================================")
            break
        else:
            print("Ищи 3 чипа, у тебя недостаточно.")
            
    else:
        print("Неизвестная команда! Пиши: искать, лечиться, ворота или сдаться")

if hp <= 0 or action == "сдаться":
    print("\n" + "="*40)
    print(" ИГРА ОКОНЧЕНА. БУНКЕР ЗАБРАЛ ЕЩЕ ОДНУ ЖИЗНЬ...")
    print("="*40)

input("\nНажми Enter, чтобы закрыть игру...")
