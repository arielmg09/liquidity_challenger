def idiosyncratic_scenario(week):

    if week <= 2:

        return {
            "Retail_Floating": 0.10,
            "Wholesale_Floating": 0.25
        }

    return {
        "Retail_Floating": 0.03,
        "Wholesale_Floating": 0.10
    }


def market_wide_scenario(week):

    return {
        "Retail_Floating": 0.04,
        "Wholesale_Floating": 0.12
    }


def combined_scenario(week):

    if week <= 2:

        return {
            "Retail_Floating": 0.12,
            "Wholesale_Floating": 0.30
        }

    return {
        "Retail_Floating": 0.05,
        "Wholesale_Floating": 0.15
    }
