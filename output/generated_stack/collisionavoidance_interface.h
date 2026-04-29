
#ifndef COLLISIONAVOIDANCE_INTERFACE_H
#define COLLISIONAVOIDANCE_INTERFACE_H

#include <ara/com/com_error_domain.h>

namespace qorix {
namespace collisionavoidance {
    class CollisionAvoidanceInterface {
    public:
        virtual ~CollisionAvoidanceInterface() = default;
        virtual void ReportStatus() = 0;
        virtual void TriggerOptimization() = 0;
    };
}
}
#endif
