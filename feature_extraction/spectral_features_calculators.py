import numpy as np
from scipy.signal import welch, find_peaks
from scipy.integrate import simpson
from scipy.stats import entropy, skew, kurtosis, trim_mean, mode
import librosa

def calculate_spectral_centroid(freqs, magnitudes, order=1):
        """
        Calculates the spectral centroid of the given spectrum.

        The spectral centroid is a measure that indicates where the center of mass of the spectrum is located.
        It is often associated with the perceived brightness of a sound. This function computes the spectral
        centroid by taking the weighted mean of the frequencies, with the magnitudes as weights.

        Parameters:
        ----------
        freqs : numpy.array
            An array of frequencies corresponding to the spectrum bins.
        magnitudes : numpy.array
            An array of magnitude values of the spectrum at the corresponding frequencies.
        order : int, optional
            The order of the centroid calculation. Default is 1, which calculates the standard spectral centroid (mean frequency).
            Higher orders can be used for other types of spectral centroid calculations.

        Returns:
        -------
        numpy.array
            An array containing the calculated spectral centroid. The array is of length 1 for consistency in return type.
            
        Reference:
        ---------
            Barandas et al., 2020, https://doi.org/10.1016/j.softx.2020.100456
        """
                
        spectral_centroid = np.sum(magnitudes * (freqs ** order)) / np.sum(magnitudes)
        return np.array([spectral_centroid])

def calculate_spectral_variance(self, freqs, magnitudes):
        """
        Calculates the spectral variance (also known as spectral spread) of the given spectrum.

        The spectral variance is a measure of the spread of the spectrum around its centroid.
        It quantifies how much the frequencies in the spectrum deviate from the spectral centroid.

        Parameters:
        ----------
        freqs : numpy.array
            An array of frequencies corresponding to the spectrum bins.
        magnitudes : numpy.array
            An array of magnitude values of the spectrum at the corresponding frequencies.

        Returns:
        -------
        numpy.array
            An array containing the calculated spectral variance. The array is of length 1 for consistency in return type.
        
        Reference:
        ---------
            Barandas et al., 2020, https://doi.org/10.1016/j.softx.2020.100456
        """
        mean_frequency = self.calculate_spectral_centroid(freqs, magnitudes)
        spectral_variance = np.sum(((freqs - mean_frequency) ** 2) * magnitudes) / np.sum(magnitudes)
        return np.array([spectral_variance])

def calculate_spectral_skewness(self, freqs, magnitudes):
        """
        Calculates the spectral skewness of the given spectrum.

        Spectral skewness is a measure of the asymmetry of the distribution of frequencies in the spectrum
        around the spectral centroid. It indicates whether the spectrum is skewed towards higher or lower
        frequencies.

        Parameters:
        ----------
        freqs : numpy.array
            An array of frequencies corresponding to the spectrum bins.
        magnitudes : numpy.array
            An array of magnitude values of the spectrum at the corresponding frequencies.

        Returns:
        -------
        float
            The calculated spectral skewness.
        
        Reference:
        ---------
            Barandas et al., 2020, https://doi.org/10.1016/j.softx.2020.100456
        """
        mu1 = self.calculate_spectral_centroid(freqs, magnitudes, order=1)
        mu2 = self.calculate_spectral_centroid(freqs, magnitudes, order=2)
        spectral_skewness = np.sum(magnitudes * (freqs - mu1) ** 3) / (np.sum(magnitudes) * mu2 ** 3)
        return spectral_skewness

def calculate_spectral_kurtosis(self, freqs, magnitudes):
        """
        Calculate the spectral kurtosis of the given spectrum.

        Spectral kurtosis measures the "tailedness" or peakiness of the frequency distribution around the spectral centroid.
        It quantifies how outlier-prone the spectrum is and reflects the degree of concentration of the spectral energy.
        A higher kurtosis value indicates a more peaked distribution with heavy tails.

        Parameters:
        ----------
        freqs : numpy.array
            An array of frequencies corresponding to the spectrum bins.
        magnitudes : numpy.array
            An array of magnitude values of the spectrum at the corresponding frequencies.

        Returns:
        -------
        float
            The calculated spectral kurtosis.
        
        Reference:
        ---------
            Barandas et al., 2020, https://doi.org/10.1016/j.softx.2020.100456
        """
        mu1 = self.calculate_spectral_centroid(freqs, magnitudes, order=1)
        mu2 = self.calculate_spectral_centroid(freqs, magnitudes, order=2)
        spectral_kurtosis = np.sum(magnitudes * (freqs - mu1) ** 4) / (np.sum(magnitudes) * mu2 ** 4)
        return spectral_kurtosis

