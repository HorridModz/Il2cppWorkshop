#After the first 60 or so lines, there is documentation, well-commented code, etc.

import os
import sys

#This line tells the script where the Il2cppWorkshop directory is. The Il2cppWorkshop folder contains data that Il2cppWorkshop.py needs to function.
#If you have moved Il2cppWorkshop.py to a new directory, please replace the code in line 9 with this code:
#rootdirectory = r"PUTYOURFILEPATHHERE"
rootdirectory = os.getcwd()
if not(r"\Il2cppWorkshop" in rootdirectory):
    print("Il2cppWorkshop.py appears to have been moved to a new directory, or the Il2cppWorkshop folder may have been renamed.\n\n\
If the latter is the cause, please rename the folder back to \"Il2cppWorkshop\".\n\nIf you have moved Il2cppWorkshop.py to a new directory, please change \"rootdirectory = os.getcwd()\" in line 9 of the Il2cppWorkshop.py file to this:\n\n\
rootdirectory = r\"PUTYOURFILEPATHHERE\"\n")
    isnewdir = input("Have you have moved Il2cppWorkshop.py to a new directory?\nY/N\n").lower()
    if isnewdir == "y":
        newdir = input("\nPlease enter the directory of the Il2cppWorkshop folder\n")
        if(r"\Il2cppWorkshop" in newdir):
            if ((newdir[len(newdir) - 1] == "\\") or (newdir[len(newdir) - 1] == "/")):
                newdir = newdir[0:len(newdir) - 1]
            print("Attemping to self-correct")
            try:
                currentfile = open(__file__,"r",encoding = "utf8")
            except:
                try:
                    currentfile = open(__file__,"r",encoding = "utf16")
                except:
                    try:
                        currentfile = open(__file__,"r",encoding = "utf32")
                    except:
                        print("The program failed to self-correct. Please edit the file manually with the instructions you are given on line 6.")
                        print("\n")
                        sys.exit("Due to this exception, execution has been terminated.")
            currentfilecontent = currentfile.read()
            currentfile.close()
            try:
                currentfile = open(__file__,"w",encoding = "utf8")
            except:
                try:
                    currentfile = open(__file__,"w",encoding = "utf16")
                except:
                    try:
                        currentfile = open(__file__,"w",encoding = "utf32")
                    except:
                        print("The program failed to self-correct. Please edit the file manually with the instructions you are given on line 6.")
                        print("\n")
                        sys.exit("Due to this exception, execution has been terminated.")
            if ("\nrootdirectory = os.getcwd()\n" in currentfilecontent):
                currentfilecontent = currentfilecontent.replace("\nrootdirectory = os.getcwd()\n","\nrootdirectory = r\"" + newdir + "\"\n")
                currentfile.write(currentfilecontent)
                currentfile.close()
                print("\n")
                sys.exit("The Il2cppWorkshop.py file has modified itself and self-corrected!")
            else:
                currentfile.close()
                print("The program failed to self-correct. Please edit the file manually with the instructions you are given on line 6.")
        else:
            print("\nThis file path appears to be invalid. Did you rename the Il2cppWorkshop folder?")
    print("\n")
    sys.exit("Due to this exception, execution has been terminated.")



#TO ANYONE READING THIS: These notes are messy and unfinished - they are more like notes for my notes.
#Do not bother reading them beyond the known bugs / limitations section.

#Wanna test and debug? Here's what to do.
#1. Go to the bottom of the code and type init() to make sure everything is set up.
#2. Go to a function that is not already tested. (Some may be unfinished, but at the time of writing this, everything is finished. Feel free to ask me if something
#is finished!)
#3. Read the function to understand what it does, how it works, and what the syntax for the inputs is.
#Keep in mind that almsost all functions return a string, list, or boolean. Barely any of them directly modify any value. Almost everything is immutable with these functions.
#4. Go to the bottom of the code, and after the init() statement, type print() and put your function call inside there.
#5. Thouroughly test every scenario with every input. If you find no bugs, please tell me the function is bug-free. If not, tell me any bugs you find.
#If you fix a function, please do not send me the fully modified program as I am constantly updating it on my end and it will likely be outdated on yours. Instead,
#send me only the fixed function, or tell me what is wrong and how to fix it.

#Known Bugs / Limitations (if you know how to fix, please tell me how!):
#1.
#In some functions, case-sensitivity only supports all lowercase, all uppercase, first letter of all words uppercase, or first letter of uppercase.
#This is because case-sensitivity works by manually making lowercase and checking, making first letter uppercase and checking, making uppercase and checking, and
#making first letter of all words uppercase and checking. I do not want to make it have to check every single way,
#because one, it would be tedious, repetitive, and inefficient to code, and two, it would take more processing to complete long tasks.
#If you know of a better, while still cheap, way to implement case-sensitivity, please tell me!
#2.
#indexofstr() and maybe (untested) findstr() functions work fine when given substrings of any length, both forward and backwards, except for one thing:
#when given a string that appears forward and not backward (ex: substr "32" in "1234", going backwards). In this case, it doesn't return the length of the string
#like it should, and idk what causes the result. I'm too tired to debug this!
#3.
#Index and backward inputs to some functions are buggy and may not work as expected.
#I prefer to do these things myself, instead of relying on the functions.
#4.
#Fields like "internal Player_move_c.GadgetEffect effect; // 0x0" will have "Player_move_c.GadgetEffect effect" instead of just "effect" as the field name.
#This is because there is not a great way to know what's what. The most likely way I would fix this issue is to also store the class name when processing fields,
#and remove the class name in any fields. However, I do not feel like worrying about this right now.
#5.
#Genericintsmethods will not be processed.
#6.
#Fields without fields offsets will purposely not be recognized as fields. I don't feel like worrying about this right now.
#7. Attempts to deal with attributes are made, but they are just too complicated and plentiful to deal with. It is highly recommended to dump without attributes.

#I recommend opening this in your favorite text editor if you want  to read the comments or code, as official python IDE does not have word wrapping.
#In my opionion, official python IDE is also tough to read.
#I suggest using notepad++ or quickedits.
#You do not have to take my advice, though. Suit yourself!

#       Structure (for creator to use as notes):
#   Cloud Uploads:
#All uploads are converted into strings (like save codes) and uploaded to pastebin. The response to the post http request then tells the program what the link is. To get this data back, the link is loaded, and the string is extracted using the httpparser module. For private uploads, the link is stored in the files of the program's designated directory, and given to the user so they can store it someplace safe. For public uploads, the user is prompted the name of the data, and who uploaded it, then the uploader, name, and link are added to the anyone can access google document. To browse and search for public uploads, the project gets the data from the google document.


 
#       Manual (PLEASE READ BEFORE USING)

#       Contact me
#The official github page for this project (go here to make suggestions, give feedback, get help, and contribute):
#https://github
#You can also contact me here:
#1
#2
#3

#       Welcome
#Welcome to Libil2cppWorkshop by (me)! This python program is a megatool for modding libil2cpp games. Some features work on games that aren't libil2cpp, too.
#Please read (or at least skim through) this manual before using.
#If you're looking for a megatool for modding, you should also check out Il2cppInspector by DJKaty! This is nothing compared to what they have made (and are still working on) after years of nonstop work! Il2cppInspector was my main inspiration, and it is what I look up to for this megatool and it makes me believe my goals are possible.
#https://github.com/djkaty/Il2CppInspector

#       Privacy Policy / Security
#This program is not a virus, but I recommend not taking my word, and putting it into virustotal, and maybe scanning the code. The project is open source, so you are able to analyze everything it does, how, and why.
#Here are some things the program does and does not do and why:

#The program DOES NOT:
#Automatically collect or store any data or analytics, with the exclusion of manual uploads and auto backups.
#Store or associate your ip address when you upload files to the cloud contribution system.
#Run or create any other programs, with the exclusion of .lua files and .cpp files for features like script generators and mod menu workshop.
#Read or write any files or folders outside of its designated directory.
#Store any more data to the cloud than what is neccessary and agreed upon.
#Store old backups. Each backup overwrites your old one. Do not rely on old backups if something goes run.
#Show ip addresses or usernames or return "Not Done"words to anyone, not even administrators.
#Delete uploaded files. The only way uploaded files (including backups) can be deleted is by the server being wiped completely. This may happen from time to time, when the servers are inactive or overflowing.

#The program DOES:
#Create and view pastebin pastes. All private backups and public uploads are stored on pastebin. For private backups, they are made as pastes only visable by url. The url is stored in the program files, but you should put it somewhere safe (as this is what the point of a backup is). The names of, uploaders of, and links to all public pastes are stored in the master paste, which is one public paste anyone can edit.
#Use a third-person cloud hosting service, which may be slow and vulnerable to database leaks or man in the middle attacks, which could possibly lead to leaked ip addresses, downloading of malware, being hacked, etc. (but this is a risk for anything that uses cloud servers).
#Use a third-person cloud hosting service. The server may be down temporarily, down permanently, or lose or corrupt data. Please be aware that just because your data is in the cloud, that does not mean it cannot be lost.
#Create, modify, and delete any files in the project's designated directory. Do not put your in there or modify existing ones, as your changes may be lost.
#Upload backup data to the cloud, if this feature is turned on. Everything in the project's designated directory will be uploaded during back ups, so please do not put personal files there for security in the extremely rare case of database leaks.
#MAYBE store your ip address. Some features may use ip address, or may use username and return "Not Done"word or token login systems. My goal is for ip addresses to not be stored.
#Stores backups by ip address, or hopefully username and return "Not Done"word or token logins. If someone can find and spoof your ip or crack your username and return "Not Done"word or token, they can view any of your files in the database.
#Show public uploads to everyone. Make sure public uploads such as notes files do not contain personal information!
#You have the option to include a custom name to be displayed as the uploader each time you make a public upload, or remain anonymous. This name is not your username - it is set manually each upload, and cannot be changed after the upload is uploaded.
# Files may be deleted as the server may sometimes be wiped completely. This may happen from time to time, when the servers are inactive or overflowing.

#            License
            
            

#            How to use
            
            
#       Features (IF YOU ARE READING THIS, THESE ARE JUST MY GOALS. DON'T CALL ME CRAZY PLEASE, I DON'T EXPECT TO ACCOMPLISH ALL OF THESE. THIS IS JUST AN IDEA LIST):
    #Finished Features:
    
    #WIP Features (please do not try to use these!)
# - Macro / Plugin System: You can code plugins /macros in any language, or make them with the plugin / macro maker GUI! You can set the program to perform your own routine with user inputs. Basically, you write your own program, made of of some of your own code and some il2cppworkshop functions. Similar to il2cpp plugin system. EX: Auto-updating hex patch script: Tell user to input apk file path, then dump, deobfuscate a set class and method by comparing with a set unobfuscated dump.cs, and create a hex patch script using your set options.
#Plugins / macros can also be uploaded and downloaded via the cloud contribution system.
# - Infinite loop protection: These program has multiple defenses against it getting stuck in infinite loops. There is an error system, where the code checks for errors and can log the error to the console and / or visually display the error, and some errors will cause it to forcefully terminate. There is also a warning system, and a log system so you can find what went wrong. There are debugging tools and live analytics, helping you know when the program is stuck and why. In addition, loops don't just run and delay everything else: Some loops have abort systems, log things, and check if they are stuck in an infinite loop.
# - Cloud backup system: Backup the program data to the cloud, so you do not lose your progress / data! Each ip address has their own backup folder. Make sure you do not use a vpn, and you have a static ip address, or this backup will not sync. OR maybe there will be a username and return "Not Done"word or token system. You can choose to manually backup, and automatic backups may be available from time to time, depending on the capabilities of the server hosting.
# - Import your own files, or choose from one of the existing ones. Maybe even a cloud system where people can upload files for others?
# - Cloud contribution system: Want to help yourself, and others? When you are done with a task, you can choose to upload the result (deobfuscated things, hex values, dump files, gameguardian scripts, etc.) to the cloud. You can upload it with a custom name. After uploading, you can access these files by searching for them in the cloud database - this way you never lose them. Even better, others can also access these files! You can also upload notes files (such as repositories of methods) to the cloud for others to use. You can also upload checkpoints, so everyone can help contribute to big and time-consuming tasks. You can also upload useful files with apks and dump.cs files. This system also supports the cloud plugin upload / download system.
# - Brute Force Deobfuscation (Comparitive Deobfuscation): A deobfuscation method that works by comparing unobfuscated and obfuscated dump.cs. It finds the class or member etc. by name. Then, it takes the class, and replaces the names and dynamic values with a certain string ('offset','methodname','classname','comment',etc.). This way, things such as data types, params, # of methods and fields, etc. can be compared. It then converts this into lists of methods, and each method has its method type, and the method params. Same is done on fields and class itself. There is a strikes system with a customizable strictness. It can automatically adapt by narrowing down the perfect strictness by moving it up and down and seeing how little results it can get while still getting results (the toggleable smart mode, changeable in settings or function parameters). This method takes a long time.
# - Regex search deobfuscation (String search deobfuscation): This method is faster, simpler, and better. Both are useful though. This method finds unchanging string (such as <int,float> and private readonly Dictionary<) by searching strings until it finds one with low occurences (like 300 or less), and it finds the one with the lowest. It can also remove names / dynamic values and uses regex search. It can also use the renamer to remove changing things. Then it sees if this comes up in obfuscated. It uses brute force deobfuscation on the resulting classes methods etc. This is done until the right one is found.
# - Mutual Name Deobfuscation (Cross Reference Deobfuscation): This deobfuscation method is kind of like string search deobfuscation. It searches for the name you want to deobfuscate and finds other instances of the name, either as parameters in methods, methods with the same name in other classes, or fields with the same name in other classes. It tries to find one of these where the method or class is unobfuscated, or known through previous deobfuscation. Then, it goes to this class and used brute force deobfuscation to find the right method or field.
# - Same Name Deobfuscation: In some games, such as pixel gun 3d, different obfuscated names with the same original names will have the same obfuscated names. This is probably caused by manual find-and-replace-ing. This can be forced by the user, or detected by the program when it finds this out via another form of deobfuscation. When activated, this mode simply finds and replaces text, the same way the names were likely obfuscated - but reversed. This only occurs in weak obfuscation by foolish developers, so don't expect to get lucky with it!
# - Deobfuscation by name: Put in the name of a method, class, field, etc. and the program attempts to deobfuscate it by comparing unobfuscated and obfuscated dump.cs. Make sure you have get_ or set_ in front of some methods! If a method is not the found, the program looks for it with get_, and if still not, it looks for it with set_.
# - Finding by name: Put in the name of a method, field, class etc., and the program will try to find more details about it. You can choose what details you want. Details include, fields of class, methods of class, class type, parameter of method, type of field or method, etc. 
# - Auto Deobfuscation: Uses brute force deobfuscation to try to deobfuscate as much as it can, all at once. Failed methods and classes etc. try to use other two methods.
# - Beebyte deobfuscation: This project has built-in beebyte deobfuscation with GUI thanks to beebyte deobfuscator. It is not as easy to use or reliable!
# - AU deobfuscator (Only for mac / linux): This project has built-in deobfuscation with GUI thanks to au deobfuscator. It only works on mac / linux. You need to first dump the game to get the dummy dll, use il2cppinspector to decompile the dll, and get the  il2cpp-types.h and il2cpp-types-ptr.h files. It is not as easy to use or reliable!
# - Saves work: The project saves deobfuscated names, files, script workshop sessions, etc. and restores them next time. You can also store things in the cloud, for yourself and others!
# - Task close and resume: Time-consuming tasks like deobfuscation will have checkpoints saved every minute. These checkpoints have almost no effect on storage space or speed (they are usually only kilobytes long). They do not fill up your files, as they are in their own folder in the program's data and each checkpoint replaces the previous one's file, rather than deleting it. You can resume from your checkpoint by going to settings. You will automatically be prompted whether you would like to or not when you restart the project (there is a yes, no, and do not ask again dialog). You can also delete these checkpoints, or import checkpoints from others to finish the job for you. You can disable
# - Adort button: If you would like to cancel something, click the abort button in the GUI. This will close and save the progress of currently running task.
# - Checkpoint button: There is also a button to manually create checkpoints (see task close and resume).
# - Hex patching tools: Method to offset, offset to hex, hex to offset, etc.
# - Direct hex patching: Directly modify lib files by offset or hex value. You can also replace all hex values that match. You can also use numbers.
# - Dump.cs and lib file analysis: Generate hex patch scripts, find hex values, search for numbers and strings, go to offsets, and more in files like libil2cpp. This is basically a hex editor (with GUI!). Inspired by HxD Workshop (HxD Hex Editor).
# - Name remover: This features removes all names in dump.cs of unobfuscated and obfuscated. It also removes dynamic things such as offsets. This way, things match up. This is also useful for unobfuscated things, because it removes dynamic things. It can be used for things such as deobfuscating and auto-updating.
# - Renamer: Inspired by de4dot, this feature replaces names and / or things like offsets and comments with clearer names. For example, obfuscated functions can be renamed.
# - GG script generator: Can generate custom gg lua scripts for things such as hex patch scripts.
# - GG Script workshop: UI for making scripts of pieces of scripts such as mod menus and http request.
# - Mod menu workshop: UI for generating mod menu code
# - Arm hex converter: Convert arm assembly code for hex opcodes for arm64, armv7, and thumb back and forth. Also, have ret values as an option (just type value u want to ret and it generated hex code). You can also convert hex values into numbers (useful for gameguardian).
# - Easilly get useful files: Can get files such as metadata, libil2cpp, etc. with root directory and file name. Choose from the list of files and script uses root directory + "pathoffile" to get file.
# - GG script encryption / decryption: Can encrypt, obfuscate, decrypt, and decompile gameguardian scripts with multiple methods (unicode, binary, moonsec obfuscator, etc.)
# - Live analytics: Data such as progress, memory used, disk space used, etc. You can disable, enable, and expand things in the settings menu.
# - Settings menu: Customize how the project works, both behind the scenes and in your face, with features such as keybinds changing, high contrast mode, low memory mode, and more!
# - Great GUI: Buttons, sliders, live analytics, and more! There's even a settings menu to customize it!
# - Command Line: If you don't like the GUI, you can use the command line version instead!
# - Call functions from the project itself: As a third option, you can you can call edit the program yourself and add function calls to the bottom of the code (make sure to un-comment the template and use that).
# - Available as command line .exe and GUI .exe
# - Programmed in both c++ and python, so if you want to modify it, write plugins, 
# - Debugging tools: There are special debugging tools such as monitoring variables, when functions are called, etc.
# - Warning and error system: A live warning system and an error system, so you know what goes wrong and why. You can dismiss errors, investigate errors, use debug tools in the way the error / warning suggests, and there is an ignore option and a do not show again option.
# - 100% Open Source: All the code is clean, open source, and commented. You are free to use pieces of it with credit, modify it, etc.
# - Auto libil2cpp dumping: Built-in perfare il2cppdumper and il2cppdumper online (https://il2cppdumper.com/the-dumper-tool), so you don't have to worry about dumping yourself!
# - Automatic Mod Menu Installion: Give the program the apk for a mod menu and the type of menu (LGL, OctoWolve, ImGUI, etc.) - or let it auto-detect it - and the program will try to automatically find and modify .txt files like androidmanifest.xml and mainactivity.smali, as well as find places for and add your mod menu files like your mod menu's lib and smali.

