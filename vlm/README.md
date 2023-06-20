# Video Utils

## Prerequisites

- Python 3.x
- OpenCV library

## Installation

1. Clone the repository.s

2. Install the required dependencies using pip:

   ```bash
   pip install opencv-python
   ```

### Video Converter

The Video Converter is a Python script that takes a directory of image frames and converts them into a video file. It uses the OpenCV library to read the frames, create a video writer, and save the video in a specified output format.


```
python video_converter.py frames_dir [output_dir] [output_fps]
```

- frames_dir (required): Path to the directory containing the image frames.

- output_dir (optional): Path to the output directory where the video will be saved. If not provided, the default output directory will be the same as the frames directory.

- output_fps (optional): Frames per second (FPS) of the output video. The default value is 30 FPS.

#### Examples

```
python video_converter.py /path/to/frames /path/to/output 24
```


#### Frame Extractor
Video Frame Extractor is a Python script that extracts frames from a video file and saves them as individual image files.


Run the script with the following command:

```
python frame_extractor.py <video_path> <output_path>
```

Replace `<video_path>` with the path to your video file, and `<output_path>` with the desired location to save the frames. For example:


The frames will be extracted from the video and saved as individual JPEG images in the specified output folder.



