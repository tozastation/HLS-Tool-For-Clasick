ffmpeg -i ./src/canon_in_d/ori_canon_in_d.mp3 \
       -map 0 \
       -f segment\
       -segment_time 5 \
       -segment_list ./src/canon_in_d/canon_in_d.m3u8 ./src/canon_in_d/canon_in_d-%03d.ts

# ffmpeg -i ./src/canon_in_d/ori_canon_in_d.mp3 -f hls ./src/canon_in_d/canon_in_d.m3u8