def calculate_median_frequency(self, freqs, psd):
        """
        Calculate the cumulative distribution function (CDF) of the PSD

        Parameters:
        ----------
        freqs : numpy.array
            An array of frequencies corresponding to the PSD bins.
        psd : numpy.array
            An array of power spectral density values at the corresponding frequencies.

        Returns:
        -------
        numpy.array
            An array containing the calculated median frequency.
            
        Reference:
        ---------
            Chung et al., 2008, https://doi.org/10.1109/iembs.2008.4649357
        """
        cdf = np.cumsum(psd)
        median_freq = freqs[np.searchsorted(cdf, cdf[-1] / 2)]
        return np.array([median_freq])

def calculate_spectral_flatness(self, magnitudes):
        """
        Calculate the spectral flatness of a given spectrum.

        Spectral flatness quantifies how flat or peaky a spectrum is, indicating how noise-like or tonal a signal is.
        It is often used to distinguish between noise and tonal signals. It can also be referred to as Wiener's entropy.

        Parameters:
        ----------
        magnitudes : numpy.array
            An array of magnitude values of the spectrum.

        Returns:
        -------
        numpy.array
            An array containing the calculated spectral flatness.

        Reference:
        --------
            Sayeed et al., 2016, https://doi.org/10.1016/B978-0-12-398499-9.00012-1
        """
        spectral_flatness = np.exp(np.mean(np.log(magnitudes))) / np.mean(magnitudes)
        return np.array([spectral_flatness])

def calculate_spectral_slope_logarithmic(self, freqs, magnitudes):
        """
        Calculate the logarithmic spectral slope of the given spectrum.

        The logarithmic spectral slope provides a measure of the rate at which the spectrum's magnitude changes
        across frequencies on a logarithmic scale.

        Parameters:
        ----------
        freqs : numpy.array
            An array of frequencies corresponding to the magnitude spectrum bins.
        magnitudes : numpy.array
            An array of magnitude values of the spectrum at the corresponding frequencies.

        Returns:
        -------
        numpy.array
            An array containing the calculated logarithmic spectral slope. The array is of length 1 for consistency in return type.

        Reference:
        ---------
            Barandas et al., 2020, https://doi.org/10.1016/j.softx.2020.100456
        """
        slope = np.polyfit(freqs, np.log(magnitudes), 1)[0]
        return np.array([slope])

def calculate_spectral_slope_linear(self, freqs, magnitudes):
        """
        Calculate the spectral slope of a signal given its frequencies and magnitudes.

        The spectral slope is determined by fitting a linear regression line to the 
        frequency-magnitude data. The slope of this line indicates how the magnitudes
        change with respect to frequency.

        Parameters:
        ---------
        freqs: numpy.array 
            An array of frequency values.
        magnitudes: numpy.array
            An array of magnitude values corresponding to the frequencies.

        Returns:
        -------
        numpy.array:
            A numpy array containing a single element, the slope of the linear fit.
            
        Reference:
        ---------
            Barandas et al., 2020, https://doi.org/10.1016/j.softx.2020.100456
        """
        slope = np.polyfit(freqs, magnitudes, 1)[0]
        return np.array([slope])

def calculate_peak_frequencies(self, freqs, psd):
        """
        Identifies the peak frequencies from the given Power Spectral Density (PSD) values.

        Parameters:
        ----------
        freqs:numpy.array
            An array of frequency values.
        psd:numpy.array
            An array of Power Spectral Density (PSD) values corresponding to the frequencies.

        Returns:
        -------
        numpy.array: 
            A numpy array containing the peak frequencies.
        
        Reference:
        ---------
            Murthy et al., 1971, https://doi.org/10.1016/0025-5564(71)90072-1
        """
        peak_frequencies = freqs[np.argsort(psd)[-self.n_dom_freqs:][::-1]]
        return np.array(peak_frequencies)

def calculate_spectral_edge_frequency(self, freqs, psd):
        """
        Calculate the spectral edge frequencies for given cumulative power thresholds.

        The spectral edge frequency is the frequency below which a certain percentage 
        of the total power of the signal is contained. This function calculates the 
        spectral edge frequencies for multiple thresholds provided in 
        `self.cumulative_power_thresholds`.

        Parameters:
        ----------
        freqs: numpy.array
            An array of frequency values.
        psd: numpy.array
            An array of Power Spectral Density (PSD) values corresponding to the frequencies.

        Returns:
        -------
        numpy.array: 
            A numpy array containing the spectral edge frequencies for each threshold.
        
        Reference:
        ---------
            Drummond et al., 1991, https://doi.org/10.1111/j.1399-6576.1991.tb03374.x   
        """
        # A special case would be roll-off frequency (threshold = .85)
        feats = []
        cumulative_power = np.cumsum(psd) / np.sum(psd)
        for threshold in self.cumulative_power_thresholds:
            feats.append(freqs[np.argmax(cumulative_power >= threshold)])
        return np.array(feats)

