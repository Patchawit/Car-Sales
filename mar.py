import matplotlib.pyplot as plt

def demo():
    x = range(10)
    y = (26673, 18811, 10197, 8008, 6772, 6870, 6646, 2373, 2402, 2018)
    xtick = ("Toyota", "Isuzu", "Honda", "Mitsubishi", "Ford", "Nissan", "Mazda", "MG", "Suzuki", "Chevrolet")
    plt.bar(x, y, color="green")
    plt.xticks(x, xtick)
    plt.title("Car-Sales\nMar 2018", fontsize=17)
    plt.ylabel("Sales")
    plt.xlabel("Brand")
    plt.show()
demo()