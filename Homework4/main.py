from cruds import *
import sqlite3,csv
import random as r
while(True):
    print("*****************")
    print("Tips Main Menu")
    print("*****************")
    print("1.Show Tips")
    print("2.Add Tips")
    print("3.Update Tips")
    print("4.Delete Tips")
    print("5.Tips by time")
    print("6.Search by keyword")
    print("7.Random Tip of the day")
    choice1=input("Enter an option(-1 to exit and export):")
    if choice1=="-1":
          break
    if choice1=="1":
        cat_count=display_categories()
        try:
            cat_id=int(input("Enter Category:"))
        except ValueError:
            print("Not a valid integer")
            continue
        if cat_id not in cat_count:
              print("Not a valid category")
              continue
        display_tips_filtered(cat_id)
    elif choice1=="2":
         print("Add New Tip")
         print("*******************")
         t=input("Enter Tip Title:")
         c=input("Enter Content:")
         cat_count=display_categories()
         try:
               ci=int(input("Enter Category Id:"))
         except ValueError:
               print("Not a valid integer")
               continue
         if ci not in cat_count:
              print("Not a valid category")
              continue
         try:
               f=int(input("Favourite(1(yes)/0(no)):"))
         except ValueError:
               print("Not a valid integer")
               continue
         if f not in [0,1]:
              print("Not a valid option")
              continue
         create_tips(t,c,ci,f)
    elif choice1=="3":
             display_tips()
             try:
               target_id=int(input("Enter tip id:"))
             except ValueError:
               print("Not a valid integer")
               continue
             if target_id not in tips_dict.keys():
              print("Not a valid option")
              continue
             print("*****************")
             print("1.Update Title")
             print("2.Update Content")
             print("3.Update Category")
             print("4.Set favourite" if tips_dict[target_id][4]==0 else "4.Unset favourite")
             choice2=input("Enter the answer:")
             if choice2=="1":
                   new_title=input("Enter the new title:")
                   update_title(target_id,new_title)
             elif choice2=="2":
                   new_content=input("Enter new content:")
                   update_content(target_id,new_content)
             elif choice2=="3":
                   cat_count=display_categories()
                   try:
                        new_category=int(input("Enter new category:"))
                   except ValueError:
                        print("Not a valid integer")
                        continue
                   if new_category not in cat_count:
                        print("Not a valid category")
                        continue
                   update_category(target_id,new_category)
             elif choice2=="4":
                    if tips_dict[target_id][4]==0:
                          update_favourite(target_id,1)
                    else:
                          update_favourite(target_id,0)
    elif choice1=="4":
            display_tips()
            try:
               target_id=int(input("Enter tip id:"))
            except ValueError:
               print("Not a valid integer")
               continue
            if target_id not in tips_dict.keys():
              print("Not a valid option")
              continue
            delete_tips(target_id)
    elif choice1=="5":
             display_by_date()
    elif choice1=="6":
             keyword=input("Enter a keyword:")
             search_by_keyword(keyword)
    elif choice1=="7":
             print("Tip of the day")
             print("****************")
             c=r.choice(list(tips_dict.keys()))
             show_tip_by_index(c)

with sqlite3.connect("tips_database.db") as conn, open("tips.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([d[0] for d in conn.execute("SELECT * FROM tips").description])
    writer.writerows(conn.execute("SELECT * FROM tips"))