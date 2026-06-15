import pandas as pd

from config import BALANCES
from config import HORIZON_WEEKS


def run_dynamic_model(
        scenario,
        alpha,
        amplification_cap):

    balances = BALANCES.copy()

    initial_floating = (
        balances["Retail_Floating"]
        + balances["Wholesale_Floating"]
    )

    results = []

    for week in range(1, HORIZON_WEEKS + 1):

        current_balance = (
            balances["Retail_Floating"]
            + balances["Wholesale_Floating"]
        )

        cumulative_outflow_ratio = (
            initial_floating
            - current_balance
        ) / initial_floating

        amplification = (
            1
            + alpha * cumulative_outflow_ratio
        )

        amplification = min(
            amplification,
            amplification_cap
        )

        runoff = scenario(week)

        retail_runoff = (
            runoff["Retail_Floating"]
            * amplification
        )

        wholesale_runoff = (
            runoff["Wholesale_Floating"]
            * amplification
        )

        retail_outflow = (
            balances["Retail_Floating"]
            * retail_runoff
        )

        wholesale_outflow = (
            balances["Wholesale_Floating"]
            * wholesale_runoff
        )

        balances["Retail_Floating"] -= retail_outflow
        balances["Wholesale_Floating"] -= wholesale_outflow

        results.append({
            "Week": week,
            "Remaining_Deposits":
                balances["Retail_Floating"]
                + balances["Wholesale_Floating"],
            "Amplification": amplification
        })

    return pd.DataFrame(results)
