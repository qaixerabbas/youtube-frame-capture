# Automatic YouTube Visual Data Collection

Make your life easy :) 

Note: FFMPEG is required for OpenCV to work with local downloaded videos (especially .AVI files) make sure you download and use latest FFMPEG from [this](https://www.ffmpeg.org/download.html) link.

## Build your own dataset for object recognition and object detection/segmentation

You can use this python code to download the frames of youtube video without downloading video. 

### Step 1. pip install -r requirements.txt
Then select the output directory where you want to save the frames (edit python code to set paths and directories)

### Step 2. update the .py file 
Add youtube video and output dir in python script

### step 3. python <script-name.py>

It will start capturing frames from youtube video and download it into the specified folders.



Usage
---
Alternatively you can use the cli.py file if you do not want to manually modify the main script.
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

Running like above example will start downloading the video frames into the provided destination. Optionally, you can provide ``` --showframe ``` argument in command line if you want to show the frames that are being saved to local disk.

Example

``` >>> python cli.py --videolink "https://www.youtube.com/watch?v=PWRg_wak9oI" --destination "D:\dataset\test" --showframe ```

NOTE: Make sure ``` --videolink ``` and ``` --destination ``` are both strings (enclosed in quotation marks)

### Todo

- [ ] Add framecount in argparse 
- [ ] work with any online videos ( YouTube + more )

### In Progress

- [ ] Working on improving readme, How-To and upload on PyPI. 

### Done ✓

- [x] Capturing frames from remote YouTube videos.
- [x] merge this to deepds
- [x] Saving frames to target directory.
- [x] Cli.py file for easy usage.
