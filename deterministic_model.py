import pandas as pd

from config import BALANCES
from config import HORIZON_WEEKS


def run_deterministic_model(scenario):

    balances = BALANCES.copy()

    results = []

    initial_floating = (
        balances["Retail_Floating"]
        + balances["Wholesale_Floating"]
    )

    for week in range(1, HORIZON_WEEKS + 1):

        runoff = scenario(week)

        retail_outflow = (
            balances["Retail_Floating"]
            * runoff["Retail_Floating"]
        )

        wholesale_outflow = (
            balances["Wholesale_Floating"]
            * runoff["Wholesale_Floating"]
        )

        balances["Retail_Floating"] -= retail_outflow
        balances["Wholesale_Floating"] -= wholesale_outflow

        remaining = (
            balances["Retail_Floating"]
            + balances["Wholesale_Floating"]
        )

        results.append({
            "Week": week,
            "Remaining_Deposits": remaining,
            "Amplification": 1.0
        })

    return pd.DataFrame(results)
