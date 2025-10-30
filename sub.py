import matplotlib.pyplot as plt
import numpy as np
from scipy.special import gamma
from typing import List, Dict


class MittagLefflerFunction:

    def __init__(self, alpha: float, beta: float, max_terms: int = 200,
                 tolerance: float = 1e-12) -> None:
        self.alpha = alpha
        self.beta = beta
        self.max_terms = max_terms
        self.tolerance = tolerance

    def _calc_term(self, k: int, z: np.ndarray) -> np.ndarray:
        gamma_args = self.alpha * k + self.beta
        gamma_values = gamma(gamma_args)
        term = (z ** k) / gamma_values
        return term

    def evaluate(self, z: np.ndarray) -> np.ndarray:
        E = np.zeros(z.shape)
        converged_mask = np.zeros(z.shape, dtype=bool)

        for k in range(self.max_terms):

            if np.all(converged_mask):
                # print(f"Early stop at k={k}") # debug
                break

            term = self._calc_term(k, z)

            if np.any(np.abs(term) > 1e10):
                break

            E += term

            if k > 0:
                small_term = np.abs(term) < self.tolerance * np.abs(E)

                newly_converged = np.logical_and(small_term, np.abs(E) > 1e-15)
                converged_mask = np.logical_or(converged_mask, newly_converged)

        return E


def plot_mittag_leffler(z_values: np.ndarray, ml_func_list: List[Dict],
                        z_min: float, z_max: float,
                        y_limit: float = 15) -> None:
    """
    A function to plot the graph of multiple Mittag-Leffler function instances
    """
    plt.figure(figsize=(10, 6))

    for item in ml_func_list:
        func_instance = item["instance"]
        label = item["label"]
        style = item["style"]
        color = item.get("color", None)

        E_values = func_instance.evaluate(z_values)

        plt.plot(z_values, E_values, label=label, linestyle=style, color=color)

    # TODO Graph decoration
    plt.title(r'Mittag-Leffler Function $E_{\alpha,\beta}(z)$')
    plt.xlabel(r'$z$')  # LaTeX notation
    plt.ylabel(r'$E_{\alpha,\beta}(z)$')  # LaTeX notation
    plt.axhline(0, color="black", linestyle="-", linewidth=0.5)
    plt.axvline(0, color="black", linestyle="-", linewidth=0.5)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(fontsize=10)
    plt.ylim(-1, y_limit)
    plt.xlim(z_min, z_max)

    plt.show()


Z_MIN, Z_MAX = -5.0, 5.0
Z = np.linspace(Z_MIN, Z_MAX, 500)

ml_exp = MittagLefflerFunction(alpha=1.0, beta=1.0)
ml_half = MittagLefflerFunction(alpha=0.5, beta=1.0)
ml_custom = MittagLefflerFunction(alpha=1.0, beta=0.5)
ml_custom_05 = MittagLefflerFunction(alpha=0.5, beta=0.5)

plot_list = [
    {
        'instance': ml_exp,
        'label': r'$E_{1.0, 1.0}(z) = e^z$',
        'style': '-',
        'color': 'blue'
    },
    {
        'instance': ml_half,
        'label': r'$E_{0.5, 1.0}(z)$',
        'style': '-',
        'color': 'red'
    },
    {
        'instance': ml_custom,
        'label': r'$E_{1.0, 0.5}(z)$',
        'style': '-',
        'color': 'green'
    },
    {
        'instance': ml_custom_05,
        'label': r'$E_{0.5, 0.5}(z)$',
        'style': '-',
        'color': 'purple'
    }
]

plot_mittag_leffler(Z, plot_list, Z_MIN, Z_MAX)