import os
import sys
import cv2

class FrameExtractor:
    def __init__(self, video_path, output_dir):
        self.video_path = video_path
        self.output_dir = output_dir

    def extract_frames(self):
        video_name = os.path.splitext(os.path.basename(self.video_path))[0]
        output_path = os.path.join(self.output_dir, video_name)

        # Create output directory if it doesn't exist
        if not os.path.exists(output_path):
            os.makedirs(output_path)

        # Read the video
        video = cv2.VideoCapture(self.video_path)
        success, frame = video.read()
        count = 0

        while success:
            # Save the frame as an image file
            frame_path = os.path.join(output_path, f"{video_name}_frame{count}.jpg")
            cv2.imwrite(frame_path, frame)

            # Read the next frame
            success, frame = video.read()
            count += 1

        # Release the video capture
        video.release()

if __name__ == "__main__":
    # Check if video_path and output_dir are provided as command line arguments
    if len(sys.argv) < 3:
        print("Usage: python frame_extractor.py video_path output_dir")
        sys.exit(1)

    video_path = sys.argv[1]
    output_dir = sys.argv[2]

    frame_extractor = FrameExtractor(video_path, output_dir)
    frame_extractor.extract_frames()
