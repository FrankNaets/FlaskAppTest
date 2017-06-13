from numpy  import exp, cos, linspace
import os, time, glob

def damped_vibrations(t, A, b, w):
	return A*exp(-b*t)*cos(w*t)

def compute(A, b, w, T, resolution=500):

	t = linspace(0, T, resolution+1)
	u = damped_vibrations(t, A, b, w)

	# Pass data to view:
	return t,u

if __name__=='__main__':
	print(compute(1, 0.1, 1, 20))
