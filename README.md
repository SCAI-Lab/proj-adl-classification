# proj-adl-classification

## statistical_feature.py
Using GPU to compute statistical features based on PyTorch.  

Also compare the results with the features computed by CPU (Numpy).  

The return is a pd dataframe with columns: 'feature name', 'feature value gpu', 'feature value cpu', and 'time consumption'. 

#### X - Time series
"*": No reference
<br>
"* **": More than one reference and one is questionable
<br>
"~": Further research required on feature
<br>

## Statistical Features


|Number| Feature    | Description | Reference |
| -------- | ------- | ------- | ------- |
1| calculate_mean(X) | Calculates the mean of X |
2| calculate_geometric_mean(X) | Calculates the geometric mean of X |
3| calculate_trimmed_mean(X) | Calculates the trimmed mean of X |
4| calculate_mean_abs(X) | Calculates the mean of the absolute values of X |
5| calculate_geometric_mean_abs(X) | Calculates the geometric mean of the absolute values of X ||
6| calculate_harmonic_mean_abs(X)| Calculates the harmonic mean of the absolute values of X| * |
7|calculate_trimmed_mean_abs(X)| Calculates the trimmed mean of absolute values of X| * |
8|calculate_std(X) | Calculates the standard deviation of X |
9|calculate_std_abs(X) | Calculates the standard deviation of the absolute values of X | * |
10|calculate_skewness(X)|Calculates the skewness of X|
11|calculate_skewness_abs(X)| Calculate skewness of absolute values of X|*|
12|calculate_kurtosis(X)|Calculates the kurtosis of X|
13|calculate_kurtosis_abs(X)|Calculates the kurtosis of the absolute values of X| * |
14|calculate_median(X)|Calculates median of X|
15|calculate_median_abs|Calculates the median of the absolute values of X|*|
16|calculate_min(X)|Calculates the minimum value of X||
17|calculate_min_abs(X)|Calculates the minimum value of the absolute values of X| *|
18|calculate_max(X)|Calculates the maximum value of X|
19|calculate_max_abs(X)|Calculates the maximum value of the absolute values of X| |
20|calculate_range(X)|Calculates the range of X| |
21|calculate_range_abs(X)|Calculates the range of the absolute values of X|*|
22|calculate_variance(X)|Calculates the variance of X |
23|calculate_variance_abs(X)|Calculates the variance of the absolute values of X|*|
24|calculate_interquartile_range(X)|Calculates the interquartile range of X|
25|calculate_mean_absolute_deviation(X)|Calculates the mean of the absolute deviation of X |
26|calculate_root_mean_square(X)|Calculates the root mean square of X||
27|calculate_signal_energy(X)|Calculates the energy of X|
28|calculate_log_energy(X)|Calculates the log of the energy of X||
29|calculate_entropy(X)|Calculates the entropy of X|
30|calculate_zero_crossings(X)|Calculates the number of times X crosses zero|
31|calculate_crest_factor(X)|Calculates the crest factor of X|
32|calculate_clearance_factor(X)|Calculates the clearance factor of X|
33|calculate_shape_factor(X)|Calculates the shape factor of X|
34|calculate_mean_crossing(X)|Calculates the number of times X crosses the mean|
35|calculate_impulse_factor(X)|Calculates the impulse factor of X|
36|calculate_mean_auto_correlation(X)|Calculates the mean of the autocorrelation of X|
37|calculate_higher_order_moments(X)|Calculates the higher order moments of X| |
38|calculate_coefficient_of_variation(X)|Calculates the coefficient of X|
39|calculate_median_absolute_deviation(X)|Calculates the median deviation of absolute X|
40|calculate_signal_magnitude_area(X)|Calculates the magnitude area of X. The sum of the absolute values of X|
41|calculate_avg_amplitude_change(X)|Calculates the average wavelength of X|
42|calculate_slope_sign_change(X)|Calculates the number of times the slope of X changes sign|
43|calculate_higuchi_fractal_dimensions(X)|Uses the Higuchi method to calculate the fractal dimensions of X|
44|calculate_permutation_entropy(X)|Calculates the permutation entropy of X|
45|calculate_svd_entropy(X)|Singular Value Decomposition|
46|calculate_hjorth_mobility_and_complexity(X)|Calculates mobility and complexity of X which are bases on the first and second derivatives of X|
47|calculate_cardinality(X)||*|
48|calculate_rms_to_mean_abs(X)|Computes the ratio of the RMS value to mean absolute value of X|*|
49|calculate_tsallis_entropy(X)|Tsallis entropy estimates the information X||
50|calculate_renyi_entropy(X)|Computes the Renyi entropy of X|
51|calculate_absolute_energy(X)|Calculates the absolute energy of X|
52|calculate_approximate_entropy(X)|Computes the approximate entropy of X|
53|calculate_area_under_curve(X)|Calculates the area under the curve of X|
53|calculate_area_under_squared_curve(X)|Computed the area under the curve of X squared|*|
54|calculate_autoregressive_model_coefficients(X)|Calculates the autoregressive model coefficients of X|
55|calculate_count(X)|Returns the number of values in X|*|
56|calculate_count_above_mean(X)|Computes the number of values of X above the mean of X|
57|calculate_count_below_mean(X)|Computes the number of values of X below the mean of X|
58|calculate_count_of_negative_values(X)|Returns the number of values of X that are negative|
59|calculate_count_of_positive_values(X)|Returns the number of values of X that are positive|
60|calculate_covariance(X,Y)|Calculates the covariance of X and Y|
61|calculate_cumulative_energy(X)|Calculates the cumulative energy of X|
62|calculate_cumulative_sum(X)|Calculates the cumulative sum along the specified dimension of X|
63|calculate_differential_entropy(X)|Computes the differential entropy of X|
64|calculate_energy_ratio_by_chunks(X, param)|Calculates the energy of chunk i out of N chunks expressed as a ratio with the sum of squares over the X|
65|calculate_exponential_moving_average(X, param)|Calculates the exponential moving average of X|*|
66|calculate_first_location_of_maximum(X)|Returns the first location of the maximum value of X|
67|calculate_first_location_of_minimum(X)|Returns the first location of the minimum value of X|
68|calculate_first_order_difference(X)|Returns the first order differential of X|
69|calculate_first_quartile(X)|Computes the first quartile of X|*|
70|calculate_fisher_information(X)|Computes the Fisher information of X|
71|calculate_histogram_bin_frequencies(X, param)|Returns the histogram bin frequencies of X|
72|calculate_intercept_of_linear_fit(X)||~|
73|calculate_katz_fractal_dimension(X)|Computes the Katz fractal dimension of X|
74|calculate_last_location_of_maximum(X)|Returns the last location of the maximum value of X|
75|calculate_last_location_of_minimum(X)|Returns the last location of the minimum value of X|
76|calculate_linear_trend_with_full_linear_regression_results(X)|Calculate the linear trend of a signal and return the full set of linear regression results.||
77|calculate_local_maxima_and_minima(X)|Calculates the local maxima and minima of X|
78|calculate_log_return(X)|Returns the logarithm of the ratio between the last and first values of  which is a measure of the percentage change in X|~|
79|calculate_longest_strike_above_mean(X)|Computes the length of the longest consecutive subsequence of X  that is greater than the mean of X|
80|calculate_longest_strike_below_mean(X)|Computes the length of the longest consecutive subsequence of X  that is lesser than the mean of X|
81|calculate_lower_complete_moment(X)||*|
82|calculate_mean_absolute_change(X)||
83|calculate_mean_crossings(X)|Calculates the number of times X crossed the mean value|
84|calculate_mean_relative_change(X)|Returns the mean relative change of X|
85|calculate_mean_second_derivative_central(X)|Returns the mean of the second derivative of X|
86|calculate_median_second_derivative_central(X)|Calculates the median of the second derivative of X|*|
87|calculate_mode(X)|Returns the mode of X|*|
88|calculate_moving_average(X)|Returns the moving average of X|
89|calculate_number_of_inflection_points(X)|Computes the number of inflection points in X|
90|calculate_peak_to_peak_distance(X)|Calculates the peak-to-peak distance of X|
91|calculate_pearson_correlation_coefficient(X)|Calculates the pearson correlation coefficient of X|
92|calculate_percentage_of_negative_values(X)|Returns the percentage of negative values of X |*|
93|calculate_percentage_of_positive_values(X)|Returns the percentage of positive values of X |
94|calculate_percentage_of_reoccurring_datapoints_to_all_datapoints(X)|Returns the percentage of values that occur another time in the time series X|
95|calculate_percentage_of_reoccurring_values_to_all_values(X)|Calculates the percentage of values in X that occur more than once|
96|calculate_percentile(X)|Calculates the 20th, 50th and 75th percentile of X|*|
97|calculate_petrosian_fractal_dimension(X)|Computes the petrosian fractal dimension of X|
98|calculate_ratio_beyond_r_sigma(X)|Returns the ratio of values that are more than r * std away from the mean of X|
99|calculate_ratio_of_fluctuations(X)|Computes the ratio of positive and negative fluctuations in X|*|
100|calculate_ratio_value_number_to_sequence_length(X)|Returns the ratio of length of a set of X to the length X|*|
101|calculate_sample_entropy(X)|Returns the sample entropy of X|
102|calculate_second_order_difference(X)|Returns the second differential of X|**|
103|calculate_signal_resultant(X)||*|
104|calculate_signal_to_noise_ratio(X)|Calculates the signal to noise ratio of X|
106|calculate_smoothing_by_binomial_filter(X)||~|
107|calculate_stochastic_oscillator_value(X)|Calculates the stochastic oscillator of X|~|
108|calculate_sum(X)|Returns the overall sum of values in X|
109|calculate_sum_of_negative_values(X)|Calculates the sum of negative values in X|*|
110|calculate_sum_of_positive_values(X)|Returns the sum of positive values in X|*|
111|calculate_sum_of_reoccurring_data_points(X)|Calculates the sum of values of X that occur more than once|
112|calculate_sum_of_reoccurring_values(X)||
113|calculate_third_quartile(X)|Returns the third quartile of X|*|
114|calculate_variance_of_absolute_differences(X)|Returns variance of the absolute of the first order difference of X|
115|calculate_weighted_moving_average(X)|Returns the weighted moving average of X|
116|calculate_winsorized_mean(X)|Calculates the winsorized mean of X which replaces the lowest and highest outliers with closer non-extreme values before calculating the average|
117|calculate_zero_crossing_rate(X)|Returns the zero-crossing rate of X|

