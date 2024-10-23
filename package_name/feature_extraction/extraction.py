import pandas as pd
import multiprocessing as mp
from functools import partial

import package_name.feature_extraction.statistical_feature_calculators as statistical_feature_calculators
import package_name.feature_extraction.spectral_feature_calculators as spectral_feature_calculators
import package_name.feature_extraction.time_frequency_feature_calculators as time_frequency_feature_calculators
from package_name.feature_extraction.settings import StatisticalFeatureParams, SpectralFeatureParams, TimeFrequencyFeatureParams
from package_name.utils.extraction_utils import get_calculators, extract_features
from package_name.feature_extraction.data import TimeSeries, SpectralTimeSeries

def calculate_all_features(data, stat_params, spec_params, tf_params, columns=None, signal_name=None, njobs=None):
    """
    Calculates statisctical, spectral, and time frequency features for the
    given dataset.

    Parameters:
    ----------
    data: pandas.DataFrame or array-like
        The dataset to calculate features for.
    stat_params: StatisticalFeatureParams
        Parameters to use in statistical feature extraction.
    spec_params: SpectralFeatureParams
        Parameters to use in spectral feature extraction.
    tf_params: TimeFrequencyFeatureParams
        Parameters to use in time frequency feature extraction.
    columns: list
        Columns to calculate features for or names of the np.array columns.
    signal_name: str
        Name to prepend to the column names.
    njobs: int
        Number of worker processes to use. If None, the number returned by
        os.cpu_count() is used.
    
    Returns:
    -------
    features: pandas.DataFrame
        DataFrame of calculated features.
    """
    stat_features = calculate_statistical_features(data, stat_params, columns=columns, signal_name=signal_name, njobs=njobs)
    spec_features = calculate_spectral_features(data, spec_params, columns=columns, signal_name=signal_name, njobs=njobs)
    tf_features = calculate_time_frequency_features(data, tf_params, columns=columns, signal_name=signal_name, njobs=njobs)
    return pd.concat([stat_features, spec_features, tf_features], axis=1)


def calculate_statistical_features(data, params=None, window_size=None, columns=None, signal_name=None, njobs=None):
    """
    Calculates all statistical features for the given dataset.

    Parameters:
    ----------
    data: pandas.DataFrame or array-like
        The dataset to calculate features for.
    params: StatisticalFeatureParams
        Parameters to use in feature extraction.
    window_size: int
        Window size to use for feature extraction.
    columns: list
        Columns to calculate features for or names of the np.array columns.
    signal_name: str
        Name to prepend to the column names.
    njobs: int
        Number of worker processes to use. If None, the number returned by
        os.cpu_count() is used.

    Returns:
    -------
    features: pandas.DataFrame
        DataFrame of calculated features.
    """
    if params is None:
        params = StatisticalFeatureParams(window_size)

    time_series = TimeSeries(data, columns=columns, name=signal_name)

    features = calculate_ts_features(time_series, "statistical", params, njobs=njobs)
    return features

def calculate_spectral_features(data, params=None, fs=None, columns=None, signal_name=None, njobs=None):
    """
    Calculates all spectral features for the given dataset.

    Parameters:
    ----------
    data: pandas.DataFrame or array-like
        The dataset to calculate features for.
    params: SpectralFeatureParams
        Parameters to use in feature extraction.
    fs: float
        Sampling frequency of the data.
    columns: list
        Columns to calculate features for or names of the np.array columns.
    signal_name: str
        Name to prepend to the column names.
    njobs: int
        Number of worker processes to use. If None, the number returned by
        os.cpu_count() is used.

    Returns:
    -------
    features: pandas.DataFrame
        DataFrame of calculated features.
    """
    if params is None:
        params = SpectralFeatureParams(fs)
    time_series = SpectralTimeSeries(data, columns=columns, name=signal_name, fs=params.fs)
    features = calculate_ts_features(time_series, "spectral", params,  njobs=njobs)
    return features

def calculate_time_frequency_features(data, params=None, window_size=None, columns=None, signal_name=None, njobs=None):
    """
    Calculates all time frequency features for the given dataset.

    Parameters:
    ----------
    data: pandas.DataFrame or array-like
        The dataset to calculate features for.
    params: TimeFrequencyFeatureParams
        Parameters to use in feature extraction.
    window_size: int
        Window size to use for feature extraction.
    columns: list
        Columns to calculate features for or names of the np.array columns.
    signal_name: str
        Name to prepend to the column names.
    njobs: int
        Number of worker processes to use. If None, the number returned by
        os.cpu_count() is used.

    Returns:
    -------
    features: pandas.DataFrame
        DataFrame of calculated features.
    """
    if params is None:
        params = TimeFrequencyFeatureParams(window_size)

    time_series = TimeSeries(data, columns=columns, name=signal_name)
    features = calculate_ts_features(time_series, "time_frequency", params, njobs=njobs)
    return features

def calculate_ts_features(time_series, module, params, njobs=None):
    """
    Calculate features from the given module for the given time series data.

    Parameters:
    ----------
    time_series: TimeSeries
        The time series data to calculate features for.
    module: str
        The module with the feature calculators to use.
    params: BaseFeatureParams
        Parameters to use in feature extraction.
    njobs: int
        Number of worker processes to use. If None, the number returned by
        os.cpu_count() is used.
    
    Returns:
    -------
    features_df: pandas.DataFrame
        DataFrame of calculated features.
    """
    features = []
    index = []

    pool = mp.Pool(njobs)

    param_dict = params.get_settings_as_dict()

    results = pool.imap(partial(extract_features, module=module, param_dict=param_dict), time_series)

    for r in results:
        index.append(r.label)
        features.append(r.features)

    features_df = pd.DataFrame(features, index=index)
    return features_df