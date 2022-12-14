import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()
G.add_edge(106, 21)
G.add_edge(105, 21)
G.add_edge(104, 105)
G.add_edge(104, 106)
G.add_edge(30, 100)
G.add_edge(96, 100)
G.add_edge(96, 101)
G.add_edge(97, 101)
G.add_edge(99, 102)
G.add_edge(103, 102)
G.add_edge(103, 99)
G.add_edge(101, 102)
G.add_edge(101, 100)
G.add_edge(100, 32)
G.add_edge(99, 97)
G.add_edge(97, 96)
G.add_edge(96, 30)
G.add_edge(95, 36)
G.add_edge(94, 76)
G.add_edge(92, 76)
G.add_edge(92, 77)
G.add_edge(93, 91)
G.add_edge(93, 92)
G.add_edge(92, 36)
G.add_edge(91, 79)
G.add_edge(79, 77)
G.add_edge(77, 76)
G.add_edge(76, 46)
G.add_edge(64, 66)
G.add_edge(60, 66)
G.add_edge(71, 70)
G.add_edge(71, 64)
G.add_edge(72, 70)
G.add_edge(75, 70)
G.add_edge(75, 74)
G.add_edge(74, 73)
G.add_edge(73, 72)
G.add_edge(72, 71)
G.add_edge(71, 69)
G.add_edge(70, 67)
G.add_edge(69, 66)
G.add_edge(67, 64)
G.add_edge(66, 65)
G.add_edge(65, 63)
G.add_edge(64, 60)
G.add_edge(63, 60)
G.add_edge(63, 62)
G.add_edge(62, 61)
G.add_edge(61, 59)
G.add_edge(60, 45)
G.add_edge(59, 45)
G.add_edge(59, 57)
G.add_edge(57, 50)
G.add_edge(57, 52)
G.add_edge(57, 56)
G.add_edge(56, 55)
G.add_edge(55, 54)
G.add_edge(54, 53)
G.add_edge(53, 50)
G.add_edge(52, 50)
G.add_edge(52, 51)
G.add_edge(52, 45)
G.add_edge(51, 42)
G.add_edge(51, 44)
G.add_edge(50, 42)
G.add_edge(50, 49)
G.add_edge(49, 46)
G.add_edge(42, 46)
G.add_edge(46, 43)
G.add_edge(47, 34)
G.add_edge(47, 32)
G.add_edge(47, 46)
G.add_edge(46, 36)
G.add_edge(45, 44)
G.add_edge(44, 41)
G.add_edge(43, 39)
G.add_edge(42, 34)
G.add_edge(42, 41)
G.add_edge(41, 40)
G.add_edge(40, 39)
G.add_edge(39, 34)
G.add_edge(39, 37)
G.add_edge(37, 33)
G.add_edge(36, 32)
G.add_edge(35, 32)
G.add_edge(35, 34)
G.add_edge(34, 31)
G.add_edge(34, 33)
G.add_edge(33, 23)
G.add_edge(32, 30)
G.add_edge(31, 23)
G.add_edge(31, 30)
G.add_edge(31, 17)
G.add_edge(30, 29)
G.add_edge(29, 27)
G.add_edge(27, 26)
G.add_edge(26, 17)
G.add_edge(26, 19)
G.add_edge(26, 25)
G.add_edge(25, 24)
G.add_edge(23, 22)
G.add_edge(24, 20)
G.add_edge(22, 7)
G.add_edge(12, 11)
G.add_edge(20, 16)
G.add_edge(20, 19)
G.add_edge(19, 9)
G.add_edge(21, 15)
G.add_edge(17, 7)
G.add_edge(19, 17)
G.add_edge(17, 9)
G.add_edge(7, 6)
G.add_edge(15, 12)
G.add_edge(16, 15)
G.add_edge(14, 13)
G.add_edge(13, 12)
G.add_edge(11, 9)
G.add_edge(11, 4)
G.add_edge(4, 2)
G.add_edge(10, 9)
G.add_edge(6, 2)

# explicitly set positions
pos = {1: (5, 0.2), 2: (2.466, 0.2), 3: (3.937, 0.196), 4: (2.643, 0.202), 5: (3.3072, 0.200), 6: (2.407, 0.19916),
       7: (2.464, 0.19838), 9: (2.796, 0.20034), 10: (2.513, 0.20056), 11: (3.023, 0.20094), 12: (3.153, 0.20109),
       13: (3.153, 0.20219), 14: (2.894, 0.20122), 15: (3.347, 0.20083), 16: (3.466, 0.20019), 17: (2.866, 0.19877),
       19: (3.341, 0.19934), 20: (3.599, 0.19980), 21: (3.035, 0.19988), 22: (2.496, 0.19800), 23: (2.480, 0.19753),
       24: (3.607, 0.19972), 25: (3.551, 0.19887), 26: (3.349, 0.19856), 27: (3.357, 0.19836), 29: (3.446, 0.19789),
       30: (3.438, 0.19745), 31: (3.116, 0.19730), 32: (3.40, 0.19579), 33: (2.379, 0.19682), 34: (2.473, 0.19590),
       35: (2.829, 0.19671), 36: (3.29, 0.19382), 37: (2.217, 0.19650), 39: (2.062, 0.19593), 40: (1.916, 0.19501),
       41: (1.830, 0.19413), 42: (2.106, 0.19347), 43: (2.244, 0.19447), 44: (1.722, 0.19323), 45: (1.69, 0.19119),
       46: (3.02, 0.19290), 47: (3.01, 0.19437), 49: (2.92, 0.19185), 50: (2.76, 0.19121), 51: (1.70, 0.19217),
       52: (2.11, 0.19144), 53: (2.93, 0.19103), 54: (3.03, 0.19027), 55: (2.99, 0.18984), 56: (2.68, 0.19001),
       57: (2.01, 0.18996), 59: (1.79, 0.19017), 60: (1.37, 0.19166), 61: (1.68, 0.18996), 62: (1.45, 0.19022),
       63: (1.31, 0.19053), 64: (1.20, 0.19274), 65: (1.13, 0.19115), 66: (1.0, 0.19223), 67: (1.21, 0.19413),
       69: (0.96, 0.19346), 70: (1.35, 0.19583), 71: (1.04, 0.19511), 72: (1.26, 0.19727), 73: (1.34, 0.19753),
       74: (1.51, 0.19712), 75: (1.51, 0.19681), 76: (3.17, 0.19135), 77: (3.32, 0.18986), 79: (3.52, 0.18996),
       91: (3.59, 0.19058), 92: (3.43, 0.19104), 93: (3.49, 0.19084), 94: (3.08, 0.19207), 95: (3.350, 0.19243),
       96: (3.64, 0.19784), 97: (3.91, 0.19897), 99: (4.07, 0.19939), 100: (3.59, 0.19640), 101: (3.95, 0.19825),
       102: (4.11, 0.19881), 103: (4.18, 0.19933), 104: (3.19, 0.20000), 105: (3.08, 0.20015), 106: (3.11, 0.19974)}

options = {
    "font_size": 0,
    "node_size": 0,
    "node_color": "white",
    "edgecolors": "black",
    "linewidths": 1,
    "width": 3,
}
nx.draw_networkx(G, pos, **options)

# Set margins for the axes so that nodes aren't clipped
ax = plt.gca()
ax.margins(0.20)
plt.axis("off")
plt.show()
