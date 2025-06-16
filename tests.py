from functions.get_file_content import get_file_content

if __name__ == "__main__":

    print("Testing main.py:")
    print(get_file_content("calculator", "main.py"))
    
    print("\nTesting pkg/calculator.py:")
    print(get_file_content("calculator", "pkg/calculator.py"))
    
    print("\nTesting /bin/cat (should return error):")
    print(get_file_content("calculator", "/bin/cat"))
