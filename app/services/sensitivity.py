import numpy as np
from app.services.dcf import dcf_valuation


def sensitivity_matrix(fcffs, base_wacc, base_g,
                       wacc_range=0.02, g_range=0.01, steps=5):
    wacc_values = np.linspace(
        base_wacc - wacc_range,
        base_wacc + wacc_range,
        steps
    )

    g_values = np.linspace(
        base_g - g_range,
        base_g + g_range,
        steps
    )

    matrix = []

    for g in g_values:
        row = []
        for wacc in wacc_values:
            if wacc <= g:
                row.append(None)
            else:
                ev = dcf_valuation(fcffs, wacc, g)["enterprise_value"]
                row.append(ev)
        matrix.append(row)

    return {
        "wacc_values": wacc_values.tolist(),
        "terminal_growth_values": g_values.tolist(),
        "enterprise_value_matrix": matrix
    }

def sensitivity_matrix(fcffs, base_wacc, base_g,
                       wacc_range=0.02, g_range=0.01, steps=5, net_debt=0.0):
    wacc_values = np.linspace(base_wacc - wacc_range, base_wacc + wacc_range, steps)
    g_values = np.linspace(base_g - g_range, base_g + g_range, steps)

    ev_matrix = []
    eq_matrix = []

    for g in g_values:
        ev_row, eq_row = [], []
        for wacc in wacc_values:
            if wacc <= g:
                ev_row.append(None)
                eq_row.append(None)
            else:
                ev = dcf_valuation(fcffs, wacc, g)["enterprise_value"]
                ev_row.append(ev)
                eq_row.append(ev - net_debt)
        ev_matrix.append(ev_row)
        eq_matrix.append(eq_row)

    return {
        "wacc_values": wacc_values.tolist(),
        "terminal_growth_values": g_values.tolist(),
        "enterprise_value_matrix": ev_matrix,
        "equity_value_matrix": eq_matrix
    }
