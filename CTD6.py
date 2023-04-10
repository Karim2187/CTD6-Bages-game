import random
from PIL import Image
from PIL import ImageDraw
def Game():
    bags = [10,10,10]
    user_name = input("Username: ")
    player = user_name
    while 1:
        if player == user_name:
            print(bags) 
            while 1:
                try:
                    choice = int(input("Select a bag: "))
                    if choice not in [1,2,3]:
                        raise ValueError("Chose from bags 1,2 or 3")
                    break
                except:
                    print("Enter a valid bag number from 1 to 3")
            while 1:
                try:
                    o_num = int(input("Select number of objects: "))  
                    if o_num not in range(1,6):
                        raise ValueError(" Max selection is 5")
                    break
                except:
                    print("Select up to 5 objects only")
            bags[choice - 1] -= o_num
            print(f"you removed {o_num} from bag {choice}")
            player = "computer"
        else:
            comp = [i for i, x in enumerate(bags) if x != 0]
            choice = random.choice(comp) + 1
            o_num = random.randint(1,5)
            if o_num > bags[choice - 1]:
                o_num = bags[choice - 1]
            bags[choice - 1] -= o_num
            print(f"Computer removed {o_num} from bag {choice}")
            player = user_name
        if sum(bags) == 0:
            if player == user_name:
                Results_lose()
            else:
                Results_won(user_name)
            break


def Results_won(user_name):
    img = Image.open('won.jpg')
    I1 = ImageDraw.Draw(img)
    I1.text((28, 55), user_name, fill=(255, 0, 0))
    img.show()
def Results_lose():
    img = Image.open('images.jpeg')
    I1 = ImageDraw.Draw(img)
    I1.text((55, 60), " ", fill=(255, 0, 0))
    img.show()
Game()