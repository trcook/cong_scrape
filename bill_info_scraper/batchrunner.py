#!/usr/bin/env python


import logging
import csv
import argparse
import os
import shutil
import subprocess

LOGGO = logging.getLogger('loggo')
LD = LOGGO.debug
logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',\
                    level=logging.ERROR,\
                    datefmt='%H:%M:%S')
LOGGO.setLevel(logging.DEBUG)


PARSER = argparse.ArgumentParser()
PARSER.add_argument('file',metavar='<path>', type=str,
                        help='path to the file with public laws')


class Batcher(object):
    def __init__(self,file):
        self.file = file
        self.runs = 0

    def batch(self):
        if self.runs == 0:
            shutil.copy(self.file,'./active.csv')
            LD(os.getcwd())
            LD(os.listdir('.'))
        else:
            os.rename('plaw2.csv','active.csv')
        subprocess.call("/opt/theunitedstates.io/congress/run bill_info_batch --file_input=/data/active.csv",shell=True)
        self.runs += 1
        if os.path.exists('./plaw2.csv'):
            self.remainder = file_len('./plaw2.csv')


def file_len(fname):
    with open(fname,'rb') as f:
        for i, l in enumerate(f):
            pass
    return i + 1



if __name__ == "__main__":
    ARGS = PARSER.parse_args()
    print ARGS.file
    x = Batcher(ARGS.file)
    print x.file
    print x.runs
    LD("dir is %s"%os.listdir('.'))
    x.remainder = file_len(ARGS.file)
    x.batch()
    while x.runs <10 and x.remainder<50:
        x.batch()
