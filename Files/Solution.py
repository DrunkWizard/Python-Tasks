import random
import struct
numbersList = []
listSize = int(input('Задайте размер списка: '))
file = open("Bytes.bin", 'w+b')
def listGeneration():
    for i in range(listSize):
        numbersList.append(random.uniform(-100, 200))
def fileWrite():
    for i in range(listSize):
        file.write(struct.pack('d', numbersList[i]))
def fileRead():
    file.seek(0)
    unpackedList = []
    unpackedList.append(struct.unpack_from(str(listSize) + 'd', file.read()))
    result = list(unpackedList[0])
    return result
listGeneration()
fileWrite()

def checkValue():
    if(numbersList == fileRead()):
        return True
    else:
        return False

print(checkValue())

def statsCount():
    numbers = fileRead()
    numbersLen = len(numbers)
    numbers.sort()
    max = numbers[numbersLen - 1]
    min = numbers[0]
    averageValue = sum(numbers) / numbersLen
    index = int(numbersLen / 2 - 1)
    index1 = int(numbersLen / 2)
    index2 = int((numbersLen) / 2)
    if numbersLen % 2 == 0:
        mediana = (numbers[index] + numbers[index1]) / 2
    else:
        mediana = numbers[index2]
    fileStatsWrite(max, min, averageValue, mediana)

def fileStatsWrite(max, min, average, mediana):
    fileStats = open("Stats.bin", 'w+b')
    testList = [max, min, average, mediana]
    for i in range(len(testList)):
        fileStats.write(struct.pack('d', testList[i]))
statsCount()