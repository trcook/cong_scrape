"""bills module will call up json files loaded. Optionally allow for search by regex.
"""
import os, re, sys, json, argparse, logging, csv
LOGGO = logging.getLogger('loggo')
LD = LOGGO.debug
logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',\
                    level=logging.ERROR,\
                    datefmt='%H:%M:%S')
LOGGO.setLevel(logging.DEBUG)
class Bills(object):
    """Bills class. go Bills! """
    def __init__(self, base_dir):
        self.getfilelist(base_dir)
        self.records = []

    def getfilelist(self, base_dir, **kwargs):
        """ gets the initial file list. recall here to generate new file list
        """
        ext_search = kwargs['ext'] if 'ext' in kwargs else 'json'
        self.files = [os.path.join(paths[0], j) for paths in os.walk(base_dir) \
                    for j in     paths[2] if j.endswith(ext_search)]


    def getrecords(self, fields, n=None):
        """ grab specified json keys from the first n files in bills.records """
        if n:
            files = self.files[0:n]
        else:
            files = self.files
        for idx, j in enumerate(files):
            jfile = get_json(j)
            rec = {}
            for field in fields:
                LD(self.files[idx])
                if re.match('enacted_as', field):
                    # hard coding in way of getting and setting public law number
                    rec["PL_num"] = "PL%s-%s"%\
                            (get_path(jfile, 'enacted_as.congress'), \
                                get_path(jfile, 'enacted_as.number'))
                rec_key = re.sub(r'(.+?\.)(\w+)$', r'\2', field)
                rec_val = get_path(jfile, field)
                rec_val = re.sub(r'\n', r' \\n ', rec_val)\
                            if isinstance(rec_val, unicode) else rec_val
                rec[rec_key] = rec_val
            self.records.append(rec)

    def search_records(self, key, loc, regex_str,**kwargs):
        """search with this method"""
        LD(self.records)
        for record in self.records:
            LD(record)
            search_loc = get_path(record, "%s"% loc)
            LD(type(search_loc))
            LD(msg="location is %s"%loc)
            record["%s_text"%key] = re.findall(regex_str, search_loc)
            record["%s_len"%key] = len(record["%s_text"%key])
            if (kwargs['notext'] if 'notext' in kwargs else False):
                root_key = re.findall(r'\w+?(?=\.|$)', loc)[0]
                record[root_key] = None
        LD(self.records)
        return

def get_path(dct, path):
    """ paths to nested json more sensibly """
    for list_index, dict_key in re.findall(r'(\d+)|(\w+)', path):
        dct = dct[dict_key or int(list_index)]
    return dct

def get_json(file_name):
    """gets a given json file from path and returns in obj format"""
    with open(file_name, 'rb') as thefile:
        return json.load(thefile)

class NoFilesError(Exception):
    def __init__(self, s):
        self.val = s
        print self.val
    def __str__(self):
        return repr(self.val)
class NoMatchesError(Exception):
    def __init__(self, s):
        self.val = s
        print self.val
    def __str__(self):
        return repr(self.val)

if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='Process files and\
                                    return search results.')
    PARSER.add_argument('datadir',
                        metavar='<path>', type=str,
                        help='the path to search')
    PARSER.add_argument('--key', dest='search_key',
                        nargs=1,
                        metavar='search_key', type=str,
                        help='''
                        the key to examine. E.g. \'text\'. Must be sufficient to
                        identify the unicode string to search. Seperate nested
                        levels with a period. search_key should begin with a
                        field that has been extracted (as directed by the
                        --fields argument''',\
                        default="text")
    PARSER.add_argument('--fields', dest='record_key',
                        metavar='record_keys', type=str, nargs='+',
                        help='''
                        the fields to keep (seperate with space.).  E.g. \'summary\' \'enacted_as\'. Seperate nested levels with a period -- to get the \"text\" part of \"summary\", write \'summary.text\'.
                        When traversing nested levels, only the last element will be preserved as the header name in the output. In other words, \'summary.text\' will yeild \'text\' as the record key (i.e. header in output). This is important to note when specifying a complimentary search_key (see search_key). Defaults pull \'summary.text\' as a field and search key as \'text\'
                        ''',\
                        default=["summary.text", "enacted_as", "bill_id"])
    PARSER.add_argument('--regex', dest='regex',
                        metavar='regex', type=str,
                        help=r'''the regex string to use (defaults to
                        (\w{0,10}end(?:\w+?\s){0,6}fund.+?\s) )''',
                        default=r"(\w{0,10}end(?:\w+?\s){0,6}fund.+?\s)")
    PARSER.add_argument('--verbose', '-v', dest='verbose',
                        metavar='output_file',
                        type=str, help='file for output')
    PARSER.add_argument('--out', '-o', dest='out', metavar='output_file',
                        type=str, help='file for output')
    PARSER.add_argument('--keeptext','-k', dest='notext', action='store_false')
    PARSER.add_argument('-n', dest='n', type=int,help='number of records to search -- useful for debugging',default=None)
    ARGS = PARSER.parse_args()
    LD(msg=ARGS.notext)
    LD(msg="Search key %s"%ARGS.search_key)
    LD(msg="Search key type: %s"%type(ARGS.search_key).__name__)
    LD(msg="Record key %s"%ARGS.record_key)
    LD(msg="Record key type:  %s"%type(ARGS.record_key).__name__)
    LD(msg="REGEX %s"%ARGS.regex)
    LD(msg="REGEX key type:  %s"%type(ARGS.regex).__name__)
    # if isinstance(ARGS.search_key, str):
    #     LD('Converting search_key to list')
    #     ARGS.search_key = [ARGS.search_key]
    #     LD(ARGS.search_key)
    if isinstance(ARGS.record_key, str):
        LD('Converting record_key to list')
        ARGS.record_key = [ARGS.record_key]

    # turn off debug messages after this unless requested
    if not ARGS.verbose:
        LOGGO.setLevel(logging.WARNING)

    # pull bill listing from specified directory:
    X = Bills(ARGS.datadir)

    # handle if no files found
    if len(X.files) < 1:
        LOGGO.error("No Files Found")
        raise NoFilesError("directory searched: %s"%ARGS.datadir)

    X.getrecords(ARGS.record_key, n=ARGS.n if ARGS.n else None)
    X.search_records("match", ARGS.search_key,\
                      ARGS.regex, notext=ARGS.notext)
    if ARGS.out:
        # return only matching data
        OUTPUT = [i for i in X.records if i['match_len'] > 0]
        if len(OUTPUT)<1:
            LOGGO.warn("No Matches Found!!!")
            raise NoMatchesError("Pattern was %s"%ARGS.regex)

        OUTEXT = os.path.splitext(ARGS.out)[1]
        LD(OUTEXT)
        with file(ARGS.out, 'wb') as f:
            if re.findall(OUTEXT, r'\.json', flags=re.IGNORECASE):
                json.dump(OUTPUT, f)
                f.close()
            elif re.findall(OUTEXT, r'\.csv', flags=re.IGNORECASE):
                FIELDNAMES = OUTPUT[0].keys()
                CWRITER = csv.DictWriter(f, delimiter=',', fieldnames=FIELDNAMES)
                CWRITER.writeheader()
                for i in OUTPUT:
                    CWRITER.writerow(i)
                f.close()
