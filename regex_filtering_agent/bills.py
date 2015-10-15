"""bills module will call up json files loaded. Optionally allow for search by regex.
"""
import os, re, json, sys, argparse

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
    PARSER.add_argument('dir', metavar='<path>', type=str,
                        help='the path to search')
    PARSER.add_argument('--key',dest='search_key', metavar='search_key', type=str,
                        help='the key to examine. E.g. \'summary\'',\
                        default="summary")
    PARSER.add_argument('--fields',dest='record_key', metavar='record_keys', type=str, nargs='+',
                       help='the records to keep. E.g. \'summary enacted_as\'',\
                        default="summary")
    PARSER.add_argument('--regex',dest='regex', metavar='regex', type=str,
                       help='the regex string to use (defaults to (\w{0,10}end(?:\w+?\s){0,6}fund.+?\s) )',\
                        default="(\w{0,10}end(?:\w+?\s){0,6}fund.+?\s)")
    ARGS = PARSER.parse_args()
    print ARGS.search_key
    print ARGS.record_key
    print ARGS.regex
    print re.escape(ARGS.regex)
    if len(sys.argv) < 3:
        X = Bills(".")
        print "both path and regex pattern are needed"
        sys.exit(1)
    elif len(sys.argv) > 2:
        print "Correct Usage: python bill PATH"
        print len(sys.argv)
        print sys.argv
        sys.exit(1)
    X.getrecords(ARGS.record_key)
    X.search_records("match", ARGS.search_key,\
                     ARGS.regex)
    print [i['match_len'] for i in X.records if i['match_len'] > 0]
