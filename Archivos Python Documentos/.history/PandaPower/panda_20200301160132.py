import pandapowere as pp
import pandapower.networks

net = pandapower.networks.example_simple()
net
pp.runpp(net)
print(net.res_bus)
