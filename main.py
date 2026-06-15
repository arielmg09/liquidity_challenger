from config import ALPHAS
from config import AMPLIFICATION_CAP

from scenarios import idiosyncratic_scenario

from deterministic_model import (
    run_deterministic_model
)

from sensitivity_analysis import (
    run_alpha_sensitivity
)

from reverse_stress_testing import (
    reverse_stress_test
)

from visualisation import (
    plot_deposit_paths
)

# ---------------------------------
# Base deterministic model
# ---------------------------------

deterministic = run_deterministic_model(
    idiosyncratic_scenario
)

# ---------------------------------
# Challenger models
# ---------------------------------

dynamic_results = run_alpha_sensitivity(
    scenario=idiosyncratic_scenario,
    alphas=ALPHAS,
    amplification_cap=AMPLIFICATION_CAP
)

# ---------------------------------
# Charts
# ---------------------------------

plot_deposit_paths(
    deterministic,
    dynamic_results
)

# ---------------------------------
# Reverse stress testing
# ---------------------------------

alpha_breakpoint = reverse_stress_test(
    scenario=idiosyncratic_scenario,
    threshold=500,
    amplification_cap=AMPLIFICATION_CAP
)

print(
    f"Critical alpha: {alpha_breakpoint}"
)
