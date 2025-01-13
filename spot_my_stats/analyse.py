

from collections import defaultdict

def _is_podcast(d: dict) -> bool:
    return d["spotify_episode_uri"] is not None

def _is_song(d: dict) -> bool:
    return d["spotify_track_uri"] is not None

# also do podcasts

def total_time_played(data: list[dict]) -> tuple[int, defaultdict[str, int], defaultdict[str, int]]:
    total_ms: int = 0
    total_ms_by_track: dict[str, int] = defaultdict(int)
    total_ms_by_artist: dict[str, int] = defaultdict(int)
    for d in data:
        if _is_song(d):
            total_ms += d["ms_played"]
            total_ms_by_track[d["master_metadata_track_name"]] += d["ms_played"]
            if not d["master_metadata_album_artist_name"]:
                print(d)
            total_ms_by_artist[d["master_metadata_album_artist_name"]] += d["ms_played"]
    
    return total_ms, total_ms_by_track, total_ms_by_artist
