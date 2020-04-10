#!/usr/bin/env sh

for file in "$@"; do
	echo "$file" | grep -E ".jpe?g$" || continue
	convert "$file" -sampling-factor 4:2:0 -strip -quality 85 -interlace JPEG -colorspace sRGB -gaussian-blur 0.05 image_converted.jpg
done
