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

#### n=10, time=0.1, runs=20, population_size=160
```
Algorithm                       Mean    Min     Max
Island GA Watts Strogatz        13.42   8.10    23.60
Island GA Rewired Caveman       13.71   8.05    19.62
Island GA Caveman               14.03   9.22    20.17
Island GA Cell                  14.41   9.09    23.51
Island GA Ring Lattice          14.45   10.65   23.59
Island GA Hierarchy             15.71   7.15    26.21
Genetic Algorithm               54.47   37.63   73.42
```

#### n=10, time=0.5, runs=20, population_size=160
```
Algorithm                       Mean    Min     Max
Island GA Watts Strogatz        13.42   8.10    23.60
Island GA Rewired Caveman       13.71   8.05    19.62
Island GA Caveman               14.03   9.22    20.17
Island GA Ring Lattice          14.13   10.65   17.27
Island GA Cell                  14.41   9.09    23.51
Island GA Hierarchy             15.71   7.15    26.21
Genetic Algorithm               49.77   32.73   62.75
```

#### n=10, time=1, runs=20, population_size=160
```
Algorithm                       Mean    Min     Max
Island GA Watts Strogatz        13.42   8.10    23.60
Island GA Rewired Caveman       13.71   8.05    19.62
Island GA Caveman               14.03   9.22    20.17
Island GA Ring Lattice          14.13   10.65   17.27
Island GA Cell                  14.41   9.09    23.51
Island GA Hierarchy             15.71   7.15    26.21
Genetic Algorithm               45.73   22.62   58.66
```

#### n=10, time=5, runs=20, population_size=160
```
Algorithm                       Mean    Min     Max
Island GA Watts Strogatz        13.42   8.10    23.60
Island GA Rewired Caveman       13.71   8.05    19.62
Island GA Caveman               14.03   9.22    20.17
Island GA Ring Lattice          14.13   10.65   17.27
Island GA Cell                  14.41   9.09    23.51
Island GA Hierarchy             15.71   7.15    26.21
Genetic Algorithm               41.01   22.62   51.27
```

#### n=10, time=0.1, runs=20, population_size=320
```
Algorithm                       Mean    Min     Max
Island GA Cell                  11.25   6.76    14.46
Island GA Watts Strogatz        11.96   3.62    18.98
Island GA Ring Lattice          12.48   5.35    41.53
Island GA Caveman               13.27   8.26    19.80
Island GA Rewired Caveman       16.51   6.52    104.30
Island GA Hierarchy             16.79   10.84   25.88
Genetic Algorithm               59.15   35.20   76.60
```

#### n=10, time=0.5, runs=20, population_size=320
```
Algorithm                       Mean    Min     Max
Island GA Rewired Caveman       10.24   6.52    16.22
Island GA Ring Lattice          10.86   5.35    16.16
Island GA Cell                  11.25   6.76    14.46
Island GA Watts Strogatz        11.96   3.62    18.98
Island GA Caveman               13.27   8.26    19.80
Island GA Hierarchy             16.79   10.84   25.88
Genetic Algorithm               49.91   35.20   62.19
```

#### n=10, time=1, runs=20, population_size=320
```
Algorithm                       Mean    Min     Max
Island GA Rewired Caveman       10.24   6.52    16.22
Island GA Ring Lattice          10.86   5.35    16.16
Island GA Cell                  11.25   6.76    14.46
Island GA Watts Strogatz        11.96   3.62    18.98
Island GA Caveman               13.27   8.26    19.80
Island GA Hierarchy             16.79   10.84   25.88
Genetic Algorithm               49.58   35.20   62.19
```


#### n=10, time=5, runs=20, population_size=320
```
Algorithm                       Mean    Min     Max
Island GA Rewired Caveman       10.24   6.52    16.22
Island GA Ring Lattice          10.86   5.35    16.16
Island GA Cell                  11.25   6.76    14.46
Island GA Watts Strogatz        11.96   3.62    18.98
Island GA Caveman               13.27   8.26    19.80
Island GA Hierarchy             16.79   10.84   25.88
Genetic Algorithm               42.30   33.97   52.53
```

