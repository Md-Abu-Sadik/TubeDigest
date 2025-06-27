from youtube_transcript_api import YouTubeTranscriptApi

def get_video_id(url):
    if "v=" in url:
        return url.split("v=")[1].split("&")[0]
    elif "youtu.be/" in url:
        return url.split("youtu.be/")[1].split("?")[0]
    else:
        return None

while True:
    url = input("\nEnter YouTube video URL (or type 'exit' to quit): ")

    if url.lower() == "exit":
        print("Goodbye!")
        break

    video_id = get_video_id(url)

    if video_id:
        try:
            transcript = YouTubeTranscriptApi.get_transcript(video_id)
            print("\n--- Transcript ---\n")
            for line in transcript:
                print(line['text'])
        except Exception as e:
            print("❌ Error fetching transcript:", e)
    else:
        print("❌ Invalid YouTube URL. Try again.")
