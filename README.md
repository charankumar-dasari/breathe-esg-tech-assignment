# ESG Data Ingestion and Analyst Review Platform

## Overview

This project is a prototype ESG ingestion and analyst review platform developed using Django REST Framework and React.

The platform simulates real-world ESG onboarding workflows where enterprise data arrives from multiple systems such as SAP exports, utility electricity reports, and corporate travel platforms.

The application ingests records, normalizes them into a unified structure, detects suspicious values, and provides an analyst dashboard for review and approval before audit workflows.

---

# Key Features

## 1. Multi-Source ESG Data Ingestion

The system supports ingestion from multiple enterprise-style sources:

- SAP fuel and procurement exports
- Utility electricity consumption data
- Corporate travel activity data

The current prototype uses CSV upload simulation to represent realistic enterprise onboarding workflows.

---

## 2. Unified Data Normalization

Incoming records from different systems are normalized into a common ESG structure.

Normalized fields include:
- source type
- activity type
- quantity
- unit
- CO2e value
- workflow status
- suspicious flag

This simplifies:
- analyst review
- filtering
- reporting
- auditing

---

# 3. Analyst Review Dashboard

The React dashboard allows analysts to:

- view all uploaded records
- identify suspicious rows
- approve records
- reject records
- monitor workflow status

Suspicious rows are visually highlighted for easier validation.

---

# 4. Suspicious Record Detection

The prototype includes basic anomaly detection logic.

Current validation rule:
- records with quantity > 10000 are automatically flagged

Flagged rows are highlighted in the dashboard.

This simulates real-world analyst review workflows.

---

# 5. Audit Logging

The system tracks:
- previous status
- updated status
- analyst action
- timestamps

Audit logs provide traceability and support future compliance workflows.

---

# Tech Stack

## Backend
- Django
- Django REST Framework
- SQLite

## Frontend
- React
- Axios
- Vite

---

# System Architecture

```text
CSV Upload
    ↓
Django REST API
    ↓
Data Normalization
    ↓
SQLite Database
    ↓
React Dashboard
    ↓
Analyst Review Workflow
```

---

# API Endpoints

## Get All Records

GET

```bash
/api/records/
```

Returns all normalized ESG records.

---

## Upload ESG CSV File

POST

```bash
/api/upload/
```

Uploads and processes ESG activity records.

---

## Update Record Status

PUT

```bash
/api/records/<id>/status/
```

Updates workflow status:
- APPROVED
- REJECTED

---

# Database Models

## EmissionRecord

Stores normalized ESG activity data.

Key fields:
- source_type
- activity_type
- quantity
- unit
- co2e
- status
- is_flagged
- uploaded_at

---

## AuditLog

Stores analyst workflow history.

Key fields:
- record
- action
- old_status
- new_status
- changed_by
- changed_at

---

# Project Structure

```text
breathe-esg-project/
│
├── backend/
│
├── frontend/
│
├── docs/
│   ├── MODEL.md
│   ├── DECISIONS.md
│   ├── TRADEOFFS.md
│   └── SOURCES.md
│
└── README.md
```

---

# Running Backend

```bash
cd backend
python manage.py runserver
```

Backend runs at:

```text
http://127.0.0.1:8000
```

---

# Running Frontend

```bash
cd frontend
npm install
npm run dev
```

Frontend runs at:

```text
http://localhost:5173
```

---

# Sample CSV Format

```csv
source_type,activity_type,quantity,unit
SAP,Diesel Fuel,500,Liters
UTILITY,Electricity,12000,kWh
TRAVEL,Flight Travel,300,km
```

---

# Design Decisions

The prototype prioritizes:
- simplicity
- explainability
- ingestion workflow clarity
- auditability
- analyst usability

instead of:
- infrastructure complexity
- enterprise-scale integrations
- advanced authentication systems

---

# Tradeoffs

The following features were intentionally not implemented:
- direct SAP integrations
- OAuth authentication
- PDF OCR parsing
- advanced emissions calculations
- tenant isolation
- cloud-scale infrastructure

The goal was to focus on a clean and understandable prototype under limited development time.

---

# Future Improvements

Potential future enhancements:
- PostgreSQL migration
- enterprise authentication
- tenant-based isolation
- real SAP/API integrations
- utility PDF parsing
- AI anomaly detection
- advanced emissions engines
- Docker deployment
- CI/CD pipelines

---

# Author

Charan Kumar Dasari

Tech Intern Assignment Submission
Breathe ESG