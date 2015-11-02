#!/usr/bin/env python
"""
the entire and only reason we need this file is because there is some weval of
an encoding problem somewhere that prevents all the bills being downloaded in
one fell swoop. As a result, we need to run through everything once and then
again to get the bills that didn't download and then again etc untill all get
downloaded.
Luckily, the library's caching features help us out here with speed.
"""


import logging
import argparse
import os
import shutil
import subprocess



LOGGO = logging.getLogger('loggo')
LD = LOGGO.debug
logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',
                    level=logging.ERROR,
                    datefmt='%H:%M:%S')
LOGGO.setLevel(logging.DEBUG)


PARSER = argparse.ArgumentParser()
PARSER.add_argument('file', metavar='<path>', type=str,
                    help='path to the file with public laws')

if not os.path.exists("./log"):
    os.mkdir("./log")
class Batcher(object):

    def __init__(self, plaw_file):
        self.file = plaw_file
        self.runs = 0
        self.remainder = file_len(self.file)
    def __str__(self):
        print self.file
    def pep8compliance(self):
        pass
    def batch(self):
        if self.runs == 0:
            shutil.copy(self.file, './active.csv')
            LD(os.getcwd())
            LD(os.listdir('.'))
        else:
            log_name = "./log/RUN_%s_NOTCAPTURED.log"%self.runs
            shutil.copy('plaw2.csv', log_name,)
            os.rename('plaw2.csv', 'active.csv')
        subprocess.call(
            "/opt/theunitedstates.io/congress/run bill_info_batch \
             --file_input=/data/active.csv", shell=True)
        self.runs += 1
        if os.path.exists('./plaw2.csv'):
            self.remainder = file_len('./plaw2.csv')


def file_len(fname):
    num = 0
    with open(fname, 'rb') as the_file:
        for bill_num in enumerate(the_file):
            num = bill_num[0]
        the_file.close()
    if num:
        return num + 1


if __name__ == "__main__":
    ARGS = PARSER.parse_args()
    print ARGS.file
    x = Batcher(ARGS.file)
    print x.file
    print x.runs
    msg = "dir is %s" % os.listdir('.')
    LD(msg)
    x.remainder = file_len(ARGS.file)
    x.batch()
    while x.runs < 30 and x.remainder > 2:
        msg = "files remaining: %s"%x.remainder
        LD(msg)
        msg = "run number: %s"%x.runs
        LD(msg)
        x.batch()
