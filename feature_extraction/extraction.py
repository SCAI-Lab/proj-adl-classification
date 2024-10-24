from feature_extraction.statistical_feature_calculators import *
from feature_extraction.spectral_features_calculators import *
from scipy.signal import welch


def calculate_statistical_features(self, signal, signal_name):
        # A list for storing all the features
        feats = []
        # A list for storing feature names
        feats_names = []

        # Mean of the signal
        feats.extend(calculate_mean(signal))
        feats_names.append(f"{signal_name}_mean")
        # Geometric mean
        feats.extend(calculate_geometric_mean(signal))
        feats_names.append(f"{signal_name}_geometric_mean")
        # Trimmed mean
        trimmed_means = calculate_trimmed_mean(signal, self.trimmed_mean_thresholds)
        feats.extend(trimmed_means)
        for threshold in self.trimmed_mean_thresholds:
            feats_names.append(f"{signal_name}_trimmed_mean_thresh_{str(threshold)}")
        # Mean of the absolute signal
        feats.extend(calculate_mean_abs(signal))
        feats_names.append(f"{signal_name}_mean_of_abs")
        # Geometric mean of the absolute signal
        feats.extend(calculate_geometric_mean_abs(signal))
        feats_names.append(f"{signal_name}_geometric_mean_of_abs")
        # Harmonic mean of the absolute signal
        feats.extend(calculate_harmonic_mean_abs(signal))
        feats_names.append(f"{signal_name}_harmonic_mean_of_abs")
        # Trimmed mean of the absolute signal
        trimmed_mean_abs = calculate_trimmed_mean_abs(signal, self.trimmed_mean_thresholds)
        feats.extend(trimmed_mean_abs)
        for threshold in self.trimmed_mean_thresholds:
            feats_names.append(f"{signal_name}_trimmed_mean_of_abs_thresh_{str(threshold)}")
        # Standard deviation
        feats.extend(calculate_std(signal))
        feats_names.append(f"{signal_name}_std")
        # Standard deviation of the absolute signal
        feats.extend(calculate_std_abs(signal))
        feats_names.append(f"{signal_name}_std_of_abs")
        # Skewness
        feats.extend(calculate_skewness(signal))
        feats_names.append(f"{signal_name}_skewness")
        # Skewness of the absolute signal
        feats.extend(calculate_skewness_abs(signal))
        feats_names.append(f"{signal_name}_skewness_of_abs")
        # Kurtosis
        feats.extend(calculate_kurtosis(signal))
        feats_names.append(f"{signal_name}_kurtosis")
        # Kurtosis of the absolute signal
        feats.extend(calculate_kurtosis_abs(signal))
        feats_names.append(f"{signal_name}_kurtosis_of_abs")
        # Median
        feats.extend(calculate_median(signal))
        feats_names.append(f"{signal_name}_median")
        # Median of the absolute signal
        feats.extend(calculate_median_abs(signal))
        feats_names.append(f"{signal_name}_median_of_abs")
        # Maximum value
        feats.extend(calculate_max(signal))
        feats_names.append(f"{signal_name}_max")
        # Maximum value of the absolute signal
        feats.extend(calculate_max_abs(signal))
        feats_names.append(f"{signal_name}_max_of_abs")
        # Minimum value
        feats.extend(calculate_min(signal))
        feats_names.append(f"{signal_name}_min")
        # Minimum value of the absolute signal
        feats.extend(calculate_min_abs(signal))
        feats_names.append(f"{signal_name}_min_of_abs")
        # Range of the amplitude
        feats.extend(calculate_range(signal))
        feats_names.append(f"{signal_name}_range")
        # Range of the amplitude for the absolute signal
        feats.extend(calculate_range_abs(signal))
        feats_names.append(f"{signal_name}_range_of_abs")
        # Variance
        feats.extend(calculate_variance(signal))
        feats_names.append(f"{signal_name}_var")
        # Variance of the absolute signal
        feats.extend(calculate_variance_abs(signal))
        feats_names.append(f"{signal_name}_var_of_abs")
        # Coefficient of variation
        feats.extend(calculate_coefficient_of_variation(signal))
        feats_names.append(f"{signal_name}_coefficient_of_variation")
        # Inter-quartile range
        feats.extend(calculate_interquartile_range(signal))
        feats_names.append(f"{signal_name}_iqr")
        # Quantiles
        feats.extend(calculate_quantile(signal, self.q))
        for i in (self.q):
            if i == 0.25:
                feats_names.append(f"{signal_name}_first_quartile")
            elif i == 0.75:
                feats_names.append(f"{signal_name}_third_quartile")
            else:
                feats_names.append(f"{signal_name}_quantile_{i}")
        # Mean absolute deviation
        feats.extend(calculate_mean_absolute_deviation(signal))
        feats_names.append(f"{signal_name}_mean_abs_deviation")
        # Root-mean-square
        feats.extend(calculate_root_mean_square(signal))
        feats_names.append(f"{signal_name}_rms")
        # Energy
        feats.extend(calculate_signal_energy(signal))
        feats_names.append(f"{signal_name}_energy")
        # Log of energy
        feats.extend(calculate_log_energy(signal))
        feats_names.append(f"{signal_name}_log_of_energy")
        # Entropy
        feats.extend(calculate_entropy(signal, self.window_size))
        feats_names.append(f"{signal_name}_entropy")
        # Permutation entropy
        feats.extend(calculate_permutation_entropy(signal, self.window_size, self.permutation_entropy_order, self.permutation_entropy_delay))
        feats_names.append(f"{signal_name}_permutation_entropy")
        # Tsallis entropy
        feats.extend(calculate_tsallis_entropy(signal, self.window_size, self.tsallis_q_parameter))
        feats_names.append(f"{signal_name}_tsallis_entropy")
        # Renyi entropy
        feats.extend(calculate_renyi_entropy(signal, self.window_size, self.renyi_alpha_parameter))
        feats_names.append(f"{signal_name}_renyi_entropy")
        # Approximate Entropy
        app_entropy = calculate_approximate_entropy(signal)
        feats.append(app_entropy)
        feats_names.append(f"{signal_name}_approximate_entropy")
        # Differential Entropy
        diff_entropy = calculate_differential_entropy(signal)
        feats.append(diff_entropy)
        feats_names.append(f"{signal_name}_differential_entropy")
        # # Sample Entropy
        samp_ent = calculate_sample_entropy(signal)
        feats.append(samp_ent)
        feats_names.append(f"{signal_name}_sample_entropy")
        # Singular Value Decomposition entropy
        feats.extend(calculate_svd_entropy(signal, self.svd_entropy_order, self.svd_entropy_delay))
        feats_names.append(f"{signal_name}_svd_entropy")
        # Number of zero-crossings
        feats.extend(calculate_zero_crossings(signal))
        feats_names.append(f"{signal_name}_no._of_zero_crossings")
        # Crest factor
        feats.extend(calculate_crest_factor(signal))
        feats_names.append(f"{signal_name}_crest_factor")
        # Clearance factor
        feats.extend(calculate_clearance_factor(signal))
        feats_names.append(f"{signal_name}_clearance_factor")
        # Shape factor
        feats.extend(calculate_shape_factor(signal))
        feats_names.append(f"{signal_name}_shape_factor")
        # Number of mean-crossings
        feats.append(calculate_mean_crossing(signal))
        feats_names.append(f"{signal_name}_no._of_mean_crossings")
        # Impulse factor
        feats.extend(calculate_impulse_factor(signal))
        feats_names.append(f"{signal_name}_impulse_factor")
        # Auto-correlation
        feats.extend(calculate_mean_auto_correlation(signal, self.n_lags_auto_correlation))
        feats_names.append(f"{signal_name}_mean_of_auto_corr_lag_1_to_{self.n_lags_auto_correlation}")
        # High-order moments
        feats.extend(calculate_higher_order_moments(signal, self.moment_orders))
        for order in self.moment_orders:
            feats_names.append(f"{signal_name}_moment_order_{order}")
        # Median absolute deviation
        feats.extend(calculate_median_absolute_deviation(signal, self.adjusted))
        feats_names.append(f"{signal_name}_median_abs_deviation")
        # # Magnitude area
        # feats.extend(calculate_signal_magnitude_area(signal))
        # feats_names.append(f"{signal_name}_magnitude-area")
        # Average amplitude change
        feats.extend(calculate_avg_amplitude_change(signal))
        feats_names.append(f"{signal_name}_avg_amplitude_change")
        # Number of slope sign changes
        feats.extend(calculate_slope_sign_change(signal, self.ssc_threshold))
        feats_names.append(f"{signal_name}_no._of_slope_sign_changes")
        # Higuchi Fractal Dimensions
        feats.extend(calculate_higuchi_fractal_dimensions(signal, self.higuchi_k_values))
        for k in self.higuchi_k_values:
            feats_names.append(f"{signal_name}_higuchi_fractal_dimensions_k={k}")
            
        # Katz Fractal Dimension
        katz_fd = calculate_katz_fractal_dimension(signal)
        feats.append(katz_fd)
        feats_names.append(f"{signal_name}_katz_fractal_dimension")
        
        # Petrosian Fractal Dimension
        pfd = calculate_petrosian_fractal_dimension(signal)
        feats.append(pfd)
        feats_names.append(f"{signal_name}_petrosian_fractal_dimension")

        # Hjorth parameters
        feats.extend(calculate_hjorth_mobility_and_complexity(signal))
        feats_names.append(f"{signal_name}_hjorth_mobility")
        feats_names.append(f"{signal_name}_hjorth_complexity")
        
        # Cardinality
        feats.extend(calculate_cardinality(signal, self.window_size))
        feats_names.append(f"{signal_name}_cardinality")
        
        # RMS to mean absolute ratio
        feats.extend(calculate_rms_to_mean_abs(signal))
        feats_names.append(f"{signal_name}_rms_to_mean_of_abs")

        # Area Under the Curve
        area = calculate_area_under_curve(signal)
        feats.append(area)
        feats_names.append(f"{signal_name}_area_under_curve")

        # Area Under the Squared Curve
        area_squared = calculate_area_under_squared_curve(signal)
        feats.append(area_squared)
        feats_names.append(f"{signal_name}_area_under_squared_curve")

        # Autoregressive Model Coefficients
        ar_coeffs = calculate_autoregressive_model_coefficients(signal, self.ar_model_coefficients_order)
        for i, coeff in enumerate(ar_coeffs):
            feats.append(coeff)
            feats_names.append(f"{signal_name}_ar_coefficient_{i+1}")

        # Count
        count = calculate_count(signal)
        feats.append(count)
        feats_names.append(f"{signal_name}_count")

        # Count Above Mean
        count_above_mean = calculate_count_above_mean(signal)
        feats.append(count_above_mean)
        feats_names.append(f"{signal_name}_count_above_mean")

        # Count Below Mean
        count_below_mean = calculate_count_below_mean(signal)
        feats.append(count_below_mean)
        feats_names.append(f"{signal_name}_count_below_mean")

        # Count of Negative Values
        count_of_negative_values = calculate_count_below(signal, self.count_below_or_above_x)
        feats.append(count_of_negative_values)
        feats_names.append(f"{signal_name}_count_below_{self.count_below_or_above_x}")

        # Count of Positive Values
        count_pos = calculate_count_above(signal, self.count_below_or_above_x)
        feats.append(count_pos)
        feats_names.append(f"{signal_name}_count_above_{self.count_below_or_above_x}")

        # Covariance with a shifted version of the signal (for demonstration)
        cov = calculate_covariance(signal, np.roll(signal, 1))
        feats.append(cov)
        feats_names.append(f"{signal_name}_covariance")

        # Cumulative Sum
        cum_sum = calculate_cumulative_sum(signal)
        feats.append(cum_sum)
        feats_names.append(f"{signal_name}_cumulative_sum")

        # Energy Ratio by Chunks
        energy_ratio = calculate_energy_ratio_by_chunks(signal, self.energy_ratio_chunks)
        for i, ratio in enumerate(energy_ratio):
            feats.append(ratio)
            feats_names.append(f"{signal_name}_energy_ratio_chunk_{i+1}")

        # Moving Average
        moving_average = calculate_moving_average(signal, self.window_size, self.mode)  # Example window size
        feats.append(moving_average)
        feats_names.append(f"{signal_name}_moving_average")
        
        # Weighted Moving Average
        weighted_ma = calculate_weighted_moving_average(signal, self.weights, self.mode)
        feats.append(weighted_ma[-1])  # Assuming last value of WMA is of interest
        feats_names.append(f"{signal_name}_weighted_moving_average")
        
        # Exponential Moving Average
        ema = calculate_exponential_moving_average(signal, self.ema_alpha)
        feats.append(ema)
        feats_names.append(f"{signal_name}_exponential_moving_average")

        # First Location of Maximum
        first_max = calculate_first_location_of_maximum(signal)
        feats.append(first_max)
        feats_names.append(f"{signal_name}_first_location_of_maximum")

        # First Location of Minimum
        first_min = calculate_first_location_of_minimum(signal)
        feats.append(first_min)
        feats_names.append(f"{signal_name}_first_location_of_minimum")

        # First Order Difference
        first_diff = calculate_first_order_difference(signal)
        feats.append(first_diff[-1])  # Assuming we want the last first order difference
        feats_names.append(f"{signal_name}_first_order_difference")

        # Fisher Information
        fisher_info = calculate_fisher_information(signal)
        feats.append(fisher_info)
        feats_names.append(f"{signal_name}_fisher_information")

        # Histogram Bin Frequencies
        hist_bins = calculate_histogram_bin_frequencies(signal, self.hist_bins)
        for i, bin_count in enumerate(hist_bins):
            feats.append(bin_count)
            feats_names.append(f"{signal_name}_histogram_bin_{i}")

        # Last Location of Maximum
        last_max = calculate_last_location_of_maximum(signal)
        feats.append(last_max)
        feats_names.append(f"{signal_name}_last_location_of_maximum")

        # Last Location of Minimum
        last_min = calculate_last_location_of_minimum(signal)
        feats.append(last_min)
        feats_names.append(f"{signal_name}_last_location_of_minimum")

        # Linear Trend with Full Linear Regression Results
        lin_trend_results = calculate_linear_trend_with_full_linear_regression_results(signal)
        feats.extend(lin_trend_results)
        feats_names.extend([f"{signal_name}_slope", f"{signal_name}_intercept", f"{signal_name}_r_squared", f"{signal_name}_p_value", f"{signal_name}_std_err"])

        # Local Maxima and Minima
        num_maxima, num_minima = calculate_local_maxima_and_minima(signal)
        feats.append(num_maxima)
        feats_names.append(f"{signal_name}_local_maxima")
        feats.append(num_minima)
        feats_names.append(f"{signal_name}_local_minima")

        # Log Return
        log_return = calculate_log_return(signal)
        feats.append(log_return)
        feats_names.append(f"{signal_name}_log_return")

        # Longest Strike Above Mean
        longest_above = calculate_longest_strike_above_mean(signal)
        feats.append(longest_above)
        feats_names.append(f"{signal_name}_longest_strike_above_mean")

        # Longest Strike Below Mean
        longest_below = calculate_longest_strike_below_mean(signal)
        feats.append(longest_below)
        feats_names.append(f"{signal_name}_longest_strike_below_mean")

        # Lower Complete Moment
        lower_moment = calculate_lower_complete_moment(signal)
        feats.append(lower_moment)
        feats_names.append(f"{signal_name}_lower_complete_moment")

        # Mean Absolute Change
        mean_abs_change = calculate_mean_absolute_change(signal)
        feats.append(mean_abs_change)
        feats_names.append(f"{signal_name}_mean_absolute_change")

        # Mean Relative Change
        mean_rel_change = calculate_mean_relative_change(signal)
        feats.append(mean_rel_change)
        feats_names.append(f"{signal_name}_mean_relative_change")

        # Mean Second Derivative Central
        mean_sec_deriv = calculate_mean_second_derivative_central(signal)
        feats.append(mean_sec_deriv)
        feats_names.append(f"{signal_name}_mean_second_derivative_central")

        # Median Second Derivative Central
        median_second_derivative = calculate_median_second_derivative_central(signal)
        feats.append(median_second_derivative)
        feats_names.append(f"{signal_name}_median_second_derivative_central")

        # Mode
        signal_mode = calculate_mode(signal)
        feats.append(signal_mode)
        feats_names.append(f"{signal_name}_mode")

        # Number of Inflection Points
        inflection_points = calculate_number_of_inflection_points(signal)
        feats.append(inflection_points)
        feats_names.append(f"{signal_name}_number_of_inflection_points")

        # Peak to Peak Distance
        peak_to_peak_distance = calculate_peak_to_peak_distance(signal)
        feats.append(peak_to_peak_distance)
        feats_names.append(f"{signal_name}_peak_to_peak_distance")

        # Percentage of Negative Values
        percentage_negative = calculate_percentage_of_negative_values(signal)
        feats.append(percentage_negative)
        feats_names.append(f"{signal_name}_percentage_of_negative_values")

        # Percentage of Positive Values
        percentage_positive = calculate_percentage_of_positive_values(signal)
        feats.append(percentage_positive)
        feats_names.append(f"{signal_name}_percentage_of_positive_values")

        # Percentage of Reoccurring Datapoints to All Datapoints
        percentage_reoccurring_datapoints = calculate_percentage_of_reoccurring_datapoints_to_all_datapoints(signal)
        feats.append(percentage_reoccurring_datapoints)
        feats_names.append(f"{signal_name}_percentage_of_reoccurring_datapoints_to_all_datapoints")

        # Percentage of Reoccurring Values to All Values
        percentage_reoccurring_values = calculate_percentage_of_reoccurring_values_to_all_values(signal)
        feats.append(percentage_reoccurring_values)
        feats_names.append(f"{signal_name}_percentage_of_reoccurring_values_to_all_values")

        # Ratio Beyond r Sigma
        for r in [0.5, 1, 1.5, 2, 2.5, 3, 5, 6, 7, 10]:
            rbs = calculate_ratio_beyond_r_sigma(signal, r)
            feats.append(rbs)
            feats_names.append(f"{signal_name}_ratio_beyond_{r}_sigma")

        # Ratio of Fluctuations
        ratio_positive, ratio_negative, ratio_pn = calculate_ratio_of_fluctuations(signal)
        feats.append(ratio_positive)
        feats_names.append(f"{signal_name}_ratio_of_positive_fluctuations")
        feats.append(ratio_negative)
        feats_names.append(f"{signal_name}_ratio_of_negative_fluctuations")
        feats.append(ratio_pn)
        feats_names.append(f"{signal_name}_ratio_of_positive_to_negative_fluctuations")

        # Ratio Value Number to Sequence Length
        rvnsl = calculate_ratio_value_number_to_sequence_length(signal)
        feats.append(rvnsl)
        feats_names.append(f"{signal_name}_ratio_value_number_to_sequence_length")

        # Second Order Difference
        second_diff = calculate_second_order_difference(signal)
        feats.append(second_diff[-1])
        feats_names.append(f"{signal_name}_second_order_difference")

        # Signal Resultant
        signal_resultant = calculate_signal_resultant(signal)
        feats.append(signal_resultant)
        feats_names.append(f"{signal_name}_signal_resultant")

        # Signal to Noise Ratio
        snr = calculate_signal_to_noise_ratio(signal)
        feats.append(snr)
        feats_names.append(f"{signal_name}_signal_to_noise_ratio")

        # Smoothing by Binomial Filter
        smoothed_signal = calculate_smoothing_by_binomial_filter(signal)
        feats.append(smoothed_signal[-1])  # Assuming last value after smoothing is of interest
        feats_names.append(f"{signal_name}_smoothed_signal_last_value")

        # Stochastic Oscillator Value
        stochastic_value = calculate_stochastic_oscillator_value(signal)
        feats.append(stochastic_value)
        feats_names.append(f"{signal_name}_stochastic_oscillator_value")

        # Sum
        total_sum = calculate_sum(signal)
        feats.append(total_sum)
        feats_names.append(f"{signal_name}_total_sum")

        # Sum of Negative Values
        sum_negatives = calculate_sum_of_negative_values(signal)
        feats.append(sum_negatives)
        feats_names.append(f"{signal_name}_sum_of_negative_values")

        # Sum of Positive Values
        sum_positives = calculate_sum_of_positive_values(signal)
        feats.append(sum_positives)
        feats_names.append(f"{signal_name}_sum_of_positive_values")

        # Sum of Reoccurring Data Points
        sum_reoccurring_data_points = calculate_sum_of_reoccurring_data_points(signal)
        feats.append(sum_reoccurring_data_points)
        feats_names.append(f"{signal_name}_sum_of_reoccurring_data_points")

        # Sum of Reoccurring Values
        sum_reoccurring_values = calculate_sum_of_reoccurring_values(signal)
        feats.append(sum_reoccurring_values)
        feats_names.append(f"{signal_name}_sum_of_reoccurring_values")

        # Variance of Absolute Differences
        variance_abs_diffs = calculate_variance_of_absolute_differences(signal)
        feats.append(variance_abs_diffs)
        feats_names.append(f"{signal_name}_variance_of_absolute_differences")

        # Winsorized Mean
        winsorized_mean = calculate_winsorized_mean(signal, self.wm_limits)
        feats.append(winsorized_mean)
        feats_names.append(f"{signal_name}_winsorized_mean")

        # Zero Crossing Rate
        zero_crossing_rate = calculate_zero_crossing_rate(signal)
        feats.append(zero_crossing_rate)
        feats_names.append(f"{signal_name}_zero_crossing_rate")
        
        # Hurst exponent
        hurst_exponent = calculate_hurst_exponent(signal)
        feats.append(hurst_exponent)
        feats_names.append(f"{signal_name}_hurst_exponent")

        # Augmented dickey fuller test
        adf_test, adf_test_names = calculate_augmented_dickey_fuller_test(signal)
        for i, value in enumerate(adf_test):
            feats.append(value)
            feats_names.append(f"{signal_name}_augmented_dickey_fuller_{adf_test_names[i]}")
        # return np.array(feats), feats_names
        
        # Has duplicates
        has_duplicates = calculate_duplicates(signal)
        feats.append(has_duplicates)
        feats_names.append(f"{signal_name}_has_duplicates")
        
        # Max has duplicates
        max_duplicates = calculate_max_duplicates(signal)
        feats.append(max_duplicates)
        feats_names.append(f"{signal_name}_max_has_duplicates")
        
        # Min has duplicates
        min_duplicates = calculate_min_duplicates(signal)
        feats.append(min_duplicates)
        feats_names.append(f"{signal_name}_min_has_duplicates")
        
        # Lempel-Ziv Complexity
        for i, bins in enumerate(self.bins):
            lz_complexity = calculate_lempel_ziv_complexity(signal, bins)
            feats.append(lz_complexity)
            feats_names.append(f"{signal_name}_lempel_ziv_complexity_bins_{bins}")
        
        # Complex-Invariant Distance Complexity Estimate
        for i, normalize in enumerate(self.cid_ce_normalize):
            cid_complexity_estimate = calculate_cid_ce(signal, normalize)
            feats.append(cid_complexity_estimate)
            feats_names.append(f"{signal_name}_cid_ce_{normalize}")
            
        feats.append(calculate_mean_to_variance(signal))
        feats_names.append(f"{signal_name}_mean_to_variance")
            
            
        
        return feats, feats_names


