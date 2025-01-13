import click

from .analyse import total_time_played
from .parser import load

from datetime import date, datetime

from .visualise import vis_time_played, vis_top_artists, vis_top_tracks


@click.command()
@click.option("--dir", default="data/streaming_history", help="Streaming history relative directory. Should contain json files with streaming history from spotify")
@click.option("--date-start", default="1970-01-01", help="Date to start filtering on, inclusive. Format: YYYY-MM-DD", type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option("--date-end", default=str(date.today()), help="Date to stop filtering on, inclusive. Format: YYYY-MM-DD", type=click.DateTime(formats=["%Y-%m-%d"]))
@click.option("--time-played/--no-time-played", default=True)
@click.option("--artists", default=False, is_flag=True)
@click.option("--tracks", default=False, is_flag=True)
@click.option("--num-tracks", default=10, type=int)
@click.option("--num-artists", default=10, type=int)
@click.option('-v', '--verbose', count=True)
def main(dir: str, date_start: datetime, date_end: datetime, time_played: bool, artists: bool, tracks: bool, num_tracks: int, num_artists: int, verbose: int) -> None:
    date_start = date_start.date()
    date_end = date_end.date()  
    data = load(dir, date_start, date_end)

    total_ms, total_ms_by_track, total_ms_by_artist = total_time_played(data)
    if time_played:
        vis_time_played(total_ms, total_ms_by_track, total_ms_by_artist)
    if artists:
        vis_top_artists(total_ms_by_artist, num_artists, verbose)
    if tracks:
        vis_top_tracks(total_ms_by_track, num_tracks, verbose)

if __name__ == "__main__":  
    main()  
