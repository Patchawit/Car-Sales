import matplotlib.pyplot as plt

def demo():
    x = range(10)
    y = (27746, 12947, 10549, 7172, 5001, 6371, 6707, 2087, 2845, 1590)
    xtick = ("Toyota", "Isuzu", "Honda", "Mitsubishi", "Ford", "Nissan", "Mazda", "MG", "Suzuki", "Chevrolet")
    plt.bar(x, y, color="green")
    plt.xticks(x, xtick)
    plt.title("Car-Sales\nJun 2018", fontsize=17)
    plt.ylabel("Sales")
    plt.xlabel("Brand")
    plt.show()
demo()