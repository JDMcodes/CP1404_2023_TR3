"""
CP1404 Practical - Client code to use the Programming class.
estimate: 30min
actual:25 min
"""

from programming_language import ProgrammingLanguage


def main():
    python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
    ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
    visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)
    print(python)
    languages_list = [python, ruby, visual_basic]
    print("The dynamically typed languages are:")
    for i in range(0, len(languages_list)):
        if languages_list[i].is_dynamic():
            print(f"{languages_list[i].name}")


main()
