import unittest
from src.ai_engine.arch_logic import AutoArchEngine

class TestAutoArch(unittest.TestCase):
    def setUp(self):
        self.engine = AutoArchEngine()

    def test_safety_injection(self):
        manifest = self.engine.generate_manifest("Steering")
        self.assertEqual(manifest["ServiceInstance"]["ASIL"], "D")

    def test_validation_logic(self):
        invalid_manifest = {"ServiceInstance": {"Name": "Test"}}
        is_safe, msg = self.engine.validate_safety(invalid_manifest)
        self.assertFalse(is_safe)

if __name__ == "__main__":
    unittest.main()
