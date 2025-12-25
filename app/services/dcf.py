def discount(values, rate):
    return [
        round(v / ((1 + rate) ** (i + 1)), 2)
        for i, v in enumerate(values)
    ]


def terminal_value(last_fcf, wacc, g):
    return round((last_fcf * (1 + g)) / (wacc - g), 2)


def dcf_valuation(fcffs, wacc, terminal_growth):
    discounted_fcffs = discount(fcffs, wacc)
    tv = terminal_value(fcffs[-1], wacc, terminal_growth)
    discounted_tv = round(tv / ((1 + wacc) ** len(fcffs)), 2)

    enterprise_value = round(sum(discounted_fcffs) + discounted_tv, 2)

    return {
        "discounted_fcffs": discounted_fcffs,
        "terminal_value": discounted_tv,
        "enterprise_value": enterprise_value
    }


