import matplotlib.pyplot as plt
import numpy as np
from MarketData import MarketData
from MarketCalculator import MarketCalculator

class PresentationManager:
    def __init__(self, calculator, marketData):
        self.calculator = calculator
        self.marketData = marketData
        
    def present(self):
        plt.subplot(211)
        self.drawLinePlot (self.marketData.day, self.marketData.data)
        plt.xticks(np.arange(0, len(self.marketData.day)+1, 100))
        plt.subplot(212)
        self.drawLinePlot (self.marketData.day, self.calculator.macd)
        self.drawLinePlot(self.marketData.day, self.calculator.signal)

        plt.plot(np.array(self.marketData.day)[self.calculator.intersections], np.array(self.calculator.macd)[self.calculator.intersections], 'ro')
        plt.xticks(np.arange(0, len(self.marketData.day)+1, 100))
        plt.show()

    def drawLinePlot(self, dataX, dataY):
        plt.plot(dataX, dataY)
        #plt.axis([0, 6, 0, 20])
        

data = MarketData("cdr_d.csv")
calculator = MarketCalculator(data)
presentation = PresentationManager(calculator, data)
presentation.present()
#input("Press Enter to continue...")