# ValuEdge Pro – Backend

FastAPI-powered valuation engine supporting:
- Discounted Cash Flow (DCF)
- Sensitivity Analysis
- Comparable Company Analysis
- PDF valuation reports

## Tech Stack
- FastAPI
- Pydantic
- NumPy / Pandas
- Uvicorn
- Render (deployment)

## Live API
https://valuedge-backend-1.onrender.com

## Key Endpoints
- POST /valuation/dcf
- POST /valuation/sensitivity
- POST /valuation/comps
- POST /export/pdf

## Run Locally
```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
