set datafile separator ","

y = y0 - a*x

y0 = log( / )

set fit prescale
fit F(x) 'v7.csv' using 5:4:7:6 xyerrors via a

# Set up the plot
set xlabel "x"
set ylabel "y"
set grid
set key off

set xrange [0:*]
set yrange [0:*]

set label 1 sprintf("k1 = %.2f ± %.2f", k, k_err) at graph 0.05, 0.95

set terminal pngcairo size 800,600 enhanced
set output 'vzmet7.png'

plot 'v7.csv' using 5:4:7:6 with xyerrorbars, \F(x) lt rgb "red"

set output
