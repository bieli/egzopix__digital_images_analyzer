import tempfile
import unittest

from egzopix.modules import VisualModuleProperty
from egzopix.modules.file_selector import FileSelectorVisualModule
from PIL import Image, ImageDraw


class FileSelectorVisualModuleTest(unittest.TestCase):
    def test_should_serialize_fields(self):
        expected_results = """\
{'inputs': {'file_path': VisualModuleProperty(name='file_name', description='File name', type=<class 'str'>, \
hidden=True, payload=None)}, \
'outputs': {'file_name': VisualModuleProperty(name='file_name', description='File name', type=<class 'str'>, \
hidden=True, payload=None), \
'file_temp': VisualModuleProperty(name='file_temp', description='File temporary path', type=<class 'str'>, \
hidden=True, payload=None), \
'file_body': VisualModuleProperty(name='file_body', description='File body', type=<class 'bytes'>, \
hidden=False, payload=None)}, 'exceptions': {'inputs': [], 'outputs': []}}"""

        unit = FileSelectorVisualModule()

        result = str(unit)

        self.assertEqual(expected_results, result)

    def test_should_process_and_read_empty_file_from_path(self):
        file_path_to_test = tempfile.mkstemp()[1]
        input = VisualModuleProperty("file_name", "File name", str, True, file_path_to_test)
        unit = FileSelectorVisualModule()

        result, exceptions = unit.process(input=input)

        self.assertIsNotNone(result)
        self.assertIsNone(exceptions)
        self.assertEqual(result['file_name'].payload, file_path_to_test)
        self.assertIsInstance(result['file_body'].payload, str)
        self.assertEqual(result['file_body'].payload, '')

    def test_should_process_and_read_binary_file_from_path(self):
        expected_image_content = b'\x89PNG\r\n\x1a\n\x00\x00\x00\rIHDR\x00\x00\x00\x01\x00\x00\x00\x01'\
                                 b'\x08\x02\x00\x00\x00\x90wS\xde\x00\x00\x00\x0cIDATx\x9cc\xf8\xcf\xc0\x00'\
                                 b'\x00\x03\x01\x01\x00\xc9\xfe\x92\xef\x00\x00\x00\x00IEND\xaeB`\x82'
        file_path_to_test = tempfile.mkstemp()[1] + '.png'

        img = Image.new('RGB', (1, 1), color='red')
        img.save(file_path_to_test)

        input = VisualModuleProperty("file_name", "File name", str, True, file_path_to_test)
        unit = FileSelectorVisualModule()

        result, exceptions = unit.process(input=input)

        self.assertIsNotNone(result)
        self.assertIsNone(exceptions)
        self.assertEqual(result['file_name'].payload, file_path_to_test)
        self.assertIsInstance(result['file_body'].payload, bytes)
        self.assertEqual(result['file_body'].payload, expected_image_content)
