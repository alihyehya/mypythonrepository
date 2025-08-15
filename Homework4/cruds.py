import sqlite3
def read_tips():
    conn = sqlite3.connect('tips_database.db')
    cursor = conn.cursor()
    tips_dict={}
    for row in cursor.execute("SELECT * FROM tips"):
        l=list(row)
        tips_dict[l[0]]=l
    conn.close()
    return tips_dict
tips_dict=read_tips()
def display_categories():
    cat_range=[]
    update_dict()
    counter=0
    conn = sqlite3.connect('tips_database.db')
    cursor = conn.cursor()
    print("Categories:")
    for row in cursor.execute("SELECT * FROM categories"):
        l=list(row)
        cat_range+=[l[0]]
        print(l[0],".",l[1])
    conn.close()
    return cat_range

def display_by_date():
    update_dict()
    sorted_tips = sorted(
        tips_dict.items(),
        key=lambda kv: kv[1][5],
        reverse=True
    )
    for k,v in sorted_tips:
        print(k,v)

def search_by_keyword(keyword):
    update_dict()
    keyword_lower = keyword.lower()
    matched_dict = {
        tip_id: row
        for tip_id, row in tips_dict.items()
        if keyword_lower in str(row[1]).lower()
        or keyword_lower in str(row[2]).lower() 
    }
    for i in matched_dict:
     print (tips_dict[i][0],".",tips_dict[i][1],end=" ")
     print("★" if tips_dict[i][4] == 1 else "☆",":",end=" ")
     print(tips_dict[i][2])



def display_tips_filtered(cat_id):
    update_dict()
    for i in tips_dict:
        if tips_dict[i][3]==cat_id:
            print (tips_dict[i][0],".",tips_dict[i][1],end=" ")
            print("★" if tips_dict[i][4] == 1 else "☆",":",end=" ")
            print(tips_dict[i][2])

def display_tips():
    update_dict()
    for i in tips_dict:
        print (tips_dict[i][0],".",tips_dict[i][1],end=" ")
        print("★" if tips_dict[i][4] == 1 else "☆",":",end=" ")
        print(tips_dict[i][2])


def create_tips(t, c, ci, f=0):
    update_dict()
    conn = sqlite3.connect('tips_database.db')
    cursor = conn.cursor()
    cursor.execute("INSERT INTO tips (title, content, category_id, is_favourite) VALUES (?, ?, ?, ?)", (t, c, ci,f))
    conn.commit()
    conn.close()
    update_dict()

def update_title(target_id,new_title):
    update_dict()
    conn = sqlite3.connect('tips_database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tips SET title = ? WHERE id = ?", (new_title,target_id))
    conn.commit()
    conn.close()
    update_dict()

def update_content(target_id,new_content):
    update_dict()
    conn = sqlite3.connect('tips_database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tips SET content = ? WHERE id = ?", (new_content,target_id))
    conn.commit()
    conn.close()
    update_dict()

def update_category(target_id,new_category):
    update_dict()
    conn = sqlite3.connect('tips_database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tips SET category_id = ? WHERE id = ?", (new_category,target_id))
    conn.commit()
    conn.close()
    update_dict()

def update_favourite(target_id,new_favourite):
    update_dict()
    conn = sqlite3.connect('tips_database.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE tips SET is_favourite = ? WHERE id = ?", (new_favourite,target_id))
    conn.commit()
    conn.close()
    update_dict()

def delete_tips(target_id):
    update_dict()
    conn = sqlite3.connect('tips_database.db')
    cursor = conn.cursor()
    cursor.execute("DELETE FROM tips WHERE id = ?", (target_id,))
    conn.commit()
    conn.close()
    update_dict()

def show_tip_by_index(index):
     update_dict()
     print (tips_dict[index][0],".",tips_dict[index][1],end=" ")
     print("★" if tips_dict[index][4] == 1 else "☆",":",end=" ")
     print(tips_dict[index][2])
def update_dict():
    new_data = read_tips()
    tips_dict.clear()       
    tips_dict.update(new_data) 








