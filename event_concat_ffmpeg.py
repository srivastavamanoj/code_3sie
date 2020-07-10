import time
import os
import glob

# Name of the directory where all the files are
dirname = '/home/mks/3sie/myCode/data/' 
# How many frames we want to go back, for example, if we have the eventIdx 27, and lookBackCounter
# 5, we will have ffmpeg comands to have frames 23-27 stitched together
lookBackCounter = 5 
#prefix for two kind of files;  
prefix1 = 'foo_'
prefix2 = 'bar_'
#suffix for the files, what format, jpeg, png, txt?
suffix = '.png'
# command name and arguments
baseCmd1 = 'ffmpeg $options1 '
baseCmd2 = 'gppeg $options2 '

def create_one_file(fn):
    open(fn,'a').close()

def create_files():
    tot=30;
    idx =0;
    while (idx<tot):
        fn1 = dirname + prefix1 + str(idx) + suffix;
        fn2 = dirname + prefix2 + str(idx) + suffix;
        create_one_file(fn1)
        create_one_file(fn2)
        time.sleep(1)
        #print('crated file: {}'.format(fn1))
        idx+=1

    return 0

def get_index(s):
    splitSep = '/'
    word1 = s.split(splitSep)
    #print('word1: {}'.format(word1))
    word2 = word1[-1].split('.')
    #print('word2: {}'.format(word2))
    word3 = word2[0].split('_')
    #print('word3: {}'.format(word3))
    num = int(word3[1])
    return num

def find_latest():
    searchDir = dirname +'*'
    listFiles = glob.glob(searchDir)
    latestFile = max(listFiles, key=os.path.getctime)
    eventIdx = get_index(latestFile)
    return eventIdx

def get_cmd(baseCmd, prefix, eventIdx):
    idx = 0
    fileType = []
    cmd = baseCmd

    while idx < lookBackCounter:
        actualIdx = eventIdx- lookBackCounter + 1 + idx
        fn = dirname + prefix +  str(actualIdx) + suffix
        #print ('filename: {}'.format(fn))
        fileType.append(fn)
        idx+=1

    for l in fileType:
        cmd += l + ' '
    return cmd

if __name__ == '__main__':
    #create_files()
    eventIdx = find_latest();
    cmd1 = get_cmd (baseCmd1, prefix1, eventIdx)
    cmd2 = get_cmd (baseCmd2, prefix2, eventIdx)
    print ('cmd1: {}'.format(cmd1));
    print ('cmd2: {}'.format(cmd2));
