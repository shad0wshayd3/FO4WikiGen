import os

TopLevel = "import"
TypeLeads = [["bool", "ab"], ["float", "af"], ["int", "ai"], ["string", "as"], ["var", "av"], ["", "ak"]]
F4SEReqText, F4SEHighText, F4SEAltText = "\nRequires F4SE Version", "or higher.\n\n\n", "\n"

isF4SE = False

class memberFunction:
    def __init__(self, asParent = "", asType = "", asName = "", asArgs = "", isNative = False, isGlobal = False, isDebug = False):
        self.SetParent(asParent)
        self.SetType(asType)
        self.SetName(asName)
        self.SetArgs(asArgs)
        self.isNative = isNative
        self.isGlobal = isGlobal
        self.isDebug = isDebug

    def SetParent(self, asParent):
        self.parent = asParent

    def SetType(self, asType):
        if (len(asType) > 0):
            asType += " "

        self.type = asType

    def SetName(self, asName):
        self.name = asName

    def SetArgs(self, asArgs):
        formattedArgs = ""

        if (len(asArgs) > 0):
            argList = asArgs.split(", ")

            for arg in argList:
                argSplit = arg.split(" ")

                if (len(argSplit) == 1):
                    continue

                argType = argSplit[0]
                argName = argSplit[1]
                argLead = argName[:2].lower()
                argEquals = ""
                argDefault = ""

                if (len(argSplit) > 3):
                    argEquals = " = "
                    argDefault = argSplit[3]

                for Lead in TypeLeads:
                    if ((argType.lower() == Lead[0]) or ("" == Lead[0])):
                        if (argLead != Lead[1]):
                            argName = Lead[1] + argName[:1].upper() + argName[1:]
                            break


                formattedArgs = f"{formattedArgs}{argType} {argName}{argEquals}{argDefault}, "

        if (len(formattedArgs) > -1):
            formattedArgs = formattedArgs[:len(formattedArgs)-2]

        self.args = formattedArgs

    def CodePrint(self):
        base = f"{self.type}Function {self.name}({self.args}){' Native' if self.isNative else ''}{' Global' if self.isGlobal else ''}{' debugOnly' if self.isDebug else ''}"
        return base

    def MakePage(self):
        checkfordir(f"output/{self.parent}")
        with open(f"output//{self.parent}//{self.name} - {self.parent}.txt", "w") as outfile:
            print(f"'''{'F4SE ' if isF4SE else ''}Member of:''' [[{self.parent} Script]]", file=outfile)
            F4SEText = F4SEReqText + getversionstring(self.name + " - " + self.parent) + F4SEHighText
            print(f"{F4SEText if isF4SE else F4SEAltText}Placeholder Description.\n", file=outfile)
            print(f'== Syntax ==\n<source lang="papyrus">\n{self.CodePrint()}\n</source>\n', file=outfile)
            print(f"== Parameters ==", file=outfile)

            argsList = self.args.split(", ")
            printcount = 0

            for arg in argsList:
                name = arg.split(" ")
                if (len(name) != 1):
                    print(f"*{name[1]}: Placeholder Description.", file=outfile)
                    printcount += 1

            if (printcount == 0):
                print("*None", file=outfile)

            print(f"\n== Return Value ==\n*{'Placeholder Description.' if len(self.type) > 0 else 'None'}\n", file=outfile)

            print(f'== Examples ==\n<source lang="papyrus">\n; Placeholder Code.\n</source>\n', file=outfile)
            print(f"== See Also ==\n*[[{self.parent} Script]]\n", file=outfile)

            print(f"[[Category: Scripting]]\n[[Category: Papyrus]]\n{'[[Category: F4SE]]' if isF4SE else ''}", file=outfile)

class memberEvent(memberFunction):
    def __init__(self, asParent = "", asName = "", asArgs = ""):
        memberFunction.SetParent(self, asParent)
        memberFunction.SetName(self, asName)
        memberFunction.SetArgs(self, asArgs)

    def CodePrint(self):
        base = f"Event {self.name}({self.args})"
        return base

    def MakePage(self):
        checkfordir(f"output/{self.parent}")
        with open(f"output//{self.parent}//{self.name} - {self.parent}.txt", "w") as outfile:
            print(f"'''{'F4SE ' if isF4SE else ''}Member of:''' [[{self.parent} Script]]", file=outfile)
            F4SEText = F4SEReqText + getversionstring(self.name + " - " + self.parent) + F4SEHighText
            print(f"{F4SEText if isF4SE else F4SEAltText}Placeholder Description.\n", file=outfile)
            print(f'== Syntax ==\n<source lang="papyrus">\n{self.CodePrint()}\n</source>\n', file=outfile)
            print(f"== Parameters ==", file=outfile)

            argsList = self.args.split(", ")
            printcount = 0

            for arg in argsList:
                name = arg.split(" ")
                if (len(name) != 1):
                    print(f"*{name[1]}: Placeholder Description.", file=outfile)
                    printcount += 1

            if (printcount == 0):
                print("*None", file=outfile)

            print(f'\n== Examples ==\n<source lang="papyrus">\n; Placeholder Code.\n</source>\n', file=outfile)
            print(f"== See Also ==\n*[[{self.parent} Script]]\n", file=outfile)

            print(f"[[Category: Scripting]]\n[[Category: Papyrus]]\n[[Category: Events]]\n{'[[Category: F4SE]]' if isF4SE else ''}", file=outfile)

class memberStruct:
    def __init__(self, asParent = "", asName = "", asArgs = ""):
        self.SetName(asName)
        self.SetArgs(asArgs)
        self.parent = asParent

    def SetName(self, asName):
        self.name = asName

    def SetArgs(self, asArgs):
        formattedArgs = ""

        if (len(asArgs) > 0):
            for arg in asArgs:
                argSplit = arg.split(" ")
                argType = argSplit[0]
                argName = argSplit[1]
                argEquals = ""
                argDefault = ""

                if (len(argSplit) > 2):
                    argEquals = " = "
                    argDefault = argSplit[3]

                formattedArgs = f"{formattedArgs}    {argType} {argName}{argEquals}{argDefault}\n"

        self.args = formattedArgs

    def CodePrint(self):
        base = f"Struct {self.name}\n{self.args}EndStruct"
        return base

    def MakePage(self):
        checkfordir(f"output/{self.parent}")
        with open(f"output//{self.parent}//{self.name} Struct - {self.parent}.txt", "w") as outfile:
            print(f"'''{'F4SE ' if isF4SE else ''}Member of:''' [[{self.parent} Script]]", file=outfile)
            F4SEText = F4SEReqText + getversionstring(self.name + " - " + self.parent) + F4SEHighText
            print(f"{F4SEText if isF4SE else F4SEAltText}Placeholder Description.\n", file=outfile)
            print(f'== Syntax ==\n<source lang="papyrus">\n{self.CodePrint()}\n</source>\n', file=outfile)
            print(f"== Members ==", file=outfile)

            argsList = self.args.split("\n")
            for arg in argsList:
                name = arg.split(" ")
                if (len(name) != 1):
                    print(f"*{name[5]}: Placeholder Description.", file=outfile)

            print(f'\n== Examples ==\n<source lang="papyrus">\n; Placeholder Code.\n</source>\n', file=outfile)
            print(f"== See Also ==\n*[[{self.parent} Script]]\n", file=outfile)

            print(f"[[Category: Scripting]]\n[[Category: Papyrus]]\n{'[[Category: F4SE]]' if isF4SE else ''}", file=outfile)

def checkfordir(dirName):
    if not os.path.isdir(dirName):
        os.makedirs(dirName)

