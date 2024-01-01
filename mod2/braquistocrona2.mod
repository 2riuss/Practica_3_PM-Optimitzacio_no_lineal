param n >= 0;
param a >= 0;
param b >= 0;
param g >= 0;
param eps >= 0;

param y{i in 0..n} = b*(1-((n-i)/n)^2) + eps;

var x{0..n} >= 0;

# Funcio objetiu
minimize velocitat:
		1/sqrt(2*g) * sum {i in 0..n-1} sqrt( ((x[i+1]-x[i])^2 + (y[i+1]-y[i])^2) / abs(y[i]) );

# Restriccions
subject to x_inicial:
	x[0] = 0;

subject to x_final:
	x[n] = a;