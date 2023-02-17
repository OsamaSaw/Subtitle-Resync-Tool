# Subtitle Delay Adjustment with Python
This Subtitle Resync Tool is a Python script that can adjust the delay of SRT subtitle files in a specified directory. This script can adjust the delay of all SRT files in the specified directory or a single SRT file.
### Prerequisites

-   Python 3.6 or higher must be installed on your system.

### Usage

#### Adjust delay for all SRT files in a directory

1.  Open a command prompt or terminal.
    
2.  Navigate to the directory containing the `subtitle_delay_adjuster.py` file.
    
3.  Run the following command:
```Python
import subtitle_delay_adjustment

# adjust subtitles in the directory 'C:\Users\JohnDoe\Videos\Subtitles' by a 500 millisecond delay
subtitle_delay_adjustment.adjust_subtitles_delay('C:\Users\JohnDoe\Videos\Subtitles', 500)
```

To adjust the delay of subtitles in a single SRT file, call the adjust_subtitle_file_delay function with two arguments: the path to the SRT file, and the number of milliseconds to adjust the subtitles by. For example:

```Python
import subtitle_delay_adjustment

# adjust the subtitle delay in the file 'my_subtitle_file.srt' by a 500 millisecond delay
subtitle_delay_adjustment.adjust_subtitle_file_delay('C:\Users\JohnDoe\Videos\Subtitles\movie.srt', 500)
```

### Limitations

-   This script only works with SRT files.
-   The script only adjusts the delay by a single amount for all subtitles. It does not adjust the delay for individual subtitles in the file.
