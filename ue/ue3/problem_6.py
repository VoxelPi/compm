import os

# print(f"TEST: {os.getcwd()}")

with open("./ovid.txt", "x") as file:
    file.write("In nova fert animus mutatas dicere formas corpora; Di, coeptis nam vos mutastis et illas\nadspirate meis primaque ab origine mundi ad mea perpetuum deducite tempora carmen!")

with open("./ovid.txt", "r") as file:
    for line in file.readlines():
        print(line.replace(" ", ""))

with open("./ovid.txt", "r") as file:
    for line in file.readlines():
        print(line.replace("di", "good").replace("Di", "Good"))
