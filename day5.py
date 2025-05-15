# Create a CLI to-do list manager.

tasks = []

while True:
    print("Please select the task:")
    print("1. Add task")
    print("2. View tasks")
    print("3. Remove task")
    print("4. Exit")

    select = input("Enter your choice (1,2,3,4): ")

    if select == '1':
        add_task = input("Enter your task: ")
        completed = False
        for task in tasks:
            if task[0] == add_task:
                print("Task already exists...")
                break
        else:
            tasks.append((add_task, completed))
            print(f"Task {add_task} added successfully.")


    elif select == '2':
        if not tasks:
            print("No tasks available")
        else:
            print("Tasks:")
            for i in range(0,len(tasks)):
                task,completed = tasks[i]
                status = "Completed" if completed else "Not Completed"
                print(f"{i + 1}.{task} (Status: {status})")


    elif select == '3':
        task_num = int(input("Enter your task number to remove: "))
        if 1 <= task_num <= len(tasks):
            removed_task = tasks.pop(task_num - 1)
            print(f"Task '{removed_task[0]}' removed successfully")
        else:
            print("Invalid Task Number")

    elif select == '4':
        print("Exiting...")
        break

    else:
        print("Invalid input, try again...")





# Implement a simple playlist manager for songs.
playlist = []

while True:
    print("Please select the song:")
    print("1. Add song")
    print("2. View playlist")
    print("3. Remove song")
    print("4. Play next song")
    print("5. Search the song")
    print("6. Exit")

    select = input("Enter your choice (1,2,3,4): ")

    if select == "1":
        add_song = input("Enter your song: ")
        artist = input("Enter the artist: ")
        for song in playlist:
            if song[0] == add_song:
                print("Song already exists...")
                break
        else:
            playlist.append((add_song, artist))
            print(f"Song {add_song}, artist {artist} added successfully.")

    elif select == "2":
        if not playlist:
            print("No songs available")
        else:
            print("Songs:")
            for i in range(0,len(playlist)):
                add_song,artist = playlist[i]
                print(f"{i + 1}.{add_song} by {artist})")

    elif select == "3":
        song_num = int(input("Enter your song number to remove: "))
        if 1 <= song_num <= len(playlist):
            removed_song = playlist.pop(song_num - 1)
            print(f"Song '{removed_song[0]}' removed successfully")
        else:
            print("Invalid Song Number")

    elif select == "4":
        if playlist:
            next_song = playlist.pop(0)
            print(f"Now playing: {next_song[0]} by {next_song[1]}")
        else:
            print("Playlist is empty, add songs first!")
            
    elif select == "5":
        search_song = input("Enter a word to search in songs: ").lower()
        print("Search results:")
        for i in range(len(playlist)):
            song, artist = playlist[i]
            if search_song in song.lower() or search_song in artist.lower():
                print(f"{i + 1}. {song} by {artist}")

        else:
            print("No matching songs found.")

    elif select == "6":
        print("Exiting...")
        break

    else:
        print("Invalid input, try again...")