<br>
<br>
<br>
<br>

## Time-Frequency Features
|Number| Feature    | Reference |
| -------- | ------- | ------- |
1|extract_wavelet_features(params)|||
2|extract_spectrogram_features(params)||
3|extract_stft_features(params)||
4|teager_kaiser_energy_operator(X)|

<br>
<br>

## Spectral Features
|Number| Feature    | Reference |
| -------- | ------- | ------- |
1|calculate_spectral_centroid|
2|calculate_spectral_variance|
3|calculate_spectral_skewness|
4|calculate_spectral_kurtosis|
5|calculate_median_frequency
6|calculate_spectral_bandwidth (from order 1-4)|
7|calculate_spectral_absolute_deviation|
8|calculate_spectral_slope_linear|
9|calculate_spectral_slope_logarithmic|
10|calculate_spectral_flatness|
11|calculate_peak_frequencies|
12|calculate_spectral_edge_frequency|
13|calculate_band_power|
14|calculate_spectral_entropy|
15|calculate_spectral_contrast|
16|calculate_spectral_cov|
|calculate_spectral_flux
|calculate_spectral_rolloff
|calculate_harmonic_ratio
|calculate_fundamental_frequency
|calculate_spectral_crest_factor
|calculate_spectral_decrease
|calculate_spectral_irregularity
|calculate_mean_frequency
|calculate_frequency_winsorized_mean
|calculate_total_harmonic_distortion
|calculate_inharmonicity
|calculate_tristimulus
|calculate_spectral_rollon
|calculate_spectral_hole_count
|calculate_spectral_autocorrelation
|calculate_spectral_variability
|calculate_spectral_spread_ratio
|calculate_spectral_skewness_ratio
|calculate_spectral_kurtosis_ratio
|calculate_spectral_tonal_power_ratio
|calculate_spectral_noise_to_harmonics_ratio
|calculate_spectral_even_to_odd_harmonic_energy_ratio
|calculate_spectral_strongest_frequency_phase
|calculate_spectral_frequency_below_peak
|calculate_spectral_frequency_above_peak
|calculate_spectral_cumulative_frequency
|calculate_spectral_cumulative_frequency_above
|calculate_spectral_spread_shift
|calculate_spectral_entropy_shift
|calculate_spectral_change_vector_magnitude
|calculate_spectral_low_frequency_content
|calculate_spectral_mid_frequency_content
|calculate_spectral_peak_to_valley_ratio
|calculate_spectral_valley_depth_mean
|calculate_spectral_valley_depth_std
|calculate_spectral_valley_depth_variance
|calculate_spectral_valley_width_mode
|calculate_spectral_valley_width_std
|calculate_spectral_subdominant_valley| * |
|calculate_spectral_valley_count
|calculate_spectral_peak_broadness
|calculate_spectral_valley_broadness
|calculate_frequency_variance
|calculate_frequency_std
|calculate_frequency_range
|calculate_frequency_trimmed_mean
|calculate_harmonic_product_spectrum
|calculate_smoothness|
|calculate_roughness|*|



