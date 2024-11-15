FILE_NAME = "books.txt"


def add_book():
    
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()
    except FileNotFoundError:
        books = []

    if len(books) < 10:  
        book_name = input("اسم کتاب را وارد کنید: ").strip()
        with open(FILE_NAME, "a") as file:  
            file.write(book_name + "\n")
        print(f"کتاب '{book_name}' با موفقیت اضافه شد.")
    else:
        print("ظرفیت لیست کتاب‌ها پر شده است!")


def show_books():
    try:
        with open(FILE_NAME, "r") as file:
            books = file.readlines()
    except FileNotFoundError:
        books = []

    if books:
        print("\nکتاب‌های ثبت‌شده:")
        for index, book in enumerate(books, 1):
            print(f"{index}. {book.strip()}")
    else:
        print("هیچ کتابی ثبت نشده است.")


def main():
    while True:
        print("\nمنوی اصلی:")
        print("1. اضافه کردن کتاب")
        print("2. نمایش کتاب‌ها")
        print("3. خروج")
        
        choice = input("لطفاً یک گزینه وارد کنید (1/2/3): ")
        
        if choice == "1":
            add_book()
        elif choice == "2":
            show_books()
        elif choice == "3":
            print("خروج از برنامه...")
            break
        else:
            print("لطفاً گزینه معتبر وارد کنید.")


main()
