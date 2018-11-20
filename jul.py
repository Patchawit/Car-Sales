import matplotlib.pyplot as plt

def demo():
    x = range(10)
    y = (26177, 13140, 10488, 6008, 4974, 5646, 6362, 1823, 2151, 1210)
    xtick = ("Toyota", "Isuzu", "Honda", "Mitsubishi", "Ford", "Nissan", "Mazda", "MG", "Suzuki", "Chevrolet")
    plt.bar(x, y, color="green")
    plt.xticks(x, xtick)
    plt.title("Car-Sales\nJul 2018", fontsize=17)
    plt.ylabel("Sales")
    plt.xlabel("Brand")
    plt.show()
demo()