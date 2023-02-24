import students as st

key = 1

while key != 0:
    key = int(input("Enter your choice: "))
    s = st.students()

    if key == 1:
        print("Student list:")
        s.show()
    else:
        break

