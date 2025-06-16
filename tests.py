from functions.run_python import run_python_file


if __name__ == "__main__":
    print("Test 1: Running calculator/main.py")
    print(run_python_file("calculator", "main.py"))
    print("\n" + "-" * 50 + "\n")

    print("Test 2: Running calculator/tests.py")
    print(run_python_file("calculator", "tests.py"))
    print("\n" + "-" * 50 + "\n")

    print("Test 3: Attempting to run file outside working directory")
    print(run_python_file("calculator", "../main.py"))
    print("\n" + "-" * 50 + "\n")

    print("Test 4: Attempting to run non-existent file")
    print(run_python_file("calculator", "nonexistent.py"))
