import os
from time import localtime
try:
    import storage
except:
    pass

def txtFileTime(fPath):
    retTime = localtime(max(min(2145916800,os.stat(fPath)[9]),946684800))
    fTime = []
    fTime.append(retTime[1])
    fTime.append(retTime[2])
    fTime.append(retTime[0])
    fTime.append(retTime[3])
    fTime.append(retTime[4])
    return(fTime)


cmd = ""
os.chdir("/")
while (1 == 1):
    cmdLine = input("\n"+os.getcwd()+">")
    args = cmdLine.split(" ")
    cmd = args[0].upper()
    if cmd == "DIR":
        nDirs = 2
        nFiles = 0
        print("Directory of",os.getcwd()+".")
        print("."+" "*23+"<DIR>")
        print(".."+" "*22+"<DIR>")
        for dir in os.listdir():
            if os.stat(dir)[0] & (2**15)== 0:
                fTime = txtFileTime(dir)
                print(dir+" "*(24-len(dir))+"<DIR>"+" "*18+"%2.2i-%2.2i-%4.4i %2.2i:%2.2i" % (fTime[0], fTime[1], fTime[2], fTime[3], fTime[4]))
                nDirs += 1

        tFSize = 0
        tmpDir = os.getcwd()
        try:
            availDisk = os.statvfs(tmpDir)[1]*os.statvfs(tmpDir)[4]
        except:
            availDisk = 0
        for dir in os.listdir():
            if os.stat(dir)[0] & (2**15) != 0:
                fSize = str(os.stat(dir)[6])
                tFSize += os.stat(dir)[6]
                fTime = txtFileTime(dir)
                print(dir+" "*(35-len(dir)+10-len(fSize)),fSize,"%2.2i-%2.2i-%4.4i %2.2i:%2.2i" % (fTime[0], fTime[1], fTime[2], fTime[3], fTime[4]))
                nFiles += 1

        print(" "*(4-len(str(nFiles))),nFiles,"File(s)"+" "*(32-len(str(tFSize))),tFSize,"Bytes.")
        print(" "*(4-len(str(nDirs))),nDirs,"Dir(s)"+" "*(33-len(str(availDisk))),availDisk,"Bytes free.")

    elif cmd == "RENAME" or cmd == "REN":

        if args[1] in os.listdir() and len(args) == 3:
            os.rename(args[1],args[2])
        elif len(args) != 3:
            print("Wrong number of arguments")
        else:
            print("No such file:",args[1])

    elif cmd == "DEL":

        if len(args) == 2:
            if args[1] in os.listdir():
                os.remove(args[1])
            else:
                print("Unable to delete: "+args[1]+". File not found.")
        else:
            print("Illeagal Path.")

    elif cmd == "TYPE":

        if args[1] in os.listdir():
            f = open(args[1])
            print(f.read())
            f.close()

        else:
            print("file "+args[1]+" not found.")

    elif cmd == "CD":

        if len(args) == 1:
            print(os.getcwd())

        else:
            pathDirs = args[1].split("/")
            savDir = os.getcwd()
            goodPath = True


            for path in pathDirs:
                if path == "":
                    os.chdir("/")

                elif path == "." or path == "..":
                    os.chdir(path)

                elif path in os.listdir() and (os.stat(path)[0] & (2**15) == 0):
                    os.chdir(path)

                else:
                    goodPath = False
                    break

            if goodPath == False:
                print("Unable to change to: "+args[1]+".")
                os.chdir(savDir)

    elif cmd == "COPY":

        if args[1] in os.listdir() and args[2] not in os.listdir() and len(args) == 3:
            fOrig = open(args[1])
            fCopy = open(args[2], "w")
            fCopy.write(fOrig.read())
            fOrig.close()
            fCopy.close()
        elif len(args) != 3:
            print("Wrong number of arguments")
        elif args[1] not in os.listdir():
            print("No such file:",args[1])
        else:
            print("File already exists:",args[2])

    elif cmd == "EXIT":
        break

    elif cmd == "":
        continue

    elif cmd == "FSRO":
        storage.remount("/",True)

    elif cmd == "FSRW":
        storage.remount("/",False)

    else:
        if args[0] in os.listdir() and os.stat(args[0])[0] & (2**15)!= 0 and ((args[0].split("."))[1]).upper() == "PY":
#            __import__((args[0].split("."))[0])
#            try:
                exec(open(args[0]).read())
#            except SyntaxError:
#                print("A syntax error was detected in",args[0])
#            except:
#                print("An exception occurred in the",args[0],"python script")

        else:
            print("Illegal command:",args[0]+".")
