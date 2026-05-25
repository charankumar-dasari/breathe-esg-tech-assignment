# Sources and Research Notes

This document explains the real-world source formats researched during implementation.

---

# 1. SAP Fuel and Procurement Data

## Research

Typical SAP integrations commonly expose data through:
- CSV exports
- Flat files
- IDocs
- OData APIs
- BAPIs

For this prototype, CSV export format was selected.

---

## Why CSV?

Enterprise onboarding often starts with manual exports before direct integrations are implemented.

CSV files are:
- easy to exchange
- easy to validate
- commonly used during onboarding phases

---

## Prototype Sample Structure

Example fields:
- Plant Code
- Fuel Type
- Quantity
- Unit
- Date

The prototype simplified SAP complexity while preserving realistic ingestion behavior.

---

## Real-World Challenges

Potential production issues:
- inconsistent units
- multilingual column names
- invalid dates
- missing lookup mappings
- duplicate exports

These were acknowledged but not fully implemented due to prototype scope.

---

# 2. Utility Electricity Data

## Research

Facilities teams commonly obtain electricity data through:
- utility portal CSV exports
- PDF bills
- utility APIs

CSV export was selected for implementation.

---

## Prototype Sample Structure

Example fields:
- Meter ID
- Billing Period
- Electricity Consumption
- Unit
- Tariff

---

## Real-World Challenges

Potential production issues:
- billing periods not matching calendar months
- inconsistent tariffs
- estimated meter readings
- multiple units
- missing meter identifiers

The prototype simplified validation logic while supporting suspicious record detection.

---

# 3. Corporate Travel Data

## Research

Corporate travel systems such as:
- Concur
- Navan
- TravelPerk

typically expose:
- flight bookings
- hotel bookings
- ground transportation
- airport codes
- travel distances

---

## Prototype Sample Structure

Example fields:
- Employee
- Travel Type
- Distance
- Unit

---

## Real-World Challenges

Potential production issues:
- missing distance data
- incomplete airport codes
- duplicate bookings
- inconsistent travel categories

The prototype simplified normalization while demonstrating ingestion workflow concepts.

---

# Overall Research Goal

The focus of research was to:
- understand realistic enterprise data formats
- design ingestion flows based on practical onboarding scenarios
- avoid unrealistic toy data structures

The implementation intentionally prioritizes:
- explainability
- normalization
- review workflow
- auditability