<br>


# NOT in tsfresh
<br>

## Spectral Features
1. Median frequency
2. Spectral bandwidth
3. Spectral absolute deviation
4. Spectral slope linear
5. Spectral slope logarithmic
6. Spectral flatness
7. Peak frequencies
8. Spectral edge frequency
9. Band power
10. Spectral entropy
11. Spectral contrast
12. Spectral coefficient variation
13. Spectral flux
14. Spectral rolloff
15. Harmonic ratio
16. Fundamental frequency
17. Spectral crest factor
18. Spectral decrease
19. Spectral irregularity
20. Mean frequency
21. Frequency winsorized mean
22. Total harmonic distortion
23. Inharmonicity


23. Tristimulus
24. Spectral rollon
25. Spectral hole count
26. Spectral autocorrelation
27. Spectral variability
28. Spectral spread ratio
29. Spectral skewness ratio
30. Spectral kurtosis ratio
31. Spectral tonal power ratio
32. Spectral noise to harmonics ratio
33. Spectral even to odd harmonic energy ratio
34. Spectral strongest frequency phase
35. Spectral frequency below peak
36. Spectral frequency above peak
37. Spectral cumulative frequency
38. Spectral cumulative frequency
39. Spectral cumulative frequency above
40. Spectral spread shift
41. Spectral entropy shift
42. Spectral change vector magnitude
43. Spectral low frequency content
44. Spectral mid frequency content
45. Spectral peak-to-valley ratio
46. Spectral valley depth mean
47. Spectral valley depth std
48. Spectral valley depth variance
49. Spectral valley width mode
50. Spectral valley width standard deviation
51. Spectral subdominant valley
52. Spectral valley count
53. Spectral peak broadness
54. Spectral valley broadness
55. Frequency variance
56. Frequency standard deviation
57. Frequency Range
58. Frequency Trimmed mean
59. Harmonic product spectrum
60. Smoothness
61. Roughness

<br>

# Time-Frequency Features
Statistical features from wavelets, spectrogram and short-time fourier transform


# Statistical Features
62. Hurst exponent from detrended fluctuation analysis
62. Winsorized mean
63. Weighted moving average
64. Sum of positive values
65. Sum of negative values
66. Stochastic oscillator value
67. Smoothing by binomial filter
68. Signal-to-noise ratio
69. Signal resultant
70. Second order difference
71. Ratio value number to sequence length 
72. Ratio beyond r signal
73. Petrosian fractal dimension
74. Percentage of positive values
75. Percentage of negative values
76. Pearson correlation coefficient
77. Peak-to-peak distance
78. Number of inflection points
79. Moving average
80. Mode
81. Median second derivative central
82. Mean relative change
83. Mean crossings
84. Lower complete moment
85. Log return 
86. Katz fractal dimension
88. Histogram bin frequencies
89. Fisher information
90. First quartile
91. First order difference
92. Exponential moving average
93. Energy ratio by chunks
94. Differential entropy
95. Cumulative sum
96. Covariance
97. Count
98. Area under curve
99. Area under squared curve
100. Renyi entropy
101. Tsallis entropy
102. Root mean squared to mean absolute
103. Cardinality
104. Hjorth mobility and complexity
105. Singular value decomposition (SVD) entropy
106. Higuchi fractal dimensions
107. Slope sign change
108. Average amplitude change
109. Signal magnitude area*
110. Median absolute deviation
111. Coefficient of variation
112. Higher order moments
113. Mean auto correlation
114. Impulse factor
115. Shape factor
116. Clearance factor
117. Crest factor
118. Zero crossings
119. Entropy
120. Log energy
121. Mean absolute deviation
122. Interquartile range
123. Variance absolute
124. Maximum absolute
125. Minimum absolute
125. Range absolute
126. Range
127. Median absolute
128. Kurtosis absolute
129. Skewness absolute
130. Standard deviation absolute
131. Trimmed mean absolute
132. Trimmed mean
133. Harmonic Mean
134. Harmonic mean absolute
135. Geometric mean 
136. Geometric mean absolute
137. Mean absolute


<br>

# Added features
|Number| Feature    | Description |
| -------- | ------- | ------- |
1| Augmented dickey fuller test| Perform the Augmented Dickey-Fuller (ADF) test to check for stationarity in a given time series signal.|
2| Hurst exponent| Calculate the Hurst Exponent of a given time series using Detrended Fluctuation Analysis (DFA).|

<br>

### Deleted features
Number| Feature    | Reason |
| -------- | ------- | ------- |
1|calculate_roll_mean | Same implementation as *calculate_moving_average*
2|calculate_absolute_energy | Same implementation as signal energy
3|calculate_cumulative_energy | Produces same result as the absolute energy and signal energy. These three will always be the same for a given signal.
4|calculate_intercept_of_linear_fit| This feature is returned again in the calculate_linear_trend_with_full_linear_regression_results function  


## Features that should be deleted
Number| Feature    | Reason |
| -------- | ------- | ------- |
1|calculate_first_quartile | calculate_percentile(signal, percentiles=[25, 50, 75]) returns the first, second, and third quartiles|
2|calculate_third_quartile | calculate_percentile(signal, percentiles=[25, 50, 75]) returns the first, second, and third quartiles |
3| calculate_histogram_bins|
4| calculate_signal_magnitude_area|

## Features in Tsfresh but not in SCAI toolbox
Number| Feature | Description|Added yet?|
| -------- | ------- | ------- | -------|
1|absolute sum of changes||✔️|
2|ar_coefficient(x, param)| This feature calculator fits the unconditional maximum likelihood of an autoregressive AR(k) process|
3|benford correlation|||
4|c3| uses c3 statistics to measure non-linearity in the time series
5|count_above(x, t)|Returns the percentage of values in x that are higher than t |✔️|
6|count_below(x, t)| Returns the percentage of values in x that are lower than t|✔️|
7|cid_ce(x, normalize) |This function calculator is an estimate for a time series complexity [1] (A more complex time series has more peaks, valleys etc.).|✔️|
8|friedrich_coefficients(x, param)|Coefficients of polynomial h(x), which has been fitted to the deterministic dynamics of Langevin model
9|has_duplicate(x)|Checks if any value in x occurs more than once| ✔️|
10|has_duplicate_max(x)|Checks if the maximum value of x is observed more than once| ✔️|
11|has_duplicate_min(x)|Checks if the minimal value of x is observed more than once| ✔️|
12|index_mass_quantile(x, param)|Calculates the relative index i of time series x where q% of the mass of x lies left of i.
13|mean_n_absolute_max(x, number_of_maxima)| Calculates the arithmetic mean of the n absolute maximum values of the time series.
14|large_standard_deviation(x, r)|Does time series have large standard deviation| ✔️ |
15|lempel_ziv_complexity(x, bins)|Calculate a complexity estimate based on the Lempel-Ziv compression algorithm.|✔️|
16|matrix_profile(x, param)|Calculates the 1-D Matrix Profile[1] and returns Tukey's Five Number Set plus the mean of that Matrix Profile.
17|max_langevin_fixed_point(x, r, m)|Largest fixed point of dynamics :math:argmax_x {h(x)=0}` estimated from polynomial h(x), which has been fitted to the deterministic dynamics of Langevin model
18|binned entropy |
19| symmetry looking|Boolean variable denoting if the distribution of x looks symmetric.


## Observations
1. **calculate_higher_order_moments** does not always produce the same result as mean, variance, skew and kurtosis when moment order is set to [1,2,3,4]
2. **calculate_rms_to_mean_abs** has no direct reference yet
3. **calculate_exponential_moving_average** returns the last value in the array. Is there a reason?
4. 

<br>
Corrections

1. calculate_katz_fractal_dimensions
2. calculate_sum_of_reoccurring_values
3. calculate_sum_of_reoccurring_data_points
4. calculate_petrosian_fractal_dimension
5. calculate_sample_entropy
6. calculate_approximate_entropy












