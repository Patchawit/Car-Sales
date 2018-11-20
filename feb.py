import matplotlib.pyplot as plt

def demo():
    x = range(10)
    y = (20327, 13272, 9129, 6810, 5495, 5301, 5401, 1874, 2416, 1516)
    xtick = ("Toyota", "Isuzu", "Honda", "Mitsubishi", "Ford", "Nissan", "Mazda", "MG", "Suzuki", "Chevrolet")
    plt.bar(x, y, color="green")
    plt.xticks(x, xtick)
    plt.title("Car-Sales\nFeb 2018", fontsize=17)
    plt.ylabel("Sales")
    plt.xlabel("Brand")
    plt.show()
demo()