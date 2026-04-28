import json
from src.ai_engine.arch_logic import AutoArchEngine

def run_use_cases():
    engine = AutoArchEngine()
    
    # Use Case 1: Predictive Diagnostics
    diag = engine.generate_predictive_diag()
    print(f"Generated Diag: {diag['TargetMetric']} focus.")
    
    # Use Case 2: V2X Service
    v2x = engine.generate_v2x_manifest()
    print(f"Generated V2X: {v2x['Service']} with {v2x['LatencyRequirement']} latency.")
    
    with open('output/manifests/use_cases.json', 'w') as f:
        json.dump([diag, v2x], f, indent=4)

if __name__ == "__main__":
    run_use_cases()
