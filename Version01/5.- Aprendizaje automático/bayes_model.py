#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bayesian Model for credit scoring based on the German Credit dataset.
"""
from typing import Optional
import pandas as pd
import numpy as np

class BayesModel:
    """
    A Naive Bayes-like model for calculating log-odds scores for credit applications.
    """

    def __init__(self, data_path: str = 'data/german.data.all-numeric.csv') -> None:
        """
        Initialize the BayesModel by loading and splitting the dataset.

        Args:
            data_path: The path to the numeric German Credit dataset.
        """
        self.df: pd.DataFrame = pd.read_csv(data_path, header=0)
        self.df_training: pd.DataFrame = self.df.sample(frac=0.7, replace=False, random_state=1)
        self.df_good: pd.DataFrame = self.df_training[self.df_training['is_good'] == 1]
        self.df_bad: pd.DataFrame = self.df_training[self.df_training['is_good'] != 1]
        self.variables: dict[str, Optional[float]] = {}

    def histogram_cate(self, varname: str, df: pd.DataFrame) -> pd.Series:
        """
        Compute the categorized histogram for discrete numeric variables.

        Args:
            varname: The name of the variable to bin.
            df: The DataFrame containing the variable.

        Returns:
            A pandas Series containing the binned categorical data.
        """
        var_min = df[varname].min()
        var_max = df[varname].max()
        
        # Using built-in range for integer bounds
        var_range = range(int(var_min), int(var_max) + 1, 1)
        hvar = pd.cut(df[varname], bins=var_range, labels=False)
        return hvar

    def histogram_cont(self, varname: str, df: pd.DataFrame, nbins: float = 10.0) -> pd.Series:
        """
        Compute the categorized histogram for continuous variables.

        Args:
            varname: The name of the continuous variable to bin.
            df: The DataFrame containing the variable.
            nbins: The number of bins to use. Defaults to 10.0.

        Returns:
            A pandas Series containing the binned continuous data.
        """
        var_min = df[varname].min()
        var_max = df[varname].max()
        binsize = 1.0 * (var_max - var_min) / nbins
        var_range = np.arange(var_min, var_max + binsize, binsize)
        hvar = pd.cut(df[varname], bins=var_range)
        return hvar

    def score(self, 
              cac: Optional[float] = None,
              crh: Optional[float] = None,
              prp: Optional[float] = None,
              amount: Optional[float] = None,
              pet: Optional[float] = None,
              prt: Optional[float] = None,
              age: Optional[float] = None) -> float:
        """
        Calculate the logarithmic score for a given set of applicant characteristics.

        Args:
            cac: Checking account status (numeric).
            crh: Credit history (numeric).
            prp: Purpose of credit (numeric).
            amount: Credit amount.
            pet: Present employment time (numeric).
            prt: Present residence time.
            age: Age of applicant.

        Returns:
            The computed log-odds score.
        """
        self.variables = {
            'checking_acc_numeric': cac,
            'credit_history_numeric': crh,
            'purpose_numeric': prp,
            'amount': amount,
            'p_employment_time_numeric': pet,
            'p_residence_time': prt,
            'age': age
        }
        
        pxb: float = 1.0
        pxg: float = 1.0
        pgb: float = 1.0 * self.df_good.shape[0] / self.df_bad.shape[0]
        
        for k, v in self.variables.items():
            if "numeric" in k:
                hg = self.histogram_cate(k, self.df_good)
                hb = self.histogram_cate(k, self.df_bad)
            else:
                hg = self.histogram_cont(k, self.df_good)
                hb = self.histogram_cont(k, self.df_bad)
            
            hg_counts = hg.value_counts(normalize=True)
            hb_counts = hb.value_counts(normalize=True)

            val = self.variables[k]
            
            # Check presence in index to safely look up proportions
            if val in hg_counts.index:
                pxg *= hg_counts[val]
            else:
                pxg *= pgb
                
            if val in hb_counts.index:
                pxb *= hb_counts[val]
            else:
                pxb *= 1.0
                
        return float(np.log(pgb * pxg / pxb))