#      Errors
#This was coded in python 3.10.4 for 64bit windows, so older or newer versions may have bugs. If something doesn't work, you can try downloading 3.10.4.

#If an error is not listed here or the solution listed does not work for you, look the arror up on your preffered search engine or contact me. You can also reach out on github.

#Here are some common mistakes that can cause errors:
# - Trying to use a feature that is still a WIP (see the 'Features' section so you know what is finished and what's not)
# - Modifying the code beforehand, whether accidentally or on purpose
# - Using a function incorrectly (typing the syntax wrong, missing parameters, misunderstanding what the function does, reading
# - Use features via the GUI, with the given inputs and settings, or by manually typing the functions and filling in the function parameters.

#Here are the solutions to some common errors:
#Error: ModuleNotFoundError: No module named (module name)
#Solution: The file for this module is not stored in the directory ('pythonroot directory>your python version >include') on your device. You need to add it to this directory. I recommend this tutorial (it can be adapted to work for all modules) - https://bobbyhadz.com/blog/python-no-module-named-requests.
#Error: (Disk space error thingy)
#Solution: Your device is out of storage space. Try to free up space, then run the program again.
#Error: (http error thingy)
#Solution: Make sure you have an internet connection. Features that require internet connection will say so before you use them.
#Error: Unexpected dump.cs format
#Solution: The dump may be modified or unrecognized. Try dumping again - you may have accidently typed something in your dump.cs
#file beforehand. Try dumping with this program. The dumpcs files tested do not have any spaces in method, field, property class, enum, struct, etc. names
#and are dumped with Il2cppDumper GUI 1.6.0. 

#       Requirements:
#Basic knowledge of game modding. This is only a multi-tool. It will not help someone who does not understand it.
#Fluency in English and understanding of how to use python files and type python commands (there is a function syntax guide for how to use each function and what it does).
#At least Python 3.10 installed on your device OR an online python compiler (such as https://www.programiz.com/python-programming/online-compiler/).
#I recommend NOT using an online compiler as they can be significantly slower and may not be as stable or reliable.
#If you are using Python 3.10, you need all of these modules installed on your device:
#datetime
#request
#time
#999999999999999 modules more lol
#Some features require internet connection. These features will say if they do. Unintended behavior, errors, crashes, infinite loops, etc. may occur if you try to use them without internet connection.
#Some features require to connect to the server. These features will say if they do. The server hosting is provided by (i think https://www.heliohost.org/signup/). If the server is down, unintended behavior, errors, crashes, infinite loops, etc. may occur if you try to use these features. If you think the server is down, please contact me.
#A directory for the program's data to be stored. The first time you run it, you will be asked. I suggest your appdata, programfiles, or documents folder, but you can choose whatever you want. Make sure this data stays safe, or all local data will be lost (assuming you don't have everything backed up to the cloud).
#Some features require a static ip address. This means these features may not work well if you connected to a vpn, are using LTE on a different cell phone, are connected to a different Wi-fi network, etc.


#       Credits


#       How features work


#               Documentary

#           CODE (Do not modify, delete, or add anything beyond this point unless you know what you are doing. This is the real code, not part of the documentary or manual.)

#                Initilization

#   Modules required for importing other modules

import sys
import warnings
import importlib
import pip


#   Require Correct Version

#Thanks to https://stackoverflow.com/questions/6224736/how-to-write-python-code-that-is-able-to-properly-require-a-minimal-python-versi
MIN_VERSION = (3, 7)
MAX_VERSION = (3, 10)
CURRENT_VERSION = (sys.version_info[0],sys.version_info[1])
if CURRENT_VERSION < MIN_VERSION:
    print("Python %s.%s or later is required for the program to work correctly." % MIN_VERSION)
    sys.exit("You are currently using Python %s.%s." % CURRENT_VERSION)
if CURRENT_VERSION > MAX_VERSION:
    print("WARNING:\nPython %s.%s is highly recommended. Later versions may cause bugs." % MAX_VERSION)
    print("You are currently using Python %s.%s.\n" % CURRENT_VERSION)
    
#   Importing Modules

def modulenotfounderror(module,terminate = True):
    print("Could not import module '" + module + "'.\
\nSome features may not work or give errors due to this module not being installed.")
    TRY_INSTALL = input("Would you like to try to install the module? An internet connection is required to do so.\nY\\N\n")
    if TRY_INSTALL == "Y" or TRY_INSTALL == "y":
        if not(install_and_import(module)):
            print("\n\nSuccessfully installed and imported module '" + module + "' !")
        else:
            globals()[module + "imported"] = False
            if terminate:
                sys.exit()
    else:
        globals()[module + "imported"] = False
        print("Could not import module '" + module + "'.")
        if terminate:
            sys.exit()

def install_and_import(module):
    INSTALL_ERROR = False
    try:
        importlib.import_module(module)
    except ImportError:
        try:
            import pip
            pip.main(['install', module])
        except:
             try:
                import sys
                pythonpath = sys.exec_prefix
                import os
                os.system(pythonpath + r"\python -m pip install " + package)
             except:
                INSTALL_ERROR = True
        finally:
            if not(INSTALL_ERROR):
                try:
                    globals()[module] = importlib.import_module(module)
                except:
                    INSTALL_ERROR = True
                    print("\n\nFailed to install module '" + module + "' due to unknown reason. Check that you have an internet connection and that your disk is not full.")
            return(INSTALL_ERROR)

def importmodule(module,terminate = True):
    globals()[module + "imported"] = True
    try:
        globals()[module] = importlib.import_module(module)
    except ImportError:
        modulenotfounderror(module,terminate)

importmodule("io")
#importmodule("pyperclip",False)
importmodule("math")
importmodule("random")
importmodule("string")
importmodule("statistics")
importmodule("ast")
importmodule("os")
importmodule("time")
importmodule("datetime")
importmodule("timeit")
importmodule("xml")
if osimported:
    from os.path import exists
    from os import listdir
    from os.path import isfile, join
importmodule("html",False)
if htmlimported:
    from html.parser import HTMLParser
timeimported = True
if xmlimported:
    from xml.etree import ElementTree

#   Init

isinit = False

def init():
        global isinit
        isinit = True
        
        #Restore data from last session if it exists
        def loaddata(path):
            pass

        def initlog():
            global fulllog
            fulllog = []
            global importantlog
            importantlog = []
            global truncatedfulllog
            truncatedfulllog = []
            global truncatedimportantlog
            truncatedimportantlog = []
            global truncateloglength
            truncateloglength = 200
            global _truncatedstring
            _truncatedstring = "... (truncated)"

        #settings constants
        def initsettingsconstants():
            global defaultdumpcssettings
            defaultdumpcssettings = {
                "tolerance": 80,
                "objectkeepaftercolon": False,
                }
            global defaultsettings
            defaultsettings = {
                "dumpcs": defaultdumpcssettings,
                }
            global _usethreads
            _usethreads = True
            global _threadcount #manual or auto-generated
            _threadcount = 8
        
        #messagecontants
        def initmessageconstants():
            def initerrors():
                #Files
                global filenotfounderror
                def filenotfounderror(path,actions = ["log","print"]):
                    error("File not found at path '" + path + "'",actions)
                global foldernotfounderror
                def foldernotfounderror(path,actions = ["log","print"]):
                    error("Folder not found at path '" + path + "'",actions)
                global fileencodingunknownerror
                def fileencodingunknownerror(path,actions = ["log","print"]):
                    error("Could not decode file '" + path + "' due to unknown encoding. Only utf8, utf16, and utf32 are supported.",actions)
                global unknownfileopenerror
                def unknownfileopenerror(path,actions = ["log","print"]):
                    error("Unknown error occured when attempting to open file '" + path + "'",actions)
                #Internal
                global objectnotdeclarederror
                def objectnotdeclarederror(thisobject,actions = ["log","print","terminate"]):
                    error("'" + str(thisobject) + "' is not defined. Did you forget to call the function to define it first?",actions)
                #Dumpcs
                global unexpecteddumpcsformaterror
                def unexpecteddumpcsformaterror(error,segment,actions = ["log","print"]):
                    global dumpcspath
                    #error("Unexpected format of dump.cs file '" + dumpcspath + "' : " + error + " when attempting to process '" + segment + "'.",actions)
                    #print("\nDump.cs format error:\n" + str(segment) + "\n\n")
                global dumpcsnotfounderror
                def dumpcsnotfounderror(name,actions = ["log","print"]):
                    #error("'" + str(name) + "' could not be found. Are you looking in the right place? Are you sure you are looking in an unobfuscated version?",actions)
                    print("'" + str(name) + "' could not be found. Are you looking in the right place? Are you sure you are looking in an unobfuscated version?")
                global dumpcsattributeswarning
                def dumpcsattributeswarning(path,actions = ["log","print"]):
                    #warning("Attributes detected in dump.cs at path '" + path +  "'. It is recommended to dump without atttributes. Attributes may cause bugs or errors.")
                    print("Attributes detected in dump.cs at path '" + path +  "'. It is recommended to dump without atttributes. Attributes may cause bugs or errors.")
                #APK
                global metadatafilenotfounderror
                def metadatafilenotfounderror(path,actions = ["log","print"]):
                    error("global.metadata.dat file not found at file path '" + path + "'. This game may not be an il2cpp game, or it may be an unsupported version of il2cpp. If the game is il2cpp, the metadata may be encrypted. Encrypted metadata files are currently not supported. See if you can find the metadata file manually.",actions)
                global androidmanifestfilenotfounderror
                def androidmanifestfilenotfounderror(path,actions = ["log","print"]):
                    error("AndroidManifest.xml file not found at file path '" + path + "'. This game may not be an il2cpp game, or it may be an unsupported version of il2cpp. See if you can find the AndroidManifest.xml file manually.",actions)
                def mainactivitynotfounderror(path,actions = ["log","print"]):
                    error("Could not find mainactivity in AndroidManifest.xml file '" + path + "'. This game may not be an il2cpp game, or it may be an unsupported version of il2cpp. See if APK Easy Tool can find the main activity (launch activity).",actions)
                global apknotdecompilederror
                def apknotdecompilederror(path,actions = ["log","print"]):
                    error("Expected decompiled apk folder at path '" + path + "', got apk file. You can decompile the apk file through Il2cppWorkshop itself, or use APK Easy Tool.")
                    
            initerrors()
        #stringandnumberconstants
        def initstringandnumberconstants():
            global whitespacechars
            whitespacechars = "​ " + "\v\f\n\r\t"
            #whietespacechars = string.whitespace
        #dumpcsconstants            
        def initdumpcsconstants():
            #Types Constants
            def addtypeprefixesandsuffixes(prefixes,suffixes):
                global _types
                if len(_types) > 0:
                    return
                #Capitalized
                newtypes = list(_types) #the for loop will change when we update valuetypes, so we have to make a new array, and set valuetypes to this new array when we are done using it
                for thistype in _types:
                    newtypes.append(thistype.capitalize())
                _types = newtypes #set valuetypes to the newtypes now that we are done iterating through it
                #Lowercase
                newtypes = list(_types) #the for loop will change when we update valuetypes, so we have to make a new array, and set valuetypes to this new array when we are done using it
                for thistype in _types:
                    newtypes.append(thistype.lower())
                _types = newtypes #set valuetypes to the newtypes now that we are done iterating through it
                #Suffixes
                old = list(_types) #store the old valuetypes, so we can add just suffixes, then just prefixes later on, without the update list containing suffixes
                for thissuffix in suffixes: #suffixes
                    for thistype in old: #use the old value types that have no prefixes or suffixes
                        _types.append(join(thistype,thissuffix))
                #Prefixes and suffixes
                newtypes = list(_types) #the for loop will change when we update valuetypes, so we have to make a new array, and set valuetypes to this new array when we are done using it
                for thisprefix in prefixes: #prefixes and suffixes
                    for thistype in _types: #use the new value types that already have suffixes, but not prefixes
                        newtypes.append(join(thisprefix,thistype))
                _types = newtypes #set valuetypes to the newtypes now that we are done iterating through it
                #Prefixes
                for thisprefix in prefixes: #prefixes
                    for thistype in old: #use the old value types that have no prefixes or suffixes
                        _types.append(join(thisprefix,thistype))
                #Remove duplicates
                newtypes = [] #the for loop will change when we update valuetypes, so we have to make a new array, and set valuetypes to this new array when we are done using it
                for thistype in _types: #use the new value types that already have suffixes, but not prefixes
                    if not(thistype in newtypes):
                        newtypes.append(thistype)
                _types = newtypes #set valuetypes to the newtypes now that we are done iterating through it

            #Types            
            global _types
            _types = ["t","virtual","dictionary","predicate","func","new","static","protected","public","private","internal","readonly","const","final","void","bool","byte","int16","int32","int64","uint16","uint32","uint64","char","decimal","single","double","float","int","long","sbyte","short","uint","ulong","ushort","string","array","list","delegate","object","vector","vector2","vector3","quaternion"]
            typeprefixes = ["obscured"]
            typesuffixes = ["[]","?"]
            addtypeprefixesandsuffixes(typeprefixes,typesuffixes)
            _types = set(_types)
            global _objecttypes #for all objects - value types and userdefined types
            _objecttypes = ["abstract","concrete","sealed","static","shared","instance","partial","private","protected","internal","inner","nested"]
            _objecttypes = set(_objecttypes)
            global _userdefinedtypes
            _userdefinedtypes = ["class","struct","enum","interface","union"]
            _userdefinedtypes = set(_userdefinedtypes)
            global _typenamereplace
            _typenamereplace = "name"
            #Offsets constants
            global _isoffsetstring
            _isoffsetstring = "// RVA: "
            global _offsetprefix
            _offsetprefix = "Offset: 0x"
            global _offsetsuffix
            _offsetsuffix =  " VA: 0x"
            global _offsetlength
            _offsetlength = 6
            #Object constants
            global _nonamespacename
            _nonamespacename = "-" #In dnspy, classes in global namespace are called "-". In dump.cs, they are called "".
            global _objectseparator
            _objectseparator = "// Namespace: "
            global _sharedobjectstrings
            _sharedobjectstrings = [".<","<",">",">a_",">b_",">c_",">d_",">e_",">f_",">g_",">h_",">i_",">j_",">k_",">l_",">m_",">n_",">o_",">p_",">q_",">r_",">s_",">t_",">u_",">v_",">w_",">x_",">y_",">z_","."] #don't worry, I didn't type this out. I wrote a script to make this!
            _sharedobjectstrings = tuple(_sharedobjectstrings)
            global _namespaceline
            _namespaceline = 1
            global _namespacenamestart
            _namespacenamestart = "// Namespace: "
            global _objecttypeline
            _objecttypeline = 2
            global _objecttypeend
            _objecttypeend = " // TypeDefIndex: "
            global _objectkeepaftercolon
            _objectkeepaftercolon = False
            global _objectcolon
            _objectcolon = " :"
            #Methods, fields, and properties constants
            global _fieldsstart
            _fieldsstart = "// Fields"
            global _propertiesstart
            _propertiesstart = "// Properties"
            global _methodsstart
            _methodsstart = "// Methods"
            global _contentends
            _contentends = ["}","// Methods","// Fields","// Properties"]
            _contentends = set(_contentends)
            global _genericinstmethodstart
            _genericinstmethodstart = "/* GenericInstMethod :"
            global _genericinstmethodend
            _genericinstmethodend = "*/"
            global _datatypegroupstart
            _datatypegroupstart = "<"
            global _datatypegroupend
            _datatypegroupend = ">"
            global _datatypegroupseparator
            _datatypegroupseparator = ", "
            global _processdatatypegroups
            _processdatatypegroups = True #more accurate, but slower
            global _fieldoffsetstart
            _fieldoffsetstart = "; // 0x"
            global _propertyattributesstart
            _propertyattributesstart = " { "
            global _propertyattributesend
            _propertyattributesend = "; }"
            global _propertyattributeseparator
            _propertyattributeseparator = "; "
            global _methodoffsetline
            _methodoffsetline = 1
            global _methodtypeline
            _methodtypeline = 2
            global _methodparamsstart
            _methodparamsstart = "("
            global _methodparamsend
            _methodparamsend = ")"
            global _ismethodstring
            _ismethodstring = ") {"
            global _ispropertystring
            _ispropertystring = "; }"
            global _isfieldstring
            _isfieldstring = "; // 0x"
            #Attributes constants
            global _attributestart
            _attributestart = "["
            global _attributeend
            _attributeend = "]"
            #Deobfuscation constants
            global _tolerance
            _tolerance = float(80) #By default, objects are preferred to have a similarity score of at least 80% to be considered a match (but this can be modified or adjusted)
            global _userdefinedtypeweightfalse
            _userdefinedtypeweightfalse = float(999999999999999)
            global _userdefinedtypeweighttrue
            _userdefinedtypeweighttrue = float(0)
            global _sharedweightfalse
            _sharedweightfalse = float(999999999999999)
            global _sharedweighttrue
            _sharedweighttrue = float(0)
            global _methodweightfalse
            _methodweightfalse = float(4)
            global _methodweighttrue
            _methodweighttrue = float(1)
            global _fieldweightfalse
            _fieldweightfalse = float(5)
            global _fieldweighttrue
            _fieldweighttrue = float(1.25)
            global _propertyweightfalse
            _propertyweightfalse = float(5)
            global _propertyweighttrue
            _propertyweighttrue = float(1.25)
            global _objecttypeweightfalse
            _objecttypeweightfalse = float(28) #This really shouldn't change, so it hits really heavy. But I guess it is possible?
            global _objecttypeweighttrue
            _objecttypeweighttrue = float(5)
            global _namespaceweightfalse
            _namespaceweightfalse = float(22) #This really shouldn't change, so it hits really heavy. But I guess it is possible?
            global _namespaceweighttrue
            _namespaceweighttrue = float(7)
            global _typeweighttrue
            _typeweighttrue = float(2)
            global _typeweightfalse
            _typeweightfalse = float(2)
            global _paramweighttrue
            _paramweighttrue = float(1)
            global _paramweightfalse
            _paramweightfalse = float(1)
            global _sizeweightfalse #per each sizebenchmark
            _sizeweightfalse = float(0.3)
            global _sizeweighttrue #whole thing matches
            _sizeweighttrue = float(2)
            global _sizebenchmark
            _sizebenchmark = float(4)
            global _trustnames #if two names are the same, deobfuscation will assume they are the same thing with this setting. however, some games purposely scramble names to confuse people and tools like this.
            _trustnames = True
    #init cloud stuff
        def inithttp():
            #userdefinedd from https://flaviocopes.com/python-http-server/
                global initserver
                def initserver(port):
                    global httpserver
                    class httpserver(BaseHTTPRequestHandler):
                        global httpget
                        def get(self):
                            self.send_response(200)
                            self.send_header('Content-type','text/html')
                            self.end_headers()
                            message = "Hello, World! Here is a GET response"
                            self.wfile.write(bytes(message, "utf8"))
                        global httppost
                        def post(self):
                            self.send_response(200)
                            self.send_header('Content-type','text/html')
                            self.end_headers()
                    global server
                    server = HTTPServer(('', int(port)), httpserver)
        
        global makerequest
        def makerequest(url,requesttype,gettypeorpoststr,timeout = 8):
            if requesttype == "get":
                if gettypeorpoststr == "content":
                    return(requests.get(url,timeout = int(timeout)).content)
            if requesttype == "post":
                return(requests.post(url, data = str(gettypeorpoststr),timeout = int(timeout)))

        #Init constants
        initlog()
        initstringandnumberconstants()
        initdumpcsconstants()
        initmessageconstants()
        initflags()
        initsettingsconstants()

        #Restore save data
        loaddata(rootdirectory)
        #(temp) settings specific to the game
        usenamingregex = False
        usenamingchars = False
        namingregex = "\\p{L}\\p{M}*"


