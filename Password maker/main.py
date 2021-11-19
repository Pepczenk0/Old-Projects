import random
import write

class Lists:
    list_of_letters =  ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    list_of_signs =['!','@','#','$','%','&','*','(',')']
    random_letter = random.choice(list_of_letters)
    password = []
    random_amount = random.randint(20,50)
    random_sign = random.choice(list_of_signs)
def make_password():

    for i in range(Lists.random_amount):
        choice = random.randint(1, 3)
        if choice == 1:
            """FOR INTEGERS"""
            random_amount = random.randint(20, 50)

            Lists.password.append(random_amount)


        elif choice == 2:
            """FOR LETTERS"""
            random_letter = random.choice(Lists.list_of_letters)
            Lists.password.append(random_letter)

        elif choice == 3:
            random_sign = random.choice(Lists.list_of_signs)
            Lists.password.append(random_sign)


    print("============================================================================================================================================================================")
    sort_char()

def sort_char():
    final_password = ''.join([str(item) for item in Lists.password])
    print('The Random password is: ' + final_password)
    write.Write.write(write,final_password)
    print("============================================================================================================================================================================")

make_password()