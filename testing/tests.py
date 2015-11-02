import os
import nose
from nose.tools import *
from nose import with_setup

class TestLen:

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
    def test_close(self):
        assert abs(self.lenfiles-self.lenplaw) < 3, "Downloaded files not within 20 of sampled public laws"
