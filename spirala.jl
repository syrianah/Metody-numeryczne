using Plots

plotly()

phi = 0:0.01:4*pi

x = (phi/2).*cos.(phi)
y = (phi/2).*sin.(phi)

plot(x, y)
