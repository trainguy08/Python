class Television:
    """
    These are the outer limits for each variable.
    :param MIN_VOLUME: This is the minimum volume
    :param MAX_VOLUME: This is the maximum volume
    :param MIN_CHANNEL: This is the minimum channel
    :param MAX_CHANNEL: This is the maximum channel
    """
    MIN_VOLUME = 0
    MAX_VOLUME = 2
    MIN_CHANNEL = 0
    MAX_CHANNEL = 3

    def __init__(self:int):
        """
        This is the initial values for every variable.
        :param self.__status: This determines whether the tv is on (True for on, False for off)
        :param self.__muted: This determines whether the tv is on mute (True for on, false for off)
        :param self.__volume: This determines the tv's volume
        :param self.__channel: This determines the tv's channel
        """
        self.__status = False
        self.__muted = False
        self.__volume = Television.MIN_VOLUME
        self.__channel = Television.MIN_CHANNEL
    def power(self:bool):
        """
        This function switches the tv's status from on to off or vica versa. True = on, False = off
        """
        if self.__status == False:
            self.__status = True
        else:
            self.__status = False

    def mute(self:bool):
        """
        This function switches wether the is mutedor not. True = muted, False = unmuted
        """
        if self.__muted == False:
            self.__muted = True
        else:
            self.__muted = False
    def channel_up(self: int):
        """
        This function turns the channel up one, unless the channel is at the maximum value, in which case puts the
        channel to its minimum value.
        """
        if self.__status:
            if self.__channel == Television.MAX_CHANNEL:
                self.__channel = Television.MIN_CHANNEL
            else:
                self.__channel += 1

    def channel_down(self:int):
        """
        This function turns the channel down one, unless the channel is at the minimum value, in which case puts the
        channel to its maximum value.
        """

        if self.__status:
            if self.__channel == Television.MIN_CHANNEL:
                self.__channel = Television.MAX_CHANNEL
            else:
                self.__channel -= 1
    def volume_up(self:int):
        """
        This function increases the volume by one.
        If the tv is muted, it unmutes
        If the volume is at the maximum value, nothing changes
        """
        if self.__status:
            if self.__muted == True:
                self.__muted = False
            if self.__volume < Television.MAX_VOLUME:
                self.__volume += 1
    def volume_down(self:int):
        """
        Thus function decreases the volume by one
        If the tv is muted, it unmutes
        If the volume is at the minimum value, nothing changes.
        """
        if self.__status:
            if self.__muted == True:
                self.__muted = False
            if self.__volume > Television.MIN_VOLUME:
                self.__volume -= 1
    def __str__(self) -> str:
        """
        This function displays the status of the tv when printed.
        :return: This displays the tv's power status, channel, and volume
        """
        if self.__status:
            if self.__muted:
                return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {Television.MIN_VOLUME}'
            else:
                return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
        else:
            return f'Power = {self.__status}, Channel = {self.__channel}, Volume = {self.__volume}'
