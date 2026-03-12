!pip install webvtt-py
import webvtt
import re

def clean_subtitles(vtt_file, output_txt):
    clean_lines = []

    for caption in webvtt.read(vtt_file):
        text = caption.text

        # Remove [Music], (Applause), etc.
        text = re.sub(r"\[.*?\]|\(.*?\)", "", text)

        # Remove extra spaces
        text = re.sub(r"\s+", " ", text).strip()

        if text:
            clean_lines.append(text)

    # Remove duplicate consecutive lines
    final_text = []
    for line in clean_lines:
        if not final_text or line != final_text[-1]:
            final_text.append(line)

    with open(output_txt, "w", encoding="utf-8") as f:
        f.write(" ".join(final_text))

    print("Clean subtitles saved!")

# Usage
clean_subtitles("C:\\Users\\sohai\\Desktop\\Videos_project\\Convolutional Neural Network (CNN) - Dr N Nandhini [6JjvAkze2U4].en.vtt", "clean_subtitles.txt")