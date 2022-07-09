# The-SEK
## 💀 Welcome To The Shinigami Exploit Kit 💀
```
=========================================================================
[THE-SEK] Shinigami Exploit Kit
=========================================================================
[Version] 0.1 Beta
=========================================================================

              ___           _,.---,---.,_
              |         ,;~'             '~;, 
              |       ,;                     ;,      
     Frontal  |      ;                         ; ,--- Supraorbital Foramen
      Bone    |     ,'                         /'
              |    ,;                        /' ;,
              |    ; ;      .           . <-'  ; |
              |__  | ;   ______       ______   ;<----- Coronal Suture
             ___   |  '/~"     ~" . "~     "~'  |
             |     |  ~  ,-~~~^~, | ,~^~~~-,  ~  |
   Maxilla,  |      |   |        }:{        | <------ Orbit
  Nasal and  |      |   l       / | \       !   |
  Zygomatic  |      .~  (__,.--" .^. "--.,__)  ~. 
    Bones    |      |    ----;' / | \ ';-<--------- Infraorbital Foramen
             |__     \__.       \/^\/       .__/
                ___   V| \                 / |V <--- Mastoid Process
                |      | |T~\___!___!___/~T| |
                |      | |'IIII_I_I_I_IIII'| |  
       Mandible |      |  \,III I I I III,/  | 
                |       \   '~~~~~~~~~~'    /
                |         \   .       . <-x---- Mental Foramen
                |__         \.    ^    ./
                              ^~~~^~~~^

             _______ _    _ ______    _____ ______ _  __
            |__   __| |  | |  ____|  / ____|  ____| |/ /
               | |  | |__| | |__    | (___ | |__  | ' / 
               | |  |  __  |  __|    \___ \|  __| |  <  
               | |  | |  | | |____   ____) | |____| . \ 
               |_|  |_|  |_|______| |_____/|______|_|\_\
      

      
                   13 Diffrent Types Of Malware
                   0 Diffrent Types Of Ransomware [ToDo]
                   0 Diffrent Types Of Rootkits [ToDO]
                   2 Diffrent Type Of Powershell Scripts

```
The SEK is an Exploit Kit written by shinigami for learning about malware's and other malicious softwares in The SEK youll find a bunch of diffrent types of malware's to use in your red team operation with AV Evasion Of course all the malware currently work and bypass diffrent types of AV's but in time and after use of public it will be blocked at some poit and will be on your imagination ad useing the Custom Malware module to Bypass Them. This Tool is both a learning ground in diffrent types of shellcode injection and great for red teamers to use it in their operation all of the malwares work with diffrent types of c2 server like cobalt strike, empire, metasploit ... So Have Fun While You can

### Instalation
1 - Clone The Repo
```
git clone https://github.com/insurrection-act/the-sek
```
2 - Run The install.sh file
```
sudo chmod +x install.sh
sudo install.sh
```
3 - All Good You Can Use The SEK Now
### Usage
commands : use, use malware. use payload, use ransomware [ToDo], use rootkit, [ToDo], use powershell, generate malware, generate powershell
all commands have help in The SEK just type help / ?
demo:
```
( 127.0.0.1:9002 THE-SEK) > use malware

[*] Using Malware Handler
[+] Choose The Malware You Want To Generate

[1] Self Inject To .Data Section
[2] Self Inject To .TEXT Section
[3] Self Inject To .RSRC Section
[4] Shellcode Injection To a Remote Process
[5] Simple Dll Injection
[6] Simple Hidding Some Functions Self Inject
[7] No Imports Technique
[8] Thread Context Injection
[9] Section And Views Injection
[10] Asynchronous Procedure Calls Injection
[11] Early Bird Technique (thanks to tupi)
[12] Custom Malware
[13] Enviroment Variable Injection (thanks to naser niknam) [ToDo]

[*] Enter The Number For The Malware Type You Want To Use : 1
[*] Using Malware Type 1
( 127.0.0.1:9002 THE-SEK) > use payload

[*] Using Payload Handler
[+] Choose Your Payload Type

[1] HEX
[2] RAW Bin File
[3] calc-thread 64 bit (for testing)
[4] calc-thread 32 bit (for testing)

[*] Enter The Number For The Payload Type You Want To Use : 3
[+] Using Payload Type 3

( 127.0.0.1:9002 THE-SEK) > generate malware
[+] Your Malware is Ready in [ready folder]
```
