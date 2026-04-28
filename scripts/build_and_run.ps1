Write-Host "--- Starting Full Project Build ---" -ForegroundColor Cyan

# Step 1: Run AI Analysis
Write-Host "[1/2] Running AI Architecture Analysis..." -ForegroundColor Yellow
python src/ai_engine/arch_logic.py

# Step 2: Compile C++ Middleware (Requires MinGW or MSVC)
Write-Host "[2/2] Compiling C++ Middleware Service..." -ForegroundColor Yellow
if (Get-Command g++ -ErrorAction SilentlyContinue) {
    g++ src/autosar_templates/middleware_service.cpp -o bin/middleware_service.exe
    Write-Host "Success: Middleware Compiled." -ForegroundColor Green
    Write-Host "Running Middleware Simulation..."
    ./bin/middleware_service.exe
} else {
    Write-Host "Skip: g++ not found. Please install MinGW to compile C++ files." -ForegroundColor Red
}
