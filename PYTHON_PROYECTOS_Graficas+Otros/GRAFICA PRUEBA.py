import matplotlib
import matplotlib.pyplot as plt

fig = plt.figure()
ax = fig.add_subplot()
fig.subplots_adjust(top=0.85)
# Set both x- and y-axis limits to [0, 10] instead of default [0, 1]
ax.axis([0, 10, 0, 10])

ax.annotate('holi', xy=(2, 1), xytext=(3, 4),
            arrowprops=dict(facecolor='black', shrink=1))

plt.show()