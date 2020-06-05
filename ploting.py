import matplotlib.pyplot as plt
x=[1,2,3,4,5,6]
y=[2,4,1,5,2,6]
#ploting the points
plt.plot(x,y,color='green', linestyle='dashed', linewidth='8', marker='o', markerfacecolor='blue', markersize='12')
plt.ylim(1,8)
plt.xlim(1,8)


plt.xlabel('x axis')
plt.ylabel('y  axis')

plt.title('some cool customizations!')

plt.show()

