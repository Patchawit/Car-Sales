import matplotlib.pyplot as plt

def demo():
    x = range(10)
    y = (17094, 12233, 9109, 5878, 4968, 4794, 4539, 1471, 1407, 1357)
    xtick = ("Toyota", "Isuzu", "Honda", "Mitsubishi", "Ford", "Nissan", "Mazda", "MG", "Suzuki", "Chevrolet")
    plt.bar(x, y, color="green")
    plt.xticks(x, xtick)
    plt.title("Car-Sales\nJan 2018", fontsize=17)
    plt.ylabel("Sales")
    plt.xlabel("Brand")
    plt.show()
demo()
