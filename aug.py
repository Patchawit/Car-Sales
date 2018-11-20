import matplotlib.pyplot as plt

def demo():
    x = range(10)
    y = (27086, 13135, 11307, 7020, 5927, 5732, 5920, 1928, 2407, 1793)
    xtick = ("Toyota", "Isuzu", "Honda", "Mitsubishi", "Ford", "Nissan", "Mazda", "MG", "Suzuki", "Chevrolet")
    plt.bar(x, y, color="green")
    plt.xticks(x, xtick)
    plt.title("Car-Sales\nAug 2018", fontsize=17)
    plt.ylabel("Sales")
    plt.xlabel("Brand")
    plt.show()
demo()