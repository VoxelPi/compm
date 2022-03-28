import os

# print(f"TEST: {os.getcwd()}") # Print current working directory.
# os.remove("./ovid.txt") # Delete file.

with open("./ovid.txt", "w") as file:
    file.write("In nova fert animus mutatas dicere formas corpora; Di, coeptis nam vos mutastis et illas\nadspirate meis primaque ab origine mundi ad mea perpetuum deducite tempora carmen!")

print("\nWithout spaces:")
with open("./ovid.txt", "r") as file:
    for line in file.readlines():
        print(line.replace(" ", ""), end="")
    print("")

print("\nReplaced:")
with open("./ovid.txt", "r") as file:
    for line in file.readlines():
        print(line.replace("di", "good").replace("Di", "Good"), end="")
    print("")
