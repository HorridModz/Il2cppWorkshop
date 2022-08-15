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
if osimported:
    from os.path import exists
    from os import listdir
    from os.path import isfile, join
importmodule("html",False)
if htmlimported:
    from html.parser import HTMLParser
timeimported = True

#   Init

isinit = False

def init():
        global isinit
        isinit = True
        
        #Restore data from last session if it exists
        def loaddata(path):
            pass

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
                    error("File not found at path " + path,actions)
                global foldernotfounderror
                def foldernotfounderror(path,actions = ["log","print"]):
                    error("Folder not found at path " + path,actions)
                global fileencodingunknownerror
                def fileencodingunknownerror(path,actions = ["log","print"]):
                    error("Could not decode file at " + path + " due to unknown encoding. Only utf8, utf16, and utf32 are supported.",actions)
                global unknownfileopenerror
                def unknownfileopenerror(path,actions = ["log","print"]):
                    error("Unknown error occured when attempting to open file " + path,actions)
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
                    error("Metadata file not found at file path '" + path + "'. This game may not be an il2cpp game, or it may be an unsupported version of il2cpp. If the game is il2cpp, the metadata may be encrypted. Encrypted metadata files are currently not supported. See if you can find the metadata file manually.",actions)
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
            _types = ["t","virtual","dictionary","predicate","func","new","static","protected","public","private","internal","readonly","const","final","void","bool","byte","int16","int32","int64","uint16","uint32","uint64","char","decimal","single","double","float","int","long","sbyte","short","uint","ulong","ushort","string","array","list","delegate","object","vector3"]
            typeprefixes = []
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
            
        #inithttp()
        initstringandnumberconstants()
        initdumpcsconstants()
        initmessageconstants()
        initflags()
        initsettingsconstants()
        loaddata(rootdirectory)
        #settings specific to the game
        usenamingregex = False
        usenamingchars = False
        namingregex = "\\p{L}\\p{M}*"
        #init log
        global fulllog
        fulllog = []
        global importantlog
        importantlog = []


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
    if startpos == None or endpos == None:
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
    if str(text) == None:
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
    if (fullstr == "") or (fullstr == None):
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

def getfiles(directory):
    if ((lastletter(directory) == "/") or (lastletter(directory) == "\\")):
        path = substring(directory,1,len(directory) - 1)
    if not(os.path.isdir(directory)):
        foldernotfounderror(directory)
        return(None)
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
        log("WARNING: " + warning,message)
    if ("print" in actions):
        print("WARNING: " + warning,message)

def error(message,actions = ["log","print"]):
#log, print, printlog, printcurrentsublog, terminate, stop current function, etc.
    if actions == []: #this will cause error, so set back to default
        actions = ["log","print"]
    if ("log" in actions):
        log("ERROR: " + error,message)
    if ("print" in actions):
        print("ERROR: " + error,message)

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
    if important:
        global importantlog
        importantlog.append(str(tolog))
         
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
    if getfileextension(apkpath) == "apk":
        apknotdecompilederror(apkpath)
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
    
findmetadatafromapk = getmetadatafromapk #same thing, but different name

def getlibil2cppfromapk(apkpath,returntype = "path"): #make sure apk is decompiled!
    if getfileextension(apkpath) == "apk":
        apknotdecompilederror(apkpath)
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
    
