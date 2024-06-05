# Time Complexity : O(G+S+U(S+G))
# Space Complexity : O(G+S)
# Did this code successfully run on Leetcode : Yes
# Any problem you faced while coding this : No
def favorite_genre(user_map, genre_map):
    res = {}
    song_to_genre = {}

    # Create a mapping of songs to genres
    for genre, songs in genre_map.items():
        for song in songs:
            song_to_genre[song] = genre

    user_genre_count = {}
    for user, songs in user_map.items():
        if user not in user_genre_count:
            user_genre_count[user] = {}
        for song in songs:
            genre = song_to_genre.get(song)
            if genre:
                count = user_genre_count[user].get(genre, 0) + 1
                user_genre_count[user][genre] = count

    for user, pair in user_genre_count.items():
        if user not in res:
            res[user] = []
        max_count = 0
        fav_genre = []
        for genre, count in pair.items():
            if not fav_genre:
                fav_genre.append(genre)
                max_count = count
            elif count > max_count:
                fav_genre.clear()
                fav_genre.append(genre)
                max_count = count
            elif count == max_count:
                fav_genre.append(genre)
        res[user] = fav_genre

    return res

if __name__ == "__main__":
    user_songs = {
        "David": ["song1", "song2", "song3", "song4", "song8"],
        "Emma": ["song5", "song6", "song7"]
    }

    song_genres = {
        "Rock": ["song1", "song3"],
        "Dubstep": ["song7"],
        "Techno": ["song2", "song4"],
        "Pop": ["song5", "song6"],
        "Jazz": ["song8", "song9"]
    }

    res = favorite_genre(user_songs, song_genres)
    print(res)