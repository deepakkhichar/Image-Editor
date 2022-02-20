# name: File path of the pgm image file
# Output is a 2D list of integers

def readpgm(name):
	image = []
	with open(name) as f:
		lines = list(f.readlines())
		if len(lines) < 3:
			print("Wrong Image Format\n")
			exit(0)

		count = 0
		width = 0
		height = 0
		for line in lines:
			if line[0] == '#':
				continue

			if count == 0:
				if line.strip() != 'P2':
					print("Wrong Image Type\n")
					exit(0)
				count += 1
				continue

			if count == 1:
				dimensions = line.strip().split(' ')
				print(dimensions)
				width = dimensions[0]
				height = dimensions[1]
				count += 1
				continue

			if count == 2:	
				allowable_max = int(line.strip())
				if allowable_max != 255:
					print("Wrong max allowable value in the image\n")
					exit(0)
				count += 1
				continue

			data = line.strip().split()
			data = [int(d) for d in data]
			image.append(data)
	return image	

x = readpgm('test.pgm')	 # test.pgm is the image present in the same working directory

n,m=len(x[0]),len(x)
c=[[0 for j in range(n)] for i in range (m)]
b=[[0 for j in range(n+2)] for i in range(m+2)]
d = c[:]
for i in range(m):
	for j in range(n):
		b[i+1][j+1]=x[i][j]

# img is the 2D list of integers
# file is the output file path
def findAverage():
	for i in range (m):
		for j in range (n):
			c[i][j]=(b[i][j]+b[i][j+1]+b[i][j+2]+b[i+1][j]+b[i+1][j+1]+b[i+1][j+2]+b[i+2][j]+b[i+2][j+1]+b[i+2][j+2])//9 
	for i in range(n):
		c[0][i]=x[0][i]
		c[m-1][i]=x[m-1][i]
	for i in range (m):
		c[i][0]=x[i][0]
		c[i][n-1]=x[i][n-1]
	return c



def Edgedetection():
	hdif=[[0 for j in range(n)] for i in range (m)]
	vdif=[[0 for j in range(n)] for i in range (m)]
	grad=[[0 for j in range(n)] for i in range (m)]
	for i in range (m):
		for j in range(n):
			hdif[i][j]=(b[i][j]-b[i][j+2]) + 2*(b[i+1][j]-b[i+1][j+2]) + (b[i+2][j]-b[i+2][j+2])
			vdif[i][j]=(b[i][j]-b[i+2][j]) + 2*(b[i][j+1]-b[i+2][j+1]) + (b[i][j+2]-b[i+2][j+2])
			grad[i][j]=(hdif[i][j]*hdif[i][j] + vdif[i][j]*vdif[i][j])**(1/2)
	k=0
	for i in range(m):
		for j in range(n):
			if grad[i][j]>k:
				k=grad[i][j]
	for i in range (m):
		for j in range (n):
			grad[i][j]=int(grad[i][j]*255/k)
	return grad
Edgedetection()
y=Edgedetection()

def Pathofleastenergy():
	energy=[[0 for j in range(n)] for i in range (m)]
	for j in range (n):
		energy[0][j]=y[0][j]
	for i in range (1,m):
		for j in range (n):
			if j==0:
				energy[i][j]=y[i][j] + min(energy[i-1][j],energy[i-1][j+1])
			if j==n-1:
				energy[i][j]=y[i][j] + min(energy[i-1][j-1],energy[i-1][j])
			else:
				energy[i][j]=y[i][j] + min(energy[i-1][j-1],energy[i-1][j],energy[i-1][j+1])
	f=min(energy[m-1])
	L=[]
	g=0
	for h in energy[m-1]:
		if h==f:
			L.append(g)
		g+=1
	for j in L:
		for i in range (1,m):
			x[-i][j]=255
			if j==0:
				k=min(energy[-i+1][j],energy[-i+1][j+1])
				if k==energy[-i+1][j]:
					j=j
				else:
					j=j+1
			if j==n-1:
				k=min(energy[-i+1][j-1],energy[-i+1][j])
				if k==energy[-i+1][j]:
					j=j
				else:
					j=j-1
			else:
				k=min(energy[-i+1][j-1],energy[-i+1][j],energy[-i+1][j+1])
				if k==energy[-i+1][j-1]:
					j=j-1
				if k==energy[-i+1][j]:
					j=j
				else:
					j=j+1
		x[0][j]=255
	return x


def writepgm(img, file):
	with open(file, 'w') as fout:
		if len(img) == 0:
			pgmHeader = 'p2\n0 0\n255\n'
		else:
			pgmHeader = 'P2\n' + str(len(img[0])) + ' ' + str(len(img)) + '\n255\n'
			fout.write(pgmHeader)
			line = ''
			for i in img:
				for j in i:
					line += str(j) + ' '
			line += '\n'
			fout.write(line)

########## Function Calls ##########
writepgm(findAverage(), 'findAverage.pgm')
writepgm(Edgedetection(), 'Edgedetection.pgm')
writepgm(Pathofleastenergy(), 'Pathofleastenergy.pgm')		# x is the image to output and test_o.pgm is the image output in the same working directory
###################################

