import re
from datetime import datetime, timedelta
import argparse
from progress.bar import Bar



def main(args):
    source_path = args.sourcePath
    target_path = args.targetPath
    delta = args.delta        
    fin = open(source_path, 'r', encoding='utf8')     
    fout = open(target_path, 'wt', encoding='utf8')
    lines = fin.readlines() 
    
    FMT = '%H:%M:%S,%f'
    print('starting to convet file...')
    # Strips the newline character 
    with Bar('Processing file', max=len(lines)) as bar:
        for line in lines:     
            matchObj  = re.search( r'([0-9]*:[0-9]*:[0-9]*[0-9,]*) --> ([0-9]*:[0-9]*:[0-9]*[0-9,]*)', line, re.M|re.I)    
            if matchObj:            
                fromTimeStr = re.search( r'([0-9]*):([0-9]*):([0-9]*),([0-9]*)', matchObj.group(1), re.M|re.I)   
                toTimeStr = re.search( r'([0-9]*):([0-9]*):([0-9]*),([0-9]*)', matchObj.group(2), re.M|re.I)   
                
                fromTime   = datetime.strptime(fromTimeStr.string, FMT)
                toTime   = datetime.strptime(toTimeStr.string, FMT)

                fromTime = fromTime + timedelta(seconds=delta)
                toTime =toTime + timedelta(seconds=delta)
                line = line.replace(fromTimeStr.string, fromTime.strftime(FMT)[:-3])
                line = line.replace(toTimeStr.string, toTime.strftime(FMT)[:-3])
            fout.write(line)
            bar.next()
    print('finished converting file...')




if __name__ == "__main__":
    """
    example
    python.exe .\shift_subt.py
    --sourcePath 'C:\\Users\\ashap\\Downloads\\Dolittle.2020.HDRip.800MB.x264-GalaxyRG[TGx]\\Dolittle.2020.HDRip.800MB.x264-GalaxyRG.srt.orig' 
    --targetPath 'C:\\Users\\ashap\\Downloads\\Dolittle.2020.HDRip.800MB.x264-GalaxyRG[TGx]\\Dolittle.2020.HDRip.800MB.x264-GalaxyRG.srt' 
    --delta -18
    """
    
    # Create the parser
    my_parser = argparse.ArgumentParser(description='Shift subtitle time')
    # Add the arguments
    my_parser.add_argument('--sourcePath',
                       type=str,
                       help='the path to source file')
    my_parser.add_argument('--targetPath',
                       type=str,
                       help='the path to output file')
    my_parser.add_argument('--delta',
                       type=int,
                       help='Number of seconds to add/susbtract')
    # Execute the parse_args() method
    args = my_parser.parse_args()
    main(args)