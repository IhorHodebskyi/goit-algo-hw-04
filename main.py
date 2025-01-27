from pathlib import Path
from typing import TypedDict
import sys
from colorama import Fore, init




salary_file_path = Path('salary_file.txt')

def total_salary(path: str)-> None:
    """
    Print total salary and average salary from given file with salaries.

    The given file should contain lines in the format:
    <name>,<salary>

    The function reads the file, sums up all salaries, and prints total salary
    and average salary (integer division of total salary by number of employees).
    """
    with open(path, 'r', encoding='utf-8') as file:
        salary_list = [int(line.strip().split(',')[-1]) for line in file]
    total = sum(salary_list)
    average = total / len(salary_list)
    return (total, average)








class CatInfo(TypedDict):
    id: str
    name: str
    age: str

def get_cats_info(path: str)-> list[CatInfo]:
    """
    Reads a file with info about cats and returns a list of dictionaries.
    
    The given file should contain lines in the format:
    <id>,<name>,<age>
    
    The function reads the file, creates a list of dictionaries 
    with the following keys: id, name, age and returns it.
    """
    cats_info_list = []
    with open(path, 'r', encoding='utf-8') as file:
        for line in file:
            parts = line.strip().split(',')
            cats_info_list.append({"id": parts[0], "name": parts[1], "age": parts[2]})
    return cats_info_list

cats_info_path = Path("cats_info.txt")





def list_directory(directory_path: Path, level=0)-> None:
    """
    Prints a tree-like structure of the given directory to the console.

    The function takes a Path object as an argument and prints all its contents
    (both files and directories) to the console in a tree-like structure. All
    directories are printed with a cyan color and a folder icon, all files are
    printed with a green color and a file icon. The nesting level of each
    element is represented by indentation. The function is recursive, i.e. it
    calls itself for each subdirectory it encounters.
    """
    indent = "  " * level
    init(autoreset=True)
    for element in directory_path.iterdir():
            if element.is_dir():
                print(f"{indent}{Fore.CYAN}📂 {element.name}")
                list_directory(element, level + 1)
            elif element.is_file():
                print(f"{indent}|{Fore.GREEN}📜 {element.name}")



def get_path_from_input()-> None:
    """
    Retrieves a directory path from command line arguments or user input.

    Checks if the path provided is a directory. If it is, prints its contents
    in a tree-like structure. If not, prints an error message. If no command
    line argument is provided, prompts the user to input a path.

    Returns:
        None
    """

    if len(sys.argv) > 1:
        directory_path = sys.argv[1]
    else:
        directory_path = input("Input path: ")
    part = Path(directory_path)
    if not part.is_dir():
        print(f"{Fore.RED}Вказаний шлях не є директорією або не існує.")
        return
    list_directory(part)


if __name__ == "__main__":
    print(total_salary(salary_file_path))

    cats_info = get_cats_info(cats_info_path)
    print(cats_info)

    get_path_from_input()