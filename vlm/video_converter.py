import os
import sys
import cv2

class VideoConverter:
    def __init__(self, frames_dir, output_dir=None, output_fps=30):
        self.frames_dir = frames_dir
        self.output_dir = output_dir
        self.output_fps = output_fps

    def convert_to_video(self):
        # Get the list of frames in the directory
        frame_files = sorted(os.listdir(self.frames_dir))

        if not frame_files:
            print("No frames found in the directory.")
            return

        # Read the first frame to get the frame size
        first_frame_path = os.path.join(self.frames_dir, frame_files[0])
        first_frame = cv2.imread(first_frame_path)
        height, width, channels = first_frame.shape

        # Determine the default output directory
        if not self.output_dir:
            self.output_dir = os.path.dirname(self.frames_dir)

        # Determine the output filename from the frames
        first_frame_name = frame_files[0]
        output_filename = first_frame_name.split("_")[0] + ".mp4"
        output_path = os.path.join(self.output_dir, output_filename)

        # Define the video codec and create a VideoWriter object
        fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Use appropriate codec for the desired output video format
        video_writer = cv2.VideoWriter(output_path, fourcc, self.output_fps, (width, height))

        # Iterate through each frame and write it to the video
        for frame_file in frame_files:
            frame_path = os.path.join(self.frames_dir, frame_file)
            frame = cv2.imread(frame_path)
            video_writer.write(frame)

        # Release the VideoWriter
        video_writer.release()

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
    video_converter.convert_to_video()