def calculate_band_power(self, freqs, psd):
        """
        Calculates the total power, band absolute powers and band relative powers in specified frequency bands.
        
        Parameters:
        ----------
        freqs: numpy.array
            An array of frequency values.
        psd: numpy.array
            An array of Power Spectral Density (PSD) values corresponding to the frequencies.

        Returns:
        -------
        numpy.array: 
            An array containing the total power, followed by the absolute and relative
            power for each specified frequency band.

        Reference:
        ---------
            https://www.mathworks.com/help/signal/ref/bandpower.html
        """
        # The features array for storing the total power, band absolute powers, and band relative powers
        feats = []
        freq_res = freqs[1] - freqs[0]  # Frequency resolution
        # Calculate the total power of the signal
        try:
            feats.append(simpson(psd, dx=freq_res))
        except:
            feats.append(np.nan)
        # Calculate band absolute and relative power
        for f_band in self.f_bands:
            try:
                # Keeping the frequencies within the band
                idx_band = np.logical_and(freqs >= f_band[0], freqs < f_band[1])
                # Absolute band power by integrating PSD over frequency range of interest
                feats.append(simpson(psd[idx_band], dx=freq_res))
                # Relative band power
                feats.append(feats[-1] / feats[0])
            except:
                feats.extend([np.nan, np.nan])
        return np.array(feats)

def calculate_spectral_entropy(self, psd):
        """
        Calculate the spectral entropy of a Power Spectral Density (PSD) array.

        Spectral entropy is a measure of the disorder or complexity of a signal's 
        frequency distribution. It is calculated by normalizing the PSD values to 
        form a probability distribution and then computing the entropy of this 
        distribution.
        
        Parameters:
        ---------
        psd: numpy.array
            An array of Power Spectral Density (PSD) values corresponding to the frequencies.
            
        Returns:
        numpy.array: 
            A numpy array containing the spectral entropy value.
            
        Reference:
        ---------
            Barandas et al., 2020, https://doi.org/10.1016/j.softx.2020.100456
        """
        try:
            # Formula from Matlab doc
            psd_norm = psd / np.sum(psd)
            spectral_entropy = -np.sum(psd_norm * np.log2(psd_norm))
        except:
            spectral_entropy = np.nan
        return np.array([spectral_entropy])

def calculate_spectral_contrast(self, freqs, psd):
        """
        Calculate the spectral contrast of a Power Spectral Density (PSD) array.

        Spectral contrast measures the difference between peaks and valleys in the spectrum
        for specified frequency bands. It reflects the dynamic range of the frequency content
        of the signal.
        
        Parameters:
        ----------
        freqs: numpy.array
            An array of frequency values.
        psd: numpy.array
            An array of Power Spectral Density (PSD) values corresponding to the frequencies.

        Returns:
        -------
        numpy.array:
            An array containing the spectral contrast values for each specified frequency band.

        Reference:
            McFee et al., 2024, https://zenodo.org/badge/latestdoi/6309729
        """
        feats = []
        for f_band in self.f_bands:
            try:
                idx_band = np.logical_and(freqs >= f_band[0], freqs < f_band[1])
                peak = np.max(psd[idx_band])
                valley = np.min(psd[idx_band])
                contrast = peak - valley
                feats.append(contrast)
            except:
                feats.append(np.nan)
        return np.array(feats)

def calculate_spectral_bandwidth(self, freqs, magnitudes, order):
        """
        Calculate the spectral bandwidth of a given frequency spectrum.
        
        Spectral bandwidth is a measure of the width of the spectrum, indicating the spread 
        of the magnitudes across frequencies. This function computes the spectral bandwidth 
        based on the specified order, where:
        - The 1st order spectral bandwidth corresponds to the spectral mean deviation.
        - The 2nd order spectral bandwidth corresponds to the spectral standard deviation.
        
        Parameters:
        ----------
        freqs : numpy.array
            An array of frequencies corresponding to the magnitude spectrum bins.
        magnitudes : numpy.array
            An array of magnitude values of the spectrum at the corresponding frequencies.

        order : int
        The order of the spectral bandwidth calculation. The orderdefines the type of 
        deviation being measured:
        - 1 for spectral mean deviation.
        - 2 for spectral standard deviation.
        This calculates up to the 4th order
        
        Returns:
        --------
            np.ndarray
                A 1D numpy array containing the calculated spectral bandwidth value.
        
        References:
        -----------
            - Librosa Library Documentation: https://zenodo.org/badge/latestdoi/6309729
        """
        normalized_magnitudes = magnitudes / np.sum(magnitudes)
        mean_frequency = self.calculate_spectral_centroid(freqs, magnitudes)
        spectral_bandwidth = ((np.sum(((freqs - mean_frequency) ** order) * normalized_magnitudes)) ** (1 / order))
        return np.array([spectral_bandwidth])

