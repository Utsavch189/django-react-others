def validate_book_name(value):
        print(value)
        if len(value)<10:
            raise Exception('book_name should be above 10 chars!')