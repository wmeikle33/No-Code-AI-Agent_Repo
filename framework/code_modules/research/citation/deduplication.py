from .models import Citation


def deduplicate_citations(citations: list[Citation]) -> list[Citation]:
    seen = set()
    unique = []

    for citation in citations:
        key = (
            citation.title.lower(),
            citation.url
        )

        if key not in seen:
            seen.add(key)
            unique.append(citation)

    return unique
