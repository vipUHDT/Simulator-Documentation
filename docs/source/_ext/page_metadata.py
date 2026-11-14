
import re

from docutils import nodes

from sphinx.util import logging

logger = logging.getLogger(__name__)

def add_page_metadata(app, doctree, docname):
    if app.builder.format != "html":
        return

    # Exclude the homepage and all section index pages.
    if docname == "index":
        return

    # Read the YAML metadata from the Markdown file.
    metadata = app.env.metadata.get(docname, {})
    author = metadata.get("author", "Unknown")

    if isinstance(author, list):
        author = ", ".join(str(name) for name in author)

    # Count words from the document content.
    excluded = (
        nodes.literal_block,
        nodes.literal,
        nodes.raw,
        nodes.comment,
    )

    words = []

    for text_node in doctree.findall(nodes.Text):
        parent = text_node.parent

        while parent is not None:
            if isinstance(parent, excluded):
                break
            parent = parent.parent
        else:
            words.extend(
                re.findall(r"\b[\w'-]+\b", str(text_node))
            )

    word_count = len(words)

    # Create the author and word-count paragraph.
    metadata_node = nodes.paragraph(
        classes=["page-metadata"]
    )
    metadata_node += nodes.Text(
        f"Author: {author}  |  Word Count: {word_count:,}"
    )

    # Find the first section with a title.
    for section in doctree.findall(nodes.section):
        for index, child in enumerate(section.children):
            if isinstance(child, nodes.title):
                section.insert(index + 1, metadata_node)
                return

    # Report pages where no title could be found.
    logger.warning(
        f"No title found for page metadata: {docname}"
    )


def setup(app):
    app.connect("doctree-resolved", add_page_metadata)

    return {
        "version": "1.1",
        "parallel_read_safe": True,
        "parallel_write_safe": True,
    }
