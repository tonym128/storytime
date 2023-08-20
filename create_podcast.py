# import required module
import os
from pathlib import Path
from feedgen.feed import FeedGenerator

# assign directory
directory = "_posts"
piper_directory = "../piper/"


## Save stories to piper dir
def getStoryText():
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            file1 = open(f, "r")
            Lines = file1.readlines()
            file1.close()

            count = 0
            # Strips the newline character
            file1 = open("../piper/" + os.path.splitext(Path(f).stem)[0] + ".txt", "w")
            for line in Lines:
                if count == 2:
                    print("{}".format(line.strip()))
                    file1.write(line)
                if line.startswith("---"):
                    count += 1
            file1.close()


# Get piper to process stories where there isn't an mp3
# Copy files to media directory
def processStories():
    dirlisting = os.listdir(piper_directory)
    dirlisting.sort()
    for filename in dirlisting:
        if filename.endswith(".txt"):
            if not os.path.exists(piper_directory + filename + ".mp3"):
                # story without mp3
                os.system("./piper.sh " + filename)
    return


# Check all posts and create podcast rss
def createPodcastRSS():
    fg = FeedGenerator()
    fg.load_extension("podcast")
    fg.title("AI Daily Short Story")
    fg.podcast.itunes_category("Technology", "Podcasting")
    fg.podcast.itunes_image("https://github.com/tonym128/storytime/raw/main/ai_generated_stories_3k.png")
    fg.podcast.itunes_author("Tony Mamacos")
    fg.podcast.itunes_owner('Tony Mamacos', 'tmamacos@gmail.com')
    fg.image("https://github.com/tonym128/storytime/raw/main/ai_generated_stories.png")
    fg.author({"name": "Tony Mamacos", "email": "tmamacos@gmail.com"})
    fg.language("en")

    fg.id("https://ttech.mamacos.media/storytime")
    fg.link(href="https://ttech.mamacos.media/storytime", rel="self")
    fg.description("A daily pod cast of an AI generated short story")

    listing = os.listdir(directory)
    listing.sort()
    for filename in os.listdir(directory):
        f = os.path.join(directory, filename)
        # checking if it is a file
        if os.path.isfile(f):
            file1 = open(f, "r")
            Lines = file1.readlines()
            file1.close()

            count = 0
            # Strips the newline character
            file1 = open(
                "../piper/"
                + os.path.splitext(Path(f).with_suffix("").stem)[0]
                + ".txt",
                "w",
            )
            body = ""
            values = {}
            values["filename"] = os.path.splitext(Path(f).with_suffix("").stem)[0]
            year = values["filename"][:4]
            month = values["filename"][5:7]
            day = values["filename"][8:10]
            values[
                "post_url"
            ] = "https://ttech.mamacos.media/storytime/post/{}/{}/{}/{}.html".format(
                year, month, day, values["filename"][11:]
            )
            values[
                "media_url"
            ] = "https://github.com/tonym128/storytime/raw/main/media/{}.txt.mp3".format(
                values["filename"]
            )

            for line in Lines:
                if count == 1 and not line.startswith("---"):
                    value = line.split(":")
                    values[value[0].strip()] = value[1].strip()
                if count == 2:
                    body += line.strip()
                    file1.write(line)
                if line.startswith("---"):
                    count += 1
            values["body"] = body
            file1.close()

            fe = fg.add_entry()
            fe.id(values["media_url"])
            fe.title(values["filename"][0:10] + " - " + values["title"])
            fe.description(values["body"])
            fe.podcast.itunes_author("Tony Mamacos")
            order = "{}{}{}".format(year,month,day)
            fe.podcast.itunes_order(int(order))
            fe.author({"name": "Tony Mamacos", "email": "tmamacos@gmail.com"})
            fe.link(href=values["post_url"], rel="alternate")
            fe.link(href=values["post_url"], rel="self")
            fe.enclosure(values["media_url"], 0, "audio/mpeg")
    fg.atom_file("atom.xml")  # Write the ATOM feed to a file
    fg.rss_file("rss.xml")  # Write the ATOM feed to a file
    return


getStoryText()
processStories()
createPodcastRSS()
