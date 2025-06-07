import whisper
import argparse
import sys
import logging
import time
import threading
import os

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

def log_progress(start_time, stop_event):
    """Log progress every 30 seconds"""
    elapsed_time = time.time() - start_time
    logging.info(f"Processing... Elapsed time: {elapsed_time:.2f} seconds")

    if not stop_event.is_set():
        # Schedule the next call in 30 seconds
        timer = threading.Timer(30.0, log_progress, [start_time, stop_event])
        timer.daemon = True
        timer.start()

def main():
    # Parse command-line arguments
    logging.info("Parsing command-line arguments...")
    parser = argparse.ArgumentParser(description="Transcribe audio file using Whisper")
    parser.add_argument("language", help="Language of the audio (e.g., English, German, Spanish)")
    parser.add_argument("file_path", help="Path to the audio file")
    args = parser.parse_args()

    # Validate file exists
    if not os.path.exists(args.file_path):
        print(f"Error: File '{args.file_path}' does not exist.")
        sys.exit(1)

    # Validate file has .mp3 extension
    if not args.file_path.lower().endswith('.mp3'):
        print(f"Error: File '{args.file_path}' is not an MP3 file.")
        sys.exit(1)

    # Load model and transcribe
    logging.info("Loading model...")
    model = whisper.load_model("turbo")

    # Create an event to signal when to stop the timer
    stop_event = threading.Event()

    # Record the start time
    start_time = time.time()

    # Log transcription start
    logging.info(f"Starting transcription of file: {args.file_path} with language: {args.language}")

    # Start the progress logging timer
    log_progress(start_time, stop_event)

    # Perform the transcription
    result = model.transcribe(args.file_path, **{
        "language": args.language,
        "fp16": False})

    # Stop the timer
    stop_event.set()

    # Calculate total time
    total_time = time.time() - start_time

    # Log transcription completion with total time
    logging.info(f"Transcription completed for file: {args.file_path}. Total time: {total_time:.2f} seconds")

    # Write transcription to results.txt file
    with open("results.txt", "w", encoding="utf-8") as f:
        f.write(result["text"])

    # Log file writing completion
    logging.info("Transcription results written to results.txt")

if __name__ == "__main__":
    main()
