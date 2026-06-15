from dynamic_model import run_dynamic_model


def reverse_stress_test(
        scenario,
        threshold,
        amplification_cap):

    alpha = 0.0

    while alpha <= 10:

        results = run_dynamic_model(
            scenario,
            alpha,
            amplification_cap
        )

        final_balance = (
            results.iloc[-1]
            ["Remaining_Deposits"]
        )

        if final_balance < threshold:

            return alpha

        alpha += 0.1

    return None
