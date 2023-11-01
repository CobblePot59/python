def splitbline(inputFile, numParts, outputName):
    with open(inputFile) as openInputFile:
        content = openInputFile.readlines()

    nbTotalLine = len(content)
    nbLine = nbTotalLine // numParts
    outputNameSplit = outputName.split('.') if '.' in outputName else (outputName, '')

    for i in range(1, numParts + 1):
        outputFileName = f"{outputNameSplit[0]}{i}.{outputNameSplit[1]}" if outputNameSplit[1] else f"{outputName}{i}"
        with open(outputFileName, 'a') as openOutputFile:
            openOutputFile.writelines(content[nbLine * (i - 1):nbLine * i])

    with open(f"{outputNameSplit[0]}{numParts}.{outputNameSplit[1]}", 'a') as openOutputFile:
        openOutputFile.writelines(content[nbTotalLine - 1])

# splitbline('test.txt',2,'file.txt')
