from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from app.models.inputs import DCFInput
from app.services.projections import project_fcff
from app.services.dcf import dcf_valuation
from app.services.sensitivity import sensitivity_matrix
from app.services.comps import run_comps
from app.services.pdf_report import generate_valuation_pdf


import uuid
import os

# =========================
# APP INITIALIZATION
# =========================

app = FastAPI(title="ValuEdge Pro")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =========================
# HEALTH CHECK
# =========================

@app.get("/")
def health():
    return {"status": "Backend running"}

# =========================
# DCF VALUATION
# =========================

@app.post("/valuation/dcf")
def run_dcf(data: DCFInput):
    fcffs = project_fcff(data)
    valuation = dcf_valuation(fcffs, data.wacc, data.terminal_growth)

    return {
        "fcffs": fcffs,
        "valuation": valuation
    }

# =========================
# SENSITIVITY ANALYSIS
# =========================

@app.post("/valuation/sensitivity")
def run_sensitivity(data: DCFInput):
    fcffs = project_fcff(data)

    return sensitivity_matrix(
        fcffs,
        data.wacc,
        data.terminal_growth,
        net_debt=getattr(data, "net_debt", 0.0)
    )

# =========================
# COMPARABLE COMPANY ANALYSIS
# =========================

@app.post("/valuation/comps")
def comps_endpoint(payload: dict):
    try:
        peers = payload.get("peers", [])
        metric_value = float(payload.get("metric_value", 0))
        net_debt = float(payload.get("net_debt", 0))
        shares_outstanding = float(payload.get("shares_outstanding", 1))

        if not peers:
            raise ValueError("Peers list is empty")

        return run_comps(
            peers=peers,
            metric_value=metric_value,
            net_debt=net_debt,
            shares_outstanding=shares_outstanding,
        )

    except Exception as e:
        print("COMPS ERROR:", e)
        raise HTTPException(status_code=500, detail=str(e))

# =========================
# PDF EXPORT
# =========================

@app.post("/export/pdf")
def export_pdf(payload: dict):
    file_name = f"valuation_{uuid.uuid4().hex}.pdf"
    file_path = f"/tmp/{file_name}"

    generate_valuation_pdf(payload, file_path)

    return FileResponse(
        file_path,
        media_type="application/pdf",
        filename="ValuEdge_Valuation_Report.pdf"
    )

