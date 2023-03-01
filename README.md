# Automatic YouTube Data Collection

make your life easy :) 
Python code to download the franes of a YouTube video without downloading video file 

### Build your own dataset for object recognition and object detection/segmentation

You can use this python code to download the frames of youtube video without downloading video. 

### Step 1. pip install -r requirements.txt
Then select the output directory where you want to save the frames (edit python code to set paths and directories)

### Step 2. update the .py file 
Add youtube video and output dir in python script

### step 3. python <script-name.py>

It will start capturing frames from youtube video and download it into the specified folders.

Alternatively you can use the cli.py file if you do not want to manually modify the main script.

Usage
---
```
>>> python cli.py --help
>>> usage: downlaod_youtube_frames. [-h] --videolink VIDEOLINK --destination DESTINATION

  Program to automatically download youtube images datasets.

  optional arguments:
    -h, --help            show this help message and exit
    --videolink VIDEOLINK
                         YouTube video link
    --destination DESTINATION
                         Target path to save imgz

  A simple and nice cli script to create youtube datasets
```

How to run on cli/terminal?

Example run

``` >>> python cli.py --videolink "https://www.youtube.com/watch?v=PWRg_wak9oI" --destination "D:\dataset\test" ```

Running like above example will start downloading the video frames into the provided destination.

NOTE: Make sure the --videolink and --destination are both strings (enclosed in quoutation marks)
