from F1_Input import *
from F2_Mean import *
from F3_Median import *
from F4_Mode import *
from F5_Mean_Deviation import *
from F6_Standard_Deviation import *

f = input_fi()
x, gap = input_xi()
choice = input('Enter choice:\n1)Mean\n2)Median\n3)Mode\n4)Deviation\n').lower()

if choice in ['1', 'mean']:
    mean_choice = input('Enter choice:\n1)Mean\n2)Harmonic Mean\n3)Geometric Mean\n').lower()
    if mean_choice in ['1', 'mean']:
        m = mean(f, x)
        print(m)
        print('Mean = ', round(m[0], 4))
    elif mean_choice in ['2', 'hm', 'harmonic mean']:
        hm = harmonic_mean(f, x)
        print('Harmonic Mean = ', round(hm[0], 4))
    elif mean_choice in ['3', 'gm', 'geometric mean']:
        gm = geometric_mean(x, f)
        print('Geometric Mean = ', round(gm[0], 4))
elif choice in ['2', 'median']:
    median_choice = input('Enter choice:\n1)Median\n2)Quartiles\n')
    if median_choice in ['1', 'median']:
        m = median(f, x, gap)
        print(m)
        print('Median = ', round(m[0], 4))
    elif median_choice in ['2', 'quartiles']:
        q = quartiles(x, f, gap)
        print('Quartiles: ', q[0], ', ', q[1], ', ', q[2])
elif choice in ['3', 'mode']:
    m = mode(f, x, gap)
    print('Mode = ', m)
elif choice in ['4', 'deviation']:
    deviation_choice = input('Enter choice:\n1)Mean deviation about mean\n2)Mean deviation about median\n'
                             '3)Mean deviation about mode\n4)Standard deviation\n').lower()
    if deviation_choice in ['1', 'mean deviation']:
        m = mean_deviation_about_mean(x, f)
        print(m)
        print('Mean Deviation about mean = ', round(m[0], 4))
    elif deviation_choice in ['2', 'mean deviation about median']:
        m = mean_deviation_about_median(x, f, gap)
        print(m)
        print('Mean Deviation about median = ', round(m[0], 4))
    elif deviation_choice in ['3', 'mean deviation about mode']:
        m = mean_deviation_about_mode(x, f, gap)
        print(m)
        print('Mean Deviation about mode = ', round(m, 4))
    elif deviation_choice in ['4', 'standard deviation']:
        sd = standard_deviation(x, f)
        print('Standard Deviation = ', round(sd[0], 4))
else:
    print('Try Again....\nEntered choice not available')
