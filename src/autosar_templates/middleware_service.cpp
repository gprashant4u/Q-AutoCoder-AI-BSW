#include <iostream>
#include <vector>
#include <chrono>
#include <thread>

class AdaptiveMiddleware {
public:
    void MonitorSystemHealth() {
        int cpu_load = 0;
        for(int i = 0; i < 5; ++i) {
            cpu_load = (rand() % 40) + 60; // Simulate high load 60-100%
            std::cout << "[Monitor] Current CPU Load: " << cpu_load << "%" << std::endl;
            
            if (cpu_load > 85) {
                std::cout << "  --> [AI-Trigger] Latency Critical. Throttling Non-Safety Tasks." << std::endl;
            }
            std::this_thread::sleep_for(std::chrono::milliseconds(500));
        }
    }
};

int main() {
    AdaptiveMiddleware bsw;
    bsw.MonitorSystemHealth();
    return 0;
}
