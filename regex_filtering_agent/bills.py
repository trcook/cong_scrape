"""bills module will call up json files loaded. Optionally allow for search by regex.
"""
import os, re, json, sys, argparse, logging
logging.basicConfig(format='[%(asctime)s %(levelname)s] %(message)s',\
                    level=logging.DEBUG,\
                    datefmt='%H:%M:%S')
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


    def getrecords(self, fields, **kwargs):
        """ grab specified json keys from the first n files in bills.records """
        if 'n' in kwargs:
            files = self.files[0:kwargs['n']] if kwargs['n'] else self.files
        else:
            files = self.files
        for j in files:
            self.records.append({i:get_json(j)[i] for i in fields})


    def search_records(self, key, loc, regex_str):
        """search with this method"""
        records = self.records
        for record in records:
            search_loc = get_path(record, "%s"% loc)
            record["%s_text"%key] = re.findall(regex_str, search_loc)
            record["%s_len"%key] = len(record["%s_text"%key])


def get_path(dct, path):
    """ paths to nested json more sensibly """
    for list_index, dict_key in re.findall(r'(\d+)|(\w+)', path):
        dct = dct[dict_key or int(list_index)]
    return dct

def get_json(file_name):
    """gets a given json file from path and returns in obj format"""
    with open(file_name, 'rb') as thefile:
        return json.load(thefile)


if __name__ == "__main__":
    PARSER = argparse.ArgumentParser(description='Process files and\
                                    return search results.')
    PARSER.add_argument('datadir',
                        metavar='<path>', type=str,
                        help='the path to search')
    PARSER.add_argument('--key',dest='search_key',
                        nargs=1,
                        metavar='search_key', type=str,
                        help='the key to examine. E.g. \'summary.text\'',\
                        default="summary.text")
    PARSER.add_argument('--fields',dest='record_key',
                        metavar='record_keys', type=str, nargs='+',
                        help='the fields to keep (seperate with space. Must be top-level portion of record). E.g. [\'summary\' \'enacted_as\']',\
                        default=["summary","enacted_as"])
    PARSER.add_argument('--regex',dest='regex',
                        metavar='regex', type=str,
                        help='the regex string to use (defaults to (\w{0,10}end(?:\w+?\s){0,6}fund.+?\s) )',\
                        default="(\w{0,10}end(?:\w+?\s){0,6}fund.+?\s)")
    PARSER.add_argument('--out','-o',dest='out',metavar='output_file',\
                        type=str,help='file for output')
    ARGS = PARSER.parse_args()
    ld=logging.debug
    ld("Search key %s"%ARGS.search_key)
    ld("Search key type: %s"%type(ARGS.search_key).__name__)
    ld("Record key %s"%ARGS.record_key)
    ld("Record key type:  %s"%type(ARGS.record_key).__name__)
    ld("REGEX %s"%ARGS.regex)
    ld("REGEX key type:  %s"%type(ARGS.regex).__name__)
    if type(ARGS.search_key) is str:
        ld('Converting search_key to list')
        ARGS.search_key = [ARGS.search_key]
    if type(ARGS.record_key) is str:
        ld('Converting record_key to list')
        ARGS.record_key = [ARGS.record_key]
    X = Bills(ARGS.datadir)
    if len(X.files) < 1:
        logging.error("No Files Found")
    X.getrecords(ARGS.record_key,n=500)
    X.search_records("match", ARGS.search_key,\
                      ARGS.regex)
    if ARGS.out:
        with file(ARGS.out,'wb') as f:
            json.dump([i for i in X.records if i['match_len']>0],f)
            f.close()
