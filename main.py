from pathlib import Path
from typing import List


SOURCE_PARENT = Path.home().joinpath("Downloads")


def verify(parameter: str, name: str) -> None:
    """
    Verify if parameter is blank, if so, raise ValueError.
    """
    if not parameter or parameter.isspace():
        raise ValueError(f"{name} cannot be blank!")
    if parameter.startswith(" ") or parameter.endswith(" "):
        raise ValueError(f"{name} cannot begin or end with an empty space!")


def main():

    try:
        
        sub_folders : List[str] = ["Sets", "Video"]

        folder = input("Folder: ").strip().title().replace("-", " ")
        verify(parameter = folder, name = "Folder Name")

        source = SOURCE_PARENT.joinpath(folder)
    
        print(f"Creating {source}")
        source.mkdir(exist_ok = False)

        for sub_folder in sub_folders:
            source.joinpath(sub_folder).mkdir(exist_ok = False)
    
    except(FileExistsError, ValueError) as e:
        print(e)

if __name__ == "__main__":
    main()
