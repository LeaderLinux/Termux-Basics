import os
G="\033[1;32m"
R="\033[1;31m"
Y="\033[1;33m"
W="\033[1;37m"
os.system("clear")
os.system("figlet Termux Basics|lolcat")
print(f"                {Y} Telegram{G}:{Y}Anonymous_Hacking_12")
print("")
print(f"{R}[1] {Y}Termux Tools")
print(f"{R}[0]{Y} Exit")
print("")
loop = True
while loop:
        D = input(f"{Y}Termux Bascis{R} >> {W}")
        if D == "1":
            os.system("termux-setup-storage;cd;dpkg --configure -a;pkg update -y;pkg upgrade -y;pkg install python -y;pkg install python2 -y;pkg install python2-dev -y;pkg install python3 -y;pkg install pip -y;pkg install pip2;pip2 install requests;pkg install fish -y;pkg install ruby -y;pkg install git -y;pkg install dnsutils -y;pkg install php -y;pkg install perl -y;pkg install nmap -y;pkg install bash -y;pkg install clang -y;pkg install nano -y;pkg install w3m -y;pkg install figlet -y;pkg install cowsay -y;gem install lolcat;pkg install curl -y;pkg install tar -y;pkg install zip -y;pkg install unzip -y;pkg install tor -y;pkg install wget -y;pkg install wgetrc -y;pkg install wcalc -y;pkg install bmon -y;pkg install unrar -y;pkg install toilet -y;pkg install proot -y;pkg install golang -y;pkg install chroot -y;termux-chroot -y;pkg install openssl -y;pkg install cmatrix -y;pkg install openssh -y;apt update && apt upgrade -y")
            menu()
        if D == "0":
            break
