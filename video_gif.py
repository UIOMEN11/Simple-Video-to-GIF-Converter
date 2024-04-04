from moviepy.editor import *

video = VideoFileClip("video.mp4").subclip(11,17)

video.write_gif("God.gif")