from dynamic_model import run_dynamic_model


def run_alpha_sensitivity(
        scenario,
        alphas,
        amplification_cap):

    outputs = {}

    for alpha in alphas:

        outputs[alpha] = run_dynamic_model(
            scenario=scenario,
            alpha=alpha,
            amplification_cap=amplification_cap
        )

    return outputs
