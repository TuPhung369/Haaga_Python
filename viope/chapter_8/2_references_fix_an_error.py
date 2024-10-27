playlist_1 = ["Levitating", "Hold me closer", "As it was"]
playlist_2 = playlist_1[:]  # Create a copy of playlist_1
playlist_2.append("Bad Habit")
playlist_2.append("Shivers")

print("Playlist 1: ", end="")
print(*playlist_1, sep=", ")
print("Playlist 2: ", end="")
print(*playlist_2, sep=", ")