#       Flags

#   #Init flags for what has been done and what hasn't
def initflags():
            #dumpcs flags
            global flagdumpcs
            flagdumpcs = False
            global flagdumpcspath
            flagdumpcspath = False
            global flagfullobjects
            flagfullobjects = False
            global flagremovedattributes
            flagremovedattributes = False
            global flagremovedshared
            flagremovedshared = False
            global flagremovedblanklines
            flagremovedblanklines = True

resetflags = initflags #same thing, but different name

def updateflag(flag,condition = True):
            globals()[flag] = condition
        


        
#            Basic functions

#   Renaming default functions to make them easier to use

lengthof = len

tostring = str

tostr = str

tonumber = int

tonum = int

toint = int

tofloat = float


#   String functions

def getlines(fullstr,toremoveblanklines = False,toremovewhitespace = False):
    lines = fullstr.splitlines()
    if (toremoveblanklines or toremovewhitespace):
        newlines = []
        for thisline in lines:
            if toremovewhitespace:
                thisline = removewhitespace(thisline)
            if not((iswhitespace(thisline)) and toremoveblanklines):
                newlines.append(thisline)
        return(newlines)
    else:
        return(lines)

def letter(i,text):
    if i < 1:
        return ""
    if i > len(text):
        return ""
    else:
        return (text[i - 1])
    
def lastletter(text):
    if len(text) == 0:
        return None
    else:
        return (text[len(text) - 1])

def firstletter(text):
    if 1 > len(text):
        return None
    else:
        return (text[0])

def substring(text,start,end = 999999999999999999999):
    if start < 1:
        return (text[0:end])
    else:
        return (text[start - 1:end])

def checkforstringat(substr,fullstr,i):
    return (substring(fullstr,i,(i - 1) + len(substr)) == str(substr))

checkforstring = checkforstringat #same thing, but different name


def contains(substr,fullstr,casesensitive = True,backward = False):
    if  casesensitive:
        return ((substr in fullstr) or (backward and reverse(substr) in fullstr))
    else:
        return ((substr.casefold() in fullstr.casefold()) or (backward and reverse(substr).casefold() in fullstr.casefold()))

def findstr(substr,fullstr,index = 0,casesensitive = True,backward = False,newstring = False): #index argument is bad - only use 0
    if not(casesensitive):
        substr = substr.casefold()
        fullstr = fullstr.casefold()
    if backward:
                strindex = reverse(fullstr).find(substr,index,len(fullstr)) + 1
    else:
                strindex = fullstr.find(substr,index,len(fullstr)) + 1
    if strindex == 0:
                strindex = "Not Found"
    if newstring:
        if strindex == "Not Found":
                   return("")
        else:
            if backward:
                         return(substring(fullstr,0,strindex))
            else:
                        return(substring(fullstr,strindex,len(fullstr)))
    else:
        if strindex == "Not Found":
            if backward:
                        return(len(fullstr))
            else:
                        return(0)
        else:
                    return(strindex)
      
def readbetween(fullstr,startstr,endstr,casesensitive = True):
    startpos = indexofstr(startstr,fullstr,casesensitive) + 1
    endpos = (indexofstr(endstr,fullstr,casesensitive,False) - (len(endstr) - 1)) - 1
    if startpos is None or endpos is None:
        return("")
    else:
        return(substring(fullstr,startpos,endpos))

def readafter(fullstr,startstr,casesensitive = True):
    startpos = indexofstr(startstr,fullstr,casesensitive) + 1
    endpos = len(fullstr)
    return (substring(fullstr,startpos,endpos))

def readbefore(fullstr,endstr,casesensitive = True):
    startpos = 1
    endpos = indexofstr(endstr,fullstr,startpos,casesensitive) - 1
    return (substring(fullstr,startpos,endpos))
      
def reverse(text):
    if str(text) is None:
        return ""
    else:
        text = str(text)
        new = ""
        i = 0
        while i < len(text):
            new = (new + letter(len(text) - i,text))
            i = i + 1
        return new
    
def match(str1,str2,casesensitive = True):
    if not(casesensitive):
        return (str1.casefold() == str2.casefold())
    else:
        return (str1 == str2)
    
def occurencesof(substr,fullstr,casesensitive = True):
    if not(casesensitive):
        substr = substr.casefold()
        fullstr = fullstr.casefold()
    occurences = fullstr.count(substr)
    return (occurences)

def getallinstancesof(substr,fullstr,cassensitive = True):
    return "Not Done!"

def occurencesofanyof(substrs,fullstr,casesensitive = True):
    if type(substrs) == str:
        substrs = substrs.split(",")
    occurences = 0
    for substr in substrs:
        occurences = occurences + occurencesof(substr,fullstr,casesensitive)
    return (occurences)
    
def readuntil(chars,fullstr,index = 0,backward = False,casesensitive = True,newstr = True):
    if (backward and (index == 0)):
        i = len(fullstr)
    else:
        i = index
    new = ""
    while ((letter(i,fullstr) == "") or  not(contains(letter(i,fullstr),chars,casesensitive))):
        if backward:
            i = i - 1
        else:
            i = increment(i,True)
        if (( i > len(fullstr) and not(backward)) or ((i < 1) and backward)):
                break
        if (contains(letter(i,fullstr),chars,casesensitive)):
            break
        thisletter = letter(i,fullstr)
        new = join(new,thisletter)
    if newstr:
        return new
    else:
        return i

def readuntilnot(chars,fullstr,index = 0,backward = False,casesensitive = True,newstr = True):
    if (backward and (index == 0)):
        i = len(fullstr)
    else:
        i = index
    i = index
    new = ""
    while ((letter(i,fullstr) == "") or (contains(letter(i,fullstr),chars,casesensitive))):
        if backward:
            i = i - 1
        else:
            i = increment(i,True)
        if (( i > len(fullstr) and not(backward)) or ((i < 1) and backward)):
                break
        if (contains(letter(i,fullstr),chars,casesensitive)):
            break
        thisletter = letter(i,fullstr)
        new = join(new,thisletter)
    if newstr:
        return new
    else:
        return i

def join(*strs):
    joined = ""
    for thisstr in strs:
        joined = concat([joined,str(thisstr)])
    return (joined)

def iswhitespace(char):
    return ((str(char).isspace()) or (char == ""))

def concat(stringslist,between = "",last = False):
    if type(stringslist) == str:
        stringslist = stringslist.split(",")
    combined = ""
    onstring = 0
    for item in stringslist:
        onstring = onstring + 1
        if ((onstring == len(stringslist)) and not(last)):
            tojoin = [combined,str(item)]
        else:
            tojoin = [combined,str(item),str(between)]
        combined = ''.join(tojoin)
    return(combined)
    
def indexofstr(substr,fullstr,casesensitive = True,backward = False):
    if not(((contains(substr,fullstr) and not(backward))) or ((contains(reverse(substr),fullstr) and backward))):
        if backward:
            return len(fullstr)
        else:
            return 0
    else:
        startindex = findstr(substr,fullstr,0,backward)
        if ((not(backward) and (startindex == 0)) or (backward and startindex == len(fullstr))):
            return startindex
        else:
            if backward:
                startindex = startindex + len(substr) + 1
            else:
                startindex = startindex + len(substr) - 1
            return startindex
 
def removeall(substr,fullstr,casesensitive = True):
    ''' 
    oldstr = fullstr
    newstr = removefromstr(substr,oldstr)
    while newstr != oldstr:
        oldstr = newstr
        newstr = removefromstr(substr,oldstr)
    return (newstr)
    '''
    return(replaceall(fullstr,substr,"",casesensitive))
    
def replaceall(fullstr,substr,newstr,casesensitive = True):
    new = str(fullstr).replace(str(substr),str(newstr))
    if not(casesensitive):
        new = str(new).replace(lowerstr(str(substr)),str(newstr))
        new = str(new).replace(upperstr(str(substr)),str(newstr))
        new = str(new).replace(capitalizestr(str(substr)),str(newstr))
        new = str(new).replace(capitalizewords(str(substr)),str(newstr))
    return (new)

def splitstr(fullstr,substr):
    return (str(fullstr).split(str(substr)))

def capitalizestr(word):
    return (str(word).capitalize())

def capitalizewords(sentence):
    #words = getwords(sentence)
    #newwords = []
    #for word in words:
            #newwords.append(str(word).capitalize())
    #new = concat(newwords," ")
    #return (new)
    return(capwords(sentence))
    
def upperstr(fullstr):
    return (str(fullstr).upper())

def lowerstr(fullstr,docasefold = True):
    if docasefold:
        return (str(fullstr).casefold())
    else:
        return (str(fullstr).casefold())

def removeline(index,lines):
    del lines[index - 1]
    return(lines)

def linestostring(lines):
    newstring = concat(lines,"\n")
    return (newstring)

def wordstostring(words):
    newstring = concat(words," ")
    return (newstring)


def getwords(fullstr,removewhitespacefromwords = True,allwhitespace = True,tabs = True):
    if allwhitespace:
        words = fullstr.split()
    else:
        thisword = ""
        words = []
        for i in fullstr:
            if ((i == "") or ((i == "    ") and tabs)):
                if not(iswhitespace(thisword)):
                    words.append(thisword)
                thisword = ""
            else:
                thisletter = i
                thisword = thisword + thisletter
    if removewhitespacefromwords:
        newwords = []
        for item in words:
            newwords.append(removewhitespace(item,True,True))
        words = newwords
    return (words)

def stringtoliteralstring(fullstr):
    online = 0
    stringlines = getlines(fullstr,False,False)
    encoded = "encoded = \""
    for thisline in stringlines:
        online = online + 1
        encoded = encoded + (thisline.replace("\\","\\\\")).replace("\n",r"\n").replace("\"",r"\"")
    encoded = encoded + "\""
    return encoded
                

def removewhitespace(fullstr,beginning = True,end = True,allwhitespace = False):
    if (fullstr == "") or (fullstr is None):
        return("")
    newstr = ""
    for i in fullstr:
        if not(iswhitespace(i)):
            newstr = newstr + i
    if newstr == "":
        return ""
    if allwhitespace: #this option removes all whitespace, so it overrides other two options. No need to do remove from beginning or end if all has already been removed!
        newstr = ""
        for i in fullstr:
            if not(iswhitespace(i)):
                newstr = newstr + i
    else:
        newstr = fullstr
        if beginning:
            i = 0
            while (letter(i,newstr) == "") or iswhitespace(letter(i,newstr)):
                i = i + 1
            newstr = substring(newstr,i,len(newstr))
        if end:
                i = len(newstr)
                while iswhitespace(letter(i,newstr)):
                    i = i - 1
                newstr = substring(newstr,1,i)
    return (newstr)

def removeblanklines(fullstr,beginning = True,end = True,allblanklines = False): #make sure you understand this function! it does not by default remove all blank lines, even though it sounds like it does
    lines = getlines(fullstr,False,False)
    if allblanklines: #this option removes all blank lines, so it overrides other two options. No need to do remove from beginning or end if all has already been removed!
        newlines = []
        for thisline in lines:
            if not(thisline == "\n"):
                newlines.append(i)
    else:
        newlines = []
        if beginning:
            i = 0
            while (lines[i - 1] == "\n"):
                i = i + 1
            while i < len(lines):
                i = i + 1
                newlines.append(lines[i - 1])
        if end:
                lines = newlines
                newlines = []
                i = len(lines)
                while (lines[i - 1] == "\n"):
                    i = i - 1
                while i > 1:
                    i = i - 1
                    newlines.insert(0,lines[i - 1])
    newstr = linestostring(newlines)
    return (newstr)
    

def skipspaces(fullstr,spacescount = 1,allwhitespace = True,backward = False,newstr = True):
    def countwhitespace(fullstr,allwhitespace):
         if allwhitespace:
              return occurencesofanyof(whitespacechars,fullstr)
         else:
              return occurencesof(" ",fullstr)
            
def skipspaces(fullstr,spacescount = 1,allwhitespace = True,backward = False,newstr = True):
    def countwhitespace(fullstr,allwhitespace):
         if allwhitespace:
                          return occurencesofanyof(whitespacechars,fullstr)
         else:
              return occurencesof(" ",fullstr)
    def islastwhitespace(fullstr,allwhitespace):
        hisletter = letter(i,fullstr)
        if allwhitespace:
           return (contains(thisletter,allwhitespacechars))
        else:
             return (thisletter == " ")
    '''
    if ((countwhitespace(fullstr,allwhitespace) < spacescount) or ((countwhitespace(fullstr,tabs) == spacescount) and (islastwhite(fullstr,allwhitespace)))):
         return ""
    else:
         newstr = ""
         i = 0
         counted = 0
    '''
    counted = 0
    new = fullstr
    iteration #unused, just for the for loop
    for iteration in range(spacescount):
        oldlen = len(new)
        if allwhitespace:
                new = readuntil(allwhitespace,new,0,backward,False,True)
                new = readuntilnot(allwhitespace,new,0,backward,False,True)
        else:
                new = readuntil(" ",fullstr,0,backward,False,True)
                new = readuntilnot(" ",fullstr,0,backward,False,True)
                newlen = len(new)
                counted = oldlen - newlen
    if newstr:
        return new
    else:
        return counted
         

#   List functions

def formatlist(thislist,newlines = 1):
    newlines = int(newlines)
    formatted = ""
    i = 0
    listlen = len(thislist)
    for thisitem in thislist:
        i = i + 1
        formatted = formatted + thisitem
        if i != listlen:
            formatted = formatted + ("\n" * newlines)
    return(formatted)

def listcontainslist(list1,list2,strikes = 0):
    strikecount = 0
    templist = list2
    for item in list1:
        if indexofitem(item,templist) != -1:
            listremoveitem(item,templist)
        else:
            strikecount = increment(strikecount)
    return (not(strikescount > strikes))

def listcontains(item,thislist,casesensitive = True):
    if len(thislist) == 0:
        return(False)
    else:
        if not(casesensitive):
            item = lowerstr(item)
            newlist = []
            for thisitem in thislist:
                newlist.append(lowerstr(thisitem))
            thislist = newlist
        return(item in thislist)

def listremoveindex(index,thislist):
    del thislist[index - 1:index]
    return(thislist)

def listrandom(thislist): #pick random item from list
    if len(thislist) == 0: #we can't choose from 0 choices, so random.choice gives us an error!
        return None
    else:
        return(random.choice(thislist))


