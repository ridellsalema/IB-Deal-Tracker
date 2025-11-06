# Salema & Salema Investment Banking Deal Tracker

A professional-grade backend system for organizing, analyzing, and displaying global investment banking deals.  
Developed by **Ridell Salema** under **Salema & Salema Software**.

---

## Current Progress
- Folder structure and Express backend ready  
- Mock data for testing and frontend development  

## In-Progress
- SQL Server integration (Windows Authentication) in progress  
- AI summarization and analytics pipeline coming soon  

---

## Tech Stack
- **Backend:** Node.js + Express  
- **Database:** Microsoft SQL Server (to be integrated)  
- **Data:** JSON mock data (temporary)

---

## Sample API Endpoint
| Endpoint | Description |
|----------|-------------|
| `/deals`  | Returns list of investment banking deals (mock data) |

Example Response:
```json
[
  {
    "id": 1,
    "buyer": "Goldman Sachs",
    "target": "Fintech Corp",
    "value": 1250000000,
    "sector": "Technology",
    "description": "Acquisition to expand digital payments and consumer finance reach."
  }
]
