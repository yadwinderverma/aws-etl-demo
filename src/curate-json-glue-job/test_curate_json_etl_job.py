import unittest
from curate_json_etl_job import dequote_string, dequote_json_elements

class TestCuratedJsonEtlJob(unittest.TestCase):

    def test_dequote_string_with_extra_quotes(self):
        testString =  '"{"postcode":"3000"}"'
        expectedResponse = '{"postcode":"3000"}'

        actualResponse = dequote_string(testString)
        self.assertEqual(actualResponse, expectedResponse)

    def test_dequote_string_without_extra_quotes(self):
        testString =  '{"postcode":"3000"}'
        expectedResponse = '{"postcode":"3000"}'

        actualResponse = dequote_string(testString)
        self.assertEqual(actualResponse, expectedResponse)

    def test_dequote_json_elements_with_extra_quotes(self):
        testString =  '{""postcode"":""3000""}'
        expectedResponse = '{"postcode":"3000"}'

        actualResponse = dequote_json_elements(testString)
        self.assertEqual(actualResponse, expectedResponse)

    def test_dequote_json_element_without_extra_quotes(self):
        testString =  '{"postcode":"3000"}'
        expectedResponse = '{"postcode":"3000"}'

        actualResponse = dequote_json_elements(testString)
        self.assertEqual(actualResponse, expectedResponse)