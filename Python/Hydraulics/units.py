from sympy import *

length = {
    symbols("km"): {symbols("hm"): 10, symbols("dam"): 100, symbols("m"): 1000, symbols("dm"): 10000,
                    symbols("cm"): 100000, symbols("mm"): 1000000},
    symbols("hm"): {symbols("km"): 0.1, symbols("dam"): 10, symbols("m"): 100, symbols("dm"): 1000,
                    symbols("cm"): 10000, symbols("mm"): 100000},
    symbols("dam"): {symbols("km"): 0.01, symbols("hm"): 0.1, symbols("m"): 10, symbols("dm"): 100, symbols("cm"): 1000,
                     symbols("mm"): 10000},
    symbols("m"): {symbols("km"): 0.001, symbols("hm"): 0.01, symbols("dam"): 0.1, symbols("dm"): 10, symbols("cm"): 100,
                   symbols("mm"): 1000},
    symbols("dm"): {symbols("km"): 0.0001, symbols("hm"): 0.001, symbols("dam"): 0.01, symbols("m"): 0.1, symbols("cm"): 10,
                    symbols("mm"): 100},
    symbols("cm"): {symbols("km"): 0.00001, symbols("hm"): 0.0001, symbols("dam"): 0.001, symbols("m"): 0.01, symbols("dm"): 0.1,
                    symbols("mm"): 10},
    symbols("mm"): {symbols("km"): 0.000001, symbols("hm"): 0.00001, symbols("dam"): 0.0001, symbols("m"): 0.001,
                    symbols("dm"): 0.01, symbols("cm"): 0.1},
}
