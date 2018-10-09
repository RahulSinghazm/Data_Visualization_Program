import matplotlib.pyplot as plt
x=[1,2,3,4,5,6,7,8,9,10]
y=[5,5,4,6,7,8,9,4,12,10]
x2=[1,2,3,4,5,6,7,8,9,10]
y2=[7,5,6,4,8,12,13,10,2,5]
plt.plot(x,y,label='India')
plt.plot(x2,y2,label='England')
plt.xlabel('Over Number')
plt.ylabel('Run')
plt.title('Show Rahul Singh Team Graph & Another Team Graph')
plt.legend()
plt.show()
