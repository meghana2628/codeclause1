import unittest
from src.vision.object_detection import ObjectDetector

class TestObjectDetection(unittest.TestCase):

    def setUp(self):
        self.detector = ObjectDetector()
        self.detector.load_model('path/to/model')

    def test_detect_objects(self):
        test_image = 'path/to/test/image.jpg'
        detected_objects = self.detector.detect_objects(test_image)
        self.assertIsInstance(detected_objects, list)
        self.assertGreater(len(detected_objects), 0)

    def test_load_model(self):
        model_path = 'path/to/model'
        self.detector.load_model(model_path)
        self.assertTrue(self.detector.model is not None)

if __name__ == '__main__':
    unittest.main()