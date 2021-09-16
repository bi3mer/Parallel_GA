# A Socially Structured Genetic Algorithm for Discrete Optimization

## Outside Libraries

- [TSPLIB](http://comopt.ifi.uni-heidelberg.de/software/TSPLIB95/tsp/) for TSP problems.
- [tsplib95](https://github.com/rhgrant10/tsplib95/tree/c9edc6bf905ff33e38c0f475e855b3d866d72dcd) for reading TSPLIB.

## Results

### TSP

#### bayg29 (min=1610), time=0.1, runs=20
```
Algorithm                       Mean    Min     Max
Cell                            1662.45 1610.00 1746.00
Caveman                         1675.50 1618.00 1759.00
Hierarchy                       1689.75 1610.00 1804.00
Watts Strogatz Caveman          1707.75 1615.00 1819.00
Random Restart Hill Climbing    1760.90 1653.00 1851.00
Rewired Caveman                 1761.75 1622.00 2089.00
Ring Lattice                    1800.35 1627.00 2806.00
Local Beam Search               1941.35 1684.00 2241.00
Hill Climber                    1953.75 1807.00 2154.00
Simulated Annealing             1986.10 1770.00 2255.00
Genetic Algorithm               3106.30 2731.00 3455.00
Stochastic Beam Search          3246.90 2869.00 3600.00
```

#### att48 (min=10628), time=0.1, runs=20
```
Algorithm                       Mean            Min             Max
Simulated Annealing             16328.00        14154.00        18281.00
Random Restart Hill Climbing    20470.90        15112.00        25396.00
Hill Climber                    21252.90        14240.00        35560.00
Hierarchy                       25691.25        23353.00        29002.00
Watts Strogatz Caveman          25734.15        23948.00        28458.00
Caveman                         26204.95        24665.00        28339.00
Cell                            26694.05        22751.00        30047.00
Ring Lattice                    28319.15        24998.00        33198.00
Rewired Caveman                 30578.55        25106.00        38113.00
Genetic Algorithm               35883.85        32755.00        38362.00
Local Beam Search               39756.60        37261.00        42160.00
Stochastic Beam Search          40688.35        37961.00        43448.00
```

#### att48 (min=10628), time=1, runs=20
```
Algorithm                       Mean            Min             Max
Cell                            11393.45        10941.00        11903.00
Watts Strogatz Caveman          11436.25        11067.00        11895.00
Rewired Caveman                 11542.80        11058.00        12175.00
Caveman                         11596.50        11089.00        12258.00
Hierarchy                       11785.85        11280.00        12926.00
Ring Lattice                    11905.55        11362.00        12669.00
Random Restart Hill Climbing    13876.20        12633.00        16734.00
Hill Climber                    14881.55        12953.00        17273.00
Simulated Annealing             15638.95        13196.00        17976.00
Local Beam Search               24060.80        21565.00        26920.00
Genetic Algorithm               30647.00        26149.00        34112.00
Stochastic Beam Search          37595.05        35180.00        39786.00
```

### Rastigan

#### n=5, time=1, runs=5

```
Algorithm                       Mean    Min     Max
Cell                            0.01    0.00    0.02
Ring Lattice                    0.01    0.00    0.01
Caveman                         0.01    0.00    0.02
Rewired Caveman                 0.01    0.00    0.02
Watts Strogatz Caveman          0.02    0.00    0.03
Hierarchy                       0.02    0.00    0.08
Genetic Algorithm               7.44    4.31    10.90
Stochastic Beam Search          49.77   29.38   66.13
Local Beam Search               58.92   48.17   66.20
Hill Climber                    88.36   58.12   102.24
Random Restart Hill Climbing    100.51  73.64   143.83
Simulated Annealing             103.88  73.64   144.62
```

#### n=6, time=1, runs=5

```
Algorithm                       Mean    Min     Max
Rewired Caveman                 0.07    0.02    0.23
Ring Lattice                    0.12    0.04    0.33
Caveman                         0.12    0.01    0.38
Watts Strogatz Caveman          0.27    0.07    0.46
Hierarchy                       0.38    0.05    0.92
Cell                            0.56    0.00    2.47
Genetic Algorithm               12.62   10.45   16.95
Stochastic Beam Search          63.04   51.91   83.93
Local Beam Search               65.81   57.68   85.28
Random Restart Hill Climbing    115.66  88.51   168.31
Simulated Annealing             119.12  91.88   173.55
Hill Climber                    119.58  96.90   148.33
```

#### n=7, time=1, runs=5

```
Algorithm                       Mean    Min     Max
Caveman                         0.66    0.05    1.97
Rewired Caveman                 0.77    0.46    1.04
Watts Strogatz Caveman          0.82    0.24    2.07
Ring Lattice                    1.27    0.68    2.04
Cell                            1.32    0.13    3.38
Hierarchy                       2.80    0.87    3.88
Genetic Algorithm               22.52   18.48   26.07
Stochastic Beam Search          64.58   49.80   89.87
Local Beam Search               68.31   59.19   89.87
Hill Climber                    127.68  79.27   171.88
Random Restart Hill Climbing    135.58  98.65   182.09
Simulated Annealing             142.16  102.02  202.47
```

#### n=8, time=1, runs=5

```
Algorithm                       Mean    Min     Max
Ring Lattice                    3.56    2.03    5.40
Watts Strogatz Caveman          3.79    1.42    5.79
Cell                            4.64    1.73    7.71
Rewired Caveman                 5.23    2.22    8.63
Caveman                         5.27    2.64    7.78
Hierarchy                       6.66    3.98    10.04
Genetic Algorithm               29.34   23.51   35.60
Stochastic Beam Search          88.64   76.30   101.09
Local Beam Search               89.94   76.30   98.19
Hill Climber                    140.22  117.16  154.03
Random Restart Hill Climbing    146.95  102.74  186.19
Simulated Annealing             157.30  106.11  209.85
```


## Citation

If you use this work, please cite:

```
TBD
```