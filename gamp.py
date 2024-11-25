import time
import random

def print_road(player_pos, obstacles):
    """Yo'lni matnda chizish."""
    road = ["|       |"] * 10
    for obstacle in obstacles:
        road[obstacle] = "|   #   |"
    road[player_pos] = "|   P   |"  # O'yinchi avtomobili
    print("\n" * 2)  # Toza ekran uchun
    for line in road:
        print(line)
    print("=========")

def move_obstacles(obstacles):
    """To'siqlarni pastga siljitish."""
    return [o + 1 for o in obstacles if o < 9]

def check_collision(player_pos, obstacles):
    """To'qnashuvni tekshirish."""
    return player_pos in obstacles

def main():
    print("Trafik Rider: Matnli versiyasi")
    print("O'yinni boshlash uchun ENTER tugmasini bosing!")
    input()

    player_pos = 8
    obstacles = []
    score = 0

    try:
        while True:
            # To'siqlarni yangilash
            if random.random() < 0.3:  # Tasodifiy to'siq yaratish
                obstacles.append(0)
            obstacles = move_obstacles(obstacles)

            # To'qnashuvni tekshirish
            if check_collision(player_pos, obstacles):
                print("O'yin tugadi!")
                print(f"Jami ball: {score}")
                break

            # Yo'lni chizish
            print_road(player_pos, obstacles)

            # Harakat qilish
            print("Harakat: [w] yuqoriga | [s] pastga | [q] chiqish")
            action = input(">>> ").strip().lower()

            if action == "w" and player_pos > 0:
                player_pos -= 1
            elif action == "s" and player_pos < 9:
                player_pos += 1
            elif action == "q":
                print("O'yindan chiqdingiz.")
                break

            score += 1
            time.sleep(0.3)

    except KeyboardInterrupt:
        print("\nO'yin to'xtatildi.")

if __name__ == "__main__":
    main()
