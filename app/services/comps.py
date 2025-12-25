def run_comps(peers, metric_value, net_debt, shares_outstanding):
    """
    peers: list of dicts with { "name": str, "multiple": float }
    metric_value: EBITDA or Revenue (same unit as EV calc)
    """
    implied_evs = [p["multiple"] * metric_value for p in peers]

    min_ev = min(implied_evs)
    median_ev = sorted(implied_evs)[len(implied_evs)//2]
    max_ev = max(implied_evs)

    def ev_to_price(ev):
        equity = ev - net_debt
        return equity / shares_outstanding

    return {
        "enterprise_value": {
            "min": min_ev,
            "median": median_ev,
            "max": max_ev,
        },
        "implied_price": {
            "min": ev_to_price(min_ev),
            "median": ev_to_price(median_ev),
            "max": ev_to_price(max_ev),
        },
    }