def listremoveitem(item,thislist):
    ''' i = 0
    found = True
    while str(thislist[i - 1]) != str(item):
        i = i + 1
        if i > len(thislist):
            found = False
            break
    if found:
        listremoveindex(i,thislist) '''
    thislist.remove(item)
    return(thislist)

def listreplaceall(thislist,item,new):
    ''' i = 0
    found = True
    while str(thislist[i - 1]) != str(item):
        i = i + 1
        if i > len(thislist):
            found = False
            break
    if found:
        listremoveindex(i,thislist)
        '''
    for i in range(len(thislist)):
        thisitem = thislist[i]
        if thisitem == item: #type is considered
            thislist[i] = new
    return(thislist)  

def listreplaceindex(thislist,index,new):
    ''' i = 0
    found = True
    while str(thislist[i - 1]) != str(item):
        i = i + 1
        if i > len(thislist):
            found = False
            break
    if found:
        listremoveindex(i,thislist) '''
    thislist[index - 1] = new
    return (thislist)
    
def indexofitem(item,thislist):
    if len(thislist) == 0:
        return(-1)
    try:
        return(thislist.index(item) + 1)
    except Exception:
        return(-1)

def listitembyname(itemname,namelist,wantedlist):
    return wantedlist[indexofitem(itemname,namelist) - 1]

def listadd(item,thislist):
    if type(thislist) == set:
        thislist.add(item)
    else:
        thislist.append(item)
    return(thislist)
    
def listinsert(item,index,thislist):
    thislist.insert(index - 1,item)
    return(thislist)

def listitem(i,thislist):
    if i < 1:
        return None
    if i > len(thislist):
        return None
    else:
        return (thislist[i - 1])

item = listitem #same thing but different name
numberofitem = indexofitem #same thing but different name

#   Dictionary functions

def formatdict(thisdict,newlines = 1):
    newlines = int(newlines)
    formatted = ""
    i = 0
    dictlen = len(thisdict)
    for key in thisdict:
        i = i + 1
        formatted = formatted + key + ": " + thisdict[key]
        if i != dictlen:
            formatted = formatted + ("\n" * newlines)
    return(formatted)

formatdictionary = formatdict #same thing but different name

def dictitem(key,thisdict):
    return(thisdict.get(key))
    
dictget = dictitem #same thing but different name

def dictset(key,new,thisdict):
    thisdict[key] = new
    return(thisdict)

def dictremove(key,thisdict):
    del thisdict[key]
    return(thisdict)

dictadd = dictset #same thing but different name
dictremoveitem = dictremove #same thing but different name

def stringtodict(thisstring):
    return(ast.literal_eval(thisstring))

stringtodictionary = stringtodict #same thing but different name

#  Variable functions

def variableexists(varname):
    return(varname in globals())

def globalvars():
    return(globals())

class variable:
    exists = variableexists
    globalvars = globalvars

#   Math functions

def increment(val,forward = True,step = 1):
    if forward:
         return(val + step)
    else:
         return(val - step)

def roundnumber(x,digits = None):
    return (round(x, ndigits = digits))

def divisibleby(x,y):
    return((x%y) == 0)

def iseven(x):
    return(divisible(x,2))

def isodd(x):
    return(not(iseven(x)))

def mod(x,y):
    return(x%y)

def floor(x):
    return(math.floor(x))

def ceiling(x):
    return(math.ceil(x))

floorof = floor #same thing, but different name
ceilingof = ceiling #same thing, but different name
ceil = ceiling #same thing, but different name
ceilof = ceiling #same thing, but different name
even = iseven #same thing, but different name
odd = isodd #same thing, but different name
isdivisibleby = divisibleby #same thing, but different name
divisible = divisibleby #same thing, but different name
multipleof = divisibleby #same thing, but different name
ismultipleof = divisibleby #same thing, but different name
average = statistics.mean #same thing, but different name
averageof = statistics.mean #same thing, but different name
meanof = statistics.mean #same thing, but different name
mean = statistics.mean  #same thing, but different name

def randomnum(minnum,maxnum,decimalplaces = 0,step = 1):
        minnum = int(minnum) #make sure they are numbers and not strings so random function works
        maxnum = int(maxnum)
        decimalplaces = int(decimalplaces)
        step = int(step)
        minnum = str(minnum) #convert to string to get decimal places and do string manipulation
        if not("." in minnum):
            currentdecimalplaces = 0
        else:
            currentdecimalplaces = int(readafter(minnum,"."))
        if (currentdecimalplaces < decimalplaces):
            if currentdecimalplaces == 0:
                minnum = join(minnum,".") #add decimal place if it is not already there
            neededdecimalplaces = decimalplaces - currentdecimalplaces
            for decimalplace in neededdecimalplaces:
                minnum = join(minnum,0) #the number of decimal places of the number with the most decimal places is how many digits are in the random number, so we just add 0s 
        minnum = int(minnum) #convert back to number
        return(random.randrange(minnum, maxnum, step)) #finally, we can choose the random number
    
def dectohex(dec):
    return substring((hex(int(dec))),3) #remove 0x at beginning

def hextodec(hexvalue):
    if contains("0x",hexvalue):
        hexvalue = substring(hexvalue,3) #remove 0x at beginning
    return (int(hexvalue,16))

#   File  / Command functions

def runcommand(command):
    os.system(command)

command = runcommand #same thing, but different name
run_command = runcommand #same thing, but different name

def read_file(path,readtype = "r"):
    if not(fileexists(path)):
            filenotfounderror(path)
            return None
    try:
        file = openfile(path,readtype,"utf8")
        content = file.read()
    except Exception:
         try:
            file = openfile(path,readtype,"utf16")
            content = file.read()
         except Exception:
            try:
                file = openfile(path,readtype,"utf32")
                content = file.read()
            except Exception:
               unknownfileopenerror()
               return None
    file.close()
    return content
    
def write_file(path,new):
    file = openfile(path, "w")
    file.write(str(new))
    file.close()

def fileexists(path,giveerror = False):
    if (giveerror and not(exists(path))):
        filenotfounderror(path)
    return(exists(path))

def getfilename(fullname):
    if (contains("/",fullname) or (contains("\\",fullname))):
         #File path
         return(os.path.splitext(os.path.basename(str(fullname)))[0])
    else:
         #File name
         return(os.path.splitext(str(fullname))[0])

def getfileextension(fullname):
    if (contains("/",fullname) or (contains("\\",fullname))):
         #File path
         path = os.path.splitext(os.path.basename(str(fullname)))[1]
         #Remove the "". (ex: .txt -> txt)
         path = substring(path,2,len(path))
         return(path)
    else:
         #File name
         path = os.path.splitext(str(fullname))[1]
         #Remove the "". (ex: .txt -> txt)
         path = substring(path,2,len(path))
         return(path)

def getdirectory(path):
    return(os.path.basename(path))

getfiledirectory = getdirectory #same thing, but different name
getfiledir = getdirectory #same thing, but different name
getdir = getdirectory #same thing, but different name
getbasedir = getdirectory #same thing, but different name
getfilebasedir = getdirectory #same thing, but different name
getbasedirectory = getdirectory #same thing, but different name
getfilebasedir = getdirectory #same thing, but different name

def getfilename(path):
    return(os.path.dirname(path))

def folderexists(path,giveerror = False):
    if ((lastletter(path) == "/") or (lastletter(path) == "\\")):
        path = substring(path,1,len(path) - 1)
    if (giveerror and not(os.path.isdir(path))):
        foldernotfounderror(path)
    return(os.path.isdir(path))

pathexists = folderexists #same thing, but different name
direxists = folderexists #same thing, but different name
directoryexists = folderexists #same thing, but different name

def getfiles(directory,getfolders = True):
    if ((lastletter(directory) == "/") or (lastletter(directory) == "\\")):
        path = substring(directory,1,len(directory) - 1)
    if not(os.path.isdir(directory)):
        foldernotfounderror(directory)
        return(None)
    else:
        if getfolders:
            files = listdir(directory)
        else:
            #Thanks to https://stackoverflow.com/questions/3207219/how-do-i-list-all-files-of-a-directory
            files = [f for f in listdir(directory) if isfile(buildpath(directory, f))]
        return(files)


def openfile(path,opentype,encodingtype = "utf8"):
    exceptions = ["w","a"] #some modes create a new file if it does not exist, so we do not need to return None if it does not exist
    if not(fileexists(path,False)):
        if len(exceptions) == 0:
               filenotfounderror(path)
               return None
        else:
            if not(opentype in exceptions):
               filenotfounderror(path)
               return None 
    file = None
    if contains("b",opentype):
        file = open(path, str(opentype))
    else:
        try:
            file = open(path, str(opentype),encoding = encodingtype)
        except Exception:
            try:
                file = open(path, str(opentype),encoding = "utf8")
            except UnicodeDecodeError:
                try:
                    file = open(path, str(opentype),encoding = "utf16")
                except UnicodeDecodeError:
                    try:
                        file = open(path, str(opentype),encoding = "utf32")
                    except UnicodeDecodeError:
                        fileencodingunknownerror(path)
                        file = None
            else:
               unknownfileopenerror(path)
               return None
    return(file)


def buildpath(directory,name):
    directory = str(directory)
    name = str(name)
    if contains("/",directory):
        separator = "/"
    else:
        separator = "\\"
    if lastletter(directory) == separator:
        return(directory + name)
    else:
        return(concat([directory,separator,name]))

def filetostring(path):
    online = 0
    if not(fileexists(path)):
        sys.exit("Error: File not found at path \"" + path + "\"")
    thisfile = open(path,"r")
    totallines = len(thisfile.readlines())
    encoded = "encoded = \""
    thisfile = open(path,"r")
    for thisline in thisfile.readlines():
        online = online + 1
    return(encoded)

def getsubfile(root,subpath,returntype = "path"):
    newpath = buildpath(root,subpath)
    if ((returntype == "path") or (returntype == "p")):
        return(newpath)
    else:
        if fileexists(newpath):
            if ((returntype == "read") or (returntype == "r") or (returntype == "content")):
                return(read_file(newpath),"r")
            elif ((returntype == "readbytes") or (returntype == "rb") or (returntype == "bytes")):
                return(read_file(newpath),"rb")
            elif ((returntype == "w") or (returntype == "write")):
                return(openfile(newpath),"w")
            elif ((returntype == "wb") or (returntype == "writebytes")):
                return(openfile(newpath),"wb")
            else:
                #Return type not recognized - assume path
                return(newpath)
        else:
            filenotfounderror(newpath)
            return None

def getsubfolder(root,subpath,returntype = "path"):
    newpath = buildpath(root,subpath)
    if ((returntype == "path") or (returntype == "p")):
        return(newpath)
    else:
        if folderexists(newpath):
            if ((returntype == "read") or (returntype == "r") or (returntype == "content") or (returntype == "files")):
                return(getfiles(newpath,True))
            else:
                #Return type not recognized - assume path
                return(newpath)
        else:
            foldernotfounderror(newpath)
            return None

def parsexmlfile(path):
    log("Parsing xml file: " + path)
    if fileexists(path,True):
        extension = getfileextension(path)
        if extension != "xml":
            warning("Attempting to parse '" + path + "' as an xml file, even though it's file extension is '" +  extension + "'.")
        success = 1
        try:
            return(ElementTree.parse(path))
        except:
            success = 0
        finally:
            if success:
                log("Successfully parsed xml file: " + path)
            else:
                error("Failed to parse xml file: '" + path + "': Invalid Format. This file may be corrupted.")
                return(None)
    else:
        error("Failed to parse xml file: '" + path + "': File not found at this file path.")
        return(None)

def parsexmlstring(xmlstring):
        log("Parsing xml string: " + xmlstring)
        success = 1
        try:
            return(ElementTree.fromstring(xmlstring))
        except:
            success = 0
        finally:
            if success:
                log("Successfully parsed xml strin: " + xmlstring)
            else:
                error("Failed to parse xml string: '" + xmlstring + "': Invalid Format. This data may be corrupted.")
                return(None)

def getxmlroot(parsedxml):
    log("Getting root of xml data: " + str(parsedxml))
    success = 1
    try:
        root = parsedxml.getroot()
        return(root)
    except:
        success = 0
    finally:
        if success:
            log("Got root of xml data '" + str(parsedxml) + "': " + str(root))
        else:
            error("Failed to get root of xml data: '" + str(parsedxml) + "'")
            
def getxmlroottag(parsedxml):
    log("Getting root tag of xml data: " + str(parsedxml))
    success = 1
    try:
        #root = str(parsedxml.getroot())
        #root = readafter(root,"'")
        #root = readbefore(root,"'")
        #root = substring(root,1,len(root) - 2)
        root = parsedxml.getroot().tag
        return(root)
    except:
        success = 0
    finally:
        if success:
            log("Got root tag of xml data '" + str(parsedxml) + "': " + root)
        else:
            error("Failed to get root tag of xml data: '" + str(parsedxml) + "'")
            return(None)

def getxmlrootelements(xmlroot):
    elements = []
    for thiselement in xmlroot:
        elements.append(thiselement)
    return(elements)

def getmainactivityfromxmlroot(xmlroot):
    candidates = xmlroot.findall("application/activity")
    newcandidates = []
    for thiscandidate in candidates:
        thiscandidateattributes = thiscandidate.attrib
        #if (list(thiscandidateattributes.keys()) == ['{http://schemas.android.com/apk/res/android}configChanges', '{http://schemas.android.com/apk/res/android}hardwareAccelerated', '{http://schemas.android.com/apk/res/android}launchMode', '{http://schemas.android.com/apk/res/android}name', '{http://schemas.android.com/apk/res/android}screenOrientation']):
        #if (("{http://schemas.android.com/apk/res/android}configChanges" in thiscandidateattributes) and ("{http://schemas.android.com/apk/res/android}name" in thiscandidateattributes) and ("{http://schemas.android.com/apk/res/android}screenOrientation" in thiscandidateattributes) and ("{http://schemas.android.com/apk/res/android}launchMode" in thiscandidateattributes)):
            #newcandidates.append(thiscandidate)
        newcandidates.append(thiscandidate)
    candidates = newcandidates
    mainactivitycandidates = []
    for thiscandidate in candidates:
        thiscandidateattributes = thiscandidate.attrib
        mainactivitycandidates.append(thiscandidateattributes["{http://schemas.android.com/apk/res/android}name"])
    if len(mainactivitycandidates) == 0:
        return(None)
    else:
        mainactivity = mainactivitycandidates[0]
        return(mainactivity)

def getxmlrootattributes(parsedxml):
    log("Getting root tag of xml data: " + str(parsedxml))
    success = 1
    try:
        #root = str(parsedxml.getroot())
        #root = readafter(root,"'")
        #root = readbefore(root,"'")
        #root = substring(root,1,len(root) - 2)
        root = parsedxml.getroot().attrib
        return(root)
    except:
        success = 0
    finally:
        if success:
            log("Got root attributes of xml data '" + str(parsedxml) + "': " + str(root))
        else:
            error("Failed to get root attributes of xml data: '" + str(parsedxml) + "'")
            return(None)

class filemanager:
    read = read_file
    write = write_file
    openfile = openfile
    exists = fileexists
    fileexists = fileexists
    folderexists = folderexists
    pathexists = pathexists
    directoryexists = directoryexists
    direxists = direxists
    buildpath = buildpath
    filetostring = filetostring
    subfile = getsubfile
    getsubfile = getsubfile

#   Date / time functions

def gettime(timeparam = True,dateparam = False):
    if timeparam:
        currenttime = time.localtime()
        formattedtime = time.strftime("%H:%M:%S",currenttime)
        if dateparam:
            currenttime = time.localtime()
            formattedtime = formattedtime + ": " + time.strptime("%Y-%m-%d",currenttime)  
    else:
        if dateparam:
            currenttime = time.localtime()
            formattedtime = time.strptime("%Y-%m-%d",currenttime)  
    return(formattedtime)

def formattime(rawtime,timeparam = True,dateparam = False):
    if timeparam:     
        formattedtime = time.strftime("%H:%M:%S",rawtime)
        if dateparam:
            formattedtime = formattedtime + ": " + time.strptime("%Y-%m-%d",rawtime) 
    else:
        if dateparam:
            formattedtime = time.strptime("%Y-%m-%d",rawtime)  
    return(formattedtime)

def getrawtime(): #time in miliseconds
    return (int(time.perf_counter()*1000)) #localtime only returns seconds, not miliseconds

def waitmili(miliseconds):
    time.sleep(miliseconds / 1000)

def waitseconds(seconds):
    time.sleep(seconds)

def sleepmili(miliseconds):
    time.sleep(miliseconds / 1000)

def sleepseconds(seconds):
    time.sleep(seconds)

def startspeedtest():
    global starttime
    starttime = getrawtime()

def endspeedtest():
    speedtesttime = getrawtime() - starttime #unformatted int in miliseconds
    global endtime #global
    endtime = speedtesttime
    speedtesttimetaken = str(endtime)  #formatted string | to-do: make formatted
    global timetaken
    timetaken = speedtesttimetaken #global
    return(speedtesttimetaken)

class timemanager:
    rawtime = getrawtime
    formattime = formattime
    gettime = gettime
    sleepseconds = sleepseconds
    wait = waitseconds
    waitmili = waitmili
    waitseconds = waitseconds
    sleep = sleepseconds
    sleepmili = sleepmili
    sleepseconds = sleepseconds
    startspeedtest = startspeedtest
    endspeedtest = endspeedtest
    global speedtest
    class speedtest:
        start = startspeedtest
        end = endspeedtest
        def timetaken(formatted = True):
            if formatted:
                return(timetaken)
            else:
                return(endtime)
        time = timetaken

#   IO Functions

def prompt(ask = ""):
    answer = input(str(ask) + "\n")
    print("\n")
    return(answer)

def cleario():
    print("\nNot done, idk how!\n")

outputtext = print #same thing, but different name
flushio = cleario #same thing, different name
clearconsole = cleario  #same thing, but different name

class console:
    prompt = prompt
    output = outputtext
    clear = cleario
    flush = cleario