# ------------------------------------------------------------------------------------------------------------------
# Spectral features
# ------------------------------------------------------------------------------------------------------------------
    
    
def calculate_frequency_features(self, signal, signal_name):
        # An array for storing the spectral features.
        feats = []
        # A list for storing feature names
        feats_names = []

        # FFT (only positive frequencies)
        spectrum = np.fft.rfft(signal)  # Spectrum of positive frequencies
        spectrum_magnitudes = np.abs(spectrum)  # Magnitude of positive frequencies
        spectrum_magnitudes_normalized = spectrum_magnitudes / np.sum(spectrum_magnitudes)
        length = len(signal)
        freqs_spectrum = np.abs(np.fft.fftfreq(length, 1.0 / self.fs)[:length // 2 + 1])

        # Calculating the power spectral density using Welch's method.
        freqs_psd, psd = welch(signal, fs=self.fs)
        psd_normalized = psd / np.sum(psd)

        # Calculating the spectral features.
        # Spectral centroid (order 1-4)        
        for order in range(1, 5):
            feats.extend(calculate_spectral_centroid(freqs_spectrum, spectrum_magnitudes, order=order))
            feats_names.append(f"{signal_name}_spectral_centroid_order_{order}")
        
        # Spectral variance / spectral spread
        feats.extend(calculate_spectral_variance(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_var")
        
        # # Spectral standard deviation / spectral spread
        # feats.extend(calculate_spectral_standard_deviation(freqs_spectrum, spectrum_magnitudes))
        # feats_names.append(f"{signal_name}_spectral_std")

        # Spectral skewness
        feats.extend(calculate_spectral_skewness(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_skewness")

        # Spectral kurtosis
        feats.extend(calculate_spectral_kurtosis(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_kurtosis")

        # Median frequency of the power spectrum of a signal
        feats.extend(calculate_median_frequency(freqs_psd, psd))
        feats_names.append(f"{signal_name}_median_frequency")

        # Spectral bandwidth order 1 / Spectral mean deviation
        feats.extend(calculate_spectral_bandwidth(freqs_spectrum, spectrum_magnitudes, 1))
        feats_names.append(f"{signal_name}_spectral_mean_deviation")
        # Spectral bandwidth order 2 / Spectral standard deviation
        feats.extend(calculate_spectral_bandwidth(freqs_spectrum, spectrum_magnitudes, 2))
        feats_names.append(f"{signal_name}_spectral_std")
        # Spectral bandwidth order 3
        feats.extend(calculate_spectral_bandwidth(freqs_spectrum, spectrum_magnitudes, 3))
        feats_names.append(f"{signal_name}_spectral_bandwidth_order_3")
        # Spectral bandwidth order 4
        feats.extend(calculate_spectral_bandwidth(freqs_spectrum, spectrum_magnitudes, 4))
        feats_names.append(f"{signal_name}_spectral_bandwidth_order_4")

        # Spectral mean absolute deviation
        # https://zenodo.org/badge/latestdoi/6309729
        feats.extend(calculate_spectral_absolute_deviation(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_abs_deviation_order_1")
        # Spectral mean absolute deviation order 3
        feats.extend(calculate_spectral_absolute_deviation(freqs_spectrum, spectrum_magnitudes, order=3))
        feats_names.append(f"{signal_name}_spectral_abs_deviation_order_3")

        # Spectral linear slope for spectrum
        feats.extend(calculate_spectral_slope_linear(freqs_spectrum, spectrum_magnitudes_normalized))
        feats_names.append(f"{signal_name}_spectral_linear_slope")

        # Spectral logarithmic slope for spectrum
        feats.extend(calculate_spectral_slope_logarithmic(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectrum_logarithmic_slope")

        # Spectral linear slope for psd
        feats.extend(calculate_spectral_slope_linear(freqs_psd, psd))
        feats_names.append(f"{signal_name}_power_spectrum_linear_slope")

        # Spectral logarithmic slope for psd
        feats.extend(calculate_spectral_slope_logarithmic(freqs_psd, psd))
        feats_names.append(f"{signal_name}_power_spectrum_logarithmic_slope")

        # Spectral flatness
        feats.extend(calculate_spectral_flatness(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_flatness")

        # Spectral peaks of power spectral density
        feats.extend(calculate_peak_frequencies(freqs_psd, psd, self.n_dom_freqs))
        for rank in range(1, self.n_dom_freqs+1):
            feats_names.append(f"{signal_name}_peak_freq_{rank}")

        # Spectral edge frequency for different thresholds
        feats.extend(calculate_spectral_edge_frequency(freqs_psd, psd, self.cumulative_power_thresholds))
        for threshold in self.cumulative_power_thresholds:
            feats_names.append(f"{signal_name}_edge_freq_thresh_{threshold}")

        # Spectral band power for different bands
        feats.extend(calculate_band_power(freqs_psd, psd, self.f_bands))
        feats_names.append(f"{signal_name}_spectral_total_power")
        for band in self.f_bands:
            feats_names.append(f"{signal_name}_spectral_abs_band_power_{str(band)}")
            feats_names.append(f"{signal_name}_spectral_rel_band_power_{str(band)}")

        # Spectral entropy
        feats.extend(calculate_spectral_entropy(psd))
        feats_names.append(f"{signal_name}_spectral_entropy")

        # Spectral contrast for different bands
        feats.extend(calculate_spectral_contrast(freqs_psd, psd, self.f_bands))
        for band in self.f_bands:
            feats_names.append(f"{signal_name}_spectral_contrast_band_{str(band)}")
        
        # Spectral coefficient of variation
        feats.extend(calculate_spectral_cov(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_coefficient_of_variation")

        # Spectral flux
        feats.extend(calculate_spectral_flux(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_flux")

        # Spectral roll-off
        feats.extend(calculate_spectral_rolloff(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_rolloff")

        # Harmonic Ratio
        feats.extend(calculate_harmonic_ratio(signal))
        feats_names.append(f"{signal_name}_harmonic_ratio")

        # Fundamental Frequency
        feats.extend(calculate_fundamental_frequency(signal))
        feats_names.append(f"{signal_name}_fundamental_frequency")

        # Spectral Crest Factor
        feats.extend(calculate_spectral_crest_factor(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_crest_factor")

        # Spectral Decrease
        feats.extend(calculate_spectral_decrease(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_decrease")

        # Spectral Irregularity
        feats.extend(calculate_spectral_irregularity(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_irregularity")

        # Frequency Winsorized Mean: A mean that reduces the effect of outliers by limiting extreme values.
        feats.extend(calculate_spectral_winsorized_mean(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_winsorized_mean")

        # Total Harmonic Distortion: Measures the distortion due to harmonics in a signal.
        feats.extend(calculate_total_harmonic_distortion(signal, self.fs))
        feats_names.append(f"{signal_name}_total_harmonic_distortion")

        # Inharmonicity: Measures the deviation of the frequencies of the overtones from whole number multiples of the fundamental frequency.
        feats.extend(calculate_inharmonicity(signal,spectrum_magnitudes,  self.fs))
        feats_names.append(f"{signal_name}_inharmonicity")

        # Tristimulus: Measures the relative amplitude of the first few harmonics.
        feats.extend(calculate_tristimulus(spectrum_magnitudes))
        feats_names.extend([f"{signal_name}_tristimulus_1", f"{signal_name}_tristimulus_2", f"{signal_name}_tristimulus_3"])

        # Spectral Roll-On: The opposite of spectral roll-off, measuring the frequency above which a certain percentage of the total spectral energy is contained.
        feats.extend(calculate_spectral_rollon(freqs_spectrum, spectrum_magnitudes))
        # https://doi.org/10.1016/j.softx.2020.100456
        feats_names.append(f"{signal_name}_spectral_rollon")

        # Spectral Hole Count: The number of significant dips in the spectrum.
        # feats.extend(calculate_spectral_hole_count(spectrum_magnitudes))
        # feats_names.append(f"{signal_name}_spectral_hole_count")

        # # Spectral Auto-correlation: The auto-correlation of the spectrum.
        # feats.append(calculate_spectral_autocorrelation(spectrum_magnitudes))
        # feats_names.append(f"{signal_name}_spectral_autocorrelation")

        # Spectral Variability: Measures the variability of the spectrum.
        feats.extend(calculate_spectral_variability(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_variability")

        # Spectral Spread Ratio: The ratio of spectral spread to some reference value.
        feats.extend(calculate_spectral_spread_ratio(freqs_spectrum, spectrum_magnitudes))
        # https://doi.org/10.1016/j.softx.2020.100456
        feats_names.append(f"{signal_name}_spectral_spread_ratio")

        # Spectral Skewness Ratio: The ratio of spectral skewness to some reference value.
        feats.extend(calculate_spectral_skewness_ratio(freqs_spectrum, spectrum_magnitudes))
        # https://doi.org/10.1016/j.softx.2020.100456
        feats_names.append(f"{signal_name}_spectral_skewness_ratio")

        # Spectral Kurtosis Ratio: The ratio of spectral kurtosis to some reference value.
        feats.extend(calculate_spectral_kurtosis_ratio(freqs_spectrum, spectrum_magnitudes))
        # https://doi.org/10.1016/j.softx.2020.100456
        feats_names.append(f"{signal_name}_spectral_kurtosis_ratio")

        # Spectral Tonal Power Ratio: The ratio of tonal power to total power.
        feats.extend(calculate_spectral_tonal_power_ratio(signal))
        feats_names.append(f"{signal_name}_spectral_tonal_power_ratio")

        # Spectral Noise to Harmonics Ratio: The ratio of noise energy to harmonic energy.
        feats.extend(calculate_spectral_noise_to_harmonics_ratio(signal))
        feats_names.append(f"{signal_name}_spectral_noise_to_harmonics_ratio")
        
        # Spectral Harmonics to Noise Ratio: The ratio of harmonics to noise ratio
        feats.extend(calculate_spectral_harmonics_to_noise_ratio(signal))
        feats_names.append(f"{signal_name}_spectral_harmonics_to_noise_ratio")

        # Spectral Even to Odd Harmonic Energy Ratio: The ratio of even harmonic energy to odd harmonic energy.
        # feats.extend(calculate_spectral_even_to_odd_harmonic_energy_ratio(signal))
        # feats_names.append(f"{signal_name}_spectral_even_to_odd_harmonic_energy_ratio")

        # Spectral Strongest Frequency Phase: The phase of the strongest frequency component.
        feats.extend(calculate_spectral_strongest_frequency_phase(spectrum))
        feats_names.append(f"{signal_name}_spectral_strongest_frequency_phase")

        # Spectral Frequency Below Peak: Frequency below the peak frequency.
        feats.extend(calculate_spectral_frequency_below_peak(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_frequency_below_peak")

        # Spectral Frequency Above Peak: Frequency above the peak frequency (next frequency value after the peak).
        feats.extend(calculate_spectral_frequency_above_peak(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_frequency_above_peak")

        # Spectral Frequency Cumulative Power Above 50%: The frequency at which the cumulative power reaches or exceeds 50% threshold.
        feats.extend(calculate_frequency_cumulative_power_above(freqs_spectrum, spectrum_magnitudes, 0.5))
        feats_names.append(f"{signal_name}_frequency_cumulative_power_above_50%")

        # Spectral Frequency Cumulative Power Above 75%: The frequency at which the cumulative power reaches or exceeds 75% threshold.
        feats.extend(calculate_frequency_cumulative_power_above(freqs_spectrum, spectrum_magnitudes, 0.75))
        feats_names.append(f"{signal_name}_frequency_cumulative_power_above_75%")

        # Spectral Cumulative Frequency Above 75% Power: The frequency above which 75% of the spectral power is contained.
        feats.extend(calculate_frequency_cumulative_power_below(freqs_spectrum, spectrum_magnitudes, 0.75))
        feats_names.append(f"{signal_name}_spectral_cumulative_frequency_below_75_percent_power")

        # Spectral Change Vector Magnitude: The magnitude of change in the spectral features over time.
        feats.extend(calculate_spectral_change_vector_magnitude(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_change_vector_magnitude")

        # Spectral Low Frequency Content: The amount of energy in the low-frequency band.
        feats.extend(calculate_spectral_low_frequency_content(freqs_spectrum, spectrum_magnitudes, psd))
        # https://resources.pcb.cadence.com/blog/2022-an-overview-of-frequency-bands-and-their-applications
        feats_names.append(f"{signal_name}_spectral_low_frequency_content")

        # Spectral Mid Frequency Content: The amount of energy in the mid-frequency band.
        feats.append(calculate_spectral_mid_frequency_content(freqs_spectrum, spectrum_magnitudes, psd))
        feats_names.append(f"{signal_name}_spectral_mid_frequency_content")

        # Spectral Peak-to-Valley Ratio: The ratio of peak to valley values in the spectrum.
        feats.extend(calculate_spectral_peak_to_valley_ratio(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_peak_to_valley_ratio")

        # Spectral Valley Depth Mean: The mean depth of valleys in the spectrum.
        feats.extend(calculate_spectral_valley_depth_mean(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_valley_depth_mean")

        # Spectral Valley Depth Standard Deviation: The standard deviation of valley depths.
        feats.extend(calculate_spectral_valley_depth_std(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_valley_depth_std")

        # Spectral Valley Depth Variance: The variance of valley depths.
        feats.extend(calculate_spectral_valley_depth_variance(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_valley_depth_variance")

        # Spectral Valley Width Mode: The most frequent valley width.
        feats.extend(calculate_spectral_valley_width_mode(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_valley_width_mode")

        # Spectral Valley Width Standard Deviation: The standard deviation of valley widths.
        feats.extend(calculate_spectral_valley_width_std(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_valley_width_std")

        # Spectral Subdominant Valley: The second most prominent valley in the spectrum.
        feats.extend(calculate_spectral_subdominant_valley(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_subdominant_valley")

        # Spectral Valley Count: The number of valleys in the spectrum.
        feats.extend(calculate_spectral_valley_count(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_valley_count")

        # Spectral Peak Broadness: The width of the spectral peaks.
        feats.extend(calculate_spectral_peak_broadness(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_peak_broadness")

        # Spectral Valley Broadness: The width of the spectral valleys.
        feats.extend(calculate_spectral_valley_broadness(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_spectral_valley_broadness")

        # Frequency Range: Range of the frequencies.
        feats.extend(calculate_spectral_range(freqs_spectrum))
        feats_names.append(f"{signal_name}_frequency_range")

        # Frequency Trimmed Mean: The mean frequency after trimming a percentage of the highest and lowest values.
        feats.extend(calculate_spectral_trimmed_mean(freqs_spectrum, spectrum_magnitudes))
        feats_names.append(f"{signal_name}_frequency_trimmed_mean")

        # Harmonic Product Spectrum: The product of harmonics in the spectrum.
        feats.extend(calculate_harmonic_product_spectrum(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_harmonic_product_spectrum")

        # Smoothness: Measures the smoothness of the spectrum.
        feats.extend(calculate_smoothness(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_smoothness")

        # Roughness: Measures the roughness of the spectrum.
        feats.extend(calculate_roughness(spectrum_magnitudes))
        feats_names.append(f"{signal_name}_roughness")


        # Returning the spectral features and the feature names
        # return np.array(feats), feats_names
        return feats, feats_names