findlibil2cppfromapk = getlibil2cppfromapk #same thing, but different name

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
    #if localfullobjects == None:
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
    if usetolerance == None:
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
#a = "// Namespace: \npublic sealed class WeaponSounds : PGBehaviour // TypeDefIndex: 13691\n{\n	// Fields\n	internal const string 东三丌且上与丘一丅 = \"RememberedTierWhenObtainGun_\";\n	internal static readonly string 丙上丄丘不丂上丒七; // 0x0\n	internal static readonly string 世万不上万一不丌丁; // 0x8\n	internal static readonly string 丑丂且丗丐一上丂丛; // 0x10\n	internal static readonly string 丒三丞世不不世丙丁; // 0x18\n	internal static readonly string 丛丛与丝世丙三丑丄; // 0x20\n	internal static readonly string 丛丏丆丆一七丙七三; // 0x28\n	internal static readonly string 专丞丗丝丂丘一东丟; // 0x30\n	internal static readonly string 下丑不丘丕丞丆世丏; // 0x38\n	internal static readonly string 下丄上与丌且万丙丄; // 0x40\n	internal static readonly string 丙丝专丗东三丈丂丛; // 0x48\n	internal static readonly string 丒业丝丑与丛业与三; // 0x50\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87548 Offset: 0x1D87548 VA: 0x1D87548\n	public int categoryNabor; // 0x48\n	public int[] filterMap; // 0x50\n	public WeaponSounds.丏与丈业丄丒不七业 typeDead; // 0x58\n	public int ammoInClip; // 0x5C\n	public int InitialAmmo; // 0x60\n	public int maxAmmo; // 0x64\n	public int ammoForBonusShotMelee; // 0x68\n	public int ammoFromBonus; // 0x6C\n	public string localizeWeaponKey; // 0x70\n	public static string[] alternativeNames; // 0x58\n	[丗上下万上丘世一丐] // RVA: 0x1D87580 Offset: 0x1D87580 VA: 0x1D87580\n	public string alternativeName; // 0x78\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87590 Offset: 0x1D87590 VA: 0x1D87590\n	public bool IsEvent; // 0x80\n	public bool IsCraftFromSet; // 0x81\n	public bool IsCraft; // 0x82\n	[丗上下万上丘世一丐] // RVA: 0x1D875C8 Offset: 0x1D875C8 VA: 0x1D875C8\n	public bool IsClansCraft; // 0x83\n	[丝丙业丟丐业万丐上] // RVA: 0x1D875D8 Offset: 0x1D875D8 VA: 0x1D875D8\n	public Vector2 startZone; // 0x84\n	public float maxKoof; // 0x8C\n	public float tekKoof; // 0x90\n	public float upKoofFire; // 0x94\n	public float downKoofFirst; // 0x98\n	public float downKoof; // 0x9C\n	internal float 世下不丂丑丒七丙东; // 0xA0\n	[SerializeField] // RVA: 0x1D87610 Offset: 0x1D87610 VA: 0x1D87610\n	private float timerForTekKoofVisual; // 0xA4\n	[SerializeField] // RVA: 0x1D87620 Offset: 0x1D87620 VA: 0x1D87620\n	private float timerForTekKoofVisualByFireRate; // 0xA8\n	private const float 丈一丒万丌丄且丒世 = 5;\n	private const float 丒上丆丅丗东世上一 = 10;\n	public float timeForTekKoofVisual; // 0xAC\n	[SerializeField] // RVA: 0x1D87630 Offset: 0x1D87630 VA: 0x1D87630\n	private bool firstShotScatter; // 0xB0\n	internal float 业丄丄业一丛丏丙下; // 0xB4\n	[SerializeField] // RVA: 0x1D87640 Offset: 0x1D87640 VA: 0x1D87640\n	private float moveScatterCoeff; // 0xB8\n	[SerializeField] // RVA: 0x1D87650 Offset: 0x1D87650 VA: 0x1D87650\n	private bool instantHorizontalMoveScatterCoeff; // 0xBC\n	[SerializeField] // RVA: 0x1D87660 Offset: 0x1D87660 VA: 0x1D87660\n	private bool instantVerticalMoveScatterCoeff; // 0xBD\n	[SerializeField] // RVA: 0x1D87670 Offset: 0x1D87670 VA: 0x1D87670\n	private bool scatterInversion; // 0xBE\n	[SerializeField] // RVA: 0x1D87680 Offset: 0x1D87680 VA: 0x1D87680\n	private float recoilCoeff; // 0xC0\n	[丗上下万上丘世一丐] // RVA: 0x1D87690 Offset: 0x1D87690 VA: 0x1D87690\n	[SerializeField] // RVA: 0x1D87690 Offset: 0x1D87690 VA: 0x1D87690\n	private bool enableRocketScatter; // 0xC4\n	[丝丙业丟丐业万丐上] // RVA: 0x1D876C8 Offset: 0x1D876C8 VA: 0x1D876C8\n	public bool isZooming; // 0xC5\n	public bool zoomXray; // 0xC6\n	[SerializeField] // RVA: 0x1D87700 Offset: 0x1D87700 VA: 0x1D87700\n	internal Player_move_c.业丌丅丗与丙一三且 xRayType; // 0xC8\n	public GameObject iRayEffect; // 0xD0\n	[SerializeField] // RVA: 0x1D87710 Offset: 0x1D87710 VA: 0x1D87710\n	private float fieldOfViewZomm; // 0xD8\n	public bool considerScopeValues; // 0xDC\n	public float scopeCircleRadius; // 0xE0\n	public float scopePointsSpeed; // 0xE4\n	public float scopeMovementSpeed; // 0xE8\n	public float scopeTrashHoldForDistanceToPoint; // 0xEC\n	public float scopeStartValueSpeedIncreace; // 0xF0\n	public float scopeIncreaceStep; // 0xF4\n	[丗上下万上丘世一丐] // RVA: 0x1D87720 Offset: 0x1D87720 VA: 0x1D87720\n	public float scopeSpeed; // 0xF8\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87730 Offset: 0x1D87730 VA: 0x1D87730\n	[FormerlySerializedAsAttribute] // RVA: 0x1D87730 Offset: 0x1D87730 VA: 0x1D87730\n	public Vector2 startZoneZoom; // 0xFC\n	[FormerlySerializedAsAttribute] // RVA: 0x1D87790 Offset: 0x1D87790 VA: 0x1D87790\n	public float maxKoofZoom; // 0x104\n	[FormerlySerializedAsAttribute] // RVA: 0x1D877C8 Offset: 0x1D877C8 VA: 0x1D877C8\n	public float upKoofFireZoom; // 0x108\n	[FormerlySerializedAsAttribute] // RVA: 0x1D87800 Offset: 0x1D87800 VA: 0x1D87800\n	public float downKoofFirstZoom; // 0x10C\n	[FormerlySerializedAsAttribute] // RVA: 0x1D87838 Offset: 0x1D87838 VA: 0x1D87838\n	public float downKoofZoom; // 0x110\n	internal float 丞丙丟丌丙丘业丘一; // 0x114\n	[SerializeField] // RVA: 0x1D87870 Offset: 0x1D87870 VA: 0x1D87870\n	private bool firstShotScatterZoom; // 0x118\n	[SerializeField] // RVA: 0x1D87880 Offset: 0x1D87880 VA: 0x1D87880\n	private float moveScatterCoeffZoom; // 0x11C\n	[SerializeField] // RVA: 0x1D87890 Offset: 0x1D87890 VA: 0x1D87890\n	private bool instantHorizontalMoveScatterCoeffZoom; // 0x120\n	[SerializeField] // RVA: 0x1D878A0 Offset: 0x1D878A0 VA: 0x1D878A0\n	private bool instantVerticalMoveScatterCoeffZoom; // 0x121\n	[SerializeField] // RVA: 0x1D878B0 Offset: 0x1D878B0 VA: 0x1D878B0\n	private bool scatterInversionZoom; // 0x122\n	[SerializeField] // RVA: 0x1D878C0 Offset: 0x1D878C0 VA: 0x1D878C0\n	[丗上下万上丘世一丐] // RVA: 0x1D878C0 Offset: 0x1D878C0 VA: 0x1D878C0\n	private float recoilCoeffZoom; // 0x124\n	[丝丙业丟丐业万丐上] // RVA: 0x1D878F8 Offset: 0x1D878F8 VA: 0x1D878F8\n	public bool ignoreBarrier; // 0x128\n	public bool ignoreSlyWolf; // 0x129\n	[丗上下万上丘世一丐] // RVA: 0x1D87930 Offset: 0x1D87930 VA: 0x1D87930\n	public bool ignoreReflector; // 0x12A\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87940 Offset: 0x1D87940 VA: 0x1D87940\n	public bool bazooka; // 0x12B\n	public bool raycastOnRocketFire; // 0x12C\n	[SerializeField] // RVA: 0x1D87978 Offset: 0x1D87978 VA: 0x1D87978\n	private bool isMomentumProjectile; // 0x12D\n	public float bazookaDelay; // 0x130\n	public int rocketNum; // 0x134\n	public float stepTimeInSeriaBazooka; // 0x138\n	public string bazookaExplosionName; // 0x140\n	public float bazookaExplosionRadius; // 0x148\n	public float bazookaExplosionRadiusSelf; // 0x14C\n	public float bazookaImpulseRadius; // 0x150\n	public bool bazookaUseGunFlashDirection; // 0x154\n	public bool isLightning; // 0x155\n	public bool isGhost; // 0x156\n	public bool grenadeLauncher; // 0x157\n	public int countInSeriaBazooka; // 0x158\n	public bool useAmmoForEachRocketInSeriaBazooka; // 0x15C\n	public float impulseForce; // 0x160\n	public float impulseForceSelf; // 0x164\n	public bool isDifferentffectsInSeria; // 0x168\n	public bool fanRocketShoot; // 0x169\n	public float fangAngle; // 0x16C\n	public int[] bazookaRandomRockets; // 0x170\n	[丗上下万上丘世一丐] // RVA: 0x1D87988 Offset: 0x1D87988 VA: 0x1D87988\n	public bool bazookaUltimateShoot; // 0x178\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87998 Offset: 0x1D87998 VA: 0x1D87998\n	public bool isMelee; // 0x179\n	public bool isMeleeSlasher; // 0x17A\n	public float radiusRoundMelee; // 0x17C\n	public float meleeAngle; // 0x180\n	public float meleeAttackTimeModifier; // 0x184\n	public bool gradualExplosions; // 0x188\n	public bool isRoundMelee; // 0x189\n	public bool useAngleForRoundMelee; // 0x18A\n	public float meleeBackDot; // 0x18C\n	[丗上下万上丘世一丐] // RVA: 0x1D879D0 Offset: 0x1D879D0 VA: 0x1D879D0\n	public int meleePunchesCount; // 0x190\n	[丝丙业丟丐业万丐上] // RVA: 0x1D879E0 Offset: 0x1D879E0 VA: 0x1D879E0\n	public int countShots; // 0x194\n	public WeaponSounds.不三丕东丒丐且丆与 typeTracer; // 0x198\n	public bool bulletBreakout; // 0x19C\n	public bool bulletExplode; // 0x19D\n	public bool isShotGun; // 0x19E\n	public bool bulletSuperBreakout; // 0x19F\n	public WeaponSounds.与丘丑丏丌下丆丘不 typeHole; // 0x1A0\n	public float bulletDelay; // 0x1A4\n	[丗上下万上丘世一丐] // RVA: 0x1D87A18 Offset: 0x1D87A18 VA: 0x1D87A18\n	public float shootDelay; // 0x1A8\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87A28 Offset: 0x1D87A28 VA: 0x1D87A28\n	public bool freezer; // 0x1AC\n	public int countReflectionRay; // 0x1B0\n	public bool railgun; // 0x1B4\n	public string railName; // 0x1B8\n	public bool railgunStopAtWall; // 0x1C0\n	[丗上下万上丘世一丐] // RVA: 0x1D87A60 Offset: 0x1D87A60 VA: 0x1D87A60\n	public bool useSpawnPointRotationOnFreezer; // 0x1C1\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87A70 Offset: 0x1D87A70 VA: 0x1D87A70\n	public bool isCharging; // 0x1C2\n	public bool useOneAmmoOnCHarge; // 0x1C3\n	public bool isChargeOrbital; // 0x1C4\n	public GameObject chargeEffect; // 0x1C8\n	public bool chargeLoop; // 0x1D0\n	public bool crossfadeChargeAnim; // 0x1D1\n	public float crossfadeSpeed; // 0x1D4\n	public int chargeMax; // 0x1D8\n	public float chargeTime; // 0x1DC\n	[丗上下万上丘世一丐] // RVA: 0x1D87AA8 Offset: 0x1D87AA8 VA: 0x1D87AA8\n	public bool invisWhenCharged; // 0x1E0\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87AB8 Offset: 0x1D87AB8 VA: 0x1D87AB8\n	public bool isDamageHeal; // 0x1E1\n	public float damageHealMultiplier; // 0x1E4\n	public bool isGadgetDisabler; // 0x1E8\n	public float gadgetDisableTime; // 0x1EC\n	public bool isPoisoning; // 0x1F0\n	[SerializeField] // RVA: 0x1D87AF0 Offset: 0x1D87AF0 VA: 0x1D87AF0\n	private int poisonCount; // 0x1F4\n	public float poisonDamageMultiplier; // 0x1F8\n	[SerializeField] // RVA: 0x1D87B00 Offset: 0x1D87B00 VA: 0x1D87B00\n	private float poisonTime; // 0x1FC\n	[SerializeField] // RVA: 0x1D87B10 Offset: 0x1D87B10 VA: 0x1D87B10\n	internal 丒丝丆丁丟丂丗丒东 poisonType; // 0x200\n	[SerializeField] // RVA: 0x1D87B20 Offset: 0x1D87B20 VA: 0x1D87B20\n	internal bool isIgnoreIgnoreDamage; // 0x204\n	public bool healer; // 0x205\n	public bool jumpDisabler; // 0x206\n	public float jumpDisableTime; // 0x208\n	public bool isCursing; // 0x20C\n	public float curseTime; // 0x210\n	public float curseDamageMultiplier; // 0x214\n	public bool isSlowdown; // 0x218\n	[RangeAttribute] // RVA: 0x1D87B30 Offset: 0x1D87B30 VA: 0x1D87B30\n	public float slowdownCoeff; // 0x21C\n	public float slowdownTime; // 0x220\n	public bool isSlowdownStack; // 0x224\n	public int maxStack; // 0x228\n	public bool fireImmunity; // 0x22C\n	[HeaderAttribute] // RVA: 0x1D87B4C Offset: 0x1D87B4C VA: 0x1D87B4C\n	public bool enemyMarker; // 0x22D\n	public bool enemyMarkerWhenAiming; // 0x22E\n	public bool enemyMarkerWhenShot; // 0x22F\n	public float enemyMarketChargeTime; // 0x230\n	public float enemyMarkerAngle; // 0x234\n	public float enemyMarkerTriangleCathetLength; // 0x238\n	public int enemyMarkId; // 0x23C\n	[HeaderAttribute] // RVA: 0x1D87B84 Offset: 0x1D87B84 VA: 0x1D87B84\n	public bool isHeadMagnifier; // 0x240\n	public float headMagnifierTime; // 0x244\n	[HeaderAttribute] // RVA: 0x1D87BBC Offset: 0x1D87BBC VA: 0x1D87BBC\n	public bool isBlindEffect; // 0x248\n	[SerializeField] // RVA: 0x1D87BF4 Offset: 0x1D87BF4 VA: 0x1D87BF4\n	internal Player_move_c.下丆丙下一专东丝丏 blindEffect; // 0x24C\n	public float isBlindEffectTime; // 0x250\n	[HeaderAttribute] // RVA: 0x1D87C04 Offset: 0x1D87C04 VA: 0x1D87C04\n	public bool isCharm; // 0x254\n	public float charmTime; // 0x258\n	[HeaderAttribute] // RVA: 0x1D87C3C Offset: 0x1D87C3C VA: 0x1D87C3C\n	public bool isWeaknessEffect; // 0x25C\n	[丗上下万上丘世一丐] // RVA: 0x1D87C74 Offset: 0x1D87C74 VA: 0x1D87C74\n	public float weaknessEffectTime; // 0x260\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87C84 Offset: 0x1D87C84 VA: 0x1D87C84\n	public bool teammateDamageBoostBuff; // 0x264\n	public float teammateDamageBoostRadius; // 0x268\n	public float teammateDamageBoostMultiplier; // 0x26C\n	public float teammateDamageBoostZoneTime; // 0x270\n	[丗上下万上丘世一丐] // RVA: 0x1D87CBC Offset: 0x1D87CBC VA: 0x1D87CBC\n	public float teammateDamageBoostBuffTime; // 0x274\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87CCC Offset: 0x1D87CCC VA: 0x1D87CCC\n	public bool isDash; // 0x278\n	public float dashMaxImpulse; // 0x27C\n	public float dashDecaySpeed; // 0x280\n	[丗上下万上丘世一丐] // RVA: 0x1D87D04 Offset: 0x1D87D04 VA: 0x1D87D04\n	public float dashDeltaImpact; // 0x284\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87D14 Offset: 0x1D87D14 VA: 0x1D87D14\n	public bool harpoon; // 0x288\n	public Transform harpoonStartPoint; // 0x290\n	public float harpoonImpulse; // 0x298\n	public float harpoonDeltaUp; // 0x29C\n	public float harpooneMaxImpulse; // 0x2A0\n	public float harpooneMinImpulse; // 0x2A4\n	public float harpoonDecaySpeed; // 0x2A8\n	public float harpoonMaxDelta; // 0x2AC\n	public float harpoonMaxDistance; // 0x2B0\n	public float harpoonDeltaImpact; // 0x2B4\n	[丗上下万上丘世一丐] // RVA: 0x1D87D4C Offset: 0x1D87D4C VA: 0x1D87D4C\n	public float harpoonMinDistance; // 0x2B8\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87D5C Offset: 0x1D87D5C VA: 0x1D87D5C\n	public bool polymorpher; // 0x2BC\n	public float polymorphDuarationTime; // 0x2C0\n	public WeaponSounds.且业丗专上丟万丗丏 polymorphType; // 0x2C4\n	[丗上下万上丘世一丐] // RVA: 0x1D87D94 Offset: 0x1D87D94 VA: 0x1D87D94\n	public float polymorphMaxHealth; // 0x2C8\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87DA4 Offset: 0x1D87DA4 VA: 0x1D87DA4\n	public bool snowStorm; // 0x2CC\n	public float snowStormBonusMultiplier; // 0x2D0\n	[丗上下万上丘世一丐] // RVA: 0x1D87DDC Offset: 0x1D87DDC VA: 0x1D87DDC\n	public float snowStormBonusRange; // 0x2D4\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87DEC Offset: 0x1D87DEC VA: 0x1D87DEC\n	public string armoryPreviewName; // 0x2D8\n	[丗上下万上丘世一丐] // RVA: 0x1D87E24 Offset: 0x1D87E24 VA: 0x1D87E24\n	public bool useTextureSkinForArmoryPreview; // 0x2E0\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87E34 Offset: 0x1D87E34 VA: 0x1D87E34\n	public bool isDamageReflection; // 0x2E1\n	public bool isDamageAbsorption; // 0x2E2\n	[丗上下万上丘世一丐] // RVA: 0x1D87E6C Offset: 0x1D87E6C VA: 0x1D87E6C\n	[RangeAttribute] // RVA: 0x1D87E6C Offset: 0x1D87E6C VA: 0x1D87E6C\n	public float damageReflectionValue; // 0x2E4\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87EAC Offset: 0x1D87EAC VA: 0x1D87EAC\n	public bool isKilledTargetExplode; // 0x2E8\n	public float killedTargetExplosionRadiusDamage; // 0x2EC\n	public float killedTargetExplosionRadiusDamageSelf; // 0x2F0\n	public float killedTargetExplosionDamageMultiplier; // 0x2F4\n	[丗上下万上丘世一丐] // RVA: 0x1D87EE4 Offset: 0x1D87EE4 VA: 0x1D87EE4\n	public string explosionNameForKilledTarget; // 0x2F8\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87EF4 Offset: 0x1D87EF4 VA: 0x1D87EF4\n	public bool isCoinDrop; // 0x300\n	[丗上下万上丘世一丐] // RVA: 0x1D87F2C Offset: 0x1D87F2C VA: 0x1D87F2C\n	public float coinDropChance; // 0x304\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87F3C Offset: 0x1D87F3C VA: 0x1D87F3C\n	public bool ammoRestoreShootTemplate; // 0x308\n	[RangeAttribute] // RVA: 0x1D87F74 Offset: 0x1D87F74 VA: 0x1D87F74\n	public float ammoRestorePercent; // 0x30C\n	public bool isAmmoRestore; // 0x310\n	public int ammoRestoreNumber; // 0x314\n	[丗上下万上丘世一丐] // RVA: 0x1D87F8C Offset: 0x1D87F8C VA: 0x1D87F8C\n	public float ammoRestoreTime; // 0x318\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87F9C Offset: 0x1D87F9C VA: 0x1D87F9C\n	public bool flamethrower; // 0x31C\n	public bool isSimpleFlamethrower; // 0x31D\n	internal float 万丅下东一丆世丝七; // 0x320\n	public bool dotFlamethrower; // 0x324\n	public float dotTimeFlamethrower; // 0x328\n	public bool dotFlameTimeIsDependedOnChargeTime; // 0x32C\n	[丗上下万上丘世一丐] // RVA: 0x1D87FD4 Offset: 0x1D87FD4 VA: 0x1D87FD4\n	public bool dotFlameDamageIsDependedOnChargeTime; // 0x32D\n	[丝丙业丟丐业万丐上] // RVA: 0x1D87FE4 Offset: 0x1D87FE4 VA: 0x1D87FE4\n	public bool isFrostSword; // 0x32E\n	public float frostDamageMultiplier; // 0x330\n	public float frostRadius; // 0x334\n	public bool isFrostSwordUseAngle; // 0x338\n	[丗上下万上丘世一丐] // RVA: 0x1D8801C Offset: 0x1D8801C VA: 0x1D8801C\n	public float frostSwordAngle; // 0x33C\n	[丝丙业丟丐业万丐上] // RVA: 0x1D8802C Offset: 0x1D8802C VA: 0x1D8802C\n	public bool isInvisibleReload; // 0x340\n	public bool isInvisibleAfterKill; // 0x341\n	public float invisibleAfterKillTime; // 0x344\n	[丗上下万上丘世一丐] // RVA: 0x1D88064 Offset: 0x1D88064 VA: 0x1D88064\n	public bool firstKillCritical; // 0x348\n	[丝丙业丟丐业万丐上] // RVA: 0x1D88074 Offset: 0x1D88074 VA: 0x1D88074\n	public bool isBuffPoints; // 0x349\n	public float buffPointsRevenge; // 0x34C\n	public bool buffPointsRevengeDesigner; // 0x350\n	public float buffBonusPointsForKill; // 0x354\n	public bool buffPointsKillDesigner; // 0x358\n	public float buffBonusPointsForAssist; // 0x35C\n	public bool buffPointsAssistDesigner; // 0x360\n	[丗上下万上丘世一丐] // RVA: 0x1D880AC Offset: 0x1D880AC VA: 0x1D880AC\n	public float buffPointsOther; // 0x364\n	[丝丙业丟丐业万丐上] // RVA: 0x1D880BC Offset: 0x1D880BC VA: 0x1D880BC\n	public float shotgunMaxDamageDistance; // 0x368\n	public float shotgunMinDamageCoef; // 0x36C\n	public float shotgunOverDamageDistance; // 0x370\n	[丗上下万上丘世一丐] // RVA: 0x1D880F4 Offset: 0x1D880F4 VA: 0x1D880F4\n	public float shotgunOverDamageCoef; // 0x374\n	[丝丙业丟丐业万丐上] // RVA: 0x1D88104 Offset: 0x1D88104 VA: 0x1D88104\n	public bool isSectorsAOE; // 0x378\n	public float sectorsAOEAngleFront; // 0x37C\n	public float sectorsAOEAngleBack; // 0x380\n	public float sectorsAOEDamageMultiplierFront; // 0x384\n	public float sectorsAOEDamageMultiplierSide; // 0x388\n	public float sectorsAOEDamageMultiplierBack; // 0x38C\n	[丗上下万上丘世一丐] // RVA: 0x1D8813C Offset: 0x1D8813C VA: 0x1D8813C\n	public float sectorsAOERadiusSectorsAoE; // 0x390\n	[丝丙业丟丐业万丐上] // RVA: 0x1D8814C Offset: 0x1D8814C VA: 0x1D8814C\n	public bool portalGun; // 0x394\n	public bool isPortalExplosion; // 0x395\n	public Gradient portalGunGradient; // 0x398\n	[SerializeField] // RVA: 0x1D88184 Offset: 0x1D88184 VA: 0x1D88184\n	[丗上下万上丘世一丐] // RVA: 0x1D88184 Offset: 0x1D88184 VA: 0x1D88184\n	internal PortalChainManager.丂丞丘一丈专丝丁丒 portalType; // 0x3A0\n	[丝丙业丟丐业万丐上] // RVA: 0x1D881BC Offset: 0x1D881BC VA: 0x1D881BC\n	public bool isArmorRegeneration; // 0x3A4\n	public float armorRegenerationPercent; // 0x3A8\n	[丗上下万上丘世一丐] // RVA: 0x1D881F4 Offset: 0x1D881F4 VA: 0x1D881F4\n	public float armorRegenerationTime; // 0x3AC\n	[丝丙业丟丐业万丐上] // RVA: 0x1D88204 Offset: 0x1D88204 VA: 0x1D88204\n	public bool isAmmoSteal; // 0x3B0\n	[丗上下万上丘世一丐] // RVA: 0x1D8823C Offset: 0x1D8823C VA: 0x1D8823C\n	public float ammoStealPercent; // 0x3B4\n	[丝丙业丟丐业万丐上] // RVA: 0x1D8824C Offset: 0x1D8824C VA: 0x1D8824C\n	public float shootDistanceIfZoom; // 0x3B8\n	[丗上下万上丘世一丐] // RVA: 0x1D88284 Offset: 0x1D88284 VA: 0x1D88284\n	public WeaponSounds.丏下上丂丘丞专丏丅[] ifIsZoom; // 0x3C0\n	[丝丙业丟丐业万丐上] // RVA: 0x1D88294 Offset: 0x1D88294 VA: 0x1D88294\n	public WeaponSounds.丙丐丆专丑丄三七丟[] ifIncompleteCharged; // 0x3C8\n	[丗上下万上丘世一丐] // RVA: 0x1D882CC Offset: 0x1D882CC VA: 0x1D882CC\n	public WeaponSounds.丙丐丆专丑丄三七丟[] ifFullCharged; // 0x3D0\n	[丝丙业丟丐业万丐上] // RVA: 0x1D882DC Offset: 0x1D882DC VA: 0x1D882DC\n	public bool isIncreasedDamageFromKill; // 0x3D8\n	public float damageMultiplier; // 0x3DC\n	[丗上下万上丘世一丐] // RVA: 0x1D88314 Offset: 0x1D88314 VA: 0x1D88314\n	public int maxStackIncreasedDamage; // 0x3E0\n	[丝丙业丟丐业万丐上] // RVA: 0x1D88324 Offset: 0x1D88324 VA: 0x1D88324\n	public bool isElectricShock; // 0x3E4\n	[RangeAttribute] // RVA: 0x1D8835C Offset: 0x1D8835C VA: 0x1D8835C\n	public float electricShockCoeff; // 0x3E8\n	[丗上下万上丘世一丐] // RVA: 0x1D88374 Offset: 0x1D88374 VA: 0x1D88374\n	public float electricShockTime; // 0x3EC\n	[丝丙业丟丐业万丐上] // RVA: 0x1D88384 Offset: 0x1D88384 VA: 0x1D88384\n	public bool isFastAfterKill; // 0x3F0\n	public float fastMultiplier; // 0x3F4\n	public int maxStackAfterKill; // 0x3F8\n	[丗上下万上丘世一丐] // RVA: 0x1D883BC Offset: 0x1D883BC VA: 0x1D883BC\n	public float timeFastAfterKill; // 0x3FC\n	[丝丙业丟丐业万丐上] // RVA: 0x1D883CC Offset: 0x1D883CC VA: 0x1D883CC\n	public bool loseFlagWhenShoot; // 0x400\n	public bool isUnlimitedAmmo; // 0x401\n	public bool isShotMelee; // 0x402\n	public bool isMeleeShotAndReloaded; // 0x403\n	public bool isSpleef; // 0x404\n	public bool seriesShoot; // 0x405\n	public bool isBurstShooting; // 0x406\n	public bool isDamageFromDamageCollider; // 0x407\n	public bool isDaterWeapon; // 0x408\n	public bool isDoubleShot; // 0x409\n	public bool isDoubleSyncShot; // 0x40A\n	public bool isCameraInCenter; // 0x40B\n	public bool isExoskelet; // 0x40C\n	public bool isGrenadeWeapon; // 0x40D\n	public bool isLoopShoot; // 0x40E\n	public bool isDoubleJump; // 0x40F\n	public bool isMechWeapon; // 0x410\n	public int criticalHitChance; // 0x414\n	public float criticalHitCoef; // 0x418\n	public bool shocker; // 0x41C\n	public float shockerDamageMultiplier; // 0x420\n	public float shockerRange; // 0x424\n	public bool isDoubleShoot2Rockets; // 0x428\n	public bool isAnimReloadAfterShoot; // 0x429\n	public string groundEffectName; // 0x430\n	[丗上下万上丘世一丐] // RVA: 0x1D88404 Offset: 0x1D88404 VA: 0x1D88404\n	public bool useOnGroundEffectWithoutParent; // 0x438\n	[丝丙业丟丐业万丐上] // RVA: 0x1D88414 Offset: 0x1D88414 VA: 0x1D88414\n	public bool weaponIsNotFromConfig; // 0x439\n	[丗上下万上丘世一丐] // RVA: 0x1D8844C Offset: 0x1D8844C VA: 0x1D8844C\n	public float lengthShootFromPrefab; // 0x43C\n	[丝丙业丟丐业万丐上] // RVA: 0x1D8845C Offset: 0x1D8845C VA: 0x1D8845C\n	public Vector3 bonusLocalPosition; // 0x440\n	[丗上下万上丘世一丐] // RVA: 0x1D88494 Offset: 0x1D88494 VA: 0x1D88494\n	public Vector3 bonusLocalScale; // 0x44C\n	public List<WeaponSounds.东下丙与与丑丕不丘> InShopEffects; // 0x458\n	[HeaderAttribute] // RVA: 0x1D884A4 Offset: 0x1D884A4 VA: 0x1D884A4\n	public bool IsActiveAim; // 0x460\n	private float 丞丞下丅丛丗丄与丙; // 0x464\n	private BearInnerWeaponPars 业丕且丑丂不下业且; // 0x468\n	private float 丄且丞世下丒丅东丙; // 0x470\n	private float 与丁丑下丌一丏丈丈; // 0x474\n	private float 下业丘丅丛上与下与; // 0x478\n	[SerializeField] // RVA: 0x1D884DC Offset: 0x1D884DC VA: 0x1D884DC\n	private InnerWeaponPars _innerWeaponPars; // 0x480\n	private SkinnedMeshRenderer[] 一一丛丈上三丁上一; // 0x488\n	private Player_move_c 万丛与丂万专丏丑丒; // 0x490\n	private FirstPersonControlSharp 世世丙丏七上丁世三; // 0x498\n	[CompilerGeneratedAttribute] // RVA: 0x1D884EC Offset: 0x1D884EC VA: 0x1D884EC\n	private MinigunController <丒丕丈一丁下东业业>k__BackingField; // 0x4A0\n	[CompilerGeneratedAttribute] // RVA: 0x1D884FC Offset: 0x1D884FC VA: 0x1D884FC\n	private GunBonesRotatorController <东丙丝丗东丐业丌丟>k__BackingField; // 0x4A8\n	[HeaderAttribute] // RVA: 0x1D8850C Offset: 0x1D8850C VA: 0x1D8850C\n	[SerializeField] // RVA: 0x1D8850C Offset: 0x1D8850C VA: 0x1D8850C\n	private bool isWeaponInsideHands; // 0x4B0\n	[HeaderAttribute] // RVA: 0x1D88558 Offset: 0x1D88558 VA: 0x1D88558\n	[SerializeField] // RVA: 0x1D88558 Offset: 0x1D88558 VA: 0x1D88558\n	internal bool useLowAvatarArms; // 0x4B1\n	[SerializeField] // RVA: 0x1D885A4 Offset: 0x1D885A4 VA: 0x1D885A4\n	[HeaderAttribute] // RVA: 0x1D885A4 Offset: 0x1D885A4 VA: 0x1D885A4\n	private WeaponReloadEffect _reloadEffect; // 0x4B8\n	[SerializeField] // RVA: 0x1D885F0 Offset: 0x1D885F0 VA: 0x1D885F0\n	private WeaponSecondTimeFireAction _secondTimeFireAction; // 0x4C0\n	[SerializeField] // RVA: 0x1D88600 Offset: 0x1D88600 VA: 0x1D88600\n	private WeaponChargeShield _chargeShield; // 0x4C8\n	[SerializeField] // RVA: 0x1D88610 Offset: 0x1D88610 VA: 0x1D88610\n	private WeaponSkinChanger skinChanger; // 0x4D0\n	[SerializeField] // RVA: 0x1D88620 Offset: 0x1D88620 VA: 0x1D88620\n	internal WeaponUltimateAbility weaponUltimate; // 0x4D8\n	[CompilerGeneratedAttribute] // RVA: 0x1D88630 Offset: 0x1D88630 VA: 0x1D88630\n	private bool <万上丐丝丛丛丑丏丁>k__BackingField; // 0x4E0\n	[HeaderAttribute] // RVA: 0x1D88640 Offset: 0x1D88640 VA: 0x1D88640\n	public string ShopId; // 0x4E8\n	public Vector3 positionShop; // 0x4F0\n	public Vector3 rotationShop; // 0x4FC\n	public float scaleShop; // 0x508\n	private AnimationState 业丕七丗上东万丗不; // 0x510\n	public int armorPercent; // 0x518\n	internal 七东丒丈丂东一丌丌 丆丕丛丂丑上丆七丕; // 0x520\n	internal float 且业丐丁业且丌丟东; // 0x528\n	[SerializeField] // RVA: 0x1D88678 Offset: 0x1D88678 VA: 0x1D88678\n	internal bool healingArea; // 0x52C\n	[SerializeField] // RVA: 0x1D88688 Offset: 0x1D88688 VA: 0x1D88688\n	internal bool healingHimSelf; // 0x52D\n	[SerializeField] // RVA: 0x1D88698 Offset: 0x1D88698 VA: 0x1D88698\n	internal float radiusHealing; // 0x530\n	private Nullable<float> 丄上丈且上丁丕丅丄; // 0x534\n	private bool 丒东丆丟业丁丆丌丕; // 0x53C\n	private GameObject 丝业世丒丟丝万丅丕; // 0x540\n	public bool Blik; // 0x548\n	public bool campaignOnly; // 0x549\n	public bool CanBuy; // 0x54A\n	public int countShootInBurst; // 0x54C\n	public float delayInBurstShooting; // 0x550\n	internal float 丒丟丟且丁专三丞丒; // 0x554\n	public float[] damageByTier; // 0x558\n	public Vector2 damageRange; // 0x560\n	public DamageWeaponCollider damageWeaponCollider; // 0x568\n	public string daterMessage; // 0x570\n	public float[] dpses; // 0x578\n	public float ragdollImpulse; // 0x580\n	public bool DPSRememberWhenGet; // 0x584\n	public int fireRateShop; // 0x588\n	public float grenadeThrowTime; // 0x58C\n	public float grenadeUseTime; // 0x590\n	public List<BulletSpawnPoint> bulletSpawnPoints; // 0x598\n	public Vector3 gunPosition; // 0x5A0\n	public int inAppExtensionModifier; // 0x5AC\n	[HeaderAttribute] // RVA: 0x1D886A8 Offset: 0x1D886A8 VA: 0x1D886A8\n	public bool IsRoyaleWeapon; // 0x5B0\n	public float loudnessScale; // 0x5B4\n	public GameObject MechAnimationObject; // 0x5B8\n	public GameObject[] noFillObjects; // 0x5C0\n	public int Probability; // 0x5C8\n	public float protectionEffectValue; // 0x5CC\n	public float range; // 0x5D0\n	public ItemRarity rarity; // 0x5D4\n	public int scopeNum; // 0x5D8\n	public float shootDistance; // 0x5DC\n	public WeaponSounds.不丌上三与丈上丄丂 specialEffect; // 0x5E0\n	public float speedModifier; // 0x5E4\n	public string StorageId; // 0x5E8\n	public string Tag; // 0x5F0\n	public int tier; // 0x5F8\n	private float 一丘丟丈上丝业丑七; // 0x5FC\n	private float 丟东丟丗一且丁丗丅; // 0x600\n	public bool UseImagesFromFirstUpgrade; // 0x604\n	internal string 丈丕丙丟丄丂丌丐丁; // 0x608\n	[SpaceAttribute] // RVA: 0x1D886E0 Offset: 0x1D886E0 VA: 0x1D886E0\n	public int zoomShop; // 0x610\n	public bool useLegacyIdleAnimation; // 0x614\n	public bool useLegacyWalkAnimation; // 0x615\n	public bool disableDirectionAnimation; // 0x616\n	private bool 丘丐东丗专专丈丛业; // 0x617\n	[SerializeField] // RVA: 0x1D886F4 Offset: 0x1D886F4 VA: 0x1D886F4\n	private bool is3CatSpam; // 0x618\n	[SerializeField] // RVA: 0x1D88704 Offset: 0x1D88704 VA: 0x1D88704\n	private bool for3CatSpam; // 0x619\n	private ItemRecord 丈下丞丈上丛上丏丘; // 0x620\n	private bool 丑丅不丅丕东丑丗专; // 0x628\n	private int 丝丟与丝丄一丙东不; // 0x62C\n	private int 一丕丆丐丘丌且丐丅; // 0x630\n	private Nullable<ItemRarity> 丒专万且丑万一丈世; // 0x634\n	private float 丄丌一丁丝一丏丝丆; // 0x63C\n	private float 丕与丌东丝丐丂与下; // 0x640\n	private Renderer[] 专与丛上下丄丒丈与; // 0x648\n	private Animation 丘丞丆丝丛下丂丄七; // 0x650\n	[CompilerGeneratedAttribute] // RVA: 0x1D88714 Offset: 0x1D88714 VA: 0x1D88714\n	private WeaponAnimParticleEffects <丕丄且丙且丟丁丞丛>k__BackingField; // 0x658\n	private Transform 丏丆丏丑下丐东七丐; // 0x660\n	private string 三丈与丒上丗丈丝丕; // 0x668\n	private float 丁丐丆一丏专不丒与; // 0x670\n	private bool 东丅丘东三业专丙世; // 0x674\n\n	// Properties\n	[TupleElementNamesAttribute] // RVA: 0x1E2CA20 Offset: 0x1E2CA20 VA: 0x1E2CA20\n	internal static Dictionary<WeaponSounds.东下丙与与丑丕不丘, ValueTuple<string, string, string>> 丘丟丐丛与丏且丞丈 { get; }\n	internal bool 丄东丅丕丆丞丄丒丒 { get; }\n	public float 丐下丘专丛万丒丙丟 { get; }\n	internal bool 丈与七专业丁万丛丂 { get; }\n	internal float 丗七丝专且一万丞丗 { get; }\n	public int 东下丟下丘与丈不丅 { get; }\n	public float 丅下世丒专丌丅丄不 { get; }\n	public float 上下丝丞丘丗丅东七 { get; }\n	public bool 丅万丕丒与上万丏丛 { get; }\n	public float 丂下丐一丗丘上丒业 { get; }\n	public float 丝不上丏丄丐丈一三 { get; }\n	internal float 与丙丏不万七丛丝业 { get; }\n	internal MinigunController 专丅丝且三上丘一丅 { get; set; }\n	internal GunBonesRotatorController 业丄世丌一丐丌丗世 { get; set; }\n	public bool 丅丁专上丄不上不丘 { get; }\n	internal WeaponReloadEffect 三专丒丞不丏丄万丆 { get; }\n	internal WeaponSecondTimeFireAction 七丆世丙七丁丞与丕 { get; }\n	internal WeaponChargeShield 七丒丅丈丑丘丘下丐 { get; }\n	internal bool 丏七专丈一丑万丒丄 { get; set; }\n	internal int 丐万丂七七丟丟世丅 { get; }\n	internal bool 丌东专专一一与上丁 { get; }\n	internal bool 万丆且丄丞丂上万丑 { get; }\n	internal float 丈丛丘七丕一丆丙丟 { get; }\n	internal Dictionary<int, float> 丘丙三丛专一万丗丙 { get; }\n	public float 丁丁丘丆东丂丗不丏 { get; }\n	internal bool 与丘丁丕三丅丑万丅 { get; }\n	internal float 丆丁七丟丒丞与丘丈 { get; }\n	internal ItemRecord 与丞一丐丗丐丞下三 { get; }\n	public int 丙丅且丒下下丛一丆 { get; }\n	internal float 丝世丅丄专丌不丐丟 { get; }\n	internal float 丝丛万业与丝丑丏丗 { get; }\n	internal float 丗丕三丗丁业业丁丒 { get; }\n	internal float 丕三丘不丆且丁丈丏 { get; }\n	public float 东丞且下专丘三丕丂 { get; }\n	internal float 万三三丘不丝与丂丑 { get; }\n	internal float 丏下丁丌不丆一且丈 { get; }\n	internal GameObject 丘丗丑七世一丌三丆 { get; }\n	private SkinnedMeshRenderer[] 丛丑世上丏三万丒一 { get; }\n	private Renderer[] 专世丗业世丆丒丄一 { get; }\n	internal GameObject 丗丞业万丐丟丑七丘 { get; }\n	internal Animation 与且丛丗丁世丂丌丈 { get; }\n	internal Texture 下下丕丄丕丝世三丕 { get; }\n	internal AudioClip 七世上东一七东丝丙 { get; }\n	internal AudioClip 丅不业丅专三业上下 { get; }\n	internal AudioClip 丅不丂丅丒丄丗丒七 { get; }\n	internal AudioClip 丞丟丄不丙丟三上丌 { get; }\n	internal AudioClip 下丈业丟丂丐东业丆 { get; }\n	internal AudioClip 丌丏丏丑且丟一丌丘 { get; }\n	internal AudioClip 三丁丘丄不一丄东且 { get; }\n	internal AudioClip 丆丗丄丆万丂丒丒丌 { get; }\n	internal AudioClip 丛丏丟丂丞丒丒丁下 { get; }\n	internal AudioClip 丈丝丑丗万专一东丄 { get; }\n	internal AudioClip 丛丕丅不丛且丌丏丑 { get; }\n	internal GameObject 丑丁丌上丆七丈丞一 { get; }\n	internal GameObject 一丐东且丕且下丑丛 { get; }\n	internal Transform 专丛七丄丅丅与丂丝 { get; }\n	internal Transform 丐丕丛丝业丂丈丕丕 { get; }\n	internal Transform 业丁丒丂不丑不业丕 { get; }\n	internal Transform[] 世一丈丕丈丕丘丅万 { get; }\n	public InnerWeaponPars 一丐业丞丐且丕丅世 { get; }\n	internal WeaponAnimParticleEffects 万丛东且丏丏且万丞 { get; set; }\n	internal float 万丁丈丄世丕丌与丌 { get; }\n	internal bool 业丅丅丟世丕三丏丑 { get; }\n	internal bool 丌业丁一丛丗丈一业 { get; }\n	internal bool 丅上丐世上下丅专丙 { get; }\n	internal Vector2 万丆业丑丂专万三东 { get; }\n	private float 丗丘丂丄丁丕丞丛丞 { get; }\n	private float 丞丒丒丂一丟丒丙丄 { get; }\n	private FirstPersonControlSharp 丘下丂丌丙丂丈一丄 { get; }\n	private float 丂丑东丞且万丙丈丆 { get; }\n	private float 丘丑丐东丝不丗丙一 { get; }\n	private float 万专上丞丁三丛丈丏 { get; }\n	private float 丐七业与丂业丆丆丘 { get; }\n	private float 丈丕丞丘东且丝万丘 { get; }\n	internal Player_move_c 丝丞丞业且丙丂丂且 { get; }\n	internal string 丝丐丌下丆东丐专丑 { get; }\n	private bool 丐与丛不丄东与丝世 { get; }\n	private float 专丌丟一丏丁且丘丛 { get; }\n	internal bool 下丟下丘丅业万万一 { get; }\n\n	// Methods\n\n	// RVA: 0x3837DC4 Offset: 0x3837DC4 VA: 0x3837DC4\n	internal static Dictionary<WeaponSounds.东下丙与与丑丕不丘, ValueTuple<string, string, string>> 丁万东东万丙丈下丂() { }\n\n	// RVA: 0x3837E2C Offset: 0x3837E2C VA: 0x3837E2C\n	internal bool 丗丄丘丟丆丗下上丐() { }\n\n	// RVA: 0x3837E34 Offset: 0x3837E34 VA: 0x3837E34\n	public float get_ZoomFOV() { }\n\n	// RVA: 0x3837EE8 Offset: 0x3837EE8 VA: 0x3837EE8\n	internal bool 丁不专丝业丝七丌丙() { }\n\n	// RVA: 0x3837EF0 Offset: 0x3837EF0 VA: 0x3837EF0\n	internal float 丏丂丗丝一丟世丁且() { }\n\n	// RVA: 0x3837EF8 Offset: 0x3837EF8 VA: 0x3837EF8\n	public int get_PoisonCount() { }\n\n	// RVA: 0x3838004 Offset: 0x3838004 VA: 0x3838004\n	internal bool 丗东丛丈丘丅丙世下() { }\n\n	// RVA: 0x383800C Offset: 0x383800C VA: 0x383800C\n	internal bool 丒丁丌上丂丒且丁三(bool 东世丌丑专三业专下) { }\n\n	// RVA: 0x38380E0 Offset: 0x38380E0 VA: 0x38380E0\n	public float get_AutoAimDistance() { }\n\n	// RVA: 0x383820C Offset: 0x383820C VA: 0x383820C\n	public float get_MinDistanceAutoAim() { }\n\n	// RVA: 0x38382F0 Offset: 0x38382F0 VA: 0x38382F0\n	public bool get_IsDistanceBlockOn() { }\n\n	// RVA: 0x3838368 Offset: 0x3838368 VA: 0x3838368\n	public float get_EffectiveDistance() { }\n\n	// RVA: 0x38383E0 Offset: 0x38383E0 VA: 0x38383E0\n	public float get_RadiusAutoAim() { }\n\n	// RVA: 0x3838458 Offset: 0x3838458 VA: 0x3838458\n	internal float 丞上且丅世万丄丌七() { }\n\n	[CompilerGeneratedAttribute] // RVA: 0x1DFBE40 Offset: 0x1DFBE40 VA: 0x1DFBE40\n	// RVA: 0x3838CAC Offset: 0x3838CAC VA: 0x3838CAC\n	internal MinigunController 丒丙业专与丆丗丁丏() { }\n\n	[CompilerGeneratedAttribute] // RVA: 0x1DFBE50 Offset: 0x1DFBE50 VA: 0x1DFBE50\n	// RVA: 0x3838CB4 Offset: 0x3838CB4 VA: 0x3838CB4\n	private void 专丐专丐七丆丛丝丒(MinigunController 丗专丆丑丑丛七万不) { }\n\n	[CompilerGeneratedAttribute] // RVA: 0x1DFBE60 Offset: 0x1DFBE60 VA: 0x1DFBE60\n	// RVA: 0x3838CBC Offset: 0x3838CBC VA: 0x3838CBC\n	internal GunBonesRotatorController 东丟与丞丛万丆且万() { }\n\n	[CompilerGeneratedAttribute] // RVA: 0x1DFBE70 Offset: 0x1DFBE70 VA: 0x1DFBE70\n	// RVA: 0x3838CC4 Offset: 0x3838CC4 VA: 0x3838CC4\n	private void 丒丁下专专丟丏东丈(GunBonesRotatorController 丗专丆丑丑丛七万不) { }\n\n	// RVA: 0x3838CCC Offset: 0x3838CCC VA: 0x3838CCC\n	public bool get_IsWeaponInsideHands() { }\n\n	// RVA: 0x3838CD4 Offset: 0x3838CD4 VA: 0x3838CD4\n	internal WeaponReloadEffect 丂丝丒东七世丙万丅() { }\n\n	// RVA: 0x3838CDC Offset: 0x3838CDC VA: 0x3838CDC\n	internal WeaponSecondTimeFireAction 上丂丝下万一不东丁() { }\n\n	// RVA: 0x3838CE4 Offset: 0x3838CE4 VA: 0x3838CE4\n	internal WeaponChargeShield 丁一不丅且丛业专丕() { }\n\n	[CompilerGeneratedAttribute] // RVA: 0x1DFBE80 Offset: 0x1DFBE80 VA: 0x1DFBE80\n	// RVA: 0x3838CEC Offset: 0x3838CEC VA: 0x3838CEC\n	internal bool 万丏专七丛丗丗丛三() { }\n\n	[CompilerGeneratedAttribute] // RVA: 0x1DFBE90 Offset: 0x1DFBE90 VA: 0x1DFBE90\n	// RVA: 0x3838CF4 Offset: 0x3838CF4 VA: 0x3838CF4\n	private void 丕丆丌丈万丕东丅一(bool 丗专丆丑丑丛七万不) { }\n\n	// RVA: 0x3838D00 Offset: 0x3838D00 VA: 0x3838D00\n	internal void 万且丑专丌丄万不东(丛与丑上丄丞一丁丈 丕专上上丑丄丅丘丙) { }\n\n	// RVA: 0x38390E8 Offset: 0x38390E8 VA: 0x38390E8\n	internal int 丝丞丒丙下丞丘丌丐() { }\n\n	// RVA: 0x38391B0 Offset: 0x38391B0 VA: 0x38391B0\n	internal bool 丙三丙丟丐不不丛与() { }\n\n	// RVA: 0x38392F4 Offset: 0x38392F4 VA: 0x38392F4\n	internal bool 一三万业上丟业丕丐() { }\n\n	// RVA: 0x3839394 Offset: 0x3839394 VA: 0x3839394\n	internal float 世专业世丒丟且丄丌() { }\n\n	// RVA: 0x38396C4 Offset: 0x38396C4 VA: 0x38396C4\n	internal Dictionary<int, float> 与丐丆丏丟世七丄业() { }\n\n	// RVA: 0x38396F0 Offset: 0x38396F0 VA: 0x38396F0\n	public float get_TeammateHealMultiplier() { }\n\n	// RVA: 0x38397E0 Offset: 0x38397E0 VA: 0x38397E0\n	internal bool 与下丟下与不上专与() { }\n\n	// RVA: 0x3839850 Offset: 0x3839850 VA: 0x3839850\n	internal float 下丒丆专丗上下七丞() { }\n\n	// RVA: 0x3831458 Offset: 0x3831458 VA: 0x3831458\n	internal ItemRecord 丄丝丆业专万丈丞与() { }\n\n	// RVA: 0x3839880 Offset: 0x3839880 VA: 0x3839880\n	public int get_AmmoInClip() { }\n\n	// RVA: 0x38398B0 Offset: 0x38398B0 VA: 0x38398B0\n	public void SetArmRarity() { }\n\n	// RVA: 0x3839994 Offset: 0x3839994 VA: 0x3839994\n	internal float 七上专且东丄丄丂万() { }\n\n	// RVA: 0x3839C5C Offset: 0x3839C5C VA: 0x3839C5C\n	internal float 七上万丗万专丌三与() { }\n\n	// RVA: 0x383960C Offset: 0x383960C VA: 0x383960C\n	internal float 世业丛丞丌与丙三丛() { }\n\n	// RVA: 0x38385FC Offset: 0x38385FC VA: 0x38385FC\n	internal float 与世丞丝七丆且丏上() { }\n\n	// RVA: 0x3839E24 Offset: 0x3839E24 VA: 0x3839E24\n	public float get_reloadLength() { }\n\n	// RVA: 0x3839EC4 Offset: 0x3839EC4 VA: 0x3839EC4\n	internal float 丘三丆三丝七丁丕丅(float 丙丗丘东丗丗世丛丆 = 1, float 上丆丈丏一丁且丆万 = 0, bool 七下丈且丌三丏上东 = False) { }\n\n	// RVA: 0x38389F8 Offset: 0x38389F8 VA: 0x38389F8\n	internal float 与丏丞丌丛丁丈丝丑() { }\n\n	// RVA: 0x3832234 Offset: 0x3832234 VA: 0x3832234\n	internal float 丒丞丝丁丌且三七丘() { }\n\n	// RVA: 0x383A088 Offset: 0x383A088 VA: 0x383A088\n	internal GameObject 七万万业三不与丈与() { }\n\n	// RVA: 0x383A090 Offset: 0x383A090 VA: 0x383A090\n	private SkinnedMeshRenderer[] 七丛丂业丂丞丁七丕() { }\n\n	// RVA: 0x383A0F4 Offset: 0x383A0F4 VA: 0x383A0F4\n	private Renderer[] 丆上丘七丙七丗丞一() { }\n\n	// RVA: 0x3839544 Offset: 0x3839544 VA: 0x3839544\n	internal GameObject 且不丁丐东丞丏丒上() { }\n\n	// RVA: 0x383A1F0 Offset: 0x383A1F0 VA: 0x383A1F0\n	internal Animation 丞下专业丒七专世丕() { }\n\n	// RVA: 0x383A32C Offset: 0x383A32C VA: 0x383A32C\n	internal Texture 丗七三丟世丞丁上上() { }\n\n	// RVA: 0x383A3D0 Offset: 0x383A3D0 VA: 0x383A3D0\n	internal AudioClip 下丒七丅丝丘丝万丄() { }\n\n	// RVA: 0x383A518 Offset: 0x383A518 VA: 0x383A518\n	internal AudioClip 丙丄丟一与丗业三丌() { }\n\n	// RVA: 0x383A660 Offset: 0x383A660 VA: 0x383A660\n	internal AudioClip 与丟与上丕丆万不下() { }\n\n	// RVA: 0x383A7A8 Offset: 0x383A7A8 VA: 0x383A7A8\n	internal AudioClip 丟下上丌丌七一丞丅() { }\n\n	// RVA: 0x383A8F0 Offset: 0x383A8F0 VA: 0x383A8F0\n	internal AudioClip 一丝丄丙丝丟丏丗专() { }\n\n	// RVA: 0x383A994 Offset: 0x383A994 VA: 0x383A994\n	internal AudioClip 丝万东不丅业三世丌() { }\n\n	// RVA: 0x383AA38 Offset: 0x383AA38 VA: 0x383AA38\n	internal AudioClip 与丝下丂丄上丌丄丆() { }\n\n	// RVA: 0x383AB38 Offset: 0x383AB38 VA: 0x383AB38\n	internal AudioClip 不丆丞丌专丈东丕丑() { }\n\n	// RVA: 0x383ABDC Offset: 0x383ABDC VA: 0x383ABDC\n	internal AudioClip 万丁丏丝丏丗丆丗世() { }\n\n	// RVA: 0x383AC80 Offset: 0x383AC80 VA: 0x383AC80\n	internal AudioClip 不专三丗丏与丌丏丄() { }\n\n	// RVA: 0x383AD24 Offset: 0x383AD24 VA: 0x383AD24\n	internal AudioClip 丆丏与丙丙丄丂丝丝() { }\n\n	// RVA: 0x3839044 Offset: 0x3839044 VA: 0x3839044\n	internal GameObject 丆万丘不丄丗丛丑丛() { }\n\n	// RVA: 0x383ADC8 Offset: 0x383ADC8 VA: 0x383ADC8\n	internal GameObject 丟不丅丗丗丗丏七丐() { }\n\n	// RVA: 0x383AE6C Offset: 0x383AE6C VA: 0x383AE6C\n	internal Transform 与丅丂下丝一丘上世() { }\n\n	// RVA: 0x383AF10 Offset: 0x383AF10 VA: 0x383AF10\n	internal Transform 一上丑丞与且丘专丘() { }\n\n	// RVA: 0x383AFB4 Offset: 0x383AFB4 VA: 0x383AFB4\n	internal Transform 丛丁丛且丟且不丕丅() { }\n\n	// RVA: 0x383B0B4 Offset: 0x383B0B4 VA: 0x383B0B4\n	internal Transform[] 东且世丅丘万丌一万() { }\n\n	// RVA: 0x383A158 Offset: 0x383A158 VA: 0x383A158\n	public InnerWeaponPars get__innerPars() { }\n\n	[CompilerGeneratedAttribute] // RVA: 0x1DFBEA0 Offset: 0x1DFBEA0 VA: 0x1DFBEA0\n	// RVA: 0x383B158 Offset: 0x383B158 VA: 0x383B158\n	internal WeaponAnimParticleEffects 不丙丟万丑丐万丁专() { }\n\n	[CompilerGeneratedAttribute] // RVA: 0x1DFBEB0 Offset: 0x1DFBEB0 VA: 0x1DFBEB0\n	// RVA: 0x383B160 Offset: 0x383B160 VA: 0x383B160\n	private void 不丄丂丙丘丈上丐丕(WeaponAnimParticleEffects 丗专丆丑丑丛七万不) { }\n\n	// RVA: 0x383B168 Offset: 0x383B168 VA: 0x383B168\n	internal float 丈世下业丙七丈丐丌() { }\n\n	// RVA: 0x383B264 Offset: 0x383B264 VA: 0x383B264\n	internal bool 丄业丒丘万丒丞丒专() { }\n\n	// RVA: 0x383B280 Offset: 0x383B280 VA: 0x383B280\n	internal bool 不业万丘丌世专丁丆() { }\n\n	// RVA: 0x383B278 Offset: 0x383B278 VA: 0x383B278\n	internal bool 丒东丕丆丝丑东丌丞() { }\n\n	// RVA: 0x383B390 Offset: 0x383B390 VA: 0x383B390\n	internal Vector2 业丂一丘丞世丅丙世() { }\n\n	// RVA: 0x383B688 Offset: 0x383B688 VA: 0x383B688\n	private float 丛三丈世丅丟丒上丄() { }\n\n	// RVA: 0x383BCF4 Offset: 0x383BCF4 VA: 0x383BCF4\n	private float 丁丕上丒丘专专专专() { }\n\n	// RVA: 0x383BEDC Offset: 0x383BEDC VA: 0x383BEDC\n	private FirstPersonControlSharp 且七丈丄丌不丞丂下() { }\n\n	// RVA: 0x383BD70 Offset: 0x383BD70 VA: 0x383BD70\n	private float 丐业丙专万丄下一三() { }\n\n	// RVA: 0x383BE8C Offset: 0x383BE8C VA: 0x383BE8C\n	private float 丝下丁丈七七丞丘七() { }\n\n	// RVA: 0x383C020 Offset: 0x383C020 VA: 0x383C020\n	private float 丛丕不上丞丁丌丟丗() { }\n\n	// RVA: 0x383C0F4 Offset: 0x383C0F4 VA: 0x383C0F4\n	private float 与丏一一丙下世丘丑() { }\n\n	// RVA: 0x383C1E4 Offset: 0x383C1E4 VA: 0x383C1E4\n	private float 丑丅一专丑不下丟万() { }\n\n	// RVA: 0x38312A0 Offset: 0x38312A0 VA: 0x38312A0\n	internal Player_move_c 业七丝东不世且三且() { }\n\n	// RVA: 0x38323C8 Offset: 0x38323C8 VA: 0x38323C8\n	internal string 丟专专丈丌丆业丙丄() { }\n\n	// RVA: 0x383C2D0 Offset: 0x383C2D0 VA: 0x383C2D0\n	internal void 丂丒丅东丂丕丒丑丁(bool 丁世东丂丙丅丏丝丕) { }\n\n	// RVA: 0x383C3D8 Offset: 0x383C3D8 VA: 0x383C3D8\n	internal void 丙三丝丂世丑专丈丁(bool 万丕丁丏丈丞丛下丌) { }\n\n	// RVA: 0x383C520 Offset: 0x383C520 VA: 0x383C520\n	private void Awake() { }\n\n	// RVA: 0x383CAF0 Offset: 0x383CAF0 VA: 0x383CAF0\n	private void OnDestroy() { }\n\n	// RVA: 0x383CC4C Offset: 0x383CC4C VA: 0x383CC4C\n	private void Start() { }\n\n	// RVA: 0x383CDAC Offset: 0x383CDAC VA: 0x383CDAC\n	internal void 丕丄丆丝丏丝与丐丅() { }\n\n	// RVA: 0x383CF00 Offset: 0x383CF00 VA: 0x383CF00\n	private bool 丌一七丘丌丑专丕丅() { }\n\n	// RVA: 0x383CFD8 Offset: 0x383CFD8 VA: 0x383CFD8\n	private void Update() { }\n\n	// RVA: 0x383DBD0 Offset: 0x383DBD0 VA: 0x383DBD0\n	internal void 丒丛丗丕上丝丅丈丂() { }\n\n	// RVA: 0x383DCA8 Offset: 0x383DCA8 VA: 0x383DCA8\n	private void LateUpdate() { }\n\n	// RVA: 0x383DCAC Offset: 0x383DCAC VA: 0x383DCAC\n	internal void 丐与丂东且世一丂七() { }\n\n	// RVA: 0x383DA24 Offset: 0x383DA24 VA: 0x383DA24\n	private void 丆丂一万丌业三丙万() { }\n\n	// RVA: 0x383B964 Offset: 0x383B964 VA: 0x383B964\n	private float 世丌上丝七专七丙丂() { }\n\n	// RVA: 0x383DE6C Offset: 0x383DE6C VA: 0x383DE6C\n	internal void 丄丟丂丅丏丈丑丑上() { }\n\n	// RVA: 0x383E090 Offset: 0x383E090 VA: 0x383E090\n	public bool NextHitCritical() { }\n\n	// RVA: 0x383E098 Offset: 0x383E098 VA: 0x383E098\n	public void SetNextHitCritical(bool 丏世丒与丈七一且丅) { }\n\n	// RVA: 0x383E0A4 Offset: 0x383E0A4 VA: 0x383E0A4\n	internal bool 三七丝丑丟丒万丏上() { }\n\n	// RVA: 0x383E120 Offset: 0x383E120 VA: 0x383E120\n	internal List<GameObject> 丘丞丒丗丛上东丅丝() { }\n\n	// RVA: 0x383E230 Offset: 0x383E230 VA: 0x383E230\n	internal void 丕丏不丁丛丕丈七一() { }\n\n	// RVA: 0x3832264 Offset: 0x3832264 VA: 0x3832264\n	internal bool 上丞丄丙丝世丙丂丛() { }\n\n	// RVA: 0x383E23C Offset: 0x383E23C VA: 0x383E23C\n	internal bool 东丅丕与三丒丈丐丘() { }\n\n	// RVA: 0x383E264 Offset: 0x383E264 VA: 0x383E264\n	internal float 七丒丕丈丗丂丏丅丏() { }\n\n	// RVA: 0x383E380 Offset: 0x383E380 VA: 0x383E380\n	internal bool 东丛丗丌丛丒且丙丕() { }\n\n	// RVA: 0x383D6F0 Offset: 0x383D6F0 VA: 0x383D6F0\n	private void 丙丈上七上丂丕东丛() { }\n\n	// RVA: 0x383E388 Offset: 0x383E388 VA: 0x383E388\n	public void .ctor() { }\n\n	// RVA: 0x383E8E8 Offset: 0x383E8E8 VA: 0x383E8E8\n	private static void .cctor() { }\n}"
#a = getmethods(getfullmethods(a))
#b = "gg.setVisible(false)\ngg.setRanges(gg.REGION_CODE_APP)"
#for i in a:
#    if "int" in i["Type"] or "float" in i["Type"] or "bool" in i["Type"]:
#        b = b + "\ngg.clearResults()\ngg.searchNumber('h " + offsettohex(i["Offset"],r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.5.0/libil2cpp.so",40) + "',gg.TYPE_BYTE)\ngg.getResults(8)\ngg.editAll('h "
#        if "bool" in i["Type"]:
#            b = b + "20 00 80 D2"
#        elif "int" in i["Type"]:
#            b = b + "40 06 80 52"
#        elif "float" in i["Type"]:
#            b = b + "40 06 80 52"
#        b = b + " C0 03 5F D6',gg.TYPE_BYTE)"
#print(b)
#print(getmetadatafromapk(r"C:\Users\zachy\OneDrive\Documents\APK Easy Tool\1-Decompiled APKs\Pixel Gun 3D 16.6.1 Armv7","path"))
#print("\n")
#print(formatlist(fulllog,2))
#print(getmetadatafromapk(r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 16.6.1/Pixel Gun 3D 16.6.1 Armv7.apk","path"))
#a = "// Namespace: \ninternal static class 一丐世丟丒丞丄与世 // TypeDefIndex: 13480\n{\n	// Fields\n	private static float 丘与丆且丁专丅丁丛; // 0x0\n	[CompilerGeneratedAttribute] // RVA: 0x1D85380 Offset: 0x1D85380 VA: 0x1D85380\n	private static Dictionary<string, float> <世丝丒丂丝与一丐不>k__BackingField; // 0x8\n	private static bool 世丝丄丑丁丆丄三业; // 0x10\n\n	// Properties\n	internal static Dictionary<string, float> 丞丂业丅丐三丁七丞 { get; set; }\n	private static bool 业丁丈丑丟丝丘丟世 { get; }\n	internal static string 丝丟三丌丁七三不丈 { get; }\n	internal static string 丗丑丞七万业丏丈丞 { get; }\n	internal static string 丌上丌丆上与丘丘丘 { get; }\n	internal static string 丟丟丛世不万且万丙 { get; }\n	internal static string 丁且丈丌丁丁丙丏与 { get; }\n	internal static bool 七不丝三世丑丂不丐 { get; set; }\n	internal static float 丟上丆丕丛丕专丗与 { get; set; }\n	internal static float 万丌不丈丂丈东丂丄 { get; }\n	internal static bool 丈万七与丙与下丆丁 { get; }\n	internal static bool 一丅丞丘专丌丒业丌 { get; }\n	internal static float 丏丙丝丆丄下丐不丗 { get; }\n	internal static float 丛丌世丆丁业且丈丈 { get; }\n	internal static float 丄丘丂丗丘丈与丘丞 { get; }\n	internal static float 与下万且丑丁东三与 { get; }\n	internal static float 丗丕与丆丘不丂万专 { get; }\n	internal static bool 丄下丛丌不丁业七丟 { get; }\n	internal static float 三且丂丏丄业丐与丏 { get; }\n	internal static float 丈七丟丈一与一一丑 { get; }\n	internal static bool 丅丂下丈一不丌丑丒 { get; }\n	internal static bool 丐丕丑丐专上丂丅丅 { get; }\n	internal static bool 丝万万七七丕不丒东 { get; }\n	internal static bool 一丐丅丈丈丕丆业世 { get; }\n	internal static bool 丑丑丆丂万万丆丕丂 { get; }\n	internal static bool 万丝丈专三丌业丏丞 { get; }\n	internal static bool 不且下丐丈丂七丗业 { get; }\n	internal static bool 世万丗上世丅丁三丕 { get; }\n	internal static bool 丛丞丒一上丂丘丌三 { get; }\n	internal static bool 丗与丂丗丆丈丌万万 { get; }\n	internal static bool 丞东专东一丆丌丁丟 { get; }\n	internal static bool 丙丕一丈一丐丐丏三 { get; }\n	internal static bool 丂丙丅与丑丙且丁丞 { get; }\n	internal static bool 丛丌丄下业丒丂丝丂 { get; }\n	private static bool 与东丒不丅丙万丘丂 { get; }\n\n	// Methods\n\n	// RVA: 0x4095680 Offset: 0x4095680 VA: 0x4095680\n	private static void .cctor() { }\n\n	[CompilerGeneratedAttribute] // RVA: 0x1DF9AC4 Offset: 0x1DF9AC4 VA: 0x1DF9AC4\n	// RVA: 0x4095A90 Offset: 0x4095A90 VA: 0x4095A90\n	internal static Dictionary<string, float> 业世丞丙丆万丙东丛() { }\n\n	[CompilerGeneratedAttribute] // RVA: 0x1DF9AD4 Offset: 0x1DF9AD4 VA: 0x1DF9AD4\n	// RVA: 0x4095A24 Offset: 0x4095A24 VA: 0x4095A24\n	private static void 丟下业三下万万下下(Dictionary<string, float> 丗专丆丑丑丛七万不) { }\n\n	// RVA: 0x4095AF8 Offset: 0x4095AF8 VA: 0x4095AF8\n	private static bool 丁丂丞丁丗业丐一丄() { }\n\n	// RVA: 0x4095C54 Offset: 0x4095C54 VA: 0x4095C54\n	internal static string 上与丏丁世丈丝丐丟() { }\n\n	// RVA: 0x4095D48 Offset: 0x4095D48 VA: 0x4095D48\n	internal static string 丌万丕世丒丑丛东世() { }\n\n	// RVA: 0x4095E3C Offset: 0x4095E3C VA: 0x4095E3C\n	internal static string 上丏下丄世上专丙丆() { }\n\n	// RVA: 0x4095F30 Offset: 0x4095F30 VA: 0x4095F30\n	internal static string 丝七上丅且丅三一丏() { }\n\n	// RVA: 0x4096024 Offset: 0x4096024 VA: 0x4096024\n	internal static string 东且丑专丁且丈丈丝() { }\n\n	// RVA: 0x40960C4 Offset: 0x40960C4 VA: 0x40960C4\n	internal static bool 上丗丗与丗丝丑丏丆() { }\n\n	// RVA: 0x409612C Offset: 0x409612C VA: 0x409612C\n	internal static void 不丕三丅丈丅丛七丝(bool 丗专丆丑丑丛七万不) { }\n\n	// RVA: 0x409619C Offset: 0x409619C VA: 0x409619C\n	internal static float 丞一上丕丕丅丞丙丅() { }\n\n	// RVA: 0x4096204 Offset: 0x4096204 VA: 0x4096204\n	internal static void 且丁下丙丝七丂世丗(float 丗专丆丑丑丛七万不) { }\n\n	// RVA: 0x4096324 Offset: 0x4096324 VA: 0x4096324\n	internal static float 丆丞丘丟丞丛专三丈() { }\n\n	// RVA: 0x4096EF4 Offset: 0x4096EF4 VA: 0x4096EF4\n	internal static bool 专丝不丝丗世丞丕丂() { }\n\n	// RVA: 0x4096F74 Offset: 0x4096F74 VA: 0x4096F74\n	internal static bool 世丟且万丐丆与丏丘() { }\n\n	// RVA: 0x409775C Offset: 0x409775C VA: 0x409775C\n	internal static float 丄丂丄丙丑丈丞丌一() { }\n\n	// RVA: 0x4097B10 Offset: 0x4097B10 VA: 0x4097B10\n	internal static float 丅丝丄丏丕丝与丐下() { }\n\n	// RVA: 0x4097D04 Offset: 0x4097D04 VA: 0x4097D04\n	internal static float 丏丝丛丏万丙业丌丈() { }\n\n	// RVA: 0x4097D8C Offset: 0x4097D8C VA: 0x4097D8C\n	internal static float 万丛丐东丂丅丑业三() { }\n\n	// RVA: 0x4097F8C Offset: 0x4097F8C VA: 0x4097F8C\n	internal static float 上丐丆业丆丐与丝丗() { }\n\n	// RVA: 0x40984B8 Offset: 0x40984B8 VA: 0x40984B8\n	internal static bool 世丕丘丄世丆世丏世() { }\n\n	// RVA: 0x409875C Offset: 0x409875C VA: 0x409875C\n	internal static float 丌丛丙不丟丅一丆丛() { }\n\n	// RVA: 0x4098E64 Offset: 0x4098E64 VA: 0x4098E64\n	internal static float 丒丆专丑丗丆与丗丞() { }\n\n	// RVA: 0x40998D4 Offset: 0x40998D4 VA: 0x40998D4\n	internal static bool 丕业丄丞丆丛专且丑() { }\n\n	// RVA: 0x409993C Offset: 0x409993C VA: 0x409993C\n	internal static bool 丌丌且丙丗丈丄业丒() { }\n\n	// RVA: 0x40999A4 Offset: 0x40999A4 VA: 0x40999A4\n	internal static float 丟丄丙丒丗丂丗与七(int 丌丂丅丑丗且丌丞丑) { }\n\n	// RVA: 0x4099E48 Offset: 0x4099E48 VA: 0x4099E48\n	internal static float 业丕丟丑丏上丌一万(int 丞丕不不丘丗丟丄丈) { }\n\n	// RVA: 0x409A67C Offset: 0x409A67C VA: 0x409A67C\n	internal static float 丈专丙丅丕丌丄专下(int 丌丂丅丑丗且丌丞丑) { }\n\n	// RVA: 0x409A760 Offset: 0x409A760 VA: 0x409A760\n	internal static float 丙丐丅上七丒与丑业() { }\n\n	// RVA: 0x409A7F4 Offset: 0x409A7F4 VA: 0x409A7F4\n	internal static float 丝东下下丂丞上丕丟() { }\n\n	// RVA: 0x409A888 Offset: 0x409A888 VA: 0x409A888\n	internal static float 下丕丅下世且一东七() { }\n\n	// RVA: 0x409A91C Offset: 0x409A91C VA: 0x409A91C\n	internal static float 丁一不一万下丗丗世(int 丂丏丄且丂专业万丟) { }\n\n	// RVA: 0x409C4A4 Offset: 0x409C4A4 VA: 0x409C4A4\n	internal static float 丌丐专下丘一丑不丞(int 丂丏丄且丂专业万丟) { }\n\n	// RVA: 0x409C53C Offset: 0x409C53C VA: 0x409C53C\n	internal static float 一丆丘与业东丅与丟(string 丗下丏三东七丞专东) { }\n\n	// RVA: 0x409C9B0 Offset: 0x409C9B0 VA: 0x409C9B0\n	internal static float 与万丌专一一不丌丘(WeaponSounds 丅丏丆丆且丒世上丁, string 丗丑丞七万业丏丈丞, string 丌上丌丆上与丘丘丘, string 丟丟丛世不万且万丙) { }\n\n	// RVA: 0x409CF00 Offset: 0x409CF00 VA: 0x409CF00\n	internal static float 丐丘丗丞专丒一丟丝(int 丞下丛丆万与且丘丒) { }\n\n	// RVA: 0x409D6EC Offset: 0x409D6EC VA: 0x409D6EC\n	internal static float 丙东丟丁东丘丆七丞(int 不丏丞丗丞三丅丄丝, string 丗丑丞七万业丏丈丞, string 丌上丌丆上与丘丘丘, string 丟丟丛世不万且万丙) { }\n\n	// RVA: 0x409DBBC Offset: 0x409DBBC VA: 0x409DBBC\n	internal static float 丙业下丄丕且丝丙三() { }\n\n	// RVA: 0x409DC2C Offset: 0x409DC2C VA: 0x409DC2C\n	internal static float 世丈丂丑丝丘丂丛专() { }\n\n	// RVA: 0x409DC9C Offset: 0x409DC9C VA: 0x409DC9C\n	internal static float 下丙万丆丗丝专丙丝() { }\n\n	// RVA: 0x409DD0C Offset: 0x409DD0C VA: 0x409DD0C\n	internal static float 丈上丁丏丂丁东专丄() { }\n\n	// RVA: 0x409E074 Offset: 0x409E074 VA: 0x409E074\n	internal static float 丙丄专七丌丛丙丏三() { }\n\n	// RVA: 0x409E168 Offset: 0x409E168 VA: 0x409E168\n	internal static bool 专一丄丛丏丗下丄三() { }\n\n	// RVA: 0x409E250 Offset: 0x409E250 VA: 0x409E250\n	internal static bool 丑上丒且一丕三业一() { }\n\n	// RVA: 0x409E338 Offset: 0x409E338 VA: 0x409E338\n	internal static bool 丘丗丆丗不丘丐上且() { }\n\n	// RVA: 0x409E420 Offset: 0x409E420 VA: 0x409E420\n	internal static bool 丆丐世丕万专丑丌丑() { }\n\n	// RVA: 0x409E508 Offset: 0x409E508 VA: 0x409E508\n	internal static bool 丞丞丒东东万丞丞丙() { }\n\n	// RVA: 0x409E5F0 Offset: 0x409E5F0 VA: 0x409E5F0\n	internal static bool 丁世丝丝一一世丘丐() { }\n\n	// RVA: 0x409E698 Offset: 0x409E698 VA: 0x409E698\n	internal static bool 丏丙东不七丑丒且丄() { }\n\n	// RVA: 0x409E740 Offset: 0x409E740 VA: 0x409E740\n	internal static bool 丈丙丅丄三丘且丈丆() { }\n\n	// RVA: 0x409E7E8 Offset: 0x409E7E8 VA: 0x409E7E8\n	internal static bool 且丄东专业与万丈万() { }\n\n	// RVA: 0x409E890 Offset: 0x409E890 VA: 0x409E890\n	internal static bool 丒丟一一丄丈丁与丑() { }\n\n	// RVA: 0x409E938 Offset: 0x409E938 VA: 0x409E938\n	internal static bool 丝丆万丝丂丌丛下丞() { }\n\n	// RVA: 0x409E9E0 Offset: 0x409E9E0 VA: 0x409E9E0\n	internal static bool 丆丙丄不业丝七万七() { }\n\n	// RVA: 0x4096E2C Offset: 0x4096E2C VA: 0x4096E2C\n	private static bool 一丟丞丆丗专专且丄() { }\n}"#deobfuscateallclassesdemo()
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
