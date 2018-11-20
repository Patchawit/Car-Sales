import matplotlib.pyplot as plt

def demo():
    x = range(10)
    y = (26630, 14334, 10420, 6882, 5260, 5438, 5881, 2267, 2522, 1101)
    xtick = ("Toyota", "Isuzu", "Honda", "Mitsubishi", "Ford", "Nissan", "Mazda", "MG", "Suzuki", "Chevrolet")
    plt.bar(x, y, color="green")
    plt.xticks(x, xtick)
    plt.title("Car-Sales\nMay 2018", fontsize=17)
    plt.ylabel("Sales")
    plt.xlabel("Brand")
    plt.show()
demo()