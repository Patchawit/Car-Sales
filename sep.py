import matplotlib.pyplot as plt

def demo():
    x = range(10)
    y = (28760, 13030, 11282, 7128, 6029, 6266, 5880, 1812, 2271, 1470)
    xtick = ("Toyota", "Isuzu", "Honda", "Mitsubishi", "Ford", "Nissan", "Mazda", "MG", "Suzuki", "Chevrolet")
    plt.bar(x, y, color="green")
    plt.xticks(x, xtick)
    plt.title("Car-Sales\nSep 2018", fontsize=17)
    plt.ylabel("Sales")
    plt.xlabel("Brand")
    plt.show()
demo()