#            Higher level functions

#   Settings

class settingsmanager():
    
    def init():
        global currentsettings
        currentsettings = defaultsettings
        
        
    def update(settingname,new):
        global currentsettings
        currentsettings[settingname] = new

#   Error-handling / log functions

def warning(message,actions= ["log","print"]):
    #log, print, printlog, printcurrentsublog, terminate, stop current function, etc.
    if actions == []: #this will cause error, so set back to default
        actions = ["log","print"]
    if ("log" in actions):
        log("WARNING: " + message,True)
    if ("print" in actions):
        print("WARNING: " + message)

def error(message,actions = ["log","print"]):
#log, print, printlog, printcurrentsublog, terminate, stop current function, etc.
    if actions == []: #this will cause error, so set back to default
        actions = ["log","print"]
    if ("log" in actions):
        log("ERROR: " + message,True)
    if ("print" in actions):
        print("ERROR: " + message)

def info(message):
    print("INFO: " + message)
    
def log(message,important = True,time = True,date = False):
#logtypes = error, warning, unimportant event (ex: end while loop), important event (ex: end high level function) , user note (ex: this happens because, this is so), result (ex function return, value = )
    tolog = str(message)
    if time:
        tolog = str(gettime()) + ": " + tolog
    if date:
        if time:
            tolog = str(gettime()) + ": " + tolog
        else:
            tolog = str(gettime()) + ": " + tolog
    global fulllog
    fulllog.append(str(tolog))
    global truncatedfulllog
    if len(message) < truncateloglength: #length of original message, not of full message with date / time included
        truncatedfulllog.append(tolog)
    else:
        truncatedfulllog.append(substring(tolog,0,(200 + (len(tolog) - len(message)))) + _truncatedstring)
    if important:
        global importantlog
        importantlog.append(tolog)
        global truncatedimportantlog
        if len(message) < truncateloglength: #length of original message, not of full message with date / time included
            truncatedimportantlog.append(tolog)
        else:
            truncatedimportantlog.append(substring(tolog,0,(200 + (len(tolog) - len(message)))) + _truncatedstring)
         
#   Lib functions

def offsettohex(offset,filepath,hexbytes = 40):
    if contains("0x",offset):
        offset = readafter(offset,"0x")
    libfile = openfile(filepath,'rb')
    findoffset = int(offset, 16)
    libfile.seek(findoffset)
    return (libfile.read(int(hexbytes)).hex().upper())

def offsetstohexlist(offsetlist,filepath,hexbytes = 40,returntuple = True):
    if type(offsetlist) == str:
        if (len(offsetlist) > _offsetlength):
            if letter(_offsetlength + 1,offsetlist) == " ":
                spaces = 1
            else:
                spaces = 0
        else:
            spaces = 0 #only one offset
        if spaces == 0:
            index = -1
            while index < len(offsetlist) - 1:
                thisoffset = ""
                i2 = 0
                while i2 < _offsetlength + 1:
                    i2 = i2 + 1
                    thisoffset = thisoffset + str(offsetlist[index + i2])
                offsets.append(thisoffset)
                index = index + _offsetlength + 1
        else:
            offsets = offsetlist.split(" ")
    else:
        offsets = offsetlist
    hexlist = []
    for offset in offsetlist:
        hexlist.append(offsettohex(offset,filepath,hexbytes))
    if returntuple:
        return(hexlist)
    else:
        return(hexlist)

offsetstohex = offsetstohexlist #same thing, but different name
offsetstohexlist = offsetstohexlist #same thing, but different name

#   Arm hex conversion functions
def hextoreturnvalue(hexvalue,armtype,returnhex = False):
    code = hextoarm(hexvalue,armtype)
    if armtype == "64bit":
        returnval = readuntilnot("#",code,0,True)
        if returnhex:
            if not(contains("x",code)): #x means hex, w means decimal
                returnval = dectohex(returnval) #it's in decimal, so convert to hex
        else:
            if contains("x",code): #x means hex, w means decimal
                returnval = hextodec(returnval) #it's in hex, so convert to decimal
        return 
    

def decimalvaluetoreturnohex(decimalvalue,armtype):
    if armtype == "64bit":
        code = "Mov w0, #" + str(decimalvalue) + "\n" + "ret"
        return armtohex(code,armtype)

def hexvaluetoreturnohex(hexvalue,armtype):
    if armtype == "64bit":
        code = "Mov x0, #" + str(decimalvalue) + "\n" + "ret"
        return armtohex(code,armtype)

def armtohex(armcode,armtype):
    return "Not Done"

def hextoarm(hexcode,armtype):
    return "Not Done"

#   APK functions

def getalllibsfromapk(apkpath):
    pass

def getmetadatafromapk(apkpath,returntype = "path"): #make sure apk is decompiled!
    log("Finding global.metadata.dat for decompiled apk " + apkpath)
    if getfileextension(apkpath) == "apk":
        apknotdecompilederror(apkpath)
        return None
    if not(folderexists(apkpath)):
        foldernotfounderror(apkpath)
        return None
    if contains("/",apkpath):
        metadatapath = "assets/bin/Data/Managed/Metadata/global-metadata.dat"
    else:
        metadatapath = "assets\\bin\\Data\\Managed\\Metadata\\global-metadata.dat"
    metadatapath = getsubfile(str(apkpath),metadatapath,"path")
    if fileexists(metadatapath):
        log("Found metadata for decompiled apk " + apkpath)
        return(getsubfile(str(apkpath),metadatapath,returntype))
    else:
        log("Could not find global-metadata.dat for decompiled apk '" + apkpath + "' at expected path 'assets/bin/Data/Managed/Metadata/global-metadata.dat'")
        #Does the metadata folder exist?
        if contains("/",apkpath):
            metadatafolderpath = buildpath(str(apkpath),"assets/bin/Data/Managed/Metadata")
        else:
            metadatafolderpath = buildpath(str(apkpath),"assets\\bin\\Data\\Managed\\Metadata")
        if not(folderexists(metadatafolderpath)):
            log("Could not find Metadata folder for decompiled apk '" + apkpath + "' at expected path 'assets/bin/Data/Managed/Metadata'")
            #No metadata folder
            metadatafilenotfounderror(metadatapath)
            return None
        else:
            #Maybe the metadata file is renamed - let's check.
            files = getfiles(metadatafolderpath)
            if len(files) == 1:
                #There is only one file in this folder, like a normal metadata folder. If it is a .dat file, let's assume the metadata file was renamed!
                thisfile = files[0]
                #if checkforstringat(".dat",thisfile,len(thisfile) - 3):
                if getfileextension(thisfile) == "dat":
                    log("Found suspicous file called '" + thisfile + "' in decompiled apk '" + apkpath + "' in metadata folder ('assets/bin/Data/Managed/Metadata'). Assuming this file is global-metadata.dat remamed for obfuscation purposes.")
                    log("Found metadata for decompiled apk " + apkpath)
                    return(getsubfile(str(apkpath),buildpath(metadatafolderpath,thisfile),returntype))
            else:
                metadatafilenotfounderror(metadatapath)
                return None

def getandroidmanifestfromapk(apkpath,returntype = "path"): #make sure apk is decompiled!
    log("Finding AndroidManifest.xml for decompiled apk " + apkpath)
    if getfileextension(apkpath) == "apk":
        apknotdecompilederror(apkpath)
        return None
    if not(folderexists(apkpath)):
        foldernotfounderror(apkpath)
        return None
    manifestpath = "AndroidManifest.xml"
    manifestpath = getsubfile(str(apkpath),manifestpath,"path")
    if fileexists(manifestpath):
        log("Found AndroidManifest.xml for decompiled apk " + apkpath)
        return(getsubfile(str(apkpath),"AndroidManifest.xml",returntype))
    else:
        androidmanifestnotfounderror(metadatapath)
        log("Could not find AndroidManifest.xml for decompiled apk '" + apkpath + "' at expected path 'AndroidManifest.xml'")
        return None

def getmainactivityfromapk(apkpath): #make sure apk is decompiled!
    log("Finding mainactivity for decompiled apk '" + apkpath + "'")
    if getfileextension(apkpath) == "apk":
        apknotdecompilederror(apkpath)
        return None
    if not(folderexists(apkpath)):
        foldernotfounderror(apkpath)
        return None
    androidmanifest = getandroidmanifestfromapk(apkpath,"path")
    if androidmanifest is None:
        return(None)
    parsedxml = parsexmlfile(androidmanifest)
    if parsedxml is None:
        return(None)
    root = getxmlroot(parsedxml)
    if root is None:
        return(None)
    mainactivity = getmainactivityfromxmlroot(parsedxml)
    if mainactivity is None:
        mainactivitynotfounderror(androidmanifest)
        return(None)
    else:
        return(mainactivity)


def getallsmalifromapk(apkpath,returntype = "content"): #make sure apk is decompiled!
    log("Finding all smali folders for decompiled apk " + apkpath)
    found = []
    if getfileextension(apkpath) == "apk":
        apknotdecompilederror(apkpath)
        return None
    if not(folderexists(apkpath)):
        foldernotfounderror(apkpath)
        return None
    smalipath = "smali"
    smalipath = getsubfile(str(apkpath),smalipath,"path")
    if folderexists(smalipath):
        log("Found smali folder for decompiled apk " + apkpath)
        found.append("smali")
    else:
        log("Could not find smali folder for decompiled apk '" + apkpath + "' at expected path 'smali'")
        return None
    smalinames = ["classes","assets"]
    for thisname in smalinames:
        smalipathtry = "smali_" + thisname
        if folderexists(buildpath(str(apkpath),smalipathtry)):
            log("Found " + smalipathtry + " folder for decompiled apk " + apkpath)
            smalipath = smalipathtry
            found.append(smalipath)
        smalipathtry = "smali_" + thisname + "1"
        if folderexists(buildpath(str(apkpath),smalipathtry)):
            log("Found " + smalipathtry + " folder for decompiled apk " + apkpath)
            smalipath = smalipathtry
            found.append(smalipath)
        i = 2
        smalipathtry = "smali_" + thisname + "2"
        while folderexists(buildpath(str(apkpath),smalipathtry)):
            log("Found " + smalipathtry + " folder for decompiled apk " + apkpath)
            smalipath = smalipathtry
            found.append(smalipath)
            i = i + 1
            smalipathtry = "smali_" + thisname + str(i)
    log("Found all smali folders for decompiled apk '" + apkpath)
    smalifolders = {}
    for thissmali in found:
        smalifolders[thissmali] = getsubfolder(str(apkpath),thissmali,returntype)
    return(smalifolders)
    
findmetadatafromapk = getmetadatafromapk #same thing, but different name

#   Dump.cs functions

def loaddumpcs(path,attributeswarning = True):
    global dumpcs
    dumpcs = read_file(path)
    if (attributeswarning and (contains("[CompilerGeneratedAttribute]",dumpcs))): #and (contains("[DebuggerBrowsableAttribute]",dumpcs))):
        dumpcsattributeswarning(path)
    return(dumpcs)

def getobjectof(index):
    index = int(index)
    global dumpcs #local dumpcs defaults to global dumpcs if not defined manually
    if not(variableexists("dumpcs")):
             objectnotdeclarederror("dumpcs")
    if index > (len(dumpcs)- len("// Namespace: ")): #Impossible scenario, but ocd makes me put this here!
        return("")
    rangebehind = 0
    startpos = 0
    while startpos == 0:
        startpos = dumpcs.find("// Namespace: ",((index - rangebehind) - len("// Namespace: ")),(index - rangebehind)) + 1
        if (((index - rangebehind) - len("// Namespace: ")) < 1): #Not found - must be the beginning (shouldn't happen)
            startpos = 0
            return("") # no method
        rangebehind = rangebehind + 1
    endpos = dumpcs.find("// Namespace: ",startpos + len("// Namespace: "),len(dumpcs)) #find the next "Namespace: " after startpos
    if endpos == -1: #Not found - must be the last object
        endpos = len(dumpcs) #set to the end
    return (removeblanklines(substring(dumpcs,startpos,endpos),True,True)) #the object is between namespaces

def getmethodof(index):
    index = int(index)
    global dumpcs #local dumpcs defaults to global dumpcs if not defined manually
    if not(variableexists("dumpcs")):
             objectnotdeclarederror("dumpcs")
    if index > (len(dumpcs)- len("\n\n")): #Impossible scenario, but ocd makes me put this here!
        return("")
    rangebehind = 0
    startpos = 0
    while startpos == 0:
        startpos = dumpcs.find("\n\n",((index - rangebehind) - len("\n\n")),(index - rangebehind)) + 1
        if (((index - rangebehind) - len("\n\n")) < 1): #Not found - must be the beginning (shouldn't happen)
            startpos = 0
            return("") # no method
        rangebehind = rangebehind + 1
    endpos = dumpcs.find("\n\n",startpos + len("\n\n"),len(dumpcs)) #find the next \n after startpos
    if endpos == -1: #Not found - shouldn't be possible but we assume it is end of dump.cs
        endpos = len(dumpcs) #set to the end
    methodline = removeblanklines(substring(dumpcs,startpos,endpos)).strip()
    if ((contains(_offsetsuffix,methodline)) and (len(getlines(methodline))) == 1): #just method offset line
        rangebehind = -1
        endpos = 1
        while endpos == 1:
            endpos = dumpcs.find("\n\n",startpos + 3,(startpos + ((index - rangebehind) + len("\n\n")))) + 2
            if  (((index - rangebehind) + len("\n\n")) > len(dumpcs)): #Not found - shouldn't be possible but we assume it is end of dump.cs
                endpos = len(dumpcs) #set to the end
            rangebehind = rangebehind - 1
        methodline = removeblanklines(substring(dumpcs,startpos,endpos)).strip()
        lines = getlines(methodline)
        lines[0] = lines[0].strip() #remove whitespace from the two lines
        lines[1] = lines[1].strip()
        methodline = linestostring(lines)
        if not((contains(_isoffsetstring,methodline)) and contains(_ismethodstring,methodline)): #It isn't a method
            return("")
        else:
            return(methodline)
    else: #method offset line and method type line, or not method
        lines = getlines(methodline)
        if len(getlines(methodline)) < 2: #error - must not be a method
            return("")
        lines[0] = lines[0].strip() #remove whitespace from the two lines
        lines[1] = lines[1].strip()
        methodline = linestostring(lines)
        if not(contains(_offsetsuffix,methodline)): #error - must not be a method
            return("")
        if not((contains(_isoffsetstring,methodline)) and contains(_ismethodstring,methodline)): #It isn't a method
            return("")
            return(methodline)

def getfieldof(index):
    index = int(index)
    global dumpcs #local dumpcs defaults to global dumpcs if not defined manually
    if not(variableexists("dumpcs")):
             objectnotdeclarederror("dumpcs")
    if index > (len(dumpcs)- len("\n")): #Impossible scenario, but ocd makes me put this here!
        return("")
    rangebehind = 0
    startpos = -1
    while startpos == -1:
        startpos = dumpcs.find("\n",((index - rangebehind) - len("\n")),len(dumpcs)) + 1
        if (((index - rangebehind) - len("\n")) < 1): #Not found - must be the beginning (shouldn't happen)
            startpos = 0
            return("") # no field
    endpos = dumpcs.find("\n",startpos + 1,len(dumpcs)) #find the next \n after startpos
    if endpos == -1: #Not found - shouldn't be possible but we assume it is end of dump.cs
        endpos = len(dumpcs) #set to the end
    thisfield = (substring(dumpcs,startpos,endpos)).strip() #field is between new lines
    if not(contains(_isfieldstring,thisfield)): #It isn't a field
            return("")
    return(thisfield)

def getpropertyof(index):
    index = int(index)
    global dumpcs #local dumpcs defaults to global dumpcs if not defined manually
    if not(variableexists("dumpcs")):
             objectnotdeclarederror("dumpcs")
    if index > (len(dumpcs)- len("\n")): #Impossible scenario, but ocd makes me put this here!
        return("")
    rangebehind = 0
    startpos = -1
    while startpos == -1:
        startpos = dumpcs.find("\n",((index - rangebehind) - len("\n")),len(dumpcs)) + 1
        if (((index - rangebehind) - len("\n")) < 1): #Not found - must be the beginning (shouldn't happen)
            startpos = 0
            return("") # no field
    endpos = dumpcs.find("\n",startpos + 1,len(dumpcs)) #find the next \n after startpos
    if endpos == -1: #Not found - shouldn't be possible but we assume it is end of dump.cs
        endpos = len(dumpcs) #set to the end
    thisproperty = (substring(dumpcs,startpos,endpos)).strip() #property is between new lines
    if not(contains(_ispropertystring,thisproperty)): #It isn't a property
            return("")
    return(thisproperty)


def getlineof(index,text,removewhitespace = False):
    index = int(index)
    rangebehind = 0
    startpos = -1
    while startpos == -1:
        startpos = text.find("\n",((index - rangebehind) - len("\n")),len(text)) + 1
        if (((index - rangebehind) - len("\n")) < 1): #Not found - must be the beginning
            startpos = 0
            return("") # no field
    endpos = text.find("\n",startpos + 1,len(text)) #find the next \n after startpos
    if endpos == -1: #Not found - must be at the end
        endpos = len(text) #set to the end
    if removewhitespace:
        return((substring(text,startpos,endpos)).strip()) #this line is between new lines
    else:
        return((substring(text,startpos,endpos))) #this line is between new lines

def offsettomethod(offset):
    if contains("0x",offset):
        offset = readafter(offset,"0x")
    global dumpcs #local dumpcs defaults to global dumpcs if not defined manually
    if not(variableexists("dumpcs")):
             objectnotdeclarederror("dumpcs")
    offsetindex = dumpcs.find(_offsetprefix + offset + _offsetsuffix)
    if offsetindex == -1: #not found
        return("")
    else:
        return(getmethodof(offsetindex))
       
getmethodofoffset = offsettomethod #same thing, but different name

def offsettofield(offset):
    if contains("0x",offset):
        offset = readafter(offset,"0x")
    global dumpcs #local dumpcs defaults to global dumpcs if not defined manually
    if not(variableexists("dumpcs")):
             objectnotdeclarederror("dumpcs")
    offsetindex = dumpcs.find(_offsetprefix + offset + _offsetsuffix)
    if offsetindex == -1: #not found
        return("")
    else:
        return(getfieldof(offsetindex))
       
getfieldofoffset = offsettofield #same thing, but different name

def getobjectofoffset(offset):
    if contains("0x",offset):
        offset = readafter(offset,"0x")
    global dumpcs #local dumpcs defaults to global dumpcs if not defined manually
    if not(variableexists("dumpcs")):
        objectnotdeclarederror("dumpcs")
    offsetindex = dumpcs.find(_offsetprefix + offset + _offsetsuffix)
    return(getobjectof(offsetindex))

offsettoobject = getobjectofoffset #same thing, but different name


def getnamespaces(fullobjects):
    global namespacenames
    global namespacecontent
    global namespaces
    namespacenames = []
    namespacecontent = [] #list of lists (each namespace has list of classes in it)
    i = 0
    for thisobject in fullobjects:
        i = i + 1
        if multipleof(i,1000):
            print(str(i) + "/" + str(len(fullobjects)))
        thisnamespacename = getobjectnamespace(thisobject)
        if len(namespacenames) > 0:
            if thisnamespacename in namespacenames:
               thisnamespacecontent = namespacecontent[indexofitem(thisnamespacename,namespacenames) - 1]
               thisnamespacecontent.append(thisobject)
               namespacecontent = listreplaceall(namespacecontent,indexofitem(thisnamespacename,namespacenames),thisnamespacecontent)
        else:
            thisnamespacecontent = [thisobject]
            namespacenames.append(thisnamespacename)
            namespacecontent.append(thisnamespacecontent)
    namespaces = {}
    for index in range(len(namespacenames)):
        namespaces[namespacenames[index - 1]] = [namespacecontent[index - 1]]
    return(namespaces)

def getfullobjects(dumpcs,getshared = True,toremoveattributes = True,toremoveblanklines = True,toremoveallblanklines = False,returntuple = True):
    global fullobjects
    fullobjects = splitstr(dumpcs,_objectseparator)
    if len(fullobjects) > 0:
        del fullobjects[0] #classes start with "// Namespace: ", so namespace gets everything before it. This means the first one will always go
    if toremoveblanklines: #remove blank lines
        new = []
        i = 0
        for thisitem in fullobjects:
            i = i + 1
            if multipleof(i,1000):
                print(str(i) + "/" + str(len(fullobjects)))
            if toremoveallblanklines:
                newitem = removeblanklines(thisitem,True,True,True)
            else:
                newitem = removeblanklines(thisitem)
            new.append(newitem)
        global flagremovedblanklines
        flagremovedblanklines = True
        fullobjects = new
    new = []
    for thisitem in fullobjects: #Add seperator back on, as string.split excludes the seperator
        newitem = join(_objectseparator,thisitem)
        new.append(newitem)
    fullobjects = new
    #fullobjects = tuple(map(lambda x: _objectseparator + x,fullobjects))
    if toremoveattributes: #remove attributes
        new = []
        i = 0
        for item in fullobjects:
            i = i + 1
            if multipleof(i,1000):
                print(str(i) + "/" + str(len(fullobjects)))
            newitem = removeattributes(item)
            new.append(newitem)
        fullobjects = new
        #fullobjects = tuple(map(removeattributes,fullobjects))
        global flagremovedattributes
        flagremovedattributes = True
    if not(getshared):
        new = []
        i = 0
        for thisitem in fullobjects: #Remove shared objects
            i = i + 1
            if multipleof(i,1000):
                print(str(i) + "/" + str(len(fullobjects)))
            if not(getisshared(thisitem)):
                new.append(thisitem)
        fullobjects = new
        #fullobjects = [thisitem for thisitem in fullobjects if not(getisshared(thisitem))]
        global flagremovedshared
        flagremovedshared = True
    if returntuple:
        return(tuple(fullobjects))
    else:
        return(list(fullobjects))

def removeattributes(thisobject,toremovenewlines = False):
    global flagremovedattributes
    if flagremovedattributes:
        return(thisobject) #attributes have already been removed!
##    lines = getlines(thisobject,False,False)
##    newlines = []
##    for thisline in lines:    
##            newline = removewhitespace(thisline,True,False,False)
##            if ((letter(1,newline) == _attributestart) and (contains(_attributeend,newline))):
##                if contains(_attributeend + " ",newline):
##                    newline = readafter(newline,_attributeend + " ")
##                else:
##                    newline = readafter(newline,_attributeend)
##                if not(newline == ""): #and not((checkforstringat(" " + _isoffsetstring,newline,1)) or (checkforstringat(_isoffsetstring,newline,1)))): # rva is only after we remove compiler generated etc., so it is useless
##                    if((checkforstringat(" " + _isoffsetstring,newline,1)) or (checkforstringat(_isoffsetstring,newline,1))):
##                        newlines.append("\n")
##                newlines.append(newline)
##            else:
##                newline = thisline
##                if not(toremovenewlines and (newline == "")):
##                    if (contains("// RVA: -1 Offset: -1",newline)):
##                        if (len(newlines) == 0):
##                            newlines.append(newline)
##                        else:
##                            if not((checkforstringat(" " + _isoffsetstring,newlines[len(newlines) - 1],1)) or (checkforstringat(_isoffsetstring,newlines[len(newlines) - 1],1))):
##                                newlines.append(newline)
##                            #else:
##                                #newlines[len(newlines) - 1] = newline
##                    else:
##                        if (len(newlines) == 0):
##                            newlines.append(newline)
##                        else:
##                            if not((checkforstringat(" " + _isoffsetstring,newlines[len(newlines) - 1],1)) or (checkforstringat(_isoffsetstring,newlines[len(newlines) - 1],1))):
##                                newlines.append(newline)
##                            else:
##                                newlines[len(newlines) - 1] = newline
    lines = getlines(thisobject,False,False)
    newlines = []
    for thisline in lines:    
            newline = removewhitespace(thisline,True,False,False)
            if ((letter(1,newline) == _attributestart) and (contains(_attributeend,newline))):
                if contains(_attributeend + " ",newline):
                    newline = readafter(newline,_attributeend + " ")
                else:
                    newline = readafter(newline,_attributeend)
                if (not(newline == "") and not((checkforstringat(" " + _isoffsetstring,newline,1)) or (checkforstringat(_isoffsetstring,newline,1)))): # rva is only after we remove compiler generated etc., so it is useless
                     newlines = listadd(newline,newlines)
            else:
                newline = thisline
                if not(toremovenewlines and (newline == "")):
                    newlines = listadd(newline,newlines)
    return(linestostring(newlines))

def getuserdefinedtype(thisobject):
    thisobject = removeattributes(thisobject)
    global isshared
    isshared = False
    userdefinedtypeofobject = "Other" #in case there are no lines or no words in line 2. not found - unknown structure, so unknown object
    lines = getlines(thisobject,False,False)
    words = getwords(item(_objecttypeline,lines))  #1st line is namespace, 2nd line describes object (abstract class, public enum, etc.)
    onword = 0
    for thisword in words:
        onword = onword + 1
        if onword > len(words): #not found - unknown structure, so unknown object. This should not happen!
            userdefinedtypeofobject = "Other"
            break
        if len(_userdefinedtypes) > 0:
            if thisword in _userdefinedtypes:
                userdefinedtypeofobject = thisword
                #isshared = (contains(".<",(item(2,lines))) or contains(" :",(item(2,lines))) or contains(">.",(item(2,lines)))) #in dump cs, a shared class has '(nameofclass).,' and ' :'.
                isshared = False
                for i in _sharedobjectstrings:
                    if contains(i,item(_objecttypeline,lines)):
                        isshared = True
                        break
                break
    userdefinedtypeofobject = userdefinedtypeofobject.strip()
    return(userdefinedtypeofobject)

def getisshared(thisobject):
    thisobject = removeattributes(thisobject)
    global isshared
    isshared = False
    lines = getlines(thisobject,False,False)
    words = getwords(item(_objecttypeline,lines))  #1st line is namespace, 2nd line describes object (abstract class, public enum, etc.)
    onword = 0
    for thisword in words:
        onword = onword + 1
        if onword > len(words): #not found - unknown structure, so unknown object. This should not happen!
            isshared = False
            break
        if len(_userdefinedtypes) > 0:
            if thisword in _userdefinedtypes:
                #isshared = (contains(".<",(item(2,lines))) or contains(" :",(item(2,lines))) or contains(">.",(item(2,lines)))) #in dump cs, a shared class has '(nameofclass).,' and ' :'.
                isshared = False
                for i in _sharedobjectstrings:
                    if contains(i,item(_objecttypeline,lines)):
                        isshared = True
                        break #break for optimization - we don't want to go through the whole list if it isn't necessary
            #we check for both of these because they might only have one or the other. there may be false positives, idk. I hope not!
                break
    return(isshared)

isshared = getisshared #same thing, but different name
getshared = getisshared #same thing, but different name

def getobjecttype(thisobject):
    thisobject = removeattributes(thisobject)
    typeofobject = ""
    lines = getlines(thisobject,False,False)
    words = getwords(item(_objecttypeline,lines)) #1st line is namespace, 2nd line describes object (abstract class, public enum, etc.)
    onword = 0
    for thisword in words:
        onword = onword + 1
        if onword > len(words): #not found - unknown structure, so unknown object. This should not happen! We assume type is correct anyway.
            break
        if thisword in _userdefinedtypes: #say we want public from public enum, or internal static from internal static class. we 
            break
        typeofobject = join(typeofobject,thisword," ")
    if lastletter(typeofobject) == "": #we should have gotten a space at the end, since each time, we add the word and " ". We don't want the last space.
        typeofobject = readbefore(typeofobject," ")
    typeofobject = typeofobject.strip()
    return typeofobject
    
def getobjectnamespace(thisobject):
    lines = getlines(thisobject)
    thisline = item(_namespaceline,lines)
    namespacename = readafter(thisline,_namespacenamestart)
    namespacename = namespacename.strip()
    if namespacename == "":
            namespacename = _nonamespacename
    return(namespacename)

def getobjectname(thisobject):
    thisobject = removeattributes(thisobject)
    lines = getlines(thisobject)
    thisline = item(_objecttypeline,lines) #2nd line is about class, like public static class
    objectname = readbetween(thisline,join(getobjecttype(thisobject)," ",getuserdefinedtype(thisobject)," "),_objecttypeend)
    if (not(_objectkeepaftercolon) and contains(_objectcolon,objectname)):
        objectname = readbefore(objectname,_objectcolon)
        objectname = substring(objectname,1,len(objectname) - len(_objectcolon)) #readbefore function still keeps up to the end of objectcolon, so remove that
    objectname = objectname.strip()
    return(objectname)
    
def getmethod(methodname,methodslist,casesensitive = False):
    i = 0
    for thismethod in methodslist:
        i = i + 1
        if match(getmethodname(thismethod),str(methodname),casesensitive):
            thismethod = {
                  "Name" : getmethodname(thismethod),
                  "Type" : getmethodtype(thismethod),
                  "Content" : thismethod,
                  "Offset" : getmethodoffset(thismethod),
                  "Params" : getmethodparams(thismethod),
                  "Param Types" : getmethodparamtypes(thismethod),
                  }
            return(thismethod)
    dumpcsnotfounderror(methodname)
    sys.exit()
    return(None)

def getfield(fieldname,fieldslist,casesensitive = False):
    i = 0
    for thisfield in fieldslist:
        i = i + 1
        if match(getfieldname(thisfield),str(fieldname),casesensitive):
            thisfield = {
                  "Name" : getfieldname(thisfield),
                  "Type" : getfieldtype(thisfield),
                  "Content" : thisfield,
                  "Offset" : getfieldoffset(thisfield),
                  }
            return(thisfield)
    dumpcsnotfounderror(fieldname)
    sys.exit()
    return(None)

def getproperty(propertyname,propertieslist,casesensitive = False):
    i = 0
    for thisproperty in propertieslist:
        i = i + 1
        if match(getpropertyname(thisproperty),str(propertyname),casesensitive):
            thisproperty = {
                  "Name" : getpropertyname(thisproperty),
                  "Type" : getpropertytype(thisproperty),
                  "Content" : thisproperty,
                  "Propeties" : getpropertyattributes(thisproperty),
                  }
            return(thisproperty)
    dumpcsnotfounderror(propertyname)
    sys.exit()
    return(None)

def getfullmethodparams(thismethod):
    lines = getlines(thismethod)
    thisline = lines[_methodtypeline - 1]
    fullmethodparams = readbetween(thisline,_methodparamsstart,_methodparamsend)
    return(fullmethodparams)

def getmethodparams(thismethod):
    fullmethodparams = getfullmethodparams(thismethod)
    methodparams = []
    thisparam = ""
    ingroup = False
    for thisletter in str(fullmethodparams):
        if ((thisletter == _datatypegroupstart) and not(ingroup)):
           ingroup = True
        if ((thisletter == _datatypegroupend) and ingroup):
           ingroup = False
        if (not(ingroup) and (thisletter == ",")):
            if (thisparam != ""):
                methodparams.append(thisparam.strip())
                thisparam = ""
        else:
            thisparam = (thisparam + thisletter)
    if (thisparam != ""):
                methodparams.append(thisparam.strip())
                thisparam = ""
    return(methodparams)

def getmethodparamtypes(thismethod,replacenames = True):
    #methodparams = getwords(getfullmethodparams(thismethod))
    methodparams = getmethodparams(thismethod)
    newparams = []
    for thisparam in methodparams:
        for thisword in getwords(thisparam):
            newparams.append(thisword)
    methodparams = newparams
    if replacenames:
        methodparams = replacetypenames(methodparams)
    return(methodparams)

def replacetypenames(thistype):
    if _processdatatypegroups:
        #Convert to string
        if type(thistype) == list:
            thistype = wordstostring(thistype)
        #Replace data type groups
        newtypes = ""
        for thisletter in thistype:
                if (thisletter == _datatypegroupstart) or (thisletter == _datatypegroupend) or (thisletter == _datatypegroupseparator) :
                	newtypes = newtypes + " "
                else:
                	newtypes = newtypes  + thisletter
        #Convert to list of words
        words = getwords(newtypes)
    else:
        #Convert to list of words
        if type(thistype) == str:
            words = getwords(thistype)
        else:
            words = thistype
    #Replace names
    newwords = []
    for thisword in words:
        if not(thisword in _types):
            newwords.append(_typenamereplace)
        else:
            newwords.append(thisword)
    if type(thistype) == str:
        newtype = wordstostring(newwords)
    else:
        newtype = newwords
    return(newtype)

def getmethodtype(thismethod,replacenames = True):
    lines = getlines(thismethod)
    thisline = lines[_methodtypeline - 1]
    thisline = substring(thisline,0,findstr(_methodparamsstart,thisline))
    methodtype = readbefore(thisline,_methodparamsstart)
    methodtype = methodtype.strip()
    words = getwords(methodtype)
    if len(words) > 0:
        del words[len(words) - 1]
    methodtype = wordstostring(words)
    if replacenames:
        methodtype = replacetypenames(methodtype)
    return(methodtype)
    
def getmethodname(thismethod):
    lines = getlines(thismethod)
    thisline = lines[_methodtypeline - 1]
    thisline = substring(thisline,0,findstr(_methodparamsstart,thisline))
    methodname = readbefore(thisline,_methodparamsstart)
    methodname = methodname.strip()
    words = getwords(methodname)
    methodname = words[len(words) - 1]
    return(methodname)

def getmethodoffset(thismethod):
    lines = getlines(thismethod)
    thisline = lines[_methodoffsetline - 1]
    methodoffset = readbetween(thisline,_offsetprefix,_offsetsuffix)
    return(methodoffset)

def removegenericinstmethods(fullmethods):
    lines = getlines(fullmethods,True,True)
    newlines = []
    ingenericinst = False
    for thisline in lines:
        if thisline == _genericinstmethodstart:
            ingenericinst = True
        else:
            if (thisline == _genericinstmethodend) and ingenericinst:
                ingenericinst = False
            else:
                if not(ingenericinst):
                    newlines.append(thisline)
    return(newlines)
    
