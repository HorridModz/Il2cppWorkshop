import os
import sys
rootdirectory = os.getcwd()
sys.path.append(rootdirectory)



from Il2cppWorkshopCore import *

def main():
    init()
    #offset = "3879A8"
    #edit = "0100A0E3"
    #hexstring = offsettohex(offset,r"C:\Users\zachy\OneDrive\Documents\Work\Projects\Angry Birds Epic\libil2cpp.so",50,"")
    #if len(edit.replace(" ","")) < 16:
    #    edit = edit + "EFF2FE1"
    #script = "gg.clearResults()\ngg.setRanges(gg.REGION_CODE_APP)\ngg.searchNumber(\"h " + hexstring + "\",gg.TYPE_BYTE)\ngg.getResults(8)\ngg.editAll(\"h " + edit + "\",gg.TYPE_BYTE)"
    #write_file(r"C:/Users/zachy/Nox_share/Download/Test2.lua",script)
    #print(script)
    #sys.exit()
    print(aobsearch(r"C:\Users\zachy\OneDrive\Documents\Work\Tools\Il2cppWorkshop\Il2cppWorkshop.cpp","??"))
    #print(dectohex("1000",False,"",True))
    #deobfuscateallclassesdemofaster()
    sys.exit("Finished")
    a = armtohex("NOP; ret",64)
    print(a)
    print(hextoarm(a,64))
    #print(generateaobfromarm(read_file(r"C:\Users\zachy\OneDrive\Documents\Work\Projects\Pixel Gun 3D\Pixel Gun Notes\PG3D All Updates Mods\aobtemp2").replace("\\n",""),32))
    #sys.exit()
    #gameguardianallupdatescriptgentest(offsets32bit = ["2B493B8","291E2C0"],offsets64bit = ["42426EC","3709238"],libs32bit = [r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.6.0/32bit libil2cpp.so",r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.6.1/32bit libil2cpp.so"],libs64bit = [r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.6.0/libil2cpp.so",r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.6.1/libil2cpp.so"],maxvalues = 3,ranges = ["350","200","100"])
    sys.exit()
    #print(getstaticbytes(["30 48 2D E9 08 B0 8D E2 FC 00 9F E5 00 00 8F E0 00 00 D0 E5 00 00 50 E3 06 00 00 1A EC 00 9F E5 00 00 9F E7 00 00 90 E5 B1 B2 01 EB E0 00 9F E5 01 10 A0 E3 00 10 CF E7 D8 00 9F E5 00 00 9F E7 00 00 90 E5 BF 10 D0 E5 02 00 11 E3 06 00 00 0A 70 10 90 E5 00 00 51 E3 03 00 00 1A B6 B2 01 EB B4 00 9F E5 00 00 9F E7 00 00 90 E5 5C 10 90 E5 04 50 91 E5 00 00 55 E3 0C 00 00 0A 9C 10 9F E5 00 20 95 E5 01 10 9F E7 B8 40 D2 E5 00 10 91 E5 B8 30 D1 E5 03 00 54 E1 04 00 00 3A 64 20 92 E5 03 21 82 E0 04 20 12 E5 01 00 52 E1 01 00 00 0A 00 00 A0 E3 30 88 BD E8 BF 10 D0 E5 02 00 11 E3 0D 00 00 0A 70 10 90 E5 00 00 51 E3 0A 00 00 1A 99 B2 01 EB 48 00 9F E5 00 00 9F E7 00 00 90 E5 5C 00 90 E5 04 50 90 E5 00 00 55 E3 02 00 00 1A 00 00 A0 E3 00 50 A0 E3 C5 B2 01 EB 05 00 A0 E1 00 10 A0 E3 30 48 BD E8 6E A2 17 EA","30 48 2D E9 08 B0 8D E2 FC 00 9F E5 00 00 8F E0 00 00 D0 E5 00 00 50 E3 06 00 00 1A EC 00 9F E5 00 00 9F E7 00 00 90 E5 BA FC 81 EB E0 00 9F E5 01 10 A0 E3 00 10 CF E7 D8 00 9F E5 00 00 9F E7 00 00 90 E5 BF 10 D0 E5 02 00 11 E3 06 00 00 0A 70 10 90 E5 00 00 51 E3 03 00 00 1A 71 34 82 EB B4 00 9F E5 00 00 9F E7 00 00 90 E5 5C 10 90 E5 04 50 91 E5 00 00 55 E3 0C 00 00 0A 9C 10 9F E5 00 20 95 E5 01 10 9F E7 B8 40 D2 E5 00 10 91 E5 B8 30 D1 E5 03 00 54 E1 04 00 00 3A 64 20 92 E5 03 21 82 E0 04 20 12 E5 01 00 52 E1 01 00 00 0A 00 00 A0 E3 30 88 BD E8 BF 10 D0 E5 02 00 11 E3 0D 00 00 0A 70 10 90 E5 00 00 51 E3 0A 00 00 1A 54 34 82 EB 48 00 9F E5 00 00 9F E7 00 00 90 E5 5C 00 90 E5 04 50 90 E5 00 00 55 E3 02 00 00 1A 00 00 A0 E3 00 50 A0 E3 D3 AB 82 EB 05 00 A0 E1 00 10 A0 E3 30 48 BD E8 BE 9C 25 EA"],False))
    #print(formatlist(getdecimalvaluesfromaob("30 48 2D E9 08 B0 8D E2 FC 00 9F E5 00 00 8F E0 00 00 D0 E5 00 00 50 E3 06 00 00 1A EC 00 9F E5 00 00 9F E7 00 00 90 E5 ?? ?? ?? EB E0 00 9F E5 01 10 A0 E3 00 10 CF E7 D8 00 9F E5 00 00 9F E7 00 00 90 E5 BF 10 D0 E5 02 00 11 E3 06 00 00 0A 70 10 90 E5 00 00 51 E3 03 00 00 1A ?? ?? ?? EB B4 00 9F E5 00 00 9F E7 00 00 90 E5 5C 10 90 E5 04 50 91 E5 00 00 55 E3 0C 00 00 0A 9C 10 9F E5 00 20 95 E5 01 10 9F E7 B8 40 D2 E5 00 10 91 E5 B8 30 D1 E5 03 00 54 E1 04 00 00 3A 64 20 92 E5 03 21 82 E0 04 20 12 E5 01 00 52 E1 01 00 00 0A 00 00 A0 E3 30 88 BD E8 BF 10 D0 E5 02 00 11 E3 0D 00 00 0A 70 10 90 E5 00 00 51 E3 0A 00 00 1A ?? ?? ?? EB 48 00 9F E5 00 00 9F E7 00 00 90 E5 5C 00 90 E5 04 50 90 E5 00 00 55 E3 02 00 00 1A 00 00 A0 E3 00 50 A0 E3 ?? ?? ?? EB 05 00 A0 E1 00 10 A0 E3 30 48 BD E8 ?? ?? ?? EA",r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.6.1/32bit libil2cpp.so",["Qword","Dword"],600)))
    #print("\n\n\n\n\n\n")
    #print(formatlist(getdecimalvaluesfromaob("F3 0F 1E F8 FD 7B 01 A9 FD 43 00 91 ?? ?? 02 ?? 68 ?? ?? 39 E8 00 00 37 ?? ?? ?? B0 08 ?? ?? F9 00 01 40 B9 ?? ?? ?? 97 E8 03 00 32 68 ?? ?? 39 ?? ?? ?? ?? 73 ?? ?? F9 60 02 40 F9 08 9C 44 39 A8 00 08 36 08 D8 40 B9 68 00 00 35 ?? ?? ?? 97 60 02 40 F9 08 5C 40 F9 08 05 40 F9 C8 01 00 B4 ?? ?? ?? F0 29 ?? ?? F9 0A 01 40 F9 29 01 40 F9 4C 81 44 39 2B 81 44 39 9F 01 0B 6B C3 00 00 54 4A 65 40 F9 4A 0D 0B 8B 4A 81 5F F8 5F 01 09 EB A0 00 00 54 FD 7B 41 A9 E0 03 1F 2A F3 07 42 F8 C0 03 5F D6",r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.6.1/libil2cpp.so",["Qword","Dword"],600)))
    #sys.exit()
    #a = getdecimalvaluesfromaob("30 48 2D E9 08 B0 8D E2 08 D0 4D E2 00 40 A0 E1 9C 00 9F E5 00 00 8F E0 00 00 D0 E5 00 00 50 E3 06 00 00 1A 8C 00 9F E5 00 00 9F E7 00 00 90 E5 ?? ?? ?? EB 80 00 9F E5 01 10 A0 E3 00 10 CF E7 00 00 A0 E3 04 00 8D E5 00 00 8D E5 3C 00 94 E5 00 00 50 E3 14 00 00 CA 60 00 9F E5 08 50 84 E2 00 00 9F E7 00 10 90 E5 05 00 A0 E1 ?? ?? ?? EB 00 00 50 E3 02 00 00 1A 04 00 A0 E1 00 10 A0 E3 ?? ?? 00 EB 38 00 9F E5 0D 40 A0 E1 05 10 A0 E1 00 00 9F E7 00 20 90 E5 04 00 A0 E1 ?? ?? ?? EB 04 00 A0 E1 00 10 A0 E3 ?? ?? ?? EB 08 D0 4B E2 30 88 BD E8",r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.6.0/32bit libil2cpp.so",["Qword"])
    #new = []
    #for this in a:
        #if this["Occurences"] < 500:
            #new.append(this)
    #print(formatlist(new))
    #sys.exit()
    #print("THIS IS A WIP / DEMO!\nNote: The program may have errors, get stuck in infinite loops, or not work correctly. This is just a demo.\nAnd of course, this may not always be accurate. It is unfinished, and even if it was finished, no deobfuscator can be perfect.\nThis will take around 20-200 minutes,\
    #depending on your device. Be patient - it is worth the wait!\n")
    c = read_file(r"C:\Users\zachy\OneDrive\Documents\Work\Projects\Pixel Gun 3D\Pixel Gun 3D 22.6.1\WeaponSoundsClass.cs")
    a = getmethods(getfullmethods(c))
    ##occurences = {}
    ##for i in a:
    ##    if "int" in getwords(i["Type"]) and i["ParamTypes"] == "int name":
    ##        occurences[getwords(i["Params"][0])[1]] = c.count(getwords(i["Params"][0])[1])
    ##        try:
    ##            occurences[getwords(i["Params"][0])[1]] = c.count(getwords(i["Params"][0])[1])
    ##        except:
    ##            pass
    b = "gg.setVisible(false)\ngg.clearList()\ngg.setRanges(gg.REGION_CODE_APP)"
    e = ""
    for i in a:
        #if "int" in getwords(i["Type"]) or "float" in getwords(i["Type"]) or "bool" in getwords(i["Type"]):
        #try:
            #d = occurences[getwords(i["Params"][0])[1]]
        #except:
            #d = 0
        if "bool" in getwords(i["Type"]) and i["Type"] == "internal bool" and i["Params"] == [] and offsettohex(i["Offset"],r"C:\Users\zachy\OneDrive\Documents\Work\Projects\Pixel Gun 3D\Pixel Gun 3D 22.6.1\32bit libil2cpp.so",80).startswith("30 48 2D"):
            g = offsettohex(i["Offset"],r"C:\Users\zachy\OneDrive\Documents\Work\Projects\Pixel Gun 3D\Pixel Gun 3D 22.6.1\32bit libil2cpp.so",80)
            print(g)
            print("\n\n\n")
            b = b + "\n--" + i["Type"] + " " + i["Name"] + "\ngg.clearResults()\ngg.searchNumber('h " + offsettohex(i["Offset"],r"C:/Users/zachy/OneDrive/Documents/Work/Projects/Pixel Gun 3D/Pixel Gun 3D 22.6.1/32bit libil2cpp.so",100) + "',gg.TYPE_BYTE)\ngg.getResults(8)\ngg.addListItems(gg.getResults(8))\ngg.editAll('h "
            if "bool" in getwords(i["Type"]):
                b = b + "20 00 80 D2"
            elif "int" in getwords(i["Type"]):
                b = b + "01 0A A0 E3"
            elif "float" in getwords(i["Type"]):
                b = b + "01 0A A0 E3"
            b = b + " 1E FF 2F E1',gg.TYPE_BYTE)"
            e = e + i["Name"] + "\n"
    b = b + "\ngg.loadResults(gg.getListItems())"
    print(e)
    ##print(b)
    sys.exit()
    #apk = r"C:\Users\zachy\OneDrive\Documents\APK Easy Tool\1-Decompiled APKs\Pixel Gun 3D 16.6.1 Armv7"
    apk = r"C:/Users/zachy/OneDrive/Documents/APK Easy Tool/1-Decompiled APKs/Bullet Force V1.89.0"
    #new = r"C:\Users\zachy\OneDrive\Documents\APK Easy Tool\1-Decompiled APKs\New Pixel Gun 3D 16.6.1 Armv7"
    new = r"C:/Users/zachy/OneDrive/Documents/APK Easy Tool/1-Decompiled APKs/Modded Bullet Force V1.89.0"
    modmenupath = r"C:\Users\zachy\OneDrive\Documents\APK Easy Tool\1-Decompiled APKs\app-debug"
    menu = ModMenuInstall(apk,new,modmenupath,"LGL (With Overlay Permission)","libModMenu.so")
    menu.modifyandroidmanifest()
    menu.modifymainactivity()
    menu.addmodmenusmali()
    menu.modifylib()
    sys.exit()
    #print(ModMenuInstall.androidmanifest(r"C:\Users\zachy\OneDrive\Documents\APK Easy Tool\1-Decompiled APKs\Bullet Force V1.88.1"))
    #print(formatlist(fulllog))
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

if __name__ == "__main__":
    main()

