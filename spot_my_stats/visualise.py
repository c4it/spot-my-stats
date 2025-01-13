from datetime import timedelta

MS_PER_SEC = 1000
MS_PER_MIN = 60000
MS_PER_HOUR = 3600000
MS_PER_DAY = 86400000
MS_PER_WORKDAY = 28800000


def _ms_to_mins(ms: int):
    td = timedelta(milliseconds=ms)
    return td.seconds // 60

# per year
# per artist
# per song

def vis_time_played(total_ms: int, total_ms_by_track: dict[str, int], total_ms_by_artist: dict[str, int]) -> None:
    verbose = 1
    top_artist = max(total_ms_by_artist, key=total_ms_by_artist.get)
    top_song = max(total_ms_by_track, key=total_ms_by_track.get)
    
    print(f"Your total time listening time is {_vis_in_days(total_ms, verbose)}\n")
    print(f"Your top artis is {top_artist}\nYou spent {_vis_in_days(total_ms_by_artist[top_artist], verbose)} listening to them\n")
    print(f"Your top song is {top_song}\nYou spent {_vis_in_days(total_ms_by_track[top_song],verbose)} listening to it!\n")

    print("Want that in work days?")
    print(f"Your total time listening time is {_vis_in_work_days(total_ms)}\n")
    print(f"Your top artis is {top_artist}\nYou spent {_vis_in_work_days(total_ms_by_artist[top_artist])} listening to them\n")
    print(f"Your top song is {top_song}\nYou spent {_vis_in_work_days(total_ms_by_track[top_song])} listening to it!\n")


def vis_top_artists(total_ms_by_artist: dict[str, int], total: int | None, verbose: int) -> None:
    total_ms_by_artist_list = sorted(list(total_ms_by_artist.items()), key=lambda v: v[1], reverse=True)
    # total_ms_by_artist.sort(key=total_ms_by_artist.get)

    print(f"Your top {total} artists:")
    for ind in range(total):
        print(f"{ind + 1}. {total_ms_by_artist_list[ind][0]} - {_vis_in_days(total_ms_by_artist_list[ind][1], verbose)}")
    print(f"\nTotal artists listened to: {len(total_ms_by_artist_list)}\n")


def vis_top_tracks(total_ms_by_track: dict[str, int], total: int | None, verbose: int) -> None:
    total_ms_by_track_list = sorted(list(total_ms_by_track.items()), key=lambda v: v[1], reverse=True)

    print(f"Your top {total} tracks:")
    for ind in range(total):
        print(f"{ind + 1}. {total_ms_by_track_list[ind][0]} - {_vis_in_days(total_ms_by_track_list[ind][1], verbose)}")

    print(f"\nTotal tracks listened to: {len(total_ms_by_track_list)}\n")

def _vis_in_days(ms: int, verbose: int):
    time_played = f"{ms // MS_PER_MIN} minutes"
    if verbose > 0:
        additional = "\n"
        if ms // MS_PER_DAY > 0:
            additional += f"{ms // MS_PER_DAY} days, "
            ms = ms % MS_PER_DAY
        if ms // MS_PER_HOUR > 0:
            additional += f"{ms // MS_PER_HOUR} hours, "
            ms = ms % MS_PER_HOUR
        if ms // MS_PER_MIN > 0:
            additional += f"{ms // MS_PER_MIN} minutes, "
            ms = ms % MS_PER_MIN
        if ms // MS_PER_SEC > 0:
            additional += f"{ms // MS_PER_SEC} seconds"
        
        if additional:
            time_played += f"Or {additional.strip(', ')}"
        
    return time_played


def _vis_in_work_days(ms: int):
    # time_played = f"Want that in work days?\n{ms // MS_PER_MIN} minutes\n"
    time_played = ""
    # ms_per_hour = ms / MS_PER_HOUR
    if ms // MS_PER_WORKDAY > 0:
        time_played += f"{ms // MS_PER_WORKDAY} days, "
        ms = ms % MS_PER_WORKDAY
    if ms // MS_PER_HOUR > 0:
        time_played += f"{ms // MS_PER_HOUR} hours, "
        ms = ms % MS_PER_HOUR
    if ms // MS_PER_MIN > 0:
        time_played += f"{ms // MS_PER_MIN} minutes, "
        ms = ms % MS_PER_MIN
    if ms // MS_PER_SEC > 0:
        time_played += f"{ms // MS_PER_SEC} seconds"
    
    return time_played.strip(", ")
