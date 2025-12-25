def project_fcff(inputs):
    revenue = inputs.revenue
    fcffs = []

    for _ in range(inputs.years):
        revenue *= (1 + inputs.revenue_growth)
        ebitda = revenue * inputs.ebitda_margin
        ebit = ebitda
        nopat = ebit * (1 - inputs.tax_rate)

        capex = revenue * inputs.capex_percent
        delta_wc = revenue * inputs.wc_percent

        fcff = nopat - capex - delta_wc
        fcffs.append(round(fcff, 2))

    return fcffs