#### n=10, time=0.1, runs=20, population_size=640
```
Algorithm                       Mean    Min     Max
Island GA Caveman               10.28   4.99    14.73
Island GA Cell                  10.67   6.22    14.60
Island GA Ring Lattice          13.40   6.97    54.99
Island GA Hierarchy             14.78   7.53    23.48
Island GA Watts Strogatz        21.61   8.01    70.99
Island GA Rewired Caveman       27.02   8.22    105.08
Genetic Algorithm               64.86   48.79   78.73
```

#### n=10, time=0.5, runs=20, population_size=640
```
Algorithm                       Mean    Min     Max
Island GA Ring Lattice          9.53    6.08    11.90
Island GA Watts Strogatz        9.72    6.26    13.19
Island GA Caveman               10.10   4.99    14.73
Island GA Rewired Caveman       10.19   5.27    13.65
Island GA Cell                  10.67   6.22    14.60
Island GA Hierarchy             14.78   7.53    23.48
Genetic Algorithm               56.45   45.23   69.42
```

#### n=10, time=1, runs=20, population_size=640
```
Algorithm                       Mean    Min     Max
Island GA Ring Lattice          9.53    6.08    11.90
Island GA Watts Strogatz        9.72    6.26    13.19
Island GA Caveman               10.10   4.99    14.73
Island GA Rewired Caveman       10.19   5.27    13.65
Island GA Cell                  10.67   6.22    14.60
Island GA Hierarchy             14.78   7.53    23.48
Genetic Algorithm               53.74   45.23   65.30
```

#### n=10, time=5, runs=20, population_size=640
```
Algorithm                       Mean    Min     Max
Island GA Ring Lattice          9.53    6.08    11.90
Island GA Watts Strogatz        9.72    6.26    13.19
Island GA Caveman               10.10   4.99    14.73
Island GA Rewired Caveman       10.19   5.27    13.65
Island GA Cell                  10.67   6.22    14.60
Island GA Hierarchy             14.78   7.53    23.48
Genetic Algorithm               47.35   38.61   55.06
```

#### n=10, time=0.1, runs=20, population_size=1280
```
Algorithm                       Mean    Min     Max
Island GA Cell                  10.75   6.54    14.01
Island GA Caveman               11.70   8.17    16.45
Island GA Hierarchy             15.38   8.88    22.26
Island GA Ring Lattice          18.97   9.79    74.50
Genetic Algorithm               72.41   59.57   78.86
*Island GA Rewired Caveman*     90.89   63.95   112.72
*Island GA Watts Strogatz*      90.89   63.95   112.72
```

#### n=10, time=0.5, runs=20, population_size=1280
```
Island GA Ring Lattice          8.11    4.75    11.32
Island GA Caveman               9.03    6.72    11.87
Island GA Cell                  9.35    6.33    13.18
Island GA Watts Strogatz        9.51    4.30    14.37
Island GA Rewired Caveman       12.58   5.19    96.01
Island GA Hierarchy             14.42   8.88    22.26
Genetic Algorithm               59.95   31.94   72.68
```

#### n=10, time=1, runs=20, population_size=1280
```
Algorithm                       Mean    Min     Max
Island GA Rewired Caveman       8.11    5.19    12.19
Island GA Ring Lattice          8.11    4.75    11.32
Island GA Watts Strogatz        8.68    4.30    14.37
Island GA Caveman               9.03    6.72    11.87
Island GA Cell                  9.35    6.33    13.18
Island GA Hierarchy             14.42   8.88    22.26
Genetic Algorithm               53.84   31.88   70.39
```

#### n=10, time=5, runs=20, population_size=1280
```
Algorithm                       Mean    Min     Max
Island GA Rewired Caveman       8.11    5.19    12.19
Island GA Ring Lattice          8.11    4.75    11.32
Island GA Watts Strogatz        8.68    4.30    14.37
Island GA Caveman               9.03    6.72    11.87
Island GA Cell                  9.35    6.33    13.18
Island GA Hierarchy             14.42   8.88    22.26
Genetic Algorithm               44.97   28.88   57.15
```

## Citation

If you use this work, please cite:

```
TBD
```