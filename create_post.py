import argparse
from datetime import datetime

def format_tags(tags):
    a = ''
    for s in tags.split():
        a += f'"{s.replace("_", " ")}",'
        
    return a[:-1]

def format_filename(date, title):
    return f'{date}-{title.replace(" ", "-").lower()}.markdown'

def write_frontmatter(args, current_time):
    text_file = open(args.content, "r")
    story_text = text_file.read().strip()
    text_file.close()
    first_sentence_index = story_text.find('.')
    args.title = story_text[0: first_sentence_index]

    f = open(f"./_posts/{format_filename(args.date, args.title)}", "w")
    f.write("---\n")
    f.write("layout: post\n")
    f.write(f"title: {args.title}\n")
    f.write(f"date: {args.date} {current_time} +0200\n")
    f.write("comments: true\n")
    f.write("published: true\n")
    f.write("categories: [\"post\"]\n")
    f.write(f"tags: [{format_tags(args.tags)}]\n")
    f.write(f"author: {args.author}\n")
    f.write("---\n")
    f.write("{data}\n")
    f.close()
    
if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Create a new post')
    parser.add_argument("--content", type=str, help="A filename for content for the post")
    parser.add_argument("--date", type=str, help="Provide a date in format yyyy-mm-dd", default="2000-01-01")
    parser.add_argument("--tags", type=str, help="Provide a comma separated list of tags", default="Story")
    parser.add_argument("--title", type=str, help="Provide a title", default="default")
    parser.add_argument("--author", type=str, help="Provide a name for the author of the post", default="Tony Mamacos")
    args = parser.parse_args()

    now = datetime.now()
    datenow = str(datetime.today()).split()[0]
    if (args.date == "2000-01-01"):
        args.date = datenow
    current_time = now.strftime("%H:%M:%S")

    write_frontmatter(args, current_time)
