import json
import os

class AUTOSAR_AI_Engine:
    def __init__(self):
        self.knowledge_base = {
            "PHM": "Platform Health Management is required for ASIL-D.",
            "SOMEIP": "SOME/IP requires a Service ID and Instance ID.",
            "DOIP": "Diagnostics over IP requires a valid logical address."
        }

    def analyze_requirement(self, file_path):
        """Mock RAG: Reads a file and 'retrieves' relevant safety standards."""
        if not os.path.exists(file_path):
            return {"error": "Source file not found."}
            
        with open(file_path, 'r') as f:
            content = f.read().upper()
            
        findings = []
        for key, value in self.knowledge_base.items():
            if key in content:
                findings.append(value)
        
        return {
            "file": file_path,
            "detected_components": [k for k in self.knowledge_base.keys() if k in content],
            "recommendations": findings
        }

if __name__ == "__main__":
    engine = AUTOSAR_AI_Engine()
    # Create a dummy requirement file to process
    with open('input_req.txt', 'w') as f:
        f.write("Need a SOMEIP service with PHM support.")
    
    report = engine.analyze_requirement('input_req.txt')
    print(json.dumps(report, indent=4))
    with open('output/analysis_report.json', 'w') as f:
        json.dump(report, f, indent=4)
