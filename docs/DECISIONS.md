# Engineering Decisions

This document explains the important implementation decisions made during development.

---

# 1. Why Django REST Framework?

Django REST Framework was selected because:
- Rapid API development
- Built-in admin panel
- Strong database integration
- Easy serialization support
- Fast prototyping capability

The assignment emphasized building a working prototype quickly while maintaining understandable architecture.

---

# 2. Why React?

React was selected for:
- Component-based UI structure
- Easy API integration
- Dynamic dashboard rendering
- Frontend scalability

The frontend focuses on analyst usability rather than advanced UI complexity.

---

# 3. Why CSV Uploads Instead of Real APIs?

Real enterprise systems such as SAP and utility platforms often export data as CSV or flat files.

Implementing direct SAP integrations, OAuth flows, or enterprise APIs would significantly increase complexity and development time.

CSV upload was selected because:
- Realistic for enterprise onboarding workflows
- Easy to test
- Faster to prototype
- Suitable for demonstrating ingestion and normalization logic

---

# 4. Why SQLite Instead of PostgreSQL?

SQLite was selected during prototype development to reduce setup complexity and accelerate implementation.

The architecture can easily migrate to PostgreSQL in production because Django ORM abstracts most database operations.

---

# 5. Why Simple Suspicious Detection Logic?

The prototype flags records where:
- quantity > 10000

This simplified rule demonstrates:
- validation workflows
- analyst review requirements
- anomaly detection concepts

In production, suspicious detection would include:
- historical baselines
- emission factor validation
- duplicate detection
- ML-based anomaly scoring

---

# 6. Why Manual Analyst Approval?

The assignment emphasized analyst review before audit lock.

Therefore:
- records remain in PENDING state initially
- analysts manually APPROVE or REJECT rows

This supports governance and auditability.

---

# 7. Why Audit Logging?

Audit logging was implemented because ESG reporting requires traceability.

The system records:
- previous status
- updated status
- action timestamp
- user performing action

This supports future audit and compliance workflows.

---

# 8. Scope Decisions

The prototype intentionally focuses on:
- ingestion
- normalization
- review workflow
- audit tracking

instead of:
- authentication complexity
- real-time sync
- advanced analytics
- cloud-scale infrastructure

The goal was to prioritize clarity and correctness under limited development time.