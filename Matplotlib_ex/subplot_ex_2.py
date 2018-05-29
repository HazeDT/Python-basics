import matplotlib.pyplot as plt 
import matplotlib.gridspec as gridspec#第二种方法时使用

#method 1:subplot2grid
######################
#plt.figure()
#ax1=plt.subplot2grid((3,3),(0,0),colspan=3,rowspan=1)#3x3表示将整个figure分为3x3个，0x0表示第一个图从0行0列开始，colspan表示这个图站多少跨度
#ax1.plot([1,2],[1,2])
#ax1.set_xlabel('ax1 title')
#ax2=plt.subplot2grid((3,3),(1,0),colspan=2,rowspan=1)
#ax3=plt.subplot2grid((3,3),(1,2),colspan=1,rowspan=2)
#ax4=plt.subplot2grid((3,3),(2,0),colspan=1,rowspan=1)
#ax1=plt.subplot2grid((3,3),(2,1),colspan=1,rowspan=1)



#method 2:gridspec
##################
#plt.figure()
#gs=gridspec.GridSpec(3,3)
#ax1=plt.subplot(gs[0,:])#其中[0,:]表示图1将0行所有列都占据
#ax2=plt.subplot(gs[1,：2])
#ax3=plt.subplot(gs[1：,2])
#ax4=plt.subplot(gs[-1,0])
#ax5=plt.subplot(gs[-1,-2])


#method 3:easy to define structure
#################################

f,((ax11,ax12),(ax21,ax22))=plt.subplots(2,2,sharex=True,sharey=True)
ax11.scatter([1,2],[1,2])


plt.tight_layout()
plt.show()