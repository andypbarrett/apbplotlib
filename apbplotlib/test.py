import numpy as np
import matplotlib.pyplot as plt

import myplot

def test():
    '''Tests hovmoller plotting routine'''
    
    year = np.arange(1850,2019)
    month = np.arange(1,13)
    nyear = year.size
    nmonth = month.size
    
    values = np.random.randn(nyear*nmonth).reshape(nmonth, nyear)

    fig, ax = plt.subplots(figsize=(11,8))

    myplot.hovmoller(year, month, values, ax=ax, add_colorbar=False, aspect=4)
    #ax.set_aspect(4.)
    
    plt.show()
    
    return

if __name__ == "__main__":
    test()
