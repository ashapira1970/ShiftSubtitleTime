import re
from datetime import datetime, timedelta



def main():
    delta = -18
    file1 = open('C:\\Users\\ashap\\Downloads\\Dolittle.2020.HDRip.800MB.x264-GalaxyRG[TGx]\\Dolittle.2020.HDRip.800MB.x264-GalaxyRG.srt.orig', 'r', encoding='utf8')     
    fout = open('C:\\Users\\ashap\\Downloads\\Dolittle.2020.HDRip.800MB.x264-GalaxyRG[TGx]\\Dolittle.2020.HDRip.800MB.x264-GalaxyRG.srt', 'wt', encoding='utf8')
    Lines = file1.readlines() 
    
    count = 0
    FMT = '%H:%M:%S,%f'
    # Strips the newline character 
    for line in Lines:     
        matchObj  = re.search( r'([0-9]*:[0-9]*:[0-9]*[0-9,]*) --> ([0-9]*:[0-9]*:[0-9]*[0-9,]*)', line, re.M|re.I)    
        if matchObj:            
            fromTimeStr = re.search( r'([0-9]*):([0-9]*):([0-9]*),([0-9]*)', matchObj.group(1), re.M|re.I)   
            toTimeStr = re.search( r'([0-9]*):([0-9]*):([0-9]*),([0-9]*)', matchObj.group(2), re.M|re.I)   
            
            fromTime   = datetime.strptime(fromTimeStr.string, '%H:%M:%S,%f')
            toTime   = datetime.strptime(toTimeStr.string, '%H:%M:%S,%f')

            fromTime = fromTime + timedelta(seconds=delta)
            toTime =toTime + timedelta(seconds=delta)
            line = line.replace(fromTimeStr.string, fromTime.strftime('%H:%M:%S,%f')[:-3])
            line = line.replace(toTimeStr.string, toTime.strftime('%H:%M:%S,%f')[:-3])
        fout.write(line)
        #print(line)




if __name__ == "__main__":
    main()