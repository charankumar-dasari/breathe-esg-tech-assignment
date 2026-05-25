# Tradeoffs

This document explains important features intentionally not implemented in the prototype.

---

# 1. Real Enterprise Integrations

Not Implemented:
- SAP OData integrations
- Concur APIs
- Utility provider APIs
- OAuth authentication flows

Reason:
These integrations require significant setup, credentials, enterprise access, and large implementation effort.

Instead, CSV ingestion was selected to realistically simulate enterprise onboarding workflows.

---

# 2. Advanced Authentication and RBAC

Not Implemented:
- JWT authentication
- Role-based access control
- Organization-level permissions
- Multi-user session management

Reason:
The assignment primarily focused on ingestion, normalization, and analyst workflows.

Simple prototype architecture was prioritized over authentication complexity.

---

# 3. Advanced Analytics and Emission Calculations

Not Implemented:
- Dynamic emission factor databases
- Real-world emissions libraries
- Scope 1/2/3 calculation engines
- Historical trend analytics
- AI anomaly detection

Reason:
The prototype focuses on ingestion and review workflows rather than complete carbon accounting systems.

Simple CO2e calculation logic was used to demonstrate normalization flow.

---

# 4. File Parsing Complexity

Not Implemented:
- PDF utility bill OCR
- SAP IDoc parsing
- XML transformation pipelines
- Unstructured document extraction

Reason:
These features require substantial parsing infrastructure and increase development complexity significantly.

CSV-based ingestion provided a simpler and more stable prototype path.

---

# 5. Production Infrastructure

Not Implemented:
- Docker containers
- Kubernetes deployment
- CI/CD pipelines
- Redis queues
- Celery background jobs

Reason:
The goal was rapid prototype delivery within limited time constraints.

The focus remained on correctness and explainability instead of infrastructure maturity.

---

# 6. Full Multi-Tenancy

Not Fully Implemented:
- Tenant-specific databases
- Data isolation policies
- Company-level dashboards

Reason:
The architecture was designed with future tenant support in mind, but complete tenant separation was outside prototype scope.