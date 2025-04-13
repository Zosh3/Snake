from game_constants import KEY_COLOUR_MAP, KEY_BLUE, KEY_ORANGE

print(f"KEY_COLOUR_MAP: {KEY_COLOUR_MAP}")

print(f"Use [] notation to access dictionary values BLUE: {KEY_COLOUR_MAP[KEY_BLUE]}" )
print(f"Use [] notation to access dictionary values ORANGE: {KEY_COLOUR_MAP[KEY_ORANGE]}" )
print(f"Use get() method to access dictionary values BLUE: {KEY_COLOUR_MAP.get(KEY_BLUE)}")
print(f"Use get() method to access dictionary values ORANGE: {KEY_COLOUR_MAP.get(KEY_ORANGE)}")


print(f"Use get() method to access dictionary values UNKNOWN: {KEY_COLOUR_MAP.get(100, "'Unknown')}")}")

print(f"Is KEY_BLUE a key in teh dictionary: {KEY_BLUE in KEY_COLOUR_MAP}")
print(f"Is 333 a key in teh dictionary: {333 in KEY_COLOUR_MAP}")
