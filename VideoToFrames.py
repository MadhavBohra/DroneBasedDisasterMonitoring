import cv2
import os

def extract_frames(input_video_path, output_directory):
    # Create the output directory if it doesn't exist
    os.makedirs(output_directory, exist_ok=True)

    # Open the video file
    cap = cv2.VideoCapture(input_video_path)

    # Get the total number of frames in the video
    total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))

    # Define the target frame count (e.g., 200 equally spaced frames)
    target_frame_count = 600
    frame_indices = [int(i * total_frames / target_frame_count) for i in range(target_frame_count)]

    # Initialize a frame counter
    frame_count = 0

    while True:
        # Read a frame from the video
        ret, frame = cap.read()

        # If the frame could not be read or we've reached the end of the video, break the loop
        if not ret:
            break

        # Check if the current frame index is in the list of target indices
        if frame_count in frame_indices:
            # Resize the frame to 128x128
            resized_frame = cv2.resize(frame, (256, 256))

            # Save the resized frame as an image
            output_path = os.path.join(output_directory, f'w05_{frame_count:04d}.jpg')
            cv2.imwrite(output_path, resized_frame)

        # Increment the frame counter
        frame_count += 1

        # Break the loop if we have extracted all the desired frames
        if frame_count >= total_frames or len(frame_indices) == 0:
            break

    # Release the video capture object and close any open windows
    cap.release()
    cv2.destroyAllWindows()

# Usage example:
input_video_path = 'Input/Sequence 04.mp4'
output_directory = 'data/images'
extract_frames(input_video_path, output_directory)
