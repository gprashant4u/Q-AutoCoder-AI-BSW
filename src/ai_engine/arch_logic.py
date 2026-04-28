import json
import os

class AutoCoder_Stack_Generator:
    def __init__(self):
        self.output_dir = "output/generated_stack"
        if not os.path.exists(self.output_dir):
            os.makedirs(self.output_dir)

    def generate_service_interface(self, service_name):
        # Generates a functional C++ Header for Adaptive AUTOSAR
        cpp_code = f"""
#ifndef {service_name.upper()}_INTERFACE_H
#define {service_name.upper()}_INTERFACE_H

#include <ara/com/com_error_domain.h>

namespace qorix {{
namespace {service_name.lower()} {{
    class {service_name}Interface {{
    public:
        virtual ~{service_name}Interface() = default;
        virtual void ReportStatus() = 0;
        virtual void TriggerOptimization() = 0;
    }};
}}
}}
#endif
"""
        file_path = os.path.join(self.output_dir, f"{service_name.lower()}_interface.h")
        with open(file_path, 'w') as f:
            f.write(cpp_code)
        return file_path

    def generate_execution_manifest(self, service_name):
        # Generates the JSON Manifest required for deployment
        manifest = {
            "ServiceInstance": service_name,
            "Deployment": "SOME/IP",
            "Port": 30490,
            "Security": "TLS_1.3",
            "ASIL": "D"
        }
        file_path = os.path.join(self.output_dir, f"{service_name.lower()}_manifest.json")
        with open(file_path, 'w') as f:
            json.dump(manifest, f, indent=4)
        return file_path

if __name__ == "__main__":
    gen = AutoCoder_Stack_Generator()
    h_file = gen.generate_service_interface("PredictiveDiag")
    j_file = gen.generate_execution_manifest("PredictiveDiag")
    print(f"Generated Code Stack: \n- {h_file}\n- {j_file}")
