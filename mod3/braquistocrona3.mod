param n >= 0;
param a >= 0;
param b >= 0;
param g >= 0;
param eps >= 0;

var x{i in 0..n} >= 0 default a*i/n;
var y{i in 0..n} >= eps;

# Funcio objetiu
minimize velocitat:
		1/sqrt(2*g) * sum {i in 0..n-1} sqrt( ((x[i+1]-x[i])^2 + (y[i+1]-y[i])^2) / abs(y[i]) );

# Restriccions
subject to x_inicial:
	x[0] = 0;

subject to x_final:
	x[n] = a;

subject to y_inicial:
	y[0] = eps;

subject to y_final:
	y[n] = b;