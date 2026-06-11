from .models import Citation


class SourceTracker:
    def __init__(self):
        self._sources = []

    def add_source(self, citation: Citation):
        self._sources.append(citation)

    def get_sources(self):
        return self._sources

    def clear(self):
        self._sources.clear()

    def count(self):
        return len(self._sources)
