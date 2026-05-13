#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Bootstrap utility analysis for model performance evaluation.
"""
from typing import Any
import numpy as np
import numpy.typing as npt
import pandas as pd

def bootstrapped_utility(
    df_testing: pd.DataFrame, 
    varname: str, 
    bins: Any
) -> npt.NDArray[np.float64]:
    """
    Calculate the expected utility across different bins using a bootstrapped sample.
    
    Args:
        df_testing: The testing DataFrame containing the predictions/scores and the 'is_good' label.
        varname: The name of the variable to bin (usually the score or probability).
        bins: The number of bins or an array of bin edges to use.
        
    Returns:
        An array representing the cumulative utility function across the bins.
    """
    if df_testing is None or varname is None or bins is None:
        raise ValueError("df_testing, varname, and bins must be provided.")

    # Business Constants
    N: int = 1500
    MKT: int = 500000
    S_bin: int = 6000
    L_bin: int = 3000
    IT_bin: float = 0.20
    IP_bin: float = 0.40
    
    df_bs: pd.DataFrame = df_testing.sample(frac=1.0, replace=True)
    df_bs_good: pd.DataFrame = df_bs[df_bs['is_good'] == 1]
    df_bs_bad: pd.DataFrame = df_bs[df_bs['is_good'] != 1]
    
    hbs_good: pd.Series = pd.cut(df_bs_good[varname], bins=bins)
    hbs_bad: pd.Series = pd.cut(df_bs_bad[varname], bins=bins)
    
    hbs_good_counts = hbs_good.value_counts()
    hbs_bad_counts = hbs_bad.value_counts()
    
    bs_purity_by_bin: list[float] = []
    bs_efficiency_by_bin: list[float] = []
    
    total_good_size = len(hbs_good)
    total_bad_size = len(hbs_bad)
    total_size = total_good_size + total_bad_size
    
    for g in range(len(hbs_good_counts)):
        good_count = hbs_good_counts.iloc[g]
        bad_count = hbs_bad_counts.iloc[g]
        sum_g_b = good_count + bad_count
        
        if sum_g_b != 0:
            bs_purity_by_bin.append(1.0 * good_count / sum_g_b)
        else:
            bs_purity_by_bin.append(1.0 * good_count)
            
        bs_efficiency_by_bin.append(1.0 * sum_g_b / total_size)
        
    purity_array: npt.NDArray[np.float64] = np.array(bs_purity_by_bin)
    efficiency_array: npt.NDArray[np.float64] = np.array(bs_efficiency_by_bin)
    
    # -1 * (purity - 1.0) is mathematically equal to (1.0 - purity)
    bs_default_by_bin: npt.NDArray[np.float64] = 1.0 - purity_array
    
    bs_DC_bin = N * efficiency_array * bs_default_by_bin * L_bin
    bs_RT_bin = N * efficiency_array * purity_array * S_bin * IT_bin
    bs_RP_bin = N * efficiency_array * bs_default_by_bin * (S_bin - L_bin) * IP_bin
    
    bs_f_bin = bs_RT_bin + bs_RP_bin - bs_DC_bin
    
    # Calculate reverse cumulative sum and subtract MKT
    bs_f: npt.NDArray[np.float64] = np.cumsum(bs_f_bin[::-1])[::-1] - MKT
    
    return bs_f
