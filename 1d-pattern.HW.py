# DRAW this PATTERN:
# * * # * * # * * ...

# print("\n")
#
# for x in range(1,21):
#     if x % 3 == 0:
#         print( "# ", end="")
#     else:
#         print( "* ", end="")
#
# print("\n")

# DRAW this PATTERN:
# * * * # # * * * # # ...

print("\n")

for x in range(1,21):
    if x % 5 == 0 or x % 5 == 4:
        print( "# ", end="")
    else:
        print( "* ", end="")

print("\n")