def getmethodslist(fullmethods):
    lines = removegenericinstmethods(fullmethods)
    methodslist = []
    if (isodd(len(lines))):
        unexpecteddumpcsformaterror("Methods section missing line or has extra line (only expected sets of 2 lines per method ie:\n         // RVA: 0x1321F3C Offset: 0x1321F3C VA: 0x1321F3C\npublic static float get_deltaTime() { }",fullmethods)
    for i in range(int(len(lines) // 2)):
        methodslist.append(concat([lines[int((((i + 1) * 2)) - 1) - 1],lines[int((((i + 1) * 2))) - 1]],"\n"))
    return(methodslist)

def getmethods(methodslist):
    if type(methodslist) == str: #got full methods, not methods list - so convert to methods list
        methodslist = getmethodslist(methodslist)
    global methods
    methods = []
    for thismethod in methodslist:
        thismethoddata = {
                  "Name" : getmethodname(thismethod),
                  "Type" : getmethodtype(thismethod),
                  "Content" : thismethod,
                  "Offset" : getmethodoffset(thismethod),
                  "Params" : getmethodparams(thismethod),
                  "ParamTypes" : getmethodparamtypes(thismethod),
                  }
        methods.append(thismethoddata)
    return(methods)


def getfullmethods(thisobject):
    global fullmethods
    thisobject = removeattributes(thisobject)
    lines = getlines(thisobject,True,True)
    if len(lines) > 0:
        if (_methodsstart in lines):
            fullmethods = ""
            i = lines.index(_methodsstart) + 1
            start = i
            thisitem = removewhitespace(lines[i])
            fullmethods = concat([fullmethods,thisitem],"\n")
            i = i + 1
            thisitem = removewhitespace(lines[i])
            i = i + 1
            while not((thisitem in _contentends) or i > (len(lines) - 1)):
                i = i + 1
                if not(iswhitespace(thisitem)):
                    fullmethods = concat([fullmethods,thisitem],"\n")
                thisitem = removewhitespace(lines[i - 1])
        else:
            fullmethods = ""
    return(fullmethods)

def methodsmatch(method1,method2,checkparams = True):
    type1 = method1["Type"]
    type2 = method2["Type"]
    typesmatch = (type1 == type2)
    if checkparams:
        params1 = method1["ParamTypes"]
        params2 = method2["ParamTypes"]
        paramsmatch = (param1 == param2)
    else:
        paramsmatch = True
    return(typesmatch and paramsmatch) #is percentage score not less than tolerated percent?
    
checkmethods = methodsmatch #same thing, but different name
comparemethods = methodsmatch #same thing, but different name

def getobject(objectnames,fullobjects,casesensitive = False):
    if type(objectnames) == str: #convert to list
        objectnames = [objectnames]
    objectsfound = []
    i = 0
    for thisfullobject in fullobjects:
        i = i + 1
        if multipleof(i,1000):
            print(str(i) + "/" + str(len(fullobjects)))
        if listcontains(getobjectname(thisfullobject),objectnames,casesensitive):
            thisobject = {
                  "Name" : getobjectname(thisfullobject),
                  "Namespace" : getobjectnamespace(thisfullobject),
                  "UserDefinedType" : getuserdefinedtype(thisfullobject),
                  "Shared" : getisshared(thisfullobject),
                  "Type" : getobjecttype(thisfullobject),
                  "Content" : thisfullobject,
                  "Fields" : getfullfields(thisfullobject),
                  "Properties" : getfullproperties(thisfullobject),
                  "Methods" : getfullproperties(thisfullobject),
                  "TypeModel" : buildtypemodel(thisfullobject),
                  }
            objectsfound.append(thisobject)
    if len(objectsfound) < len(objectnames):
        dumpcsnotfounderror(objectname)
        sys.exit()
    return(objectsfound)

def getfieldoffset(thisfield):
    fieldoffset = readafter(thisfield,_fieldoffsetstart)
    return(fieldoffset)

def getfieldtype(thisfield,replacenames = True):
    thisfield = substring(thisfield,0,findstr(_fieldoffsetstart,thisfield))
    fieldtype = readbefore(thisfield,_fieldoffsetstart)
    fieldtype = fieldtype.strip()
    words = getwords(fieldtype)
    if len(words) > 0:
        del words[len(words) - 1]
    fieldtype = wordstostring(words)
    if replacenames:
        fieldtype = replacetypenames(fieldtype)
    return(fieldtype)
    
def getfieldname(thisfield):
    thisfield = substring(thisfield,0,findstr(_fieldoffsetstart,thisfield))
    fieldname = readbefore(thisfield,_fieldoffsetstart)
    fieldname = fieldname.strip()
    words = getwords(fieldname)
    fieldname = words[len(words) - 1]
    return(fieldname)

def getfieldslist(fullfields):
    lines = getlines(fullfields,True,True)
    global fields
    fields = []
    for thisline in lines:
        if (contains(_fieldoffsetstart,thisline)):
            fields.append(thisline)
    return(fields)

def getfields(fieldslist):
    if type(fieldslist) == str: #got full fields, not fields list - so convert to fields list
        fieldslist = getfieldslist(fieldslist)
    global fields
    fields = []
    for thisfield in fieldslist:
        thisfielddata = {
                  "Name" : getfieldname(thisfield),
                  "Type" : getfieldtype(thisfield),
                  "Content" : thisfield,
                  "Offset" : getfieldoffset(thisfield),
                  }
        fields.append(thisfielddata)
    return(fields)

def buildtypemodel(thisobject):
    #To do: method params, number of shared classes for class
    objecttype = getobjecttype(thisobject)
    userdefinedtype = getuserdefinedtype(thisobject)
    isshared = getisshared(thisobject)
    fields = getfieldslist(getfullfields(thisobject))
    properties = getpropertieslist(getfullproperties(thisobject))
    methods = getmethodslist(getfullmethods(thisobject))
    fieldtypes = []
    for thisfield in fields:
        fieldtypes.append(getfieldtype(thisfield,True))
    propertytypes = []
    for thisproperty in properties:
        thispropertymodel = {
                            "Type": getpropertytype(thisproperty,True),
                            "Attributes": getpropertyattributes(thisproperty),
                            }
        propertytypes.append(thispropertymodel)
    justpropertytypes = []
    for thisproperty in properties:
        justpropertytypes.append(getpropertytype(thisproperty,True))
    methodtypes = []
    for thismethod in methods:
        thismethodmodel = {
                            "Type": getmethodtype(thismethod,True),
                            "ParamTypes": getmethodparamtypes(thismethod,True),
                            }
        methodtypes.append(thismethodmodel)
    justmethodtypes = []
    for thismethod in methods:
        justmethodtypes.append(getmethodtype(thismethod,True))
    typemodel = {
                  "UserDefinedType": userdefinedtype,
                  "Type": objecttype,
                  "Shared": isshared,
                  "Fields": fieldtypes,
                  "Properties": propertytypes,
                  "PropertyTypes": justpropertytypes,
                  "Methods": methodtypes,
                  "MethodTypes": justmethodtypes,
                  }
    return(typemodel)
    
gettypemodel = buildtypemodel #same thing, but different name
maketypemodel = buildtypemodel #same thing, but different name

def getfullfields(thisobject):
    global fullfields
    thisobject = removeattributes(thisobject)
    lines = getlines(thisobject,True,True)
    if len(lines) > 0:
        if (_fieldsstart in lines):
            fullfields = ""
            i = lines.index(_fieldsstart) + 1
            start = i
            thisitem = removewhitespace(lines[i])
            fullfields = concat([fullfields,thisitem],"\n")
            i = i + 1
            thisitem = removewhitespace(lines[i])
            i = i + 1
            while not((thisitem in _contentends) or i > (len(lines) - 1)):
                i = i + 1
                if not(iswhitespace(thisitem)):
                    fullfields = concat([fullfields,thisitem],"\n")
                thisitem = removewhitespace(lines[i - 1])
        else:
            fullfields = ""
    return(fullfields)

def getfullproperties(thisobject):
    global fullproperties
    thisobject = removeattributes(thisobject)
    lines = getlines(thisobject,True,True)
    if len(lines) > 0:
        if (_propertiesstart in lines):
            fullproperties = ""
            i = lines.index(_propertiesstart) + 1
            start = i
            thisitem = removewhitespace(lines[i])
            fullproperties = concat([fullproperties,thisitem],"\n")
            i = i + 1
            thisitem = removewhitespace(lines[i])
            i = i + 1
            while not((thisitem in _contentends) or i > (len(lines) - 1)):
                i = i + 1
                if not(iswhitespace(thisitem)):
                    fullproperties = concat([fullproperties,thisitem],"\n")
                thisitem = removewhitespace(lines[i - 1])
        else:
            fullproperties = ""
    return(fullproperties)

def getpropertytype(thisproperty,replacenames = True):
    thisproperty = substring(thisproperty,0,findstr(_propertyattributesstart,thisproperty))
    propertytype = readbefore(thisproperty,_propertyattributesstart)
    propertytype = propertytype.strip()
    words = getwords(propertytype)
    if len(words) > 0:
        del words[len(words) - 1]
    propertytype = wordstostring(words)
    if replacenames:
        propertytype = replacetypenames(propertytype)
    return(propertytype)

def getfullpropertyattributes(thisproperty):
    fullproperties = readbetween(thisproperty,_propertyattributesstart,_propertyattributesend)
    fullproperties = fullproperties.strip()
    words = getwords(fullproperties)
    fullproperties = wordstostring(words)
    return(fullproperties)

def getpropertyattributes(thisproperty):
    fullproperties = getfullpropertyattributes(thisproperty)
    properties = fullproperties.split(_propertyattributeseparator)
    return(properties)
    
def getpropertyname(thisproperty):
    thisproperty = substring(thisproperty,0,findstr(_propertyattributesstart,thisproperty))
    propertyname = readbefore(thisproperty,_propertyattributesstart)
    propertyname = propertyname.strip()
    words = getwords(propertyname)
    propertyname = words[len(words) - 1]
    return(propertyname)

def getpropertieslist(fullproperties):
    global properties
    lines = getlines(fullproperties,True,True)
    properties = []
    for thisline in lines:
        if (contains(_propertyattributesstart,thisline)):
            properties.append(thisline)
    return(properties)

def getproperties(propertieslist):
    if type(propertieslist) == str: #got full properties, not properties list - so convert to properties list
        propertieslist = getpropertieslist(propertieslist)
    global properties
    properties = []
    for thisproperty in propertieslist:
        thispropertydata = {
                  "Name" : getpropertyname(thisproperty),
                  "Type" : getpropertytype(thisproperty),
                  "Content" : thisproperty,
                  "Properties" : getpropertyattributes(thisproperty),
		  "FullProperties" : getfullpropertyattributes(thisproperty),
                  }
        properties.append(thispropertydata)
    return(properties)

def getfullclasses(objects):
    global fullclasses
    fullclasses = []
    i = 0
    for thisobject in objects:
        i = i + 1
        if multipleof(i,1000):
            print(str(i) + "/" + str(len(fullobjects)))
        if getuserdefinedtype(thisobject) == "class":
            fullclasses.append(thisobject)
    return(fullclasses)

def getfullstructs(objects):
    global fullstructs
    fullstructs = []
    for thisobject in objects:
        if getuserdefinedtype(thisobject) == "struct":
            fullstructs.append(thisobject)
    return(fullstructs)

def getfullenums(objects):
    global fullenums
    fullenums = []
    for thisobject in objects:
        if getuserdefinedtype(thisobject) == "enum":
            fullenums.append(thisobject)
    return(fullenums)

def getfullinterfaces(objects):
    global fullinterfaces
    fullinterfaces = []
    for thisobject in objects:
        if getuserdefinedtype(thisobject) == "interface":
            fullinterfacse.append(thisobject)
    return(fullinterfaces)

def getobjects(fullobjects,getshared = True,namespacefilter = None,justnameandtypemodel = False,returntuple = True):
    if type(namespacefilter) == str:
        namespacefilter = [namespacefilter] #convert to list
    if namespacefilter == [] or namespacefilter is False:
        namespacefilter = None
    global flagremovedshared
    #if localfullobjects is None:
        #global fullobjects
        #if not(variableexists("fullobjects"):
            #global dumpcs
            #if if not(variableexists("dumpcs")::
                #objectnotdeclarederror("fullobjects")
        #else:
            #getfullobjects(dumpcs,True)
            #localfullobjects = fullobjects
    global objects
    objects = []
    i = 0
    for thisfullobject in fullobjects:
        i = i + 1
        if multipleof(i,100):
            print(str(i) + "/" + str(len(fullobjects)))
        valid = True
        if not(flagremovedshared) and valid:
            if not(getshared):
                if getisshared(thisfullobject):
                    valid = False
        if (namespacefilter != None) and valid:
            if not(getobjectnamespace(thisfullobject) in namespacefilter):
                valid = False
        if valid:
            if justnameandtypemodel:
                thisobject = {
                  "Name" : getobjectname(thisfullobject),
                  "TypeModel" : buildtypemodel(thisfullobject),
                  }
            else:
                thisobject = {
                  "Name" : getobjectname(thisfullobject),
                  "Namespace" : getobjectnamespace(thisfullobject),
                  "UserDefinedType" : getuserdefinedtype(thisfullobject),
                  "Shared" : getisshared(thisfullobject),
                  "Type" : getobjecttype(thisfullobject),
                  "Content" : thisfullobject,
                  "Fields" : getfullfields(thisfullobject),
                  "Properties" : getfullproperties(thisfullobject),
                  "Methods" : getfullmethods(thisfullobject),
                  "TypeModel" : buildtypemodel(thisfullobject),
                  }
            objects.append(thisobject)
    if not(getshared):
        flagremovedshared = True
    if returntuple:
        return(tuple(objects))
    else:
        return(objects)

findobject = getobject #same thing, but different name

def typemodelsmatch(model1,model2,usetolerance = None,dosize = True,domethodparams = True,dopropertyattributes = True,donamespace = True): #make sure model1 is the unobfuscated one!
    if usetolerance is None:
        global _tolerance
        usetolerance = _tolerance
    #To do: method params, number of shared classes for class
    maxscore = _userdefinedtypeweighttrue + _objecttypeweighttrue + _sharedweighttrue + (len(model1.get("Fields")) * _fieldweighttrue) +  (len(model1.get("Methods")) * _methodweighttrue) +  (len(model1.get("Properties")) * _propertyweighttrue) #calculate maximum score
    score = float(0)
    #Size
    if dosize:
        maxscore = maxscore + 8 #start off at 8, and subtract nothing for a perfect score
        #Size follows a different structure than most other methods
        size1 = (len(model1.get("Fields")) +  len(model1.get("Methods"))  + len(model1.get("Properties"))) #how many methods, fields, and propeties are there?
        size2 = (len(model2.get("Fields")) +  len(model2.get("Methods"))  + len(model2.get("Properties"))) #how many methods, fields, and propeties are there?
        score = 8 - (((abs(size2 - size1) / _sizebenchmark) * _sizeweightfalse)) #depending on the difference in size, this could have a small impact, or be very bad
    #userdefinedType
    if model1.get("UserDefinedType") == model2.get("UserDefinedType"):
        score = score + _userdefinedtypeweighttrue
    else:
        return(False) #userdefined type MUST match
    #IsShared
    if model1.get("Shared") == model2.get("Shared"):
        score = score + _sharedweighttrue
    else:
        return(False) #Is shared MUST match
    #Type
    if model1.get("Type") == model2.get("Type"):
        score = score + _objecttypeweighttrue
    #Namespace
    if donamespace:
        maxscore = maxscore + _namespaceweighttrue
        if model1.get("Namespace") == model2.get("Namespace"):
            score = score + _objecttypeweighttrue
    #Fields
    fields1 = list(model1.get("Fields"))
    fields2 = list(model2.get("Fields"))
    templist = list(fields2) #it's very normal to add on things, but not as common to delete them. So, most of the fields in the unobfuscated (earlier) one
    #should also exist in the obfuscated one (newer)
    templist2 = list(fields1)
    for item in templist2:
        if len(templist) > 0:
            if (item in templist):
                score = score + _fieldweighttrue
                templist.remove(item)
    #Methods
    if domethodparams:
        methods1 = list(model1.get("Methods"))
        methods2 = list(model2.get("Methods"))
    else:
        methods1 = list(model1.get("MethodTypes"))
        methods2 = list(model2.get("MethodTypes"))
    templist = list(methods2) #it's very normal to add on things, but not as common to delete them. So, most of the methods in the unobfuscated (earlier) one
    #should also exist in the obfuscated one (newer)
    templist2 = list(methods1)
    for item in templist2:
            if len(templist) > 0:
                if (item in templist):
                    score = score + _methodweighttrue
                    templist.remove(item)
   #Properties
    if dopropertyattributes:
        properties1 = list(model1.get("Properties"))
        properties2 = list(model2.get("Properties"))
    else:
        properties1 = list(model1.get("PropertyTypes"))
        properties2 = list(model2.get("PropertyTypes"))
    templist = list(properties2) #it's very normal to add on things, but not as common to delete them. So, most of the properties in the unobfuscated (earlier) one
    #should also exist in the obfuscated one (newer)
    templist2 = list(properties1)
    for item in templist2:
            if len(templist) > 0:
                if (item in templist):
                    score = score + _propertyweighttrue
                    templist.remove(item)
    #To do: method params, number of shared classes for class
    matchscore = ((score / maxscore) * 100)
    endspeedtest()
    return(not(((score / maxscore) * 100) < usetolerance)) #is percentage score not less than tolerated percent?
    
comparetypemodels = typemodelsmatch  #same thing, but different name
checktypemodels = typemodelsmatch #same thing, but different name

def objectscheckformatch(object1,object2,usetolerance = None,dosize = True,domethodparams = True,dopropertyattributes = True,donamespace = True): #make sure object1 is the unobfuscated one!
    global _trustnames
    if _trustnames:
        if str(object1.get("Name")) == str(object2.get("Name")):
            return(True)
        else:
            return(typemodelsmatch(object1.get("TypeModel"),object2.get("TypeModel"),usetolerance,dosize,domethodparams,dopropertyattributes,donamespace))
    else:
        return(typemodelsmatch(object1.get("TypeModel"),object2.get("TypeModel"),usetolerance,dosize,domethodparams,dopropertyattributes,donamespace))

checkobjects = objectscheckformatch #same thing, but different name
compareobjects = objectscheckformatch #same thing, but different name
objectsmatch = objectscheckformatch #same thing, but different name

    
def bruteforcedeobfuscateobject(thisunobfuscated):
    global _tolerance
    global objectmatches
    global obfuscated
    lasttolerance = [999999999,9999999998,9999999997,9999999996]
    newtolerance = _tolerance
    while True:
            if ((lasttolerance[len(lasttolerance) - 1] == lasttolerance[len(lasttolerance) - 3]) and (lasttolerance[len(lasttolerance) - 2] == lasttolerance[len(lasttolerance) - 4])): #stuck in loop, trying to get to exactly 1 but can't
                break
            lasttolerance.append(newtolerance)
            objectmatches = []
            for thisobfuscated in obfuscated:
                if objectscheckformatch(thisunobfuscated,thisobfuscated,newtolerance):
                    objectmatches.append(thisobfuscated) #match!
            if len(objectmatches) > 1:
                newtolerance = newtolerance + 5
            elif len(objectmatches) == 0:
                newtolerance = newtolerance - 5
            else:
                break
    matchnames = []
    matchestemp = []
    for thismatch in objectmatches:
        matchnames.append(str(thismatch.get("Name")))
        matchestemp.append(thismatch)
    return(matchnames)

#       Mod Menu Installation

class ModMenuInstall():
    def androidmanifest(apk):
        if getfileextension(apk) == "apk":
            apknotdecompilederror(apk)
            return None
        content = getandroidmanifestfromapk(apk,"read")
        if content is None:
            return None
        else:
            return(content)
        

#       Demos / Tests

def comparativedeobfuscationdemo(classestofind):
    obfuscateddumpcs = r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.5.3/PG3D 22.5.3 dump.cs"
    #obfuscateddumpcs = r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.5.0/PG3D 22.5.0 dump.cs"
    unobfuscateddumpcs = r"C:\Users\zachy\OneDrive\Documents\Work\Projects\Pixel Gun 3D\Pixel Gun 3D 16.6.1\Pixel Gun 3D 16.6.1 Dump.txt"
    global _tolerance
    dumpcspath = unobfuscateddumpcs
    loaddumpcs(dumpcspath)
    startspeedtest()
    getfullobjects(dumpcs,True)
    endspeedtest()
    print("All classes/structs/interfaces/enums extracted from dump.cs in " + timetaken + " miliseconds.")
    startspeedtest()
    getfullclasses(fullobjects)
    endspeedtest()
    print("All classes extracted from dump.cs in " + timetaken + " miliseconds.")
    startspeedtest()
    unobfuscated = getobject(classestofind,fullclasses)
    endspeedtest()
    print("Unobfuscated " + str(classestofind) + " found in " + timetaken + " miliseconds.")
    resetflags()
    #dumpcspath = (r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.5.0/PG3D 22.5.0 dump.cs")
    dumpcspath = obfuscateddumpcs
    loaddumpcs(dumpcspath)
    startspeedtest()
    getfullobjects(dumpcs,True)
    endspeedtest()
    print("All classes/structs/interfaces/enums extracted from obfuscated dump.cs in " + timetaken + " miliseconds.")
    startspeedtest()
    getfullclasses(fullobjects)
    endspeedtest()
    print("All classes extracted from obfuscated dump.cs in " + timetaken + " miliseconds.")
    startspeedtest()
    obfuscated = getobjects(fullclasses,True)
    endspeedtest()
    print("All type models extracted from obfuscated dump.cs in " + timetaken + " miliseconds.")
    #while True:
        #print("Trying to deobfuscate with tolerance: " + str(_tolerance))
        #startspeedtest()
        #bruteforcedeobfuscateobject(unobfuscatedclass,objects)
        #endspeedtest()
        #print("Obfuscated " + classtofind + " found in " + timetaken + " miliseconds.")
        #print(str(len(objectmatches)) + " Matches Found:\n\n")
        #for thisobject in objectmatches:
            #print(thisobject.get("Name") + ":")
            #print(thisobject)
        #if len(objectmatches) > 1:
            #_tolerance = _tolerance + 5
        #elif len(objectmatches) == 0:
            #_tolerance = _tolerance - 5
        #else:
            #sys.exit()
##     global _tolerance
##     _tolerance = 80
##        while True:
##            if ((lasttolerance[len(lasttolerance) - 1] == lasttolerance[len(lasttolerance) - 3]) and (lasttolerance[len(lasttolerance) - 2] == lasttolerance[len(lasttolerance) - 4])): #stuck in loop, trying to get to exactly 1 but can't
##                break
##            lasttolerance.append(_tolerance)
##            objectmatches = []
##            for thisobfuscated in obfuscated:
##                if objectscheckformatch(thisunobfuscated,thisobfuscated):
##                    objectmatches.append(thisobfuscated)) #match!
##            if len(objectmatches) > 1:
##                _tolerance = _tolerance + 5
##            elif len(objectmatches) == 0:
##                _tolerance = _tolerance - 5
##            else:
##                break
##        unobfuscatednames.append(str(thisunobfuscated.get("Name")))
##        matchnames = []
##        for thismatch in objectmatches:
##            matchnames.append(str(thismatch.get("Name")))
##        obfuscatednames.append(matchnames)
##    endspeedtest()
    startspeedtest()
    global unobfuscatednames
    unobfuscatednames = []
    global obfuscatednames
    obfuscatednames = []
    oldtolerance = _tolerance
    i = 0
    for thisunobfuscated in unobfuscated:
        i = i + 1
        if multipleof(i,20):
             print(str(i) + "/" + str(len(unobfuscated)))
        lasttolerance = [999999999,9999999998,9999999997,9999999996]
        _tolerance = oldtolerance
        while True:
            if ((lasttolerance[len(lasttolerance) - 1] == lasttolerance[len(lasttolerance) - 3]) and (lasttolerance[len(lasttolerance) - 2] == lasttolerance[len(lasttolerance) - 4])): #stuck in loop, trying to get to exactly 1 but can't
                break
            lasttolerance.append(_tolerance)
            objectmatches = []
            for thisobfuscated in obfuscated:
                if objectscheckformatch(thisunobfuscated,thisobfuscated):
                    objectmatches.append(thisobfuscated) #match!
            if len(objectmatches) > 1:
                _tolerance = _tolerance + 5
            elif len(objectmatches) == 0:
                _tolerance = _tolerance - 5
            else:
                break
            if ((_tolerance < 0) or (_tolerance > 100)):
                break
        unobfuscatednames.append(str(thisunobfuscated.get("Name")))
        matchnames = []
        matchestemp = []
        for thismatch in objectmatches:
            matchnames.append(str(thismatch.get("Name")))
            matchestemp.append(thismatch)
        obfuscatednames.append(matchnames)
    _tolerance = oldtolerance
    endspeedtest()
    print("Class(es) deobfuscated in " + timetaken + " miliseconds.")
    global results
    results = {}
    for i in range(len(unobfuscatednames)):
        results[str(unobfuscatednames[i])] = list(obfuscatednames[i])
    global output
    output = ""
    for i in range(len(unobfuscatednames)):
        output = output + str(unobfuscatednames[i]) + " = " + str(obfuscatednames[i]) + "\n"
    return(output)


def deobfuscateallclassesdemo():
   global _tolerance
   unobfuscateddumpcs = r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 16.6.1/Pixel Gun 3D 16.6.1 Dump.txt"
   obfuscateddumpcs = r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.5.3/PG3D 22.5.3 dump.cs"
   #unobfuscateddumpcs = prompt("\nEnter the path to your UNOBFUSCATED dump.cs file (without quotes):")
   #obfuscateddumpcs = prompt("Enter the path to your OBFUSCATED dump.cs file (without quotes):")
   dumpcspath = unobfuscateddumpcs
   loaddumpcs(dumpcspath)
   startspeedtest()
   getfullobjects(dumpcs,False)
   endspeedtest()
   print("All classes/structs/interfaces/enums extracted from dump.cs in " + timetaken + " miliseconds.")
   startspeedtest()
   getfullclasses(fullobjects)
   endspeedtest()
   print("All classes extracted from dump.cs in " + timetaken + " miliseconds.")
   startspeedtest()
   unobfuscated = getobjects(fullclasses,False)
   endspeedtest()
   print("All type models extracted from dump.cs in " + timetaken + " miliseconds.")
   write_file(r"C:\Users\zachy\OneDrive\Documents\Work\Temp Folders\Python Temps\unobfuscatedobjects.txt",str(unobfuscated))
   global flagremovedshared
   flagremovedshared = False
   global flagremovedattributes
   flagremovedattributes = False
   global flagremovedblanklines
   flagremovedblanklines = False
   dumpcspath = obfuscateddumpcs
   loaddumpcs(dumpcspath)
   startspeedtest()
   getfullobjects(dumpcs,False)
   endspeedtest()
   print("All classes/structs/interfaces/enums extracted from obfuscated dump.cs in " + timetaken + " miliseconds.")
   startspeedtest()
   getfullclasses(fullobjects)
   endspeedtest()
   print("All classes extracted from obfuscated dump.cs in " + timetaken + " miliseconds.")
   startspeedtest()
   obfuscated = getobjects(fullclasses,False)
   endspeedtest()
   print("All type models extracted from obfuscated dump.cs in " + timetaken + " miliseconds.")
   write_file(r"C:\Users\zachy\OneDrive\Documents\Work\Temp Folders\Python Temps\obfuscatedobjects.txt",str(obfuscated))
   startspeedtest()
   global unobfuscatednames
   unobfuscatednames = []
   global obfuscatednames
   obfuscatednames = []
   oldtolerance = _tolerance
   i = 0
   for thisunobfuscated in unobfuscated:
        i = i + 1
        if multipleof(i,20):
            print(str(i) + "/" + str(len(unobfuscated)))
        lasttolerance = [999999999,9999999998,9999999997,9999999996]
        _tolerance = oldtolerance
        while True:
            if ((lasttolerance[len(lasttolerance) - 1] == lasttolerance[len(lasttolerance) - 3]) and (lasttolerance[len(lasttolerance) - 2] == lasttolerance[len(lasttolerance) - 4])): #stuck in loop, trying to get to exactly 1 but can't
                break
            lasttolerance.append(_tolerance)
            objectmatches = []
            for thisobfuscated in obfuscated:
                if objectscheckformatch(thisunobfuscated,thisobfuscated):
                    objectmatches.append(thisobfuscated) #match!
            if len(objectmatches) > 1:
                _tolerance = _tolerance + 5
            elif len(objectmatches) == 0:
                _tolerance = _tolerance - 5
            else:
                break
            if ((_tolerance < 0) or (_tolerance > 100)):
                break
        unobfuscatednames.append(str(thisunobfuscated.get("Name")))
        matchnames = []
        matchestemp = []
        for thismatch in objectmatches:
            matchnames.append(str(thismatch.get("Name")))
            matchestemp.append(thismatch)
        obfuscatednames.append(matchnames)
   _tolerance = oldtolerance
   endspeedtest()
   print("All class names deobfuscated in " + timetaken + " miliseconds.")
   global results
   results = {}
   for i in range(len(unobfuscatednames)):
       results[str(unobfuscatednames[i])] = list(obfuscatednames[i])
   global output
   output = ""
   for i in range(len(unobfuscatednames)):
       output = output + str(unobfuscatednames[i]) + " = " + str(obfuscatednames[i]) + "\n"
   return(output)

def deobfuscateallclasseswithrestore():
   global _tolerance
   unobfuscated = stringtodict(read_file(r"C:/Users/zachy/OneDrive/Documents/Work/Temp Folders/Python Temps/unobfuscatedobjects.txt"))
   obfuscated = stringtodict(read_file(r"C:/Users/zachy/OneDrive/Documents/Work/Temp Folders/Python Temps/obfuscatedobjects.txt"))
   startspeedtest()
   global unobfuscatednames
   unobfuscatednames = []
   global obfuscatednames
   obfuscatednames = []
   oldtolerance = _tolerance
   i = 0
   for thisunobfuscated in unobfuscated:
        i = i + 1
        if multipleof(i,20):
            print(str(i) + "/" + str(len(unobfuscated)))
        lasttolerance = [999999999,9999999998,9999999997,9999999996]
        _tolerance = oldtolerance
        while True:
            if ((lasttolerance[len(lasttolerance) - 1] == lasttolerance[len(lasttolerance) - 3]) and (lasttolerance[len(lasttolerance) - 2] == lasttolerance[len(lasttolerance) - 4])): #stuck in loop, trying to get to exactly 1 but can't
                break
            lasttolerance.append(_tolerance)
            objectmatches = []
            for thisobfuscated in obfuscated:
                if objectscheckformatch(thisunobfuscated,thisobfuscated):
                    objectmatches.append(thisobfuscated) #match!
            if len(objectmatches) > 1:
                _tolerance = _tolerance + 5
            elif len(objectmatches) == 0:
                _tolerance = _tolerance - 5
            else:
                break
            if ((_tolerance < 0) or (_tolerance > 100)):
                break
        unobfuscatednames.append(str(thisunobfuscated.get("Name")))
        matchnames = []
        matchestemp = []
        for thismatch in objectmatches:
            matchnames.append(str(thismatch.get("Name")))
            matchestemp.append(thismatch)
        obfuscatednames.append(matchnames)
   _tolerance = oldtolerance
   endspeedtest()
   print("All class names deobfuscated in " + timetaken + " miliseconds.")
   global results
   results = {}
   for i in range(len(unobfuscatednames)):
       results[str(unobfuscatednames[i])] = list(obfuscatednames[i])
   global output
   output = ""
   for i in range(len(unobfuscatednames)):
       output = output + str(unobfuscatednames[i]) + " = " + str(obfuscatednames[i]) + "\n"
   return(output)

def builddeobfuscationoutput():
   global results
   global output
   global unobfuscatednames
   global obfuscatednames
   results = {}
   for i in range(len(unobfuscatednames)):
       results[str(unobfuscatednames[i])] = list(obfuscatednames[i])
   output = ""
   for i in range(len(unobfuscatednames)):
       output = output + str(unobfuscatednames[i]) + " = " + str(obfuscatednames[i]) + "\n"
   return(output)


def test():
    getfullobjects(dumpcs,False)
    resetflags()

def test2():
   getfullobjects(dumpcs,False)

def timetest(times = 100):
    averagetime = []
    for i in range(times):
        speedtest.start()
        test()
        speedtest.end()
        averagetime.append(speedtest.timetaken(False))
    averagetime = mean(averagetime)
    print("Test 1: " + str(averagetime) + " miliseconds")
    averagetime = []
    for i in range(times):
        speedtest.start()
        test2()
        speedtest.end()
        averagetime.append(speedtest.timetaken(False))
    averagetime = mean(averagetime)
    print("Test 2: " + str(averagetime) + " miliseconds")
    sys.exit()

#print("THIS IS A WIP / DEMO!\nNote: The program may have errors, get stuck in infinite loops, or not work correctly. This is just a demo.\nAnd of course, this may not always be accurate. It is unfinished, and even if it was finished, no deobfuscator can be perfect.\nThis will take around 20-200 minutes,\
#depending on your device. Be patient - it is worth the wait!\n")
init()
#a = getmethods(getfullmethods(a))
#b = "gg.setVisible(false)\ngg.clearList()\ngg.setRanges(gg.REGION_CODE_APP)"
#for i in a:
#    #if "int" in getwords(i["Type"]) or "float" in getwords(i["Type"]) or "bool" in getwords(i["Type"]):
    #if "bool" in getwords(i["Type"]):
       # b = b + "\n--" + i["Type"] + " " + i["Name"] + "\ngg.clearResults()\ngg.searchNumber('h " + offsettohex(i["Offset"],r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.5.0/libil2cpp.so",40) + "',gg.TYPE_BYTE)\ngg.getResults(8)\ngg.addListItems(gg.getResults(8))\ngg.editAll('h "
      #  if "bool" in getwords(i["Type"]):
     #       b = b + "20 00 80 D2"
    #    elif "int" in getwords(i["Type"]):
   #         b = b + "40 06 80 52"
  #      elif "float" in getwords(i["Type"]):
 #           b = b + "40 06 80 52"
#        b = b + " C0 03 5F D6',gg.TYPE_BYTE)"
#b = b + "\ngg.loadResults(gg.getListItems())"
#print(b)
#root = getxmlroot(parsexmlfile(r"C:/Users/zachy/OneDrive/Documents/APK Easy Tool/1-Decompiled APKs/Bullet Force V1.88.1/AndroidManifest.xml"))
a = r"C:/Users/zachy/OneDrive/Documents/APK Easy Tool/1-Decompiled APKs/Pixel Gun 3D 16.6.1 Armv7"
print(getmainactivityfromapk(a))
#print(getxmlrootattributes(parsexmlfile(r"C:/Users/zachy/OneDrive/Documents/APK Easy Tool/1-Decompiled APKs/Bullet Force V1.88.1/AndroidManifest.xml")))
print(formatlist(fulllog))
sys.exit()
print(ModMenuInstall.androidmanifest(r"C:\Users\zachy\OneDrive\Documents\APK Easy Tool\1-Decompiled APKs\Bullet Force V1.88.1"))
print(formatlist(fulllog))
#print(getmetadatafromapk(r"C:\Users\zachy\OneDrive\Documents\APK Easy Tool\1-Decompiled APKs\Pixel Gun 3D 16.6.1 Armv7","path"))
#print("\n")
#print(formatlist(fulllog,2))
#print(getmetadatafromapk(r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 16.6.1/Pixel Gun 3D 16.6.1 Armv7.apk","path"))
#print(getfullmethods(a))
#print(getfullfields(a))
#print(getfullproperties(a))
#sys.exit()
#unobfuscateddumpcs = r"C:/Users/zachy/OneDrive/Documents/Work/Projects/AMOGUS/Among Us  2020.9.9 dump.cs"
#obfuscateddumpcs = r"C:/Users/zachy/OneDrive/Documents/Work/Projects/AMOGUS/Among Us 2022.7.12 dump.cs"
#unobfuscateddumpcs = prompt("\nEnter the path to your UNOBFUSCATED dump.cs file (without quotes):")
#obfuscateddumpcs = prompt("Enter the path to your OBFUSCATED dump.cs file (without quotes):")
#dumpcspath = unobfuscateddumpcs
#loaddumpcs(dumpcspath)
#timetest(1)
#deobfuscateallclasseswithrestore()
#sys.exit()
#deobfuscateallclassesdemo()
#comparativedeobfuscationdemo(["Rocket"])
#write_file(r"C:\Users\zachy\OneDrive\Documents\Work\Outputs\output.txt",output)
#write_file(r"C:\Users\zachy\OneDrive\Documents\Work\Temp Folders\Python Temps\output.txt",output)
#print("Done deobfuscating! Check your output folder!")
#print(output)
