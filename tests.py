from functions.get_files_info import get_files_info

if __name__ == "__main__":
    print("Testing current directory:")
    print(get_files_info("calculator", "."))

    print("\nTesting pkg directory:")
    print(get_files_info("calculator", "pkg"))

    print("\nTesting /bin directory:")
    print(get_files_info("calculator", "/bin"))

    print("\nTesting parent directory:")
    print(get_files_info("calculator", "../"))