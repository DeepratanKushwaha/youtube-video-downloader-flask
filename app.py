from flask import Flask, render_template, request
from pytube import YouTube

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def download():
    error = None
    video_url = request.form.get("url")

    if request.method == "POST":
        try:
            yt = YouTube(video_url)
            print(video_url)
        except Exception as e:
            print(video_url)
            # error = "Error: Could not access the URL. Please check and try again."
            return render_template('home.html', error=e)

        print("\nAvailable video streams:")
        for stream in yt.streams:
            print(stream)

        # Allow user to select a stream (optional)
        # preferred_stream = yt.streams.filter(progressive=True).first()  # Example: filter for progressive streams
        preferred_stream = yt.streams.first()  # Download the first stream by default

        try:
            print(f"\nDownloading: {yt.title}")
            downloaded_file = preferred_stream.download()
            print(downloaded_file)
            print(f"Download complete! Saved as: {downloaded_file.default_filename}")
        except Exception as e:
            error = f"Error downloading video: {e}"
            return render_template("home.html", error=error)

    return render_template("home.html")  # Render home.html on both GET and POST requests

if __name__ == "__main__":
    app.run(debug=True)  # Change to app.run() for production
