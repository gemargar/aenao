#!/usr/bin/env python
# Plot a graph of Data which is comming in on the fly
# uses pylab
# Author: Norbert Feurle
# Date: 12.1.2012
# License: if you get any profit from this then please share it with me
import pylab
from pylab import *

# i2c libraries
import time
import board
import busio

xAchse=pylab.arange(0,100,1)
yAchse=pylab.array([0]*100)

fig = pylab.figure(1)
ax = fig.add_subplot(111)
ax.grid(True)
ax.set_title("Realtime Waveform Plot")
ax.set_xlabel("Time")
ax.set_ylabel("Amplitude")
ax.axis([0,100,-1.5,1.5])
line1=ax.plot(xAchse,yAchse,'-')

manager = pylab.get_current_fig_manager()

values=[]
values = [0 for x in range(100)]

Ta=0.01
fa=1.0/Ta
fcos=3.5

Konstant=cos(2*pi*fcos*Ta)
T0=1.0
T1=Konstant

# initializing empty values 
# for x and y co-ordinates 
xdata, ydata = [], [] 

i2c = busio.I2C(board.SCL, board.SDA)

import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn
ads = ADS.ADS1115(i2c)

chan = AnalogIn(ads, ADS.P0, ADS.P1)

def SinwaveformGenerator(arg):
  global values,T1,Konstant,T0
  #ohmegaCos=arccos(T1)/Ta
  #print "fcos=", ohmegaCos/(2*pi), "Hz"

  Tnext = chan.voltage
  values.append(Tnext)
  '''
  Tnext=((Konstant*T1)*2)-T0
  if len(values)%100>70:
    values.append(random()*2-1)
  else:
    values.append(Tnext)
  '''
  T0=T1
  T1=Tnext

def RealtimePloter(arg):
  global values
  CurrentXAxis=pylab.arange(len(values)-100,len(values),1)
  line1[0].set_data(CurrentXAxis,pylab.array(values[-100:]))
  ax.axis([CurrentXAxis.min(),CurrentXAxis.max(),-0.2,3.5])
  manager.canvas.draw()
  #manager.show()

timer = fig.canvas.new_timer(interval=20)
timer.add_callback(RealtimePloter, ())
timer2 = fig.canvas.new_timer(interval=20)
timer2.add_callback(SinwaveformGenerator, ())
timer.start()
timer2.start()

pylab.show()