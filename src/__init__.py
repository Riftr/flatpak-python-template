# the main file the project will run from as defined in pyproject.toml
import colorama as col
from PIL import Image
import os


def run_application():
    local_path = os.path.abspath(os.path.dirname(__file__))
    img_path = local_path + "/resources/python-logo.png"

    if os.path.exists(img_path):
        im = Image.open(img_path)
        print(col.Fore.GREEN + "This is just a sample project running successfully")
        print(col.Fore.GREEN + "The python-logo.png file had the following properties:")
        print(col.Fore.CYAN + im.format, im.size, im.mode)
        print(col.Style.RESET_ALL)
        return im.format
    else:
        print(col.Fore.RED + "Couldn't load python-logo.png")
        print(col.Style.RESET_ALL)
        return None


if __name__ == "__main__":
    run_application()
    input(col.Fore.MAGENTA + "Press any key to exit...")
    print(col.Style.RESET_ALL)