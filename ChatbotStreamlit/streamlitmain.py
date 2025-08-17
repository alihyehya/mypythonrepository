from streamlitutils import *
def main():
    header()
    a=main_menu()
    if a:
        container=st.container(border=True)
        container.subheader("Conversation:")
        container.write("**You**:")
        container.write(a)
        container.write("**Bot**:")
        container.write(generate_answer(check_num(a)))

if __name__=="__main__":
    main()
    
