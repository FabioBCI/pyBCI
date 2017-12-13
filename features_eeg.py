import scipy
from scipy import signal

def pwelch(data,fs,nseg):
	f,power=signal.welch(data, fs, nperseg=nseg)
	return power.tolist()