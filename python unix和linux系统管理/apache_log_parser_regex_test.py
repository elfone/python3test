#!/usr/bin/env python3
__author__ = 'Administrator'

import unittest
import apache_log_parser_regex


class TestApacheLogParser(unittest.TestCase):
    def setUp(self):
        pass

    def testCombinedEXample(self):
        # test  the combinded example from apache.org
        combined_log_entry = '127.0.0.1 - frand [10/Oct/2000:13:55:36 -0700] ' \
                             '"GET /apache_pb.git HTTP/1.0" 200 2326 '\
                             '"http://www.example.com/start.html" "Mozilla/4.08 [en] (win98; I ; Nav)"'
        self.assertEqual(apache_log_parser_regex.dictify_logline(combined_log_entry),
                         {'remote_host': '127.0.0.1', 'status': '200', 'bytes_sent': '2326'})

    def testCommonEXample(self):
        # test  the common example from apache.org
        common_log_entry = '127.0.0.1 - frand [10/Oct/2000:13:55:36 -0700] ' \
                           '"GET /apache_pb.git HTTP/1.0" 200 2326'
        self.assertEqual(apache_log_parser_regex.dictify_logline(common_log_entry),
                         {'remote_host': '127.0.0.1', 'status': '200', 'bytes_sent': '2326'})

    # def testExtraWhitespace(self):
    #     # test for extra whitespace between fields
    #     common_log_entry = '127.0.0.1 - frand [10/Oct/2000:13:55:36 -0700] ' \
    #                        '"GET /apache_pb.git HTTP/1.0" 200 2326'
    #     self.assertEqual(apache_log_parser_split.dictify_logline(common_log_entry),
    #                      {'remote_host': '127.0.0.1', 'status': '200', 'bytes_sent': '2326'})

    def testMalformed(self):
        # test for extra whitespace between fields
        common_log_entry = '127.0.0.1 - frand [10/Oct/2000:13:55:36 -0700] ' \
                           '"GET /some/url/with white space.html HTTP/1.0" 200 2326'
        self.assertEqual(apache_log_parser_regex.dictify_logline(common_log_entry),
                         {'remote_host': '127.0.0.1', 'status': '200', 'bytes_sent': '2326'})


if __name__ == '__main__':
    unittest.main()