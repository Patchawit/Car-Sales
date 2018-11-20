import matplotlib.pyplot as plt

def demo():
    x = range(10)
    y = (23223, 14764, 10434, 6351, 5181, 4672, 4419, 1956, 2240, 1550)
    xtick = ("Toyota", "Isuzu", "Honda", "Mitsubishi", "Ford", "Nissan", "Mazda", "MG", "Suzuki", "Chevrolet")
    plt.bar(x, y, color="green")
    plt.xticks(x, xtick)
    plt.title("Car-Sales\nApr 2018", fontsize=17)
    plt.ylabel("Sales")
    plt.xlabel("Brand")
    plt.show()
demo()