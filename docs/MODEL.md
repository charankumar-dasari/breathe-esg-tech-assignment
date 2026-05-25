# Data Model

This document explains the core data model used in the ESG ingestion prototype.

## Overview

The system is designed to ingest ESG-related activity data from multiple sources such as SAP exports, utility electricity reports, and corporate travel systems.

The application normalizes incoming records into a unified structure so analysts can review, validate, and approve emissions data before audit submission.

---

# Core Models

## 1. EmissionRecord

This is the primary model used to store normalized ESG activity data.

### Fields

| Field | Purpose |
|---|---|
| source_type | Identifies the source system (SAP, Utility, Travel) |
| activity_type | Describes the activity |
| quantity | Original activity quantity |
| unit | Unit of measurement |
| co2e | Calculated carbon emission value |
| status | Review workflow status |
| is_flagged | Indicates suspicious or abnormal data |
| uploaded_at | Timestamp of ingestion |

---

## Source Normalization

Different systems expose different formats and structures.

The application normalizes all records into a single structure to simplify:
- Analyst review
- Filtering
- Auditing
- Reporting

Examples:
- SAP fuel exports
- Utility electricity consumption
- Corporate travel activity

All are converted into a common schema.

---

# Workflow Status

Each record follows a review lifecycle.

Possible statuses:
- PENDING
- APPROVED
- REJECTED

This supports analyst verification before audit lock.

---

# Suspicious Record Detection

Records are automatically flagged when abnormal values are detected.

Current prototype logic:
- Quantity values greater than 10000 are marked as suspicious.

Flagged rows are visually highlighted in the dashboard.

---

# Audit Trail

## AuditLog

The AuditLog model stores all status changes performed by analysts.

### Fields

| Field | Purpose |
|---|---|
| record | Related emission record |
| action | Type of action performed |
| old_status | Previous status |
| new_status | Updated status |
| changed_by | User performing action |
| changed_at | Timestamp |

This ensures traceability and review transparency.

---

# Multi-Tenancy Strategy

The prototype is designed to support multi-tenancy in future iterations.

A production implementation would introduce:
- Company model
- Tenant isolation
- Organization-level permissions

Due to time constraints, tenant separation was not fully implemented in this prototype.

---

# Design Goals

The data model was designed to prioritize:
- Simplicity
- Auditability
- Traceability
- Source normalization
- Analyst usability

The goal was to create a clean and understandable ingestion workflow rather than a highly complex architecture.