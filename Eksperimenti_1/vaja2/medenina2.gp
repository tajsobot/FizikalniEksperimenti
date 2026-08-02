#!/usr/bin/gnuplot
#
#    
#    	G N U P L O T
#    	Version 6.0 patchlevel 2    last modified 2024-12-19 
#    
#    	Copyright (C) 1986-1993, 1998, 2004, 2007-2024
#    	Thomas Williams, Colin Kelley and many others
#    
#    	gnuplot home:     http://www.gnuplot.info
#    	faq, bugs, etc:   type "help FAQ"
#    	immediate help:   type "help"  (plot window: hit 'h')
# set terminal pngcairo  background "#ffffff" enhanced fontscale 1.0 size 1200, 600 
# set output 'medenina.png'
unset clip points
set clip one
unset clip two
unset clip radial
set errorbars front 1.000000 
set border 31 front lt black linewidth 1.000 dashtype solid
set cornerpoles
set zdata 
set ydata 
set xdata 
set y2data 
set x2data 
set boxwidth
set boxdepth 0
set style fill  empty border
set style rectangle back fc  bgnd fillstyle   solid 1.00 border lt -1
set style circle radius graph 0.02 
set style ellipse size graph 0.05, 0.03 angle 0 units xy
set dummy x, y
set format x "% h" 
set format y "% h" 
set format x2 "% h" 
set format y2 "% h" 
set format z "% h" 
set format cb "% h" 
set format r "% h" 
set ttics format "% h"
set timefmt "%d/%m/%y,%H:%M"
set angles radians
set tics back
unset grid
unset raxis
set theta counterclockwise right
set style parallel front  lt black linewidth 2.000 dashtype solid
set key notitle
set key fixed left top vertical Right noreverse enhanced autotitle box lt black linewidth 1.000 dashtype solid
set key noinvert samplen 4 spacing 1 width 0 height 0
set key maxcolumns 0 maxrows 0
set key noopaque
unset label
set label 1 "k = 0.1257 \302\261 0.0023" at graph 0.4, 0.95, 0 left norotate back nopoint
unset arrow
unset style line
unset style arrow
set style histogram clustered gap 2 title textcolor lt -1
unset object
unset walls
set style textbox  transparent margins  1.0,  1.0 border  lt -1 linewidth  1.0
set offsets 0, 0, 0, 0
set pointsize 1
set pointintervalbox 1
set encoding default
unset parametric
unset polar
unset spiderplot
unset decimalsign
unset micro
unset minussign
set view 60, 30, 1, 1
set view azimuth 0
set rgbmax 255
set samples 100, 100
set isosamples 10, 10
set surface implicit
set surface
set mapping cartesian
set datafile separator whitespace
set datafile nocolumnheaders
unset hidden3d

unset contour
set cntrlabel  format '%8.3g' font '' start 5 interval 20
set cntrparam order 4
set cntrparam linear
set cntrparam levels 5
set cntrparam levels auto
set cntrparam firstlinetype 0 unsorted
set cntrparam points 5
set size ratio 0 1,1
set origin 0,0
set contourfill auto 5
set contourfill palette
set style data points
set style function lines
unset xzeroaxis
unset yzeroaxis
unset zzeroaxis
unset x2zeroaxis
unset y2zeroaxis
set xyplane relative 0.5
set tics scale  1, 0.5, 1, 1, 1
set mxtics default
set mytics default
set mztics default
set mx2tics default
set my2tics default
set mcbtics default
set mrtics default
set nomttics
set xtics border in scale 1,0.5 mirror norotate  autojustify
set xtics  norangelimit autofreq 
set ytics border in scale 1,0.5 mirror norotate  autojustify
set ytics  norangelimit autofreq 
set ztics border in scale 1,0.5 nomirror norotate  autojustify
set ztics  norangelimit autofreq 
unset x2tics
unset y2tics
set cbtics border in scale 1,0.5 mirror norotate  autojustify
set cbtics  norangelimit autofreq 
set rtics axis in scale 1,0.5 nomirror norotate  autojustify
set rtics  norangelimit autofreq 
unset ttics
set title "" 
set title  font "" textcolor lt -1 norotate
set timestamp bottom 
set timestamp "" 
set timestamp  font "" textcolor lt -1 norotate
set trange [ * : * ] noreverse nowriteback
set urange [ * : * ] noreverse nowriteback
set vrange [ * : * ] noreverse nowriteback
set xlabel "kot zasuka [rad]" 
set xlabel  font "" textcolor lt -1 norotate
set x2label "" 
set x2label  font "" textcolor lt -1 norotate
set xrange [ 0.00000 : 0.500000 ] noreverse writeback
set x2range [ * : * ] noreverse writeback
set ylabel "navor [Nm]" 
set ylabel  font "" textcolor lt -1 rotate
set y2label "" 
set y2label  font "" textcolor lt -1 rotate
set yrange [ * : * ] noreverse writeback
set y2range [ * : * ] noreverse writeback
set zlabel "" 
set zlabel  font "" textcolor lt -1 norotate
set zrange [ * : * ] noreverse writeback
set cblabel "" 
set cblabel  font "" textcolor lt -1 rotate
set cbrange [ * : * ] noreverse writeback
set rlabel "" 
set rlabel  font "" textcolor lt -1 norotate
set rrange [ * : * ] noreverse writeback
unset logscale
unset jitter
set zero 1e-08
set lmargin  -1
set bmargin  -1
set rmargin  -1
set tmargin  -1
set locale "en_US.UTF-8"
set pm3d explicit at s
set pm3d scansautomatic
set pm3d interpolate 1,1 flush begin noftriangles noborder corners2color mean
set pm3d clip z 
set pm3d nolighting
set palette positive nops_allcF maxcolors 0 gamma 1.5 color model RGB 
set palette rgbformulae 7, 5, 15
set colorbox default
set colorbox vertical origin screen 0.9, 0.2 size screen 0.05, 0.6 front  noinvert bdefault
set style boxplot candles range  1.50 outliers pt 7 separation 1 labels auto unsorted
set chi_shapes fraction 0.60
set loadpath 
set fontpath
set psdir
set fit brief errorvariables nocovariancevariables errorscaling prescale nowrap v5
f1(x) = a1*x+b1
f1_upper(x) = (a1 + a1_err)*x + (b1 + b1_err)
f1_lower(x) = (a1 - a1_err)*x + (b1 - b1_err)
GNUTERM = "qt"
I = {0.0, 1.0}
VoxelDistance = 0.0
GridDistance = 0.0
x = 0.0
a1 = 0.125669596970014
b1 = 0.011538164055719
FIT_ERROR = 0
FIT_CONVERGED = 1
FIT_NDF = 4
FIT_STDFIT = 0.23689302595492
FIT_WSSR = 0.224473222984313
FIT_P = 0.99415349951223
FIT_NITER = 5
a1_err = 0.00233166069570394
b1_err = 0.000277423803726501
## Last fit command: "fit f1(x) "medenina.csv" using 1:2:4 via a1,b1"
## Last datafile plotted: "medenina.csv"
## Last plot command
plot "medenina.csv" u 1:2:3:4 w xyerrorbars title "meritve (medenina)" lt 8, f1(x) title "fit" lt 3, f1_upper(x) notitle lt 3 dashtype 2, f1_lower(x) notitle lt 3 dashtype 2
#    EOF
