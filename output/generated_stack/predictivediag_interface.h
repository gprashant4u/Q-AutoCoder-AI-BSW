
#ifndef PREDICTIVEDIAG_INTERFACE_H
#define PREDICTIVEDIAG_INTERFACE_H

#include <ara/com/com_error_domain.h>

namespace qorix {
namespace predictivediag {
    class PredictiveDiagInterface {
    public:
        virtual ~PredictiveDiagInterface() = default;
        virtual void ReportStatus() = 0;
        virtual void TriggerOptimization() = 0;
    };
}
}
#endif
