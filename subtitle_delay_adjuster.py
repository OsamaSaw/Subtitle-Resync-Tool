import os
import re


def adjust_subtitles_delay(directory_path, delay_ms):
    """
    Adjusts the delay of SRT subtitle files in the given directory
    by the specified number of milliseconds.

    Arguments:
    directory_path -- The path to the directory containing the SRT files.
    delay_ms -- The number of milliseconds to adjust the subtitles by.
    """

    # Get a list of all the SRT files in the directory
    srt_files = [file for file in os.listdir(directory_path) if file.endswith('.srt')]

    # Loop through each SRT file in the directory
    for srt_file in srt_files:
        adjust_single_srt_file(os.path.join(directory_path, srt_file), delay_ms)


def adjust_single_srt_file(srt_file_path, delay_ms):
    """
    Adjusts the delay of a single SRT file by the specified number of milliseconds.

    Arguments:
    srt_file_path -- The path to the SRT file to adjust.
    delay_ms -- The number of milliseconds to adjust the subtitles by.
    """

    # Open the SRT file and read its contents
    with open(srt_file_path, 'r', encoding='utf-8') as f:
        contents = f.read()

    # Adjust the delay of the subtitles by the specified number of milliseconds
    new_contents = re.sub(r'(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)',
                          lambda match: adjust_timestamp(match, delay_ms),
                          contents)

    # Write the new contents back to the SRT file
    with open(srt_file_path, 'w', encoding='utf-8') as f:
        f.write(new_contents)


def adjust_timestamp(match, delay_ms):
    """
    Adjusts a single timestamp in an SRT file by the specified
    number of milliseconds.

    Arguments:
    match -- The match object containing the timestamp to adjust.
    delay_ms -- The number of milliseconds to adjust the timestamp by.
    """

    # Parse the start and end timestamps from the match object
    start_time, end_time = match.group(1, 2)

    # Convert the timestamps to milliseconds and add the delay
    start_ms = timestamp_to_ms(start_time) + delay_ms
    end_ms = timestamp_to_ms(end_time) + delay_ms

    # Convert the adjusted timestamps back to the SRT format
    new_start_time = ms_to_timestamp(start_ms)
    new_end_time = ms_to_timestamp(end_ms)

    # Return the adjusted timestamp in SRT format
    return f'{new_start_time} --> {new_end_time}'


def timestamp_to_ms(timestamp):
    """
    Converts a timestamp in SRT format (HH:MM:SS,mmm) to milliseconds.

    Arguments:
    timestamp -- The timestamp to convert.
    """

    parts = re.split(r'[:,]', timestamp)
    hours, minutes, seconds, milliseconds = map(int, parts)
    total_seconds = (hours * 60 * 60) + (minutes * 60) + seconds
    total_ms = (total_seconds * 1000) + milliseconds
    return total_ms


def ms_to_timestamp(milliseconds):
    """
    Converts a duration in milliseconds to SRT format (HH:MM:SS,mmm).

    Arguments:
    milliseconds -- The duration in milliseconds to convert.
    """

    total_seconds = milliseconds // 1000
    milliseconds = milliseconds % 1000
    seconds = total_seconds % 60
    total_minutes = total_seconds // 60
    minutes = total_minutes % 60
    hours = total_minutes // 60

    return f'{hours:02d}:{minutes:02d}:{seconds:02d},{milliseconds:03d}'


choice = input("choose mode\n1-single file\n2-multiple files\n choice: ")
if int(choice) == 2:
    path = input("Path to srt files: ")
    delay_ms = int(input("Enter delay in milliseconds: "))
    adjust_subtitles_delay(path, delay_ms)
else:
    path = input("Path to srt file: ")
    delay_ms = int(input("Enter delay in milliseconds: "))
    adjust_single_srt_file(path, delay_ms)
