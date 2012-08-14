'''
Created on Jul 21, 2012

@author: Nathan Woodrow
'''
from mock import Mock, patch
from ConfigParser import ConfigParser
from unittest import TestCase, main
import gazetter
import httplib2
http = httplib2.Http()


class testGazetteer(TestCase):
    @patch.object(ConfigParser, 'sections', spec=True)
    def test_get_gazetteers_returns_correct_list(self, mock):
        expected =  ['Google', 'Other']
        mock.return_value = expected
        gazetteers = gazetter.getGazetteers()
        self.assertListEqual(expected, gazetteers)
                
    def test_search_returns_result_with_correct_name(self):
        result, success = gazetter.search("Hello", "Google")
        self.assertEqual(result.gazetter, "Google")

class testGazetteer_Intergration(TestCase):
    def test_get_gazetteers_returns_correct_list_from_config(self):
        expected = ['Google', 'Another']
        gazetteers = gazetter.getGazetteers()
        self.assertListEqual(expected, gazetteers)
 
if __name__ == "__main__":
    main()

