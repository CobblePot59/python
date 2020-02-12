def splitbline(inputFile,numParts,outputName):
    with open(inputFile) as openInputFile:
        content = openInputFile.readlines()

    nbTotalLine = len(content)
    nbLine = nbTotalLine // numParts
    firstLine = 0
    lastLine = nbLine

    for i in range(1,numParts+1):
        if '.' in outputName:
            outputNameSplit=outputName.split('.')
            openOutputFile=open(outputNameSplit[0]+str(i)+'.'+outputNameSplit[1],'a')
        else:
            openOutputFile=open(outputName+str(i),'a')

        openOutputFile.writelines(content[firstLine:lastLine])
        firstLine+=nbLine
        lastLine+=nbLine
        openOutputFile.close()

    if '.' in outputName:
        outputNameSplit=outputName.split('.')
        openOutputFile=open(outputNameSplit[0]+str(numParts)+'.'+outputNameSplit[1],'a')
    else:
        openOutputFile=open(outputName+str(numParts),'a')
    openOutputFile.writelines(content[nbTotalLine-1])
    openOutputFile.close()


#splitbline('test.txt',2,'file.txt')
