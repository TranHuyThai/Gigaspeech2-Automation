
# DO CATEGORY BY CATEGORY
echo  "Selected Category: $1"
category_path="./Categories/$1"

if [ -d $category_path ]; then
	echo "Starting work on $1...."
	#Crawling videos
	./download_from_youtube_channels.sh "$category_path/channels.txt" "$category_path/download"

	#Converting to wav format
	for channel in $category_path/download/*
	do	 
		echo $channel
        	python convert_and_transcribe.py \
          	 --lang zh \
          	 --root-dir $channel \
		 --save-dir $category_path/wav_download
	done

else
	#Creating Channel and Cookie Template for each new Category
	mkdir $category_path
	touch $category_path/channels.txt
	echo "Category: $1 does not exist. Template folder created, please fill in 'channel.txt' file."

fi
