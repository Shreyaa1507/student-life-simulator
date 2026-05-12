class Activity:
    """Base class for all student activities."""
    def __init__(self, category: str):
        self.category = category
        self.learning = 0.0
        self.social = 0.0
        self.attendance = 0.0

    def gains(self):
        return [self.learning, self.social, self.attendance]


class Event(Activity):
    """Event activity with social and learning changes."""
    def __init__(self, name: str, social_increase: float, learning_increase: float):
        super().__init__("Event")
        self.name = name
        self.social = social_increase
        self.learning = learning_increase
        self.attendance = 0.0


class Lecture(Activity):
    """Lecture activity that calculates learning based on distractions."""
    def __init__(self, time: int, distractions: list):
        super().__init__("Lecture")
        self.time = time
        self.distractions = distractions

    def gains(self):
        focus = 1.0
        short_video_found = False

        for distraction in self.distractions:
            distraction = distraction.strip().lower()

            if distraction == "sleeping":
                focus = 0
                break
            elif distraction in ["reels", "tiktok", "shorts"]:
                if not short_video_found:
                    focus -= 0.5
                    short_video_found = True
            elif distraction == "talking":
                focus -= 0.25
            elif distraction == "hungry":
                focus -= 0.15

        if focus < 0:
            focus = 0

        self.learning = round(self.time * focus, 2)
        self.social = 0.0
        self.attendance = 0.0

        return [self.learning, self.social, self.attendance]


class Workshop(Activity):
    """Workshop activity that calculates learning, social, and attendance gains."""
    def __init__(self, time: int, collaboration: bool, complete: bool):
        super().__init__("Workshop")
        self.time = time
        self.collaboration = collaboration
        self.complete = complete

    def gains(self):
        self.learning = 0.0
        self.social = 0.0

        if self.collaboration:
            self.learning += 50
            self.social += 50

        if self.complete:
            self.learning += 50

        if self.time >= 90:
            self.attendance = 1
        else:
            self.attendance = 0

        return [self.learning, self.social, self.attendance]
