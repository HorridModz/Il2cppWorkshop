# Il2cppWorkshop
Contact me on discord: User123456789#6424 or User123456789#8073.
A WIP opensource mega-tool for modding il2cpp games including deobfuscation, script generation, cloud file sharing, arm hex conversion, and more!
Inspired by [Il2cppInspector](https://github.com/djkaty/Il2CppInspector)
Made in python, will maybe be ported to c++ or other languages eventually
I am aware that the code is very messy and inefficient. This is only a WIP and nothing is final. I am trying to make functionality and maintain motivation.

# Goals:
These are meant as notes for myself, sorry they are so messy

Macro / Plugin System: You can code plugins /macros in any language, or make them with the plugin / macro maker GUI! You can set the program to perform your own routine with user inputs. Basically, you write your own program, made of of some of your own code and some il2cppworkshop functions. Similar to il2cpp plugin system. EX: Auto-updating hex patch script: Tell user to input apk file path, then dump, deobfuscate a set class and method by comparing with a set unobfuscated dump.cs, and create a hex patch script using your set options. Plugins / macros can also be uploaded and downloaded via the cloud contribution system.
Infinite loop protection: These program has multiple defenses against it getting stuck in infinite loops. There is an error system, where the code checks for errors and can log the error to the console and / or visually display the error, and some errors will cause it to forcefully terminate. There is also a warning system, and a log system so you can find what went wrong. There are debugging tools and live analytics, helping you know when the program is stuck and why. In addition, loops don't just run and delay everything else: Some loops have abort systems, log things, and check if they are stuck in an infinite loop.
Cloud backup system: Backup the program data to the cloud, so you do not lose your progress / data! Each ip address has their own backup folder. Make sure you do not use a vpn, and you have a static ip address, or this backup will not sync. OR maybe there will be a username and return "Not Done"word or token system. You can choose to manually backup, and automatic backups may be available from time to time, depending on the capabilities of the server hosting.
Iport your own files, or choose from one of the existing ones. Maybe even a cloud system where people can upload files for others?
Cloud contribution system: Want to help yourself, and others? When you are done with a task, you can choose to upload the result (deobfuscated things, hex values, dump files, gameguardian scripts, etc.) to the cloud. You can upload it with a custom name. After uploading, you can access these files by searching for them in the cloud database - this way you never lose them. Even better, others can also access these files! You can also upload notes files (such as repositories of methods) to the cloud for others to use. You can also upload checkpoints, so everyone can help contribute to big and time-consuming tasks. You can also upload useful files with apks and dump.cs files. This system also supports the cloud plugin upload / download system.
Brute Force Deobfuscation (Comparitive Deobfuscation) (Differential Analysis Deobfuscation): A deobfuscation method that works by comparing unobfuscated and obfuscated dump.cs. It finds the class or member etc. by name. Then, it takes the class, and replaces the names and dynamic values with a certain string ('offset','methodname','classname','comment',etc.). This way, things such as data types, params, # of methods and fields, etc. can be compared. It then converts this into lists of methods, and each method has its method type, and the method params. Same is done on fields and class itself. There is a strikes system with a customizable strictness. It can automatically adapt by narrowing down the perfect strictness by moving it up and down and seeing how little results it can get while still getting results (the toggleable smart mode, changeable in settings or function parameters). This method takes a long time.
Regex search deobfuscation (String search deobfuscation): This method is faster, simpler, and better. Both are useful though. This method finds unchanging string (such as <int,float> and private readonly Dictionary<) by searching strings until it finds one with low occurences (like 300 or less), and it finds the one with the lowest. It can also remove names / dynamic values and uses regex search. It can also use the renamer to remove changing things. Then it sees if this comes up in obfuscated. It uses brute force deobfuscation on the resulting classes methods etc. This is done until the right one is found.
Mutual Name Deobfuscation (Cross Reference Deobfuscation): This deobfuscation method is kind of like string search deobfuscation. It searches for the name you want to deobfuscate and finds other instances of the name, either as parameters in methods, methods with the same name in other classes, or fields with the same name in other classes. It tries to find one of these where the method or class is unobfuscated, or known through previous deobfuscation. Then, it goes to this class and used brute force deobfuscation to find the right method or field.
String Count Deobfuscation: This deobfuscation method is kind of like regex search and mutual name deobfuscation. It compares the number of occurences of a name, string, or regex between game versions.
Same Name Deobfuscation: In some games, such as pixel gun 3d, different obfuscated names with the same original names will have the same obfuscated names. This is probably caused by manual find-and-replace-ing. This can be forced by the user, or detected by the program when it finds this out via another form of deobfuscation. When activated, this mode simply finds and replaces text, the same way the names were likely obfuscated - but reversed. This only occurs in weak obfuscation by foolish developers, so don't expect to get lucky with it!
Pattern Search Deobfuscation (AOB Deobfuscation): This deobfuscation methods generates aob for an unobfuscated class, method, field, etc., then searches for the aob in the new game version.
Deobfuscation by name: Put in the name of a method, class, field, etc. and the program attempts to deobfuscate it by comparing unobfuscated and obfuscated dump.cs. Make sure you have get_ or set_ in front of some methods! If a method is not the found, the program looks for it with get_, and if still not, it looks for it with set_.
Finding by name: Put in the name of a method, field, class etc., and the program will try to find more details about it. You can choose what details you want. Details include, fields of class, methods of class, class type, parameter of method, type of field or method, etc. 
Auto Deobfuscation: Uses brute force deobfuscation to try to deobfuscate as much as it can, all at once. Failed methods and classes etc. try to use other two methods.
Beebyte deobfuscation: This project has built-in beebyte deobfuscation with GUI thanks to beebyte deobfuscator. It is not as easy to use or reliable!
AU deobfuscator (Only for mac / linux): This project has built-in deobfuscation with GUI thanks to au deobfuscator. It only works on mac / linux. You need to first dump the game to get the dummy dll, use il2cppinspector to decompile the dll, and get the  il2cpp-types.h and il2cpp-types-ptr.h files. It is not as easy to use or reliable!
Saves work: The project saves deobfuscated names, files, script workshop sessions, etc. and restores them next time. You can also store things in the cloud, for yourself and others!
Task close and resume: Time-consuming tasks like deobfuscation will have checkpoints saved every minute. These checkpoints have almost no effect on storage space or speed (they are usually only kilobytes long). They do not fill up your files, as they are in their own folder in the program's data and each checkpoint replaces the previous one's file, rather than deleting it. You can resume from your checkpoint by going to settings. You will automatically be prompted whether you would like to or not when you restart the project (there is a yes, no, and do not ask again dialog). You can also delete these checkpoints, or import checkpoints from others to finish the job for you. You can disable
Adort button: If you would like to cancel something, click the abort button in the GUI. This will close and save the progress of currently running tasks.
Checkpoint button: There is also a button to manually create checkpoints (see task close and resume).
Hex patching tools: Method to offset, offset to hex, hex to offset, etc.
Direct hex patching: Directly modify lib files by offset or hex value. You can also replace all hex values that match. You can also use numbers.
Dump.cs and lib file analysis: Generate hex patch gameguardian scripts, find methods, search for numbers and strings, go to offsets, and more in files like libil2cpp. This is basically a hex editor (with GUI!). Inspired by HxD Workshop (HxD Hex Editor).
Name remover: This features removes all names in dump.cs of unobfuscated and obfuscated. It also removes dynamic things such as offsets. This way, things match up. This is also useful for unobfuscated things, because it removes dynamic things. It can be used for things such as deobfuscating and auto-updating.
Renamer: Inspired by de4dot, this feature replaces names and / or things like offsets and comments with clearer names. For example, obfuscated functions can be renamed.
Gameguardian script generator: Can generate custom gg lua scripts for things such as hex patch scripts.
Gameguardian Script workshop: UI for making scripts and pieces of scripts such as menus, hex patches, and http requests. Can also modify gg scripts to implement passwords, encryption, anti-log, etc. - and of course, it can decrypt, decompile, etc. scripts as well!
Mod menu workshop: UI for generating mod menu code
Arm hex converter: Convert arm assembly code for hex opcodes for arm64, armv7, and thumb back and forth. Also, have ret values as an option (just type value u want to ret and it generated hex code). You can also convert hex values into numbers (useful for gameguardian).
Easilly get useful files: Can get files such as metadata, libil2cpp, etc. with root directory and file name. Choose from the list of files and script uses root directory + "pathoffile" to get file.
GG script encryption / decryption: Can encrypt, obfuscate, decrypt, and decompile gameguardian scripts with multiple methods (unicode, binary, moonsec obfuscator, etc.)
Live analytics: Data such as progress, memory used, disk space used, etc. You can disable, enable, and expand things in the settings menu.
Settings menu: Customize how the project works, both behind the scenes and in your face, with features such as keybinds changing, high contrast mode, low memory mode, and more!
Great GUI: Buttons, sliders, live analytics, and more! There's even a settings menu to customize it!
Command Line: If you don't like the GUI, you can use the command line version instead!
Call functions from the project itself: As a third option, you can you can call edit the program yourself and add function calls to the bottom of the code (make sure to un-comment the template and use that).
Available as command line .exe and GUI .exe
Programmed in both c++ and python, so if you want to modify it, write plugins, 
Debugging tools: There are special debugging tools such as monitoring variables, when functions are called, etc.
Warning and error system: A live warning system and an error system, so you know what goes wrong and why. You can dismiss errors, investigate errors, use debug tools in the way the error / warning suggests, and there is an ignore option and a do not show again option.
100% Open Source: All the code is clean, open source, and commented. You are free to use pieces of it with credit, modify it, etc.
Auto il2cpp dumping: Built-in perfare il2cppdumper and il2cppdumper online (https://il2cppdumper.com/the-dumper-tool), so you don't have to worry about dumping yourself!
Automatic Mod Menu Installion: Give the program the apk for a mod menu and the type of menu (LGL, OctoWolve, ImGUI, etc.) - or let it auto-detect it - and the program will try to automatically find and modify .txt files like androidmanifest.xml and mainactivity.smali, as well as find places for and add your mod menu files like your mod menu's lib and smali.
Signature Killing: Has several built-in tools to automatically kill signature verification in APKs. Can also read signature of APKs, etc.
tatic Byte Finder: Compares multiple versions (the more the better) of a game to find unchanging bytes in order to make hex patch scripts that do not expire every update.
