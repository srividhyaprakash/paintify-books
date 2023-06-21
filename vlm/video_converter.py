import os
import subprocess
import sys

class VideoConverter:
    def __init__(self, frames_dir, output_dir=None, output_fps=30):
        self.frames_dir = frames_dir
        self.output_dir = output_dir
        self.output_fps = output_fps

    def convert_frames_to_video(self):
        # Determine the default output directory
        if not self.output_dir:
            self.output_dir = os.path.dirname(self.frames_dir)

        # Determine the output filename from the frames
        first_frame_name = os.listdir(self.frames_dir)[0]
        output_filename = first_frame_name.split("_")[0] + ".mp4"
        output_path = os.path.join(self.output_dir, output_filename)

        # FFmpeg command
        ffmpeg_cmd = [
            'ffmpeg',
            '-framerate', str(self.output_fps),
            '-i', os.path.join(self.frames_dir,  first_frame_name.split("_")[0] + '_frame%d.jpg'),
            '-c:v', 'libx264',
            '-pix_fmt', 'yuv420p',
            output_path
        ]

        # Execute FFmpeg command
        subprocess.run(ffmpeg_cmd)

        print("Video saved at {}.".format(output_path))

if __name__ == "__main__":
    # Check if frames_dir is provided as command line argument
    if len(sys.argv) < 2:
        print("Usage: python video_converter.py frames_dir [output_dir] [output_fps]")
        sys.exit(1)

    frames_dir = sys.argv[1]

    # Check if output_dir and output_fps are provided as command line arguments, otherwise set default values
    if len(sys.argv) >= 3:
        output_dir = sys.argv[2]
    else:
        output_dir = None

    if len(sys.argv) >= 4:
        output_fps = int(sys.argv[3])
    else:
        output_fps = 30

    video_converter = VideoConverter(frames_dir, output_dir, output_fps)
    video_converter.convert_frames_to_video()
