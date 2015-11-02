import os
# import nose
# from nose.tools import *
import logging
import shutil
LD = logging.Logger('root')
LD.setLevel(logging.INFO)
LD.addHandler(logging.StreamHandler())


class TestPlawLen(object):
    @classmethod
    def setup_class(cls):
        num = 0
        with open("data/plaws.csv", 'rb') as source:
            for bill_num in enumerate(source):
                num = bill_num[0]
            source.close()
            cls.lenplaw = num
        msg = "# plaws found: %s"%cls.lenplaw
        LD.info(msg)
        msg = "# plaws expected: 10819"
        LD.info(msg)
    def test_plawlen(self):
        assert abs(self.lenplaw - 10820) < 2, "Downloaded files not within 20 of sampled public laws"
        msg = "negligable diff of: %s"%abs(self.lenplaw - 10820)
        LD.info(msg)

class TestLen(object):
    @classmethod
    def setup_class(cls):
        cls.files = [os.path.join(paths[0], j) for paths in os.walk('.') \
        for j in     paths[2] if j.endswith("json")]
        cls.lenfiles = len(cls.files)
        num = 0
        with open("data/plaws.csv", 'rb') as source:
            for bill_num in enumerate(source):
                num = bill_num[0]
            source.close()
            cls.lenplaw = num
        msg = "# plaws selected: %s"%cls.lenplaw
        LD.info(msg)
        msg = "# of bills processed %s"%cls.lenfiles
        LD.info(msg)
    def test_close(self):
        assert abs(self.lenfiles-self.lenplaw) < 3, "Downloaded files not within 2 of sampled public laws"
