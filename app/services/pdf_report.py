from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4

def generate_valuation_pdf(data, file_path):
    styles = getSampleStyleSheet()
    doc = SimpleDocTemplate(file_path, pagesize=A4)
    elements = []

    elements.append(Paragraph("<b>ValuEdge Pro – Valuation Summary</b>", styles["Title"]))
    elements.append(Spacer(1, 12))

    # DCF
    dcf = data["dcf"]
    elements.append(Paragraph("<b>DCF Valuation</b>", styles["Heading2"]))
    elements.append(Paragraph(f"Enterprise Value: ${dcf['enterprise_value']}M", styles["Normal"]))
    elements.append(Paragraph(f"Equity Value: ${dcf['equity_value']}M", styles["Normal"]))
    elements.append(Paragraph(f"Implied Share Price: ${dcf['share_price']}", styles["Normal"]))
    elements.append(Spacer(1, 12))

    # COMPS
    comps = data["comps"]
    elements.append(Paragraph("<b>Comparable Company Analysis</b>", styles["Heading2"]))
    table = Table([
        ["Metric", "Min", "Median", "Max"],
        ["Enterprise Value ($M)", comps["ev_min"], comps["ev_median"], comps["ev_max"]],
        ["Share Price ($)", comps["px_min"], comps["px_median"], comps["px_max"]],
    ])
    elements.append(table)

    doc.build(elements)

