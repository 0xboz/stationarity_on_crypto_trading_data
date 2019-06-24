from arch.unitroot import ADF, PhillipsPerron, KPSS
import pandas as pd


class StationarityTests:
    """
    Stationarity Testing
    Also often called Unit Root tests
    Three commonly used tests to check stationarity of the data
    """

    def __init__(self, significance=.05):
        self.SignificanceLevel = significance
        self.pValue = None
        self.isStationary = None

    def ADF_Test(self, timeseries, printResults=True):
        """
        Augmented Dickey-Fuller (ADF) Test
        Null Hypothesis is Unit Root
        Reject Null Hypothesis >> Series is stationary >> Use price levels
        Fail to Reject >> Series has a unit root >> Use price returns
        """

        adfTest = ADF(timeseries)

        self.pValue = adfTest.pvalue

        if (self.pValue < self.SignificanceLevel):
            self.isStationary = True
        else:
            self.isStationary = False

        if printResults:

            print('Augmented Dickey-Fuller (ADF) Test Results: {}'.format(
                'Stationary' if self.isStationary else 'Not Stationary'))

    def PP_Test(self, timeseries, printResults=True):
        """
        Phillips-Perron (PP) Test
        Null Hypothesis is Unit Root
        Reject Null Hypothesis >> Series is stationary >> Use price levels
        Fail to Reject >> Series has a unit root >> Use price returns
        """

        ppTest = PhillipsPerron(timeseries)

        self.pValue = ppTest.pvalue

        if (self.pValue < self.SignificanceLevel):
            self.isStationary = True
        else:
            self.isStationary = False

        if printResults:
            print('Phillips-Perron (PP) Test Results: {}'.format(
                'Stationary' if self.isStationary else 'Not Stationary'))

    def KPSS_Test(self, timeseries, printResults=True):
        """
        Kwiatkowski-Phillips-Schmidt-Shin (KPSS) Test
        Null Hypothesis is Unit Root
        Reject Null Hypothesis >> Series has a unit root >> Use price returns
        Fail to Reject >> Series is stationary >> Use price levels
        """
        kpssTest = KPSS(timeseries)

        self.pValue = kpssTest.pvalue

        if (self.pValue < self.SignificanceLevel):
            self.isStationary = False
        else:
            self.isStationary = True

        if printResults:
            print('Kwiatkowski-Phillips-Schmidt-Shin (KPSS) Test Results: {}'.format(
                'Stationary' if self.isStationary else 'Not Stationary'))
