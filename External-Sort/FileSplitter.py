#https://github.com/spiralout/external-sort/blob/master/extsort.py

import os
import sys

class FileSplitter(object):
    BLK_FILE_NAME_STRUC = "blk_{0}.blk"
    
    blockFiles = []
    
    def __init__(self, tmpBlkFileLoc, inFile):
        self.tmpFileLoc = tmpBlkFileLoc
        self.inFile = inFile

    def write(self, data, blkNum):
        filename = self.tmpFileLoc + "\\" + "blk_{0}.blk".format(blkNum)
        fs = open(filename, 'w')
        fs.write(data)
        fs.close()
        self.blockFiles.append(fs.name)
    
    def Split(self, blkSize):
        fs = open(self.inFile, 'r')
        i = 0
        while(True):
            lines = fs.readlines(blkSize)
            if lines == []:
                break
            print(lines)
            #lines.sort()
            self.write(''.join(lines), i)
            i+=1

    def cleanup(self):
        for blkFile in self.blockFiles:
            os.remove(blkFile)


splitter = FileSplitter("D:\\TBD", "D:\\TBD\\BackPropProgram.txt")
splitter.Split(50)
splitter.cleanup();

