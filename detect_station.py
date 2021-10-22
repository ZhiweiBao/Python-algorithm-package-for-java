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
    inputfile='./data/142_JYL20009.xlsx'
    data=pd.read_excel(inputfile)
    data = data.rename(columns=lambda x: x.replace("'","").replace('"','').replace(" ",""))
    
    params = det_cal.get_params(data)
    
    i=params[0]

    
    partialCheck2 = partial(det_cal.Check2, params_1 = params[1], 
                           params_2 = params[2], 
                           params_3 = params[3], 
                           params_4 = params[4]) 
    
    #--------多进程计算------------------
    cores=int(cpu_count()/2)
    pool = Pool(processes=cores)
    
    time_start=time.time()

    Index = np.array(pool.map(partialCheck2, i))
    
    time_end=time.time()
    print('cost1: ',time_end-time_start)

    pool.close()
    pool.join()
    
        
    result = det_cal.detect_station(params[1], params[2], params[3], params[5], Index)

