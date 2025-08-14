from utils import *
more=True
header()
while(more):
    a=main_menu()
    print("***************************************************")
    print(generate_answer(check_num(a)))
    print("***************************************************")
    more=check_proceed()

