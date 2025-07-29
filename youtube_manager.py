import json


def load_data():
    try:
        with open('youtube.txt', 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []


def save_data_helper(videos):
    with open('youtube.txt', 'w') as file:
        json.dump(videos, file)


def list_all_videos(videos):
    print("\n" + "*" * 50)
    for index, video in enumerate(videos, start=1):
        print(f"{index}. {video['name']}, Duration: {video['time']}")
    print("*" * 50 + "\n")


def add_videos(videos):
    name = input("Enter video name: ")
    time = input("Enter duration of video: ")
    videos.append({'name': name, 'time': time})
    save_data_helper(videos)


def update_videos(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video number to be updated: "))
        if 1 <= index <= len(videos):
            name = input("Enter the new name of video: ")
            time = input("Enter the duration of video: ")
            videos[index - 1] = {'name': name, 'time': time}
            save_data_helper(videos)
        else:
            print("Invalid video index!")
    except ValueError:
        print("Please enter a valid number.")


def delete_videos(videos):
    list_all_videos(videos)
    try:
        index = int(input("Enter the video index to be deleted: "))
        if 1 <= index <= len(videos):
            del videos[index - 1]
            save_data_helper(videos)
        else:
            print("Invalid video index!")
    except ValueError:
        print("Please enter a valid number.")


def main():
    videos = load_data()
    while True:
        print("\nYoutube Manager | Choose an option")
        print("1. List all youtube videos.")
        print("2. Add a youtube video.")
        print("3. Update a youtube video details.")
        print("4. Delete a youtube video.")
        print("5. Exit the application.")
        choice = input("Enter your choice: ")

        match choice:
            case '1':
                list_all_videos(videos)
            case '2':
                add_videos(videos)
            case '3':
                update_videos(videos)
            case '4':
                delete_videos(videos)
            case '5':
                break
            case _:
                print("Invalid choice | Please try again.")


if __name__ == "__main__":
    main()
