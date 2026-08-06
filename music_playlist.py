class Song:
    def __init__(self, title, artist, duration):
        self.title = title
        self.artist = artist
        self.duration = duration

class PlayList:
    def __init__(self):
        self.songs = []
        
        self.available_songs = [
            Song("Blinding Lights", "The Weeknd", 50),
            Song("Shape of You", "Ed Sheeran", 40),
            Song("Believer", "Imagine Dragons", 60),
            Song("Counting Stars", "OneRepublic", 54),
            Song("Perfect", "Ed Sheeran", 43),
            Song("Someone Like You", "Adele", 180),
            Song("Memories", "Maroon 5", 190),
            Song("Radioactive", "Imagine Dragons", 185),
            Song("Viva La Vida", "Coldplay", 240),
            Song("Bad Habits", "Ed Sheeran", 230)
        ]
        
    def show_songs(self):
        print("\nWelcome to the Music! We have these songs:")
        for idx, song in enumerate(self.available_songs, 1):
            print(f"{idx}. {song.title} - Duration: {song.duration} sec")
            
    def add_song(self):
        while True:
            self.show_songs()
            choice = input("\nPlease enter the song number or name that you want to add (or type 'back' to exit): ").strip()
            
            if choice.lower() == 'back':
                break
                
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(self.available_songs):
                    selected_song = self.available_songs[index]
                    self.songs.append(selected_song)
                    print(f"✅ Added '{selected_song.title}' to your playlist successfully!")
                    break
                else:
                    print("❌ Invalid song number, please try again.")
            else:
                found = False
                for song in self.available_songs:
                    if song.title.lower() == choice.lower():
                        self.songs.append(song)
                        print(f"✅ Added '{song.title}' to your playlist successfully!")
                        found = True
                        break
                if found:
                    break
                else:
                    print("❌ Song not found, please enter a valid song name or number.")
                
    def remove_song(self):
        if not self.songs:
            print("\n❌ Your playlist is already empty!")
            return
            
        while True:
            print("\nYour current playlist:")
            for idx, song in enumerate(self.songs, 1):
                print(f"{idx}. {song.title}")
                
            choice = input("Please enter the song name or number that you want to remove: ").strip()
            
            if choice.isdigit():
                index = int(choice) - 1
                if 0 <= index < len(self.songs):
                    removed = self.songs.pop(index)
                    print(f"❌ Removed '{removed.title}' from your playlist.")
                    break
                else:
                    print("❌ Invalid number.")
            else:
                removed = None
                for song in self.songs:
                    if song.title.lower() == choice.lower():
                        removed = song
                        self.songs.remove(song)
                        break
                if removed:
                    print(f"❌ Removed '{removed.title}' from your playlist.")
                    break
                else:
                    print("❌ Song not found in your playlist.")
    
    def total_duration(self):
        if not self.songs:
            print("\n⏱️ Total duration: 0 (You haven't listened to or added any songs yet).")
            return 0
            
        total_time = 0
        for song in self.songs:
            total_time += song.duration
            
        print(f"\n⏱️ Total duration of your playlist is: {total_time} seconds.")
        return total_time


def main():
    my_playlist = PlayList()
    
    while True:
        print("\n--- Music Player Menu ---")
        print("1. Show Available Songs")
        print("2. Add Song to Playlist")
        print("3. Remove Song from Playlist")
        print("4. Calculate Total Duration")
        print("5. Exit")
        
        choice = input("Choose an option (1-5): ").strip()
        
        if choice == "1":
            my_playlist.show_songs()
        elif choice == "2":
            my_playlist.add_song()
        elif choice == "3":
            my_playlist.remove_song()
        elif choice == "4":
            my_playlist.total_duration()
        elif choice == "5":
            print("Thank you for using Music App! Goodbye 👋")
            break
        else:
            print("❌ Invalid choice, please try again.")

if __name__ == "__main__":
    main()
