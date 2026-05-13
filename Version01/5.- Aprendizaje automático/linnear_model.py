#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Linear Regression model implementation for credit scoring.
"""
from typing import Optional, Dict
import numpy as np
import numpy.typing as npt
import pandas as pd

class LinnearModel:
    """
    A custom Multiple Linear Regression model calculated via the normal equation.
    (Named 'LinnearModel' to preserve original spelling/import compatibility).
    """

    def __init__(self, varnames: Optional[list[str]] = None, data_path: str = 'data/german.data.all-numeric.csv') -> None:
        """
        Initialize the LinearModel with specified variables and load the dataset.

        Args:
            varnames: A list of feature variable names to include in the model.
            data_path: Path to the CSV dataset. Defaults to 'data/german.data.all-numeric.csv'.
        """
        if varnames is None:
            varnames = []
        else:
            varnames = varnames.copy()

        self.df: pd.DataFrame = pd.read_csv(data_path, header=0)
        
        varnames.append("is_good")
        self.df = self.df[varnames]
        
        # Transform label representation
        self.df['is_good'] = 2.0 - self.df['is_good']
        
        self.df_training: pd.DataFrame = self.df.sample(frac=0.7, replace=False, random_state=1)
        self.df_training['ones'] = 1.0
        
        # Preserve original logic for ordering the variables list
        varnames = varnames[::-1]
        varnames.append('ones')
        self.varnames: list[str] = varnames[::-1]
        
        self.df_good: pd.DataFrame = self.df_training[self.df_training['is_good'] == 1]
        self.df_bad: pd.DataFrame = self.df_training[self.df_training['is_good'] != 1]
        
        self.betas: npt.NDArray[np.float64] = np.array([])

    def train(self) -> None:
        """
        Train the model using the normal equation to find the optimal beta coefficients.
        Populates self.betas.
        """
        feature_cols = [var for var in self.varnames if var != 'is_good']
        
        # Extract features and target as numpy arrays
        X = self.df_training[feature_cols].values
        y = self.df_training['is_good'].values
        
        # Calculate X^T * X and X^T * y
        xtx = X.T.dot(X)
        xty = X.T.dot(y)
        
        # Compute betas: (X^T * X)^-1 * X^T * y
        invxtx = np.linalg.inv(xtx)
        self.betas = invxtx.dot(xty)

    def score(self, features: Optional[Dict[str, float]] = None) -> float:
        """
        Calculate the predicted score for a set of feature values.

        Args:
            features: A dictionary mapping feature names to their values.

        Returns:
            The predicted continuous score.
        """
        if features is None:
            features = {}
            
        values: list[float] = [1.0]
        for var in self.varnames:
            if var in ('ones', 'is_good'):
                continue
            values.append(float(features.get(var, 0.0)))
            
        score_val = float(np.sum(self.betas * np.array(values)))
        return score_val


if __name__ == "__main__":
    _varnames = [
        'amount', 'savings_acc_numeric', 'p_employment_time_numeric', 
        'installment_rate', 'p_residence_time', 'age', 'number_of_credits', 
        'dependants', 'has_phone_numeric', 'foreign_worker_numeric'
    ]
    
    lm = LinnearModel(varnames=_varnames)
    lm.train()
    
    _features = {
        'amount': 1000.0, 
        'savings_acc_numeric': 1.0, 
        'p_employment_time_numeric': 3.0, 
        'installment_rate': 4.0,
        'p_residence_time': 3.0, 
        'age': 36.0, 
        'number_of_credits': 2.0, 
        'dependants': 1.0, 
        'has_phone_numeric': 1.0,
        'foreign_worker_numeric': 0.0
    }
    
    _score = lm.score(_features)
    print(_score)
