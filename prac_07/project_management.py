"""CP1404 Practical - My Project Management Program

Estimate: 60min
Actual: 35min

Hard to tell how my estimating is going,
alot of distractions at home when working on the big excercises
for smaller excercises estimating is pretty good.
"""

import datetime
from project import Project


def main():
    """Runs functions based on a user input from menu"""
    choice = get_menu_choice()
    while choice != "Q":
        if choice == "L":
            file = input("please enter filename:")
            try:
                projects = load_projects(file)
            except ValueError:
                print("please enter correct file name including extensions eg. projects.txt")
                file = input("please enter filename:")
                projects = load_projects(file)
            choice = get_menu_choice()
        elif choice == "S":
            save_projects(projects,file)
            choice = get_menu_choice()
        elif choice == "D":
            display_projects(projects)
            choice = get_menu_choice()
        elif choice == "F":
            date = input("Show projects that start after date (dd/mm/yy):")
            formatted_date = format_date(date)
            filter_projects(formatted_date, projects)
            choice = get_menu_choice()
        elif choice == "A":
            add_project()
            choice = get_menu_choice()
        elif choice == "U":
            update_project()
            choice = get_menu_choice()
        else:
            break

    print("thanks")

def load_projects(file):
    "loads a file and returns a list of projects contained in it"
    project_list = []
    in_file = open(file, 'r')
    in_file.readline()
    for line in in_file:
        parts = line.strip().split()
        project = Project(parts[0], parts[1], parts[2], parts[3], parts[4])
        project_list.append(project)
    return project_list

def save_projects(project_list, file):
    project_strings_list = []
    for project in project_list:
        project_strings = f"\n{project.name}\t{project.date}\t{project.priority}\t{project.cost}\t{project.percent}\t"
        project_strings_list.append(project_strings)
    out_file = open(file, 'w')
    out_file.writelines(project_strings_list)

def display_projects(project_list):
    completed = []
    incomplete = []
    for project in project_list:
        if project.percent == 100:
            completed.append(project)
        else:
            incomplete.append(project)
    completed.sort()
    incomplete.sort()
    print("Complete Projects:")
    for project in completed:
        print(project)
    print("Incomplete Projects:")
    for project in incomplete:
        print(project)

def filter_projects(formatted_date, project_list):
    project_list.sort()
    for project in project_list:
        if project.date >= formatted_date:
            print(project)

def add_project()






def format_date():
    date_string = input("Date (d/m/yyyy): ")  # e.g., "30/9/2022"
    date = datetime.datetime.strptime(date_string, "%d/%m/%Y").date()
    print(f"That day is/was {date.strftime('%A')}")
    print(date.strftime("%d/%m/%Y"))
    return date


def get_menu_choice():
    """Gets user input from menu."""
    menu = """- (L)oad projects  
- (S)ave projects  
- (D)isplay projects  
- (F)ilter projects by date
- (A)dd new project  
- (U)pdate project
- (Q)uit"""
    print(menu)
    choice = input(">>> ").upper()
    while choice != "L" and choice != "S" and choice != "D" and choice != "F" and choice != "A" and choice != "U" and choice != "Q":
        print("Invalid option")
        print(menu)
        choice = input(">>> ").upper()
    return choice

main()
