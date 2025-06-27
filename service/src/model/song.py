from dataclasses import dataclass
from typing import Optional


@dataclass
class Song:
    path: str
    id: Optional[int] = None
    name: Optional[str] = None
    title: Optional[str] = None
    artist: Optional[str] = None
    year: Optional[int] = None
    album: Optional[str] = None
    link: Optional[str] = None
    file: Optional[str] = None
