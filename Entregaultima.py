def geom(y,b,ss):
	#no se si ya estan antes
	# b = 10
	# q = 30
	# ss = 0.001
	# n = 0.013

	a = b*y+ss*y
	dady = b+2*y*ss
	
	l = y*sqrt(ss**2+1)
	p = b+2*l
	dpdy = 2*sqrt(ss**2+1)

	r = a/p
	drdy = (p**-1)*dpdy-(a/p**2)
	return r,drdy

def NR_fgv(yini, b, n, s, ss, c0, dx, y1, z1):
	y2 = yini

	if c0 = 1:
		g = 9.81
	else:
		g = 32,2
	

	tol = 10
	iter = 0

	while tol>10**-5 and iter<100:
		iter = iter +1
		geom(y1, b, ss)
		geom(y2, b, ss)
		z2 = z1 - s*dx
		# no se como hacer que geom te guarde a y r de cada uno como a1 y r1 para ocuparlos despues
		h1 = z1 + y1 + (q**2)/(2*g*(a1**2))
		h2 = z2 + y2 + (q**2)/(2*g*(a2**2))
		sf1 = ((q*n)**2)/((c0*a1*r1**(2/3))**2
		sf2 = ((q*n)**2)/((c0*a2*r2**(2/3))**2
		# llamar a la funcion newton raphson para obtener fy2 y dfy2dy2
		yf = (y2 - fy2)/dfy2dy2
		tol = abs(yf-y2)
		y2 = yf
	return yf

def FGV(yini,Q,B,S,ss,Co,X1,Y1,alpha,dx):
	x(1)=X1
	y(1)=Y1
	z(1)=z1

	if c0 = 1:
		g = 9.81
	else:
		g = 32,2
	i=0
	while y(i+1)<(yn-diff) or y(i+1)>(yn+diff):
		i=i+1
		dist=dist + dx
		x(i+1)=x(i)+ dx
		[y(i+1),z(i+1)]=NR_fgv(yini,B,Q,n,ss,Co,dx,y(1),z(1))
	elsa = y+z
	return elsa