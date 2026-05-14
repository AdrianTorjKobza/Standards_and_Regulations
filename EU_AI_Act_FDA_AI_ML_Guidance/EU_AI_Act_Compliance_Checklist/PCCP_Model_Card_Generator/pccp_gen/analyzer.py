# Using Fairlearn to generate the "Slicing Analysis" required for regulatory transparency.

import pandas as pd
from fairlearn.metrics import MetricFrame, selection_rate, count
from sklearn.metrics import accuracy_score, recall_score
import matplotlib.pyplot as plt
import seaborn as sns
import io

class ModelAnalyzer:
    @staticmethod
    def perform_slicing(y_true, y_pred, sensitive_features):
        metrics = {
            'accuracy': accuracy_score,
            'recall': recall_score,
            'selection_rate': selection_rate,
            'count': count
        }
        
        mf = MetricFrame(metrics=metrics,
                         y_true=y_true,
                         y_pred=y_pred,
                         sensitive_features=sensitive_features)
        
        return mf.by_group

    @staticmethod
    def generate_plots(y_true, y_pred):
        # Generate a Confusion Matrix plot as a buffer.
        from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
        
        fig, ax = plt.subplots(figsize=(5, 4))
        cm = confusion_matrix(y_true, y_pred)
        disp = ConfusionMatrixDisplay(confusion_matrix=cm)
        disp.plot(ax=ax, cmap='Blues')
        
        buf = io.BytesIO()
        plt.savefig(buf, format='png', bbox_inches='tight')
        buf.seek(0)
        plt.close(fig)

        return buf