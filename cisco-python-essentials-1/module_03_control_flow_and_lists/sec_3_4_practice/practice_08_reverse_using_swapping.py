# Statement
# A museum displays five historical artifacts in chronological order.
# ["Sword","Shield","Helmet","Bow","Armor"]
# Reverse the list without using any built-in reverse method.
# Only use swapping.

artifacts = ["Sword","Shield","Helmet","Bow","Armor"]
print("Original :", artifacts)

artifacts[0], artifacts[4] = artifacts[4], artifacts[0]
artifacts[1], artifacts[3] = artifacts[3], artifacts[1]

print("Reversed :", artifacts)