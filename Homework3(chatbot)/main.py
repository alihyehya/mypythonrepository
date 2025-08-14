from utils import *
more=True
header()
while(more):
    a=main_menu()
    if(a=="-1"):
        break
    print("***************************************************")
    print(generate_answer(check_num(a)))
    print("***************************************************")
    more=check_proceed()

print ("See you Later!")