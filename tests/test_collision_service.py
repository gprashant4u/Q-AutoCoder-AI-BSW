import json
import os
import unittest

class TestCollisionAvoidanceStack(unittest.TestCase):
    def setUp(self):
        self.interface_path = "output/generated_stack/collisionavoidance_interface.h"
        self.manifest_path = "output/generated_stack/collisionavoidance_manifest.json"

    def test_interface_exists(self):
        # Validates that the C++ header was actually produced
        self.assertTrue(os.path.exists(self.interface_path), "C++ Interface file missing.")

    def test_asil_compliance(self):
        # Validates that the manifest enforces ASIL-D for Collision Avoidance
        with open(self.manifest_path, 'r') as f:
            data = json.load(f)
        self.assertEqual(data["ASIL"], "D", "Safety Violation: ASIL-D level not found in manifest.")

    def test_service_naming(self):
        # Ensures the namespace follows the Adaptive AUTOSAR standard
        with open(self.interface_path, 'r') as f:
            content = f.read()
        self.assertIn("namespace collisionavoidance", content.lower())

if __name__ == "__main__":
    unittest.main()
