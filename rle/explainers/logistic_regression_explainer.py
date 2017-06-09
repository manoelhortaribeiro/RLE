from rle.explainers.explainer import Explainer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics.pairwise import pairwise_distances
import numpy as np


class LogisticRegressionExplainer(Explainer):
    """
    This is the abstract class that needs to be extended to implement the explainers for different models.
    """

    def __init__(self,
                 sampler,
                 measure,
                 verbose=False):
        """
        :param sampler: defined@Explainer
        :param measure: defined@Explainer
        :param verbose: defined@Explainer
        :return defined@Explainer
        """

        self.model = LogisticRegression()

        super().__init__(sampler, measure, verbose)

    def explain(self, decision, measure=None):

        ms = measure if measure is not None else self.measure

        sample_f, sample_l = self.sampler.sample()

        distances = pairwise_distances(sample_f, decision.reshape(1, -1), metric='euclidean').ravel()
        exponential_distances = np.sqrt(np.exp(-(distances ** 2) / ms ** 2))
        self.model.fit(sample_f, sample_l, exponential_distances)


