heroes = {
    'Spider-Man': 80,
    'Batman': 65,
    'Superman': 85,
    'Wunder Woman': 70,
    'Iron Man': 65,
    'Thor': 90,
    'Aquaman': 65,
    'Capitan America': 65,
    'Hulk': 87
}
for i in sorted(heroes.items(), key=lambda para: (para[1], para[0])):
    # for i in sorted(heroes.items(), key=lambda para: para[1]:
    # for i in sorted(heroes.items():
    # for i in sorted(heroes.values():

    # print(i,heroes[i])
    print(i)
