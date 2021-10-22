#!/usr/bin/env python
# encoding: utf-8

from multiprocessing import Pool, cpu_count
from functools import partial
import pandas as pd
import numpy as np
import time
import detect_calculated as det_cal

if __name__ == '__main__':
    #--------获取数据------------------
    inputfile='./Data_Renew.csv'
    data=pd.read_csv(inputfile)
    params = det_cal.get_params(data)
    
    i=params[0]
    partialCheck = partial(det_cal.Check, params_1 = params[1], 
                           params_2 = params[2], 
                           params_3 = params[3], 
                           params_4 = params[4])
    
    #--------多进程计算------------------
    cores=int(cpu_count()/2)
    pool = Pool(processes=cores)
    
    time_start=time.time()

    Index = np.array(pool.map(partialCheck, i))
    
    time_end=time.time()
    print('cost1: ',time_end-time_start)

    pool.close()
    pool.join()
    
    T=[1]
    
#    result = det_cal.evaluate_station(params[1], params[2], params[3], params[5], Index, T)
    