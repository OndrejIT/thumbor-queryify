import base64
import binascii
import re
from typing import Any
from urllib.parse import parse_qs, urlparse

from thumbor.config import Config
from thumbor.handler_lists import HandlerList
from thumbor.handlers.imaging import ImagingHandler
from thumbor.url import Url

url_compile = re.compile(Url.regex())

Config.define(
    "QUERYIFY_B64",
    True,
    "Turn on base 64 encoding of query parameters",
    "Loader",
)


class QueryHandler(ImagingHandler):
    def prepare(self):
        parsed_url = urlparse(self.request.uri)
        query = self._extract_query_param(parsed_url)
        decoded_query = self._decode_base64_urlsafe(query) if self.context.config.QUERYIFY_B64 else query

        self.path_kwargs = self._extract_path_kwargs(decoded_query)
        self.request.path = self._reconstruct_uri(parsed_url.path, decoded_query)

        super().prepare()

    @staticmethod
    def _extract_query_param(parsed_url):
        """
        Extracts the "th" parameter from the query string
        or returns the entire query string if "th" is not present.
        """
        try:
            return parse_qs(parsed_url.query)["th"][0]
        except (KeyError, IndexError):
            return parsed_url.query

    @staticmethod
    def _decode_base64_urlsafe(encoded_string):
        """
        Decodes a Base64 URL-safe string. If the decoding is invalid, returns an empty string.
        """
        padding = lambda s: s + "=" * (-len(s) % 4)  # Add padding if missing
        try:
            return base64.urlsafe_b64decode(padding(encoded_string)).decode()
        except (binascii.Error, ValueError):
            return ""

    @staticmethod
    def _extract_path_kwargs(query):
        """
        Extracts parameters from a query using a regular expression.
        """
        result = re.match(url_compile, query)
        if result:
            return result.groupdict()
        return {
            "image": "",
        }

    @staticmethod
    def _reconstruct_uri(path, decoded_query):
        """
        Reestablish url
        """
        return f"{path}?{decoded_query}" if decoded_query else path


def get_handlers(context: Any) -> HandlerList:
    return [(r"[a-zA-Z0-9/\.,=_\-]+", QueryHandler, {"context": context})]
