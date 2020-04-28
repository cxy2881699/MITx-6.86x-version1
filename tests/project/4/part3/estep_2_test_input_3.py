import numpy as np
import common 

#  Correct output:
#  Input:
#
X = np.array(
[[0.85794562, 0.84725174],
 [0.6235637,  0.38438171],
 [0.29753461, 0.05671298],
 [0.,         0.47766512],
 [0.,         0.        ],
 [0.3927848,  0.        ],
 [0.,         0.64817187],
 [0.36824154, 0.        ],
 [0.,         0.87008726],
 [0.47360805, 0.        ],
 [0.,         0.        ],
 [0.,         0.        ],
 [0.53737323, 0.75861562],
 [0.10590761, 0.        ],
 [0.18633234, 0.        ]])

K = 6
mu = np.array(
[[0.6235637,  0.38438171],
 [0.3927848,  0.        ],
 [0.,         0.        ],
 [0.,         0.87008726],
 [0.36824154, 0.        ],
 [0.10590761, 0.        ]])

var = np.array([0.16865269, 0.14023295, 0.1637321,  0.3077471,  0.13718238, 0.14220473])

p = np.array([0.1680912,  0.15835331, 0.21384187, 0.14223565, 0.14295074, 0.17452722])
#  Output:
post = np.array(
[[0.65087662, 0.05857439, 0.02234959, 0.20258382, 0.0460844,  0.01953118],
 [0.36462427, 0.20175055, 0.09281546, 0.06127579, 0.17543624, 0.1040977 ],
 [0.10995174, 0.22464491, 0.20513252, 0.02839796, 0.21019956, 0.22167331],
 [0.27996042, 0.13156734, 0.18479023, 0.14012134, 0.11793063, 0.14563005],
 [0.1680912,  0.15835331, 0.21384187, 0.14223565, 0.14295074, 0.17452722],
 [0.17188253, 0.2079498,  0.16224482, 0.0981313,  0.18938262, 0.17040893],
 [0.33305679, 0.09456056, 0.14652199, 0.23671559, 0.08347925, 0.10566582],
 [0.1634873,  0.20447446, 0.16926051, 0.09967819, 0.18702813, 0.1760714 ],
 [0.34047752, 0.04761128, 0.08765585, 0.42923507, 0.04092387, 0.0540964 ],
 [0.20164864, 0.21756366, 0.14029582, 0.09378665, 0.19519249, 0.15151274],
 [0.1680912,  0.15835331, 0.21384187, 0.14223565, 0.14295074, 0.17452722],
 [0.1680912,  0.15835331, 0.21384187, 0.14223565, 0.14295074, 0.17452722],
 [0.47521046, 0.09942182, 0.06885849, 0.20917529, 0.08508798, 0.06224596],
 [0.09128906, 0.15565204, 0.25208102, 0.12427594, 0.14824935, 0.22845259],
 [0.11018277, 0.17234878, 0.22552021, 0.1149792,  0.16231678, 0.21465225]])

ll = -8.829390

def data():
    return X, K, common.GaussianMixture(mu, var, p), post, ll