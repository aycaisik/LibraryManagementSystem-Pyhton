print("Welcome to Library App")
print("press 1: Lists all books")
print("press 2: Lists all the books that are checked out")
print("press 3: Add a new book")
print("press 4: Search a book by ISBN number")
print("press 5: Search a book by name")
print("press 6: Check out a book to a student")
print("press 7: Lists all the students")
print("press 8: Lists top 3 most checked out books in the library history")
print("press 9: List top 3 most checked out books in the library history ")
print("press 0: Exit")

booktxt = open(r"Books.txt","r",encoding="utf-8") #try except file not found !!
studenttxt = open(r"students.txt","r",encoding="utf-8")

students = {} #in this part I created dictionary for searching students
books = {}
def createStudentList():
    studenttxt = open(r"students.txt", "r")
    students = {}
    for line in studenttxt :
        linesp = line.split(" ")
        id = linesp[0]
        name = linesp[1]
        surname =linesp[2]
        students[id] = [id +","+ name +"," + surname]
studenttxt.close()

for line1 in booktxt :
    linesp1 = line1.split(",")
    ISBN = linesp1[0]
    Name = linesp1[1]
    Author =linesp1[2]
    Check = linesp1[3].replace("\n","")
    books[ISBN] = [ISBN, Name, Author,Check]
booktxt.close()

while True:

    Action = int(input("please choose an action:   "))

    if Action == 0:
        print("Goodbye!!")
        break

    if Action == 1:
        for i in books:
            print(books[i])

    if Action == 2:
        for i in books:
            if books[i][3] == "T":
                print(books[i])

    if Action == 3:
        newISBN = input("please enter ISBN")
        newName= (input("please enter book name"))
        newAuthor = input("please enter author name")
        newCheck = "F"
        books[newISBN]  = [newISBN,newName,newAuthor,newCheck]

    if Action == 4:
        tempISBN = input("please enter ISBN that you want to find") #isbn not found
        for i in books:
            if books[i][0] == tempISBN:
                print(books[i])

    if Action == 5:
        tempName = input("please enter book name that you want to find")

        for i in books:
            if books[i][1] == tempName:
                print(books[i])

    if Action == 6:
        tempid = int(input("please enter your id")) #if id not found
        tempisbn = input("please enter book ISBN")

        if books[tempisbn][3] == "T":
            print("The book is not in the library")
        else:
            books[tempisbn][3] = "T"
            students[tempid][3] = books[tempisbn][1] , students[tempid][3]

    if Action == 7:
        for i in students.keys():
            print(students[i])

