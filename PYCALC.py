import colorama
import math

colorama.init()

print(f"{colorama.Fore.LIGHTBLUE_EX}P{colorama.Fore.YELLOW}Y{colorama.Fore.GREEN}CALC{colorama.Fore.LIGHTBLACK_EX} v1.0")
print(f"© Herman Kaluhin - all rights reserved{colorama.Fore.RESET}")

pi = 3.141592653589793238462643
g = 9.8

color_green = True
while True:  
    try:

        calc = eval(input(">"))

        if calc == "cr":
            for clr in range(100):
                print()
        
        if calc == "nc":
            color_green = False
        
        if calc == "c":
            color_green = True

        if color_green == True:
            print(f"{colorama.Back.GREEN}{colorama.Fore.BLACK} {calc} {colorama.Back.RESET}{colorama.Fore.RESET}")
        else:
            print(f"{calc}")

    except Exception as e:
        print(f"Error {e}")
