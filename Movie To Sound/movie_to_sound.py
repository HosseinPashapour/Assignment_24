import threading
import time
from moviepy import editor


def convert_movie_to_sound(video_name, output_path):
    video = editor.VideoFileClip(video_name)
    video.audio.write_audiofile(output_path)


movie_list = [
    ["video\Bi_kalam1.mp4", "audio/Bi_kalam1.mp3"],
    ["video\Bi_kalam2.mp4", "audio/Bi_kalam2.mp3"],
    ["video\Bi_kalam3.mp4", "audio/Bi_kalam3.mp3"],
    ["video\Bi_kalam4.mp4", "audio/Bi_kalam4.mp3"],
    ["video\Bi_kalam5.mp4", "audio/Bi_kalam5.mp3"]]


# 1. Normal program

def normal_program():
    for movie, output_path in movie_list:
        convert_movie_to_sound(movie, output_path)


# 2. Threading program

def threading_program():
    thread_list = []
    for movie, output_path in movie_list:
        thread = threading.Thread(target=convert_movie_to_sound, args=[movie, output_path])
        thread_list.append(thread)
    for thread in thread_list:
        thread.start()
    for thread in thread_list:
        thread.join()


if __name__ == "__main__":
    time_1 = time.time()
    normal_program()
    time_2 = time.time()
    print(f"Normal Program: {time_2 - time_1}") 
    threading_program()
    time_3 = time.time()
    print(f"Threading Program: {time_3 - time_2}")
