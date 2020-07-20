import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patches as patch
import math

df = pd.read_csv('C:/Users/rafae/OneDrive/Documentos/ITBA/Fisica/mediciones_fisica.csv', sep=';', decimal=',')
print(df)

x = np.array([0,1,2,3,4])

fig, ax =  plt.subplots(1,2)
plt.subplots_adjust(wspace=0.3)

print('X:',x)

ejesx = df.axes[1].insert(0,'')

ax[0].set_xticklabels(ejesx, minor=False)
print(ejesx)
# df.plot(kind='scatter',x=df.axes,y=df.columns,color='red')
for i in range(0,10):
    if i==9:
        ax[0].scatter(x, np.array(df.values[9]), c='b', alpha=0.2, s=500,linewidths=0, label='muestras')
        break
    ax[0].scatter(x, np.array(df.values[i]), c='b', alpha=0.2, s=500,linewidths=0)
    pass

ax[0].scatter(x, np.array(df.mean(0)), c='r', alpha=1, s=300,marker='+', label = 'promedio')



ax[1].set_xticklabels(ejesx, minor=False)
# df.plot(kind='scatter',x=df.axes,y=df.columns,color='red')
for i in range(0,5):
    # ax[1].axvline(x=i, ymin=, ymax=, lw=5)
    end = round(math.tan(math.radians(df.max()[i])),2)
    beg = round(math.tan(math.radians(df.min()[i])),2)
    abserr = (end-beg)/2
    ue = math.tan(math.radians(df.mean(0)[i]))
    From = ue - abserr
    To = ue + abserr
    print( df.axes[1][i], 'max:',end, 'min:', beg)
    if i==4:
        ax[1].bar(4, abserr*2, 0.1, From, color = 'orange', alpha = 0.4, label='margen de error')
        ax[1].scatter(4, ue, c = 'orange', s=250, marker='_',label='mu promedio')
        break
    ax[1].bar(i, abserr*2, 0.1, From, color = 'orange', alpha = 0.4)
    ax[1].scatter(i, ue, c = 'orange', s=250, marker='_',)
    pass

# ax[1].scatter(x, np.array(df.mean(0)), c='r', alpha=1, s=300,marker='+')

# fig.suptitle('asdasd')
ax[0].set_title('Mediciones')
ax[0].set_xlabel('Materiales')
ax[0].set_ylabel('Ángulos (grados)')
ax[0].legend(borderpad=0.7, labelspacing=1.2, shadow=True)

ax[1].set_title('Coeficientes de rozamiento')
ax[1].set_xlabel('Materiales')
ax[1].set_ylabel('mu estático')
ax[1].legend(shadow=True)

plt.show()