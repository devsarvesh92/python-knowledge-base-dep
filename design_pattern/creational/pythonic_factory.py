from dataclasses import dataclass
from pathlib import Path
from typing import Protocol, Type

class Exporter(Protocol):
    """
    Base class of exporter
    """
    def export(self,path:Path):
        """
        Defines export method
        """
        pass


class AudioExporter:
    """
    Defines audio exporter
    """

    def export(self,path:Path):
        """
        Defines export method
        """
        pass


class LowQualityAudioExporter:
    """
    Defines low quality audio exporter
    """

    def export(self,path:Path):
        """
        Defines export method
        """
        print(f'Exporting low quality audio at {path.absolute()}')


class MediumQualityAudioExporter:
    """
    Defines medium quality audio exporter
    """    

    def export(self,path:Path):
        """
        Defines medium quality export
        """
        print(f'Exporting medium quality audio at {path.absolute()}')


class HighQualityAudioExporter:
    """
    High quality audio exporter
    """

    def export(self,path:Path):
        """
        Defines medium quality export
        """
        print(f'Exporting High quality audio at {path.absolute()}')


class VideoExporter:

    def export(self,path:Path):
        """
        Defines medium quality export
        """
        print(f'Exporting medium quality video at {path.absolute()}')


class LowQualityVideoExporter:
    """
    Defines low quality video exporter
    """

    def export(self,path:Path):
        """
        Defines export method
        """
        print(f'Exporting low quality video at {path.absolute()}')


class MediumQualityVideoExporter:
    """
    Defines medium quality Video exporter
    """    

    def export(self,path:Path):
        """
        Defines medium quality export
        """
        print(f'Exporting medium quality Video at {path.absolute()}')


class HighQualityVideoExporter:
    """
    High quality Video exporter
    """

    def export(self,path:Path):
        """
        Defines medium quality export
        """
        print(f'Exporting High quality Video at {path.absolute()}')

@dataclass
class MediaExporter:
    audio_exporter:AudioExporter
    video_exporter:VideoExporter

@dataclass
class MediaExporterFactory:
    audio_class:Type[AudioExporter]
    video_class:Type[VideoExporter]

    def __call__(self) -> MediaExporter:
        return MediaExporter(audio_exporter=self.audio_class(),video_exporter=self.video_class())



FACTORY:dict[str,MediaExporterFactory] = {
    'low': MediaExporterFactory(LowQualityAudioExporter,LowQualityVideoExporter),
    'medium':MediaExporterFactory(MediumQualityAudioExporter,MediumQualityVideoExporter),
    'high':MediaExporterFactory(HighQualityAudioExporter,HighQualityVideoExporter)
}

if __name__ == '__main__':
    while True:
        ip = input('Please quality of audio: ')
        fac = FACTORY[ip]()
        fac.audio_exporter.export(Path('tmp/aud.wav'))
        fac.video_exporter.export(Path('tmp/vid.wav'))
        
