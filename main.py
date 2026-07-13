import random
import time
inventory = []
hp = 100
rooms_passed = 0
while True:
    action = input("Что делаешь? (искать / ворота / сдаться): ").lower()
    if action == "сдаться":
        print("ты умер в одиночестве..")
        break
    elif action == "искать":
        rooms_passed += 1
        hp_lost = random.randint(10, 25)
        hp -= hp_lost
        print(f"Осталось здоровья: {hp} | Инвентарь: {inventory}")
        if hp <= 0:
            print("Провалено..")
            break
        else:
            print("Обыскиваешь комнату...")
            time.sleep(2)
            
            chip_found = random.randint(1, 3)
            if chip_found == 1:
                print("Ты нашел чип!")
                inventory.append("чип")
            else:
                print("Ничего интересного, только старый хлам.")
    elif action == "ворота":
        chips_amount = inventory.count("чип")
        print(f"Чипов: {chips_amount}")
        if chips_amount >= 3:
            print("Двери открываются.. Свежий воздух!")
            print(f"Ты сбежал за {rooms_passed} комнат(ы)!")
            break
        else:
            print("Ищи 3 чипа, у тебя недостаточно")
    else:
        print("Неизвестная команда! Пиши: искать, ворота или сдаться")