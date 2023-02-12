# Factory pattern
# Seperate design and use
# Factory produces object which implements common interface

from abc import ABC, abstractmethod
from pathlib import Path
from typing import Any


class AudioExporter(ABC):
    """
    Abstract class for Audio Exporter
    """

    @abstractmethod
    def export(self,location:Path):
        """
        Export audio
        """
        pass


class HighQualityAudioExporter(AudioExporter):
    """
    High quality audio exporter
    """
    def export(self, location: Path):
        print(f"Exporting file with high quality at {location.absolute()}")


class MediumQualityAudioExporter(AudioExporter):
    """
    Medium quality audio exporter
    """
    def export(self, location: Path):
        print(f"Exporting file with medium quality at {location.absolute()}")


class LowQualityAudioExporter(AudioExporter):
    """
    Low quality audio exporter
    """

    def export(self, location: Path):
        print(f"Exporting file with low quality at {location.absolute()}")


class ExporterFactory(ABC):
    """
    Defines exporter factory
    """

    def get_audio_exporter(self)->AudioExporter:
        pass

class LowQualityExporterFactory(ExporterFactory):
    """
    Creates low quality exporters
    """

    def get_audio_exporter(self) -> AudioExporter:
        return LowQualityAudioExporter()


class MediumQualityExporterFactory(ExporterFactory):
    """
    Creates medium quality exporters
    """

    def get_audio_exporter(self) -> AudioExporter:
        return MediumQualityAudioExporter()


class HighQualityExporterFactory(ExporterFactory):
    """
    Creates medium quality exporters
    """

    def get_audio_exporter(self) -> AudioExporter:
        return HighQualityAudioExporter()


exporters :dict[str,ExporterFactory]={
    'low': LowQualityExporterFactory(),
    'medium': MediumQualityExporterFactory(),
    'high': HighQualityExporterFactory()
}

if __name__ == '__main__':
    while True:
        user_input = input("Select choice of audio exporter: ")
        exporters[user_input.strip()].get_audio_exporter().export(Path('/tmp/loc/aud.wav'))

