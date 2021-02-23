"""MIT License
Copyright (c) 2019-2020 PythonistaGuild
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import collections
from typing import Optional


class Karaoke:
    """Class representing a Karaoke filter.
    .. versionadded:: 0.10.0
    Parameters
    ------------
    level: Optional[float]
    mono_level: Optional[float]
    filter_band: Optional[float]
    filter_width: Optional[float]
    """

    def __init__(self, *, level: float = 1.0, mono_level: float = 1.0, filter_band: float = 220.0, filter_width: float = 100.0):

        self.level = level
        self.mono_level = mono_level
        self.filter_band = filter_band
        self.filter_width = filter_width

        self._name = 'Karaoke'

    def __str__(self) -> str:
        return self._name

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self):
        return f'<wavelink.filters.Karaoke: level={self.level}, mono_level={self.mono_level}, filter_band={self.filter_band}, filter_width={self.filter_width}>'

    @property
    def payload(self) -> dict:
        return {'karaoke': {'level': self.level, 'mono_level': self.mono_level, 'filter_band': self.filter_band, 'filter_width': self.filter_width}}


class Timescale:
    """Class representing a Timescale filter.
    This filter modifies the pitch or speed of the track, with the rate parameter affecting both of them at once.
    .. versionadded:: 0.10.0
    Parameters
    ------------
    speed: Optional[float]
        The scale by which the speed of the track should change.
    pitch: Optional[float]
        The scale by which the pitch of the track should change.
    rate: Optional[float]
        A combination of speed and pitch, a value of 1.25 will set both the pitch and speed to 1.25.
    """

    def __init__(self, *, speed: float = 1.0, pitch: float = 1.0, rate: float = 1.0):

        self.speed = speed
        self.pitch = pitch
        self.rate = rate

        self._name = 'Timescale'

    def __str__(self) -> str:
        return self._name

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self):
        return f'<wavelink.filters.Timescale: speed={self.speed}, pitch={self.pitch}, rate={self.rate}>'

    @property
    def payload(self) -> dict:
        return {'timescale': {'speed': self.speed, 'pitch': self.pitch, 'rate': self.rate}}


class Tremolo:
    """Class representing a Tremolo filter.
    Uses amplification to create a shuddering effect in which the volume quickly oscillates.
    .. versionadded:: 0.10.0
    Parameters
    ------------
    frequency: Optional[float]
        The frequency at which the volume should oscillate. Should be more than 0.0.
    depth: Optional[float]
        The scale by which the volume should oscillate. Should be more than 0.0 and less than or equal to 1.0.
    """

    def __init__(self, *, frequency: float = 2.0, depth: float = 0.5):

        if frequency < 0:
            raise ValueError('Frequency must be more than 0.0')
        if not 0 < depth <= 1:
            raise ValueError('Depth must be more than 0.0 and less than or equal to 1.0')

        self.frequency = frequency
        self.depth = depth

        self._name = 'Tremolo'

    def __str__(self) -> str:
        return self._name

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self):
        return f'<wavelink.filters.Tremolo: frequency={self.frequency}, depth={self.depth}>'

    @property
    def payload(self) -> dict:
        return {'tremolo': {'frequency': self.frequency, 'depth': self.depth}}


class Vibrato:
    """Class representing a Vibrato filter.
    Uses amplification to create a shuddering effect in which the pitch oscillates.
    .. versionadded:: 0.10.0
    Parameters
    ------------
    frequency: Optional[float]
        The frequency at which the pitch should oscillate. Should be more than 0.0 and less than or equal to 14.0
    depth: Optional[float]
        The scale by which the pitch should oscillate. Should be more than 0.0 and less than or equal to 1.0.
    """

    def __init__(self, *, frequency: float = 2.0, depth: float = 0.5):

        if not 0 < frequency <= 14:
            raise ValueError('Frequency must be more than 0.0 and less than or equal to 14.0')
        if not 0 < depth <= 1:
            raise ValueError('Depth must be more than 0.0 and less than or equal to 1.0')

        self.frequency = frequency
        self.depth = depth

        self._name = 'Vibrato'

    def __str__(self) -> str:
        return self._name

    @property
    def name(self) -> str:
        return self._name

    def __repr__(self):
        return f'<wavelink.filters.Vibrato: frequency={self.frequency}, depth={self.depth}>'

    @property
    def payload(self) -> dict:
        return {'vibrato': {'frequency': self.frequency, 'depth': self.depth}}


class Filter:
    """Class representing a Lavalink filter.
    .. versionadded:: 0.10.0
    Parameters
    ------------
    volume: Optional[float]
        The volume of the filter, where a value of 1.0 is 100% volume. Values over 1.0 may cause clipping.
    equalizer: Optional[:class:`Equalizer`]
        An Equalizer filter.
    karaoke: Optional[:class:`Karaoke`]
        A Karaoke filter.
    timescale: Optional[:class:`Timescale`]
        A Timescale filter.
    tremolo: Optional[:class:`Tremolo`]
        A Tremolo filter.
    vibrato: Optional[:class:`Vibrato`]
        A vibrato filter.
    """

    def __init__(self, *, volume: Optional[float] = None, equalizer: Optional[Equalizer] = None, karaoke: Optional[Karaoke] = None,
                 timescale: Optional[Timescale] = None, tremolo: Optional[Tremolo] = None, vibrato: Optional[Vibrato] = None):

        self.volume = volume
        self.equalizer = equalizer
        self.karaoke = karaoke
        self.timescale = timescale
        self.tremolo = tremolo
        self.vibrato = vibrato

    def __repr__(self):
        return f'<wavelink.filters.Filter: volume={self.volume}, equalizer={self.equalizer}, karaoke={self.karaoke}, ' \
               f'timescale={self.timescale}, tremolo={self.tremolo}, vibrato={self.vibrato}>'

    @property
    def payload(self) -> dict:

        _dict = {}

        if self.volume is not None:
            _dict['volume'] = self.volume
        if self.equalizer is not None:
            _dict['equalizer'] = self.equalizer.eq
        if self.karaoke is not None:
            _dict['karaoke'] = self.karaoke.payload
        if self.timescale is not None:
            _dict['timescale'] = self.timescale.payload
        if self.tremolo is not None:
            _dict['tremolo'] = self.tremolo.payload
        if self.vibrato is not None:
            _dict['vibrato'] = self.vibrato.payload

        return _dict
