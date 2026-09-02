from colorama import Fore, Back, Style, init

init()

print(Fore.GREEN + "This is green text")
print(Back.YELLOW + "This is text on a yellow background")
print(Style.BRIGHT + "This is bright text" + Style.RESET_ALL)
print("Back to normal text")