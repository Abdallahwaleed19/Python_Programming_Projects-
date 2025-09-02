class YouTubeChannel:

    def _init_(self, name):
        self.name = name
        self.__subscribers = []  # List of observers
        self.__latest_video = None

    def subscribe(self, subscriber):
        """Add a new subscriber"""
        if subscriber not in self.__subscribers:
            self.__subscribers.append(subscriber)
            print(f"{subscriber.name} subscribed to {self.name}")

    def unsubscribe(self, subscriber):
        """Remove a subscriber"""
        if subscriber in self.__subscribers:
            self.__subscribers.remove(subscriber)
            print(f"{subscriber.name} unsubscribed from {self.name}")

    def notify_subscribers(self):
        """Notify all subscribers about new video"""
        print(f"{self.name} notifying subscribers...")
        for subscriber in self.__subscribers:
            subscriber.update(self.__latest_video)

    def upload_video(self, video_title):
        """Upload new video and notify subscribers"""
        self.__latest_video = video_title
        print(f"{self.name} New video uploaded: '{video_title}'")
        self.notify_subscribers()


class Subscriber:
    """The Observer class - represents a channel subscriber"""

    def _init_(self, name):
        self.name = name

    def update(self, video_title):
        """Receive update from YouTube channel"""
        print(f"{self.name} received notification: New video - '{video_title}'")


if __name__ == "__main__":
    print("Observer pattern Demo")

    # Create a YouTube channel
    tech_channel = YouTubeChannel("Tech Channel")

    # Create subscribers
    subscriber1 = Subscriber("Alice")
    subscriber2 = Subscriber("Bob")

    # Subscribe to the channel
    tech_channel.subscribe(subscriber1)
    tech_channel.subscribe(subscriber2)

    # Upload new videos
    tech_channel.upload_video("Python Observer Pattern Tutorial")
    tech_channel.upload_video("Design Patterns in Python")