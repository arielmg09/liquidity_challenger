import matplotlib.pyplot as plt


def plot_deposit_paths(
        deterministic,
        dynamic_results):

    plt.figure(figsize=(10, 6))

    plt.plot(
        deterministic["Week"],
        deterministic["Remaining_Deposits"],
        linewidth=3,
        label="Deterministic"
    )

    for alpha, df in dynamic_results.items():

        plt.plot(
            df["Week"],
            df["Remaining_Deposits"],
            label=f"α={alpha}"
        )

    plt.title(
        "Remaining Floating Deposits"
    )

    plt.xlabel("Week")
    plt.ylabel("£m")

    plt.grid(True)

    plt.legend()

    plt.show()