def calculate_spectral_absolute_deviation(self, freqs, magnitudes, order=1):
        """
        Calculate the spectral absolute deviation of a given frequency spectrum.

        Spectral absolute deviation measures the average deviation of frequency components 
        from the spectral centroid (mean frequency) weighted by their magnitudes. This 
        function generalizes the concept for any given order, with the even order 
        spectral absolute deviation being equivalent to the spectral bandwidth of the 
        same order.

        Parameters:
        -----------
        freqs : numpy.array
            An array of frequencies corresponding to the magnitude spectrum bins.
        magnitudes : numpy.array
            An array of magnitude values of the spectrum at the corresponding frequencies.

        order : int, optional default=1)
            The order of the deviation calculation. When `order=2`, the result is equivalent 
            to the spectral bandwidth (standard deviation) of the spectrum.

        Returns:
        --------
        np.ndarray
            A 1D numpy array containing the calculated spectral absolute deviation.
            
        References:
        -----------
            - Librosa Library Documentation: https://zenodo.org/badge/latestdoi/6309729
        """
        # The even order spectral absolute deviation is the same as spectral bandwidth of the same order
        normalized_magnitudes = magnitudes / np.sum(magnitudes)
        mean_frequency = self.calculate_spectral_centroid(freqs, magnitudes)
        spectral_absolute_deviation = ((np.sum((np.abs(freqs - mean_frequency) ** order) * normalized_magnitudes)) ** (1 / order))
        return np.array([spectral_absolute_deviation])

def calculate_spectral_cov(self, freqs, magnitudes):
        """
        Calculate the spectral coefficient of variation (CoV) for a given frequency spectrum.

        The spectral CoV provides a normalized measure of the dispersion of frequencies 
        around the spectral centroid (mean frequency). It is calculated as the ratio of 
        the spectral standard deviation (second-order spectral bandwidth) to the spectral 
        centroid, multiplied by 100 to express it as a percentage.

        Parameters:
        -----------
        freqs : array-like
            The frequency values of the spectrum. This is a 1D array representing the 
            frequency bins of the spectrum.

        magnitudes : array-like
            The magnitude values of the spectrum corresponding to each frequency bin. 
            This is a 1D array representing the magnitude of the signal at each frequency.

        Returns:
        --------
        float
            The spectral coefficient of variation (CoV) expressed as a percentage.

        References:
        -----------
            - Cole, S., Donoghue, T., Gao, R., & Voytek, B. (2019). NeuroDSP: A package for 
            neural digital signal processing. Journal of Open Source Software, 4(36), 1272. 
            https://doi.org/10.21105/JOSS.01272
        """
        mean_frequency = self.calculate_spectral_centroid(freqs, magnitudes)
        frequency_std = self.calculate_spectral_bandwidth(freqs, magnitudes, 2)
        coefficient_of_variation = (frequency_std / mean_frequency) * 100
        return coefficient_of_variation

def calculate_spectral_flux(self, magnitudes, order=2):
        # https://doi.org/10.1016/B978-0-08-099388-1.00004-2
        spectral_flux = (np.sum(np.abs(np.diff(magnitudes)) ** order)) ** (1 / order)
        return np.array([spectral_flux])
    
def calculate_spectral_rolloff(self, freqs, magnitudes, roll_percent=0.85):
        # https://doi.org/10.1016/j.softx.2020.100456
        cumulative_magnitudes = np.cumsum(magnitudes)
        rolloff_frequency = np.min(freqs[np.where(cumulative_magnitudes >= roll_percent * cumulative_magnitudes[-1])])
        return np.array([rolloff_frequency])

def calculate_harmonic_ratio(self, signal):
        # https://www.mathworks.com/help/audio/ref/harmonicratio.html
        harmonic_ratio = librosa.effects.harmonic(signal).mean()
        return np.array([harmonic_ratio])

