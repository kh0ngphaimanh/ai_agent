from functions.get_files_info import get_file_info

def main():
    print("Result for current directory:")
    print(get_file_info("calculator", "."))
    print("Result for 'pkg' directory:")
    print(get_file_info("calculator", "pkg"))
    print("Result for '/bin' directory:")
    print(get_file_info("calculator", "/bin"))
    print("Result for '../' directory:")
    print(get_file_info("calculator", "../"))

if __name__ == "__main__":
    main()