import os
import time
print(f"""
░█████╗░██╗░░░██╗████████╗░█████╗░  ██╗░░██╗██╗░░░██╗██████╗░██████╗░██╗░░░░░░█████╗░███╗░░██╗██████╗░
██╔══██╗██║░░░██║╚══██╔══╝██╔══██╗  ██║░░██║╚██╗░██╔╝██╔══██╗██╔══██╗██║░░░░░██╔══██╗████╗░██║██╔══██╗
███████║██║░░░██║░░░██║░░░██║░░██║  ███████║░╚████╔╝░██████╔╝██████╔╝██║░░░░░███████║██╔██╗██║██║░░██║
██╔══██║██║░░░██║░░░██║░░░██║░░██║  ██╔══██║░░╚██╔╝░░██╔═══╝░██╔══██╗██║░░░░░██╔══██║██║╚████║██║░░██║
██║░░██║╚██████╔╝░░░██║░░░╚█████╔╝  ██║░░██║░░░██║░░░██║░░░░░██║░░██║███████╗██║░░██║██║░╚███║██████╔╝
╚═╝░░╚═╝░╚═════╝░░░░╚═╝░░░░╚════╝░  ╚═╝░░╚═╝░░░╚═╝░░░╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═╝░░╚═╝╚═╝░░╚══╝╚═════╝░

░█████╗░░█████╗░███╗░░██╗███████╗██╗░██████╗░██╗░░░██╗██████╗░░█████╗░████████╗░█████╗░██████╗░
██╔══██╗██╔══██╗████╗░██║██╔════╝██║██╔════╝░██║░░░██║██╔══██╗██╔══██╗╚══██╔══╝██╔══██╗██╔══██╗
██║░░╚═╝██║░░██║██╔██╗██║█████╗░░██║██║░░██╗░██║░░░██║██████╔╝███████║░░░██║░░░██║░░██║██████╔╝
██║░░██╗██║░░██║██║╚████║██╔══╝░░██║██║░░╚██╗██║░░░██║██╔══██╗██╔══██║░░░██║░░░██║░░██║██╔══██╗
╚█████╔╝╚█████╔╝██║░╚███║██║░░░░░██║╚██████╔╝╚██████╔╝██║░░██║██║░░██║░░░██║░░░╚█████╔╝██║░░██║
░╚════╝░░╚════╝░╚═╝░░╚══╝╚═╝░░░░░╚═╝░╚═════╝░░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝░░░╚═╝░░░░╚════╝░╚═╝░░╚═╝ ....is here!""")
archq = input("Are you using arch linux(if you aren't script won't work) ?:")
if archq == "y":
    gitq = input("Is git installed?: ")
    if gitq == "y":
       print("Starting installation")
       os.system("git clone https://github.com/Aptivace/hyprland-config")
       os.system("cd hyprland-config")
       print("Changed directory to hyprland-config")
       os.system("cp -r waybar ~/.config")
       print("Copied waybar config")
       os.system("cp -r wofi ~/.config")
       print("Copied wofi config")
       os.system("cp kitty/kitty.conf ~/.config/kitty")
       print("Copied kitty config")
       os.system("cp hypr/hyprpaper.conf ~/.config/hypr")
       print("Copied hyprpaper config")
       os.system("cp hypr/hyprlock.conf ~/.config/hypr")
       print("Copied hyprlock config")
       time.sleep(2) #for cool waiting
       flatq = input("Do you want to install chrome with flatpak?")
       if flatq == "y":
         os.system("sudo pacman -S flatpak")
         os.system("flatpak install com.google.Chrome")
         rbootq2 = input("Do you want to reboot to apply changes?")
         if rbootq2 == "y":
            os.system("reboot")
         elif rbootq2 == "n":
            print("Configuration has complete you may reboot when ready")
            time.sleep(2)
            os.system("exit")
       elif flatq == "n":
         rbootq = input("Do you want to reboot to apply changes?")
         if rbootq == "y":
            os.system("reboot")
         elif rbootq == "n":
            print("Configuration has complete you may reboot when ready")
            os.system("exit")

    elif gitq == "n":
       print("then install git and restart this script")
elif archq == "n":
    print("imagine using NixOS")