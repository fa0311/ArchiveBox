from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI, Schema, ModelSchema
from main import add, remove

from typing import Dict, List, Optional, Iterable, IO, Union

from datetime import datetime, timezone, timedelta


class Link(Schema):
    timestamp: str
    url: str
    title: Optional[str]
    tags: Optional[str]
    sources: List[str]
    updated: Optional[datetime]


class AddResponse(Schema):
    links: List[Link]


class RustAPI:
    api = NinjaAPI()

    @api.get("/add", response=AddResponse)
    def add(
        request,
        urls: Union[str, List[str]],
        tag: str = "",
        depth: int = 0,
        parser: str = "auto",
    ):
        input_kwargs = {
            "urls": urls,
            "tag": tag,
            "depth": depth,
            "parser": parser,
        }

        a = add(**input_kwargs)

        print(a[0].history)

        return AddResponse(links=add(**input_kwargs))