def getversionstring(asFunction):
    if isF4SE:
        versionHunting = False

        with open("data/f4se/version.txt", "r") as infile:
            lines = infile.readlines()

        for line in lines:
            if versionHunting:
                if (line.find("F4SEVERSION|") == 0):
                    return " " + line[12:].strip("\n") + " "

            if (line.find(asFunction) == 0):
                versionHunting = True

    else:
        return ""

if __name__ == "__main__":
    checkfordir("output")
    checkfordir("import")

    for root, dirs, files in os.walk(TopLevel):
        for name in files:

            with open(os.path.join(root, name), "r") as infile:
                lines = infile.readlines()

            i = 0
            start = 0
            while (i < len(lines)):
                line = str(lines[i])
                if (line.lower().find("f4se additions built") > -1):
                    start = i
                    break

                i += 1

            i = start
            while (i < len(lines)):
                line = str(lines[i])

                if (line.lower().find("function ") > -1):
                    if not (line.lower().find(";") > -1 and line.lower().find("function ") > line.lower().find(";")):
                        isNative = bool(line.lower().find("native") > -1)
                        isGlobal = bool(line.lower().find("global") > -1)
                        isDebugOnly = bool(line.lower().find("debugonly") > -1)
                        typeName = ""

                        firstWord = line[:line.find(" ")]
                        if (firstWord.lower() != "function"):
                            typeName = firstWord

                        funName = line[line.lower().find("function ") + len("function "):line.find("(")]
                        funArgs = line[line.find("(")+1:line.find(")")]

                        if not (isDebugOnly and isF4SE):
                            newFunc = memberFunction(name[:len(name)-4], typeName, funName, funArgs, isNative, isGlobal, isDebugOnly)
                            newFunc.MakePage()

                        endFound = False
                        endCount = 0

                        while (endFound == False):
                            endCount += 1

                            if (i + endCount < len(lines)):
                                newLine = str(lines[i + endCount])

                                if (newLine.lower().find("function") > -1):
                                    if (newLine.lower().find("endfunction") > -1):
                                        i += endCount

                                    endFound = True

                            else:
                                endFound = True

                elif (line.lower().find("event ") > -1):
                    if not (line.lower().find(";") > -1 and line.lower().find("event ") > line.lower().find(";")):
                        funName = line[line.lower().find("event ") + len("event "):line.find("(")]
                        funArgs = line[line.find("(")+1:line.find(")")]

                        newFunc = memberEvent(name[:len(name)-4], funName, funArgs)
                        newFunc.MakePage()

                        endFound = False
                        endCount = 0

                        while (endFound == False):
                            endCount += 1

                            if (i + endCount < len(lines)):
                                newLine = str(lines[i + endCount])

                                if (newLine.lower().find("event") > -1):
                                    if (newLine.lower().find("endevent") > -1):
                                        i += endCount

                                    endFound = True

                            else:
                                endFound = True

                elif (line.lower().find("struct") > -1):
                    if not (line.lower().find(";") > -1 and line.lower().find("struct") > line.lower().find(";")):
                        structFound = False
                        structCount = 0
                        structArgs = []

                        structName = line.split(" ")[1].translate(str.maketrans('', '', "\n"))

                        while (structFound == False):
                            structCount += 1

                            if (i + structCount < len(lines)):
                                newLine = str(lines[i + structCount]).translate(str.maketrans('', '', "\t")).translate(str.maketrans('', '', "\n"))

                                if (newLine.lower().find("endstruct") > -1):
                                    structFound = True

                                else:
                                    newArg = newLine.translate(str.maketrans('', '', ";")).split(" ")
                                    structArgs.append(f"{newArg[0]} {newArg[1][:1].upper() + newArg[1][1:]}")

                            else:
                                structFound = True

                        newStruct = memberStruct(name[:len(name)-4], structName, structArgs)
                        newStruct.MakePage()

                        i += structCount

                i += 1
