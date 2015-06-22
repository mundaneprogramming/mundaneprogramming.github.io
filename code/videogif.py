from moviepy.editor import *

CLIP_NAME = 'his_girl_friday.mp4'
clip = VideoFileClip(CLIP_NAME).subclip(250,255)
txt_clip = TextClip("My test clip", fontsize = 20,color = 'white')
txt_clip = txt_clip.set_pos('center').set_duration(5)
video = CompositeVideoClip([clip, txt_clip])
video.write_videofile("hello.mp4", audio = True)
video.write_gif('hello.gif', fps=20)