def calculate_fundamental_frequency(self, signal):
        # https://doi.org/10.1121%2F1.4740482
        f0 = librosa.yin(signal, fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C8'))
        return np.array([np.mean(f0)])

def calculate_spectral_crest_factor(self, magnitudes):
        # https://www.mathworks.com/help/signal/ref/spectralcrest.html#d126e220002
        crest_factor = np.max(magnitudes) / np.mean(magnitudes)
        return np.array([crest_factor])

def calculate_spectral_decrease(self, freqs, magnitudes):
        # https://doi.org/10.1016/j.softx.2020.100456
        k = np.arange(1, len(magnitudes) + 1)
        spectral_decrease = np.sum((magnitudes[1:] - magnitudes[0]) / k[1:])
        return np.array([spectral_decrease])

def calculate_spectral_irregularity(self, magnitudes):
        # https://docs.twoears.eu/en/latest/afe/available-processors/spectral-features/
        # https://doi.org/10.1109/ICASSP.2004.1325955
        irregularity = np.sum(np.abs(magnitudes[1:] - magnitudes[:-1])) / (len(magnitudes) - 1)
        return np.array([irregularity])

def calculate_mean_frequency(self, freqs, magnitudes):
        # https://www.mathworks.com/help/signal/ref/meanfreq.html
        mean_freq = np.sum(freqs * magnitudes) / np.sum(magnitudes)
        return np.array([mean_freq])

def calculate_frequency_winsorized_mean(self, freqs, magnitudes, limits=(0.05, 0.95)):
        # https://doi.org/10.1007/978-94-010-0231-8_13
        sorted_indices = np.argsort(magnitudes)
        lower_limit = int(limits[0] * len(magnitudes))
        upper_limit = int(limits[1] * len(magnitudes))
        trimmed_indices = sorted_indices[lower_limit:upper_limit]
        winsorized_mean = np.mean(freqs[trimmed_indices])
        return np.array([winsorized_mean])

def calculate_total_harmonic_distortion(self, signal, harmonics=5):
        # 10.1109/TCOMM.2011.061511.100749
        # https://zenodo.org/badge/latestdoi/6309729
        f0 = librosa.yin(signal, fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C8'))
        fundamental_freq = np.mean(f0)
        harmonic_frequencies = [(i+1) * fundamental_freq for i in range(harmonics)]
        harmonic_power = sum([np.sum(np.abs(np.fft.rfft(signal * np.sin(2 * np.pi * harmonic_freq * np.arange(len(signal)) / self.fs)))) for harmonic_freq in harmonic_frequencies])
        total_power = np.sum(np.abs(np.fft.rfft(signal))**2)
        thd = harmonic_power / total_power
        return np.array([thd])

    #def calculate_inharmonicity(self, signal):
        # https://zenodo.org/badge/latestdoi/6309729
    #     f0 = librosa.yin(signal, fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C8'))
    #     fundamental_freq = np.mean(f0)
    #     harmonics = [(i+1) * fundamental_freq for i in range(1, int(self.fs/(2*fundamental_freq)))]
    #     inharmonicity = sum([np.abs(harmonic - fundamental_freq * (i+1)) for i, harmonic in enumerate(harmonics)]) / len(harmonics)
    #     return np.array([inharmonicity])

def calculate_tristimulus(self, magnitudes):
        # https://zenodo.org/badge/latestdoi/6309729
        if len(magnitudes) < 3:
            return np.array([np.nan, np.nan, np.nan])
        t1 = magnitudes[0] / np.sum(magnitudes)
        t2 = magnitudes[1] / np.sum(magnitudes)
        t3 = np.sum(magnitudes[2:]) / np.sum(magnitudes)
        return np.array([t1, t2, t3])

def calculate_spectral_rollon(self, freqs, magnitudes, roll_percent=0.85):
        # https://doi.org/10.1016/j.softx.2020.100456
        cumulative_magnitudes = np.cumsum(magnitudes)
        rollon_frequency = np.min(freqs[np.where(cumulative_magnitudes >= roll_percent * cumulative_magnitudes[-1])])
        return np.array([rollon_frequency])

def calculate_spectral_hole_count(self, magnitudes, threshold=0.05):
        # https://doi.org/10.1103/PhysRevA.104.063111
        peaks, _ = find_peaks(magnitudes, height=threshold)
        dips, _ = find_peaks(-magnitudes, height=-threshold)
        return np.array([len(dips)])

def calculate_spectral_autocorrelation(self, magnitudes):
        # https://doi.org/10.48550/arXiv.1702.00105
        autocorrelation = np.correlate(magnitudes, magnitudes, mode='full')
        return autocorrelation[autocorrelation.size // 2:]

def calculate_spectral_variability(self, magnitudes):
        # https://doi.org/10.1016/j.dsp.2015.10.011
        variability = np.var(magnitudes)
        return np.array([variability])

def calculate_spectral_spread_ratio(self, freqs, magnitudes, reference_value=1.0):
        # https://doi.org/10.1016/j.softx.2020.100456
        spread = np.sqrt(np.sum((freqs - np.mean(freqs))**2 * magnitudes) / np.sum(magnitudes))
        spread_ratio = spread / reference_value
        return np.array([spread_ratio])

def calculate_spectral_skewness_ratio(self, freqs, magnitudes, reference_value=1.0):
        # https://doi.org/10.1016/j.softx.2020.100456
        mean_freq = np.mean(freqs)
        skewness = np.sum((freqs - mean_freq)**3 * magnitudes) / (len(freqs) * (np.std(freqs)**3))
        skewness_ratio = skewness / reference_value
        return np.array([skewness_ratio])

def calculate_spectral_kurtosis_ratio(self, freqs, magnitudes, reference_value=1.0):
        # https://doi.org/10.1016/j.softx.2020.100456
        mean_freq = np.mean(freqs)
        kurtosis = np.sum((freqs - mean_freq)**4 * magnitudes) / (len(freqs) * (np.std(freqs)**4)) - 3
        kurtosis_ratio = kurtosis / reference_value
        return np.array([kurtosis_ratio])

def calculate_spectral_tonal_power_ratio(self, signal):
        # https://zenodo.org/badge/latestdoi/6309729
        harmonic_power = np.sum(librosa.effects.harmonic(signal)**2)
        total_power = np.sum(signal**2)
        tonal_power_ratio = harmonic_power / total_power
        return np.array([tonal_power_ratio])

def calculate_spectral_noise_to_harmonics_ratio(self, signal):
        # https://zenodo.org/badge/latestdoi/6309729
        harmonic_part = librosa.effects.harmonic(signal)
        noise_part = signal - harmonic_part
        noise_energy = np.sum(noise_part**2)
        harmonic_energy = np.sum(harmonic_part**2)
        noise_to_harmonics_ratio = noise_energy / harmonic_energy
        return np.array([noise_to_harmonics_ratio])

    #def calculate_spectral_even_to_odd_harmonic_energy_ratio(self, signal):
        # https://zenodo.org/badge/latestdoi/6309729
    #     f0 = librosa.yin(signal, fmin=librosa.note_to_hz('C1'), fmax=librosa.note_to_hz('C8'))
    #     fundamental_freq = np.mean(f0)
    #     even_harmonics = [(2 * i + 2) * fundamental_freq for i in range(int(self.fs / (2 * fundamental_freq)))]
    #     odd_harmonics = [(2 * i + 1) * fundamental_freq for i in range(int(self.fs / (2 * fundamental_freq)))]
    #     even_energy = sum([np.sum(np.abs(np.fft.rfft(signal * np.sin(2 * np.pi * harmonic * np.arange(len(signal)) / self.fs)))) for harmonic in even_harmonics])
    #     odd_energy = sum([np.sum(np.abs(np.fft.rfft(signal * np.sin(2 * np.pi * harmonic * np.arange(len(signal)) / self.fs)))) for harmonic in odd_harmonics])
    #     even_to_odd_ratio = even_energy / odd_energy
    #     return np.array([even_to_odd_ratio])

def calculate_spectral_strongest_frequency_phase(self, freqs, spectrum):
        # https://mriquestions.com/phase-v-frequency.html
        strongest_frequency_index = np.argmax(np.abs(spectrum))
        phase = np.angle(spectrum[strongest_frequency_index])
        return np.array([phase])

def calculate_spectral_frequency_below_peak(self, freqs, magnitudes):
        # https://doi.org/10.1016/B978-012437552-9/50003-9
        peak_index = np.argmax(magnitudes)
        frequency_below_peak = freqs[max(0, peak_index - 1)]
        return np.array([frequency_below_peak])

def calculate_spectral_frequency_above_peak(self, freqs, magnitudes):
        # https://doi.org/10.1016/B978-012437552-9/50003-9
        peak_index = np.argmax(magnitudes)
        frequency_above_peak = freqs[min(len(freqs) - 1, peak_index + 1)]
        return np.array([frequency_above_peak])

def calculate_spectral_cumulative_frequency(self, freqs, magnitudes, threshold):
        # https://doi.org/10.48550/arXiv.0901.3708
        cumulative_power = np.cumsum(magnitudes) / np.sum(magnitudes)
        frequency = freqs[np.where(cumulative_power >= threshold)[0][0]]
        return np.array([frequency])

def calculate_spectral_cumulative_frequency_above(self, freqs, magnitudes, threshold):
        # https://doi.org/10.48550/arXiv.0901.3708
        cumulative_power = np.cumsum(magnitudes) / np.sum(magnitudes)
        frequency = freqs[np.where(cumulative_power <= threshold)[-1][-1]]
        return np.array([frequency])

def calculate_spectral_spread_shift(self, freqs, magnitudes):
        # https://docs.twoears.eu/en/latest/afe/available-processors/spectral-features/
        mean_frequency = np.sum(freqs * magnitudes) / np.sum(magnitudes)
        spread = np.sqrt(np.sum((freqs - mean_frequency) ** 2 * magnitudes) / np.sum(magnitudes))
        return np.array([spread])

def calculate_spectral_entropy_shift(self, magnitudes):
        # https://doi.org/10.3390/buildings12030310
        psd_norm = magnitudes / np.sum(magnitudes)
        entropy = -np.sum(psd_norm * np.log2(psd_norm))
        return np.array([entropy])

def calculate_spectral_change_vector_magnitude(self, magnitudes):
        # https://doi.org/10.3390/rs3112473
        change_vector_magnitude = np.linalg.norm(np.diff(magnitudes))
        return np.array([change_vector_magnitude])

def calculate_spectral_low_frequency_content(self, freqs, magnitudes, low_freq_threshold=300):
        # https://resources.pcb.cadence.com/blog/2022-an-overview-of-frequency-bands-and-their-applications
        low_freq_content = np.sum(magnitudes[freqs < low_freq_threshold])
        return np.array([low_freq_content])

def calculate_spectral_mid_frequency_content(self, freqs, magnitudes, mid_freq_range=(300, 3000)):
        # https://resources.pcb.cadence.com/blog/2022-an-overview-of-frequency-bands-and-their-applications
        mid_freq_content = np.sum(magnitudes[(freqs >= mid_freq_range[0]) & (freqs <= mid_freq_range[1])])
        return np.array([mid_freq_content])

def calculate_spectral_peak_to_valley_ratio(self, magnitudes):
        # https://doi.org/10.3389/fpsyg.2022.994047
        # https://openlab.help.agilent.com/en/index.htm#t=mergedProjects/DataAnalysis/27021601168830603.htm
        peaks, _ = find_peaks(magnitudes)
        valleys, _ = find_peaks(-magnitudes)
        if len(peaks) == 0 or len(valleys) == 0:
            return np.array([np.nan])
        peak_to_valley_ratio = np.max(magnitudes[peaks]) / np.min(magnitudes[valleys])
        return np.array([peak_to_valley_ratio])

def calculate_spectral_valley_depth_mean(self, magnitudes):
        # https://doi.org/10.48550/arXiv.1506.04828
        valleys, _ = find_peaks(-magnitudes)
        if len(valleys) == 0:
            return np.array([np.nan])
        valley_depth_mean = np.mean(magnitudes[valleys])
        return np.array([valley_depth_mean])

def calculate_spectral_valley_depth_std(self, magnitudes):
        # https://doi.org/10.48550/arXiv.1506.04828
        valleys, _ = find_peaks(-magnitudes)
        if len(valleys) == 0:
            return np.array([np.nan])
        valley_depth_std = np.std(magnitudes[valleys])
        return np.array([valley_depth_std])

def calculate_spectral_valley_depth_variance(self, magnitudes):
        # https://doi.org/10.48550/arXiv.1506.04828
        valleys, _ = find_peaks(-magnitudes)
        if len(valleys) == 0:
            return np.array([np.nan])
        valley_depth_variance = np.var(magnitudes[valleys])
        return np.array([valley_depth_variance])

def calculate_spectral_valley_width_mode(self, magnitudes):
        # https://doi.org/10.48550/arXiv.1506.04828
        valleys, _ = find_peaks(-magnitudes)
        if len(valleys) < 2:
            return np.array([np.nan])
        valley_widths = np.diff(valleys)
        # valley_width_mode = mode(valley_widths).mode[0]
        valley_width_mode = mode(valley_widths)[0]
        return np.array([valley_width_mode])

def calculate_spectral_valley_width_std(self, magnitudes):
        # https://doi.org/10.48550/arXiv.1506.04828
        valleys, _ = find_peaks(-magnitudes)
        if len(valleys) < 2:
            return np.array([np.nan])
        valley_widths = np.diff(valleys)
        valley_width_std = np.std(valley_widths)
        return np.array([valley_width_std])

def calculate_spectral_subdominant_valley(self, magnitudes):
        valleys, _ = find_peaks(-magnitudes)
        if len(valleys) < 2:
            return np.array([np.nan])
        sorted_valleys = np.sort(magnitudes[valleys])
        subdominant_valley = sorted_valleys[-2] if len(sorted_valleys) >= 2 else np.nan
        return np.array([subdominant_valley])

def calculate_spectral_valley_count(self, magnitudes):
        # https://doi.org/10.48550/arXiv.1506.04828
        valleys, _ = find_peaks(-magnitudes)
        return np.array([len(valleys)])

def calculate_spectral_peak_broadness(self, freqs, magnitudes):
        # https://terpconnect.umd.edu/~toh/spectrum/PeakFindingandMeasurement.htm
        peaks, _ = find_peaks(magnitudes)
        if len(peaks) < 2:
            return np.array([np.nan])
        peak_widths = np.diff(peaks)
        peak_broadness = np.mean(peak_widths)
        return np.array([peak_broadness])

def calculate_spectral_valley_broadness(self, freqs, magnitudes):
        # https://doi.org/10.48550/arXiv.1506.04828
        valleys, _ = find_peaks(-magnitudes)
        if len(valleys) < 2:
            return np.array([np.nan])
        valley_widths = np.diff(valleys)
        valley_broadness = np.mean(valley_widths)
        return np.array([valley_broadness])

def calculate_frequency_variance(self, freqs, magnitudes):
        # https://doi.org/10.1016/B978-0-12-811153-6.00003-8
        mean_freq = np.sum(freqs * magnitudes) / np.sum(magnitudes)
        variance = np.sum(((freqs - mean_freq) ** 2) * magnitudes) / np.sum(magnitudes)
        return np.array([variance])

def calculate_frequency_std(self, freqs, magnitudes):
        # https://doi.org/10.1016/B978-0-12-811153-6.00003-8
        mean_freq = np.sum(freqs * magnitudes) / np.sum(magnitudes)
        variance = np.sum(((freqs - mean_freq) ** 2) * magnitudes) / np.sum(magnitudes)
        std_dev = np.sqrt(variance)
        return np.array([std_dev])

def calculate_frequency_range(self, freqs):
        # https://doi.org/10.1016/B978-0-12-811153-6.00003-8
        freq_range = np.max(freqs) - np.min(freqs)
        return np.array([freq_range])

def calculate_frequency_trimmed_mean(self, freqs, magnitudes, trim_percent=0.1):
        # https://doi.org/10.1016/B978-0-12-811153-6.00003-8
        sorted_indices = np.argsort(magnitudes)
        lower_limit = int(trim_percent * len(magnitudes))
        upper_limit = int((1 - trim_percent) * len(magnitudes))
        trimmed_indices = sorted_indices[lower_limit:upper_limit]
        trimmed_mean = np.mean(freqs[trimmed_indices])
        return np.array([trimmed_mean])
    
def calculate_harmonic_product_spectrum(self, magnitudes):
        # 10.1109/MHS.2018.8886911
        hps = np.copy(magnitudes)
        for h in range(2, 5):
            decimated = magnitudes[::h]
            hps[:len(decimated)] *= decimated
        return np.array([np.sum(hps)])

def calculate_smoothness(self, magnitudes):
        # https://doi.org/10.3390/rs13163196
        smoothness = np.sum(np.diff(magnitudes)**2)
        return np.array([smoothness])

def calculate_roughness(self, magnitudes):
        roughness = np.sum(np.abs(np.diff(magnitudes)))
        return np.array([roughness])
    

# features haven't been implemented yet and cannot find reference
# https://musicinformationretrieval.com/spectral_features.html
# Spectral Strongest Frequency Magnitude: Magnitude of the strongest frequency component.
# Spectral Strongest Frequency: The strongest frequency component.
# Spectral Frequency at Median Power: The frequency at which the power is median.
# Spectral Cumulative Frequency Below 25% Power: The frequency below which 25% of the spectral power is contained.
# Spectral Cumulative Frequency Above 25% Power: The frequency above which 25% of the spectral power is contained.
# Spectral Cumulative Frequency Above 50% Power: The frequency above which 50% of the spectral power is contained.
# Spectral Power Ratio (between different bands): The ratio of power between different frequency bands.
# Spectral Centroid Shift: The change in spectral centroid over time.
# Spectral Flux Shift: The change in spectral flux over time.
# Spectral Rolloff Shift: The change in spectral rolloff over time.
# Spectral Energy Vector: Vector of spectral energy values.
# Spectral High Frequency Content: The amount of energy in the high-frequency band.
# Spectral Peak Distribution: The distribution of peaks in the spectrum.
# Spectral Valley Distribution: The distribution of valleys in the spectrum.
# Spectral Valley Depth Median: The median depth of valleys in the spectrum.
# Spectral Valley Depth Mode: The most frequent valley depth.
# Spectral Valley Width Mean: The mean width of valleys.
# Spectral Valley Width Median: The median width of valleys.
# Spectral Valley Width Variance: The variance of valley widths.
# Spectral Dominant Valley: The most prominent valley.
# Spectral Peak Sharpness: The sharpness of the spectral peaks.
# Spectral Valley Sharpness: The sharpness of the spectral valleys.
# Spectral Dominant Peak: The most prominent peak.
# Spectral Subdominant Peak: The second most prominent peak.