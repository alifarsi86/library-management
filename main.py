from mylibrary.library import library
library = library()
if __name__=="__main__":
    while True:
        print('1.add book')
        print('2.remove book')
        print('3.search book')
        print('4.show book')
        print('5.exit')
        choice=int(input('enter your choice : '))

        if choice==5:
            break
        elif choice==1:
            title=input('enter book title : ')
            author=input('enter book author : ')
            library.add_book(title, author)
        elif choice==2:
            title=input('enter book title : ')
            library.remove_book(title)
        elif choice==3:
            title=input('enter book title : ')
            library.search_book(title)
        elif choice==4:
            library.show_book()   