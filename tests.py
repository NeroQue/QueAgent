from functions.write_file import write_file

if __name__ == "__main__":
    print("Testing write to lorem.txt:")
    print(write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum"))

    print("\nTesting write to pkg/morelorem.txt:")
    print(write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet"))

    print("\nTesting write to /tmp/temp.txt (should return error):")
    print(write_file("calculator", "/tmp/temp.txt", "this should not be allowed"))
