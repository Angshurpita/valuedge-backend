from pydantic import BaseModel, Field

class DCFInput(BaseModel):
    revenue: float = Field(..., gt=0, description="Last year revenue")
    revenue_growth: float = Field(..., description="Annual growth rate")
    ebitda_margin: float = Field(..., description="EBITDA margin")
    tax_rate: float = Field(..., description="Corporate tax rate")
    capex_percent: float = Field(..., description="CapEx as % of revenue")
    wc_percent: float = Field(..., description="Working capital as % of revenue")
    wacc: float = Field(..., description="Weighted average cost of capital")
    terminal_growth: float = Field(..., description="Terminal growth rate")
    years: int = Field(5, description="Projection years")

