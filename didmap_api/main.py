from typing import Optional

from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware

from didmap_api.enums.filters import Filters
from didmap_api.enums.map_types import MapTypes
from didmap_api.enums.game_types import GameTypes
from didmap_api.rdf_utils.collection_graph import CollectionGraph
from didmap_api.rdf_utils.map_graph import MapGraph


app = FastAPI(
    title="Didmap API client",
    description="Unofficial Python API client for https://mapasinteractivos.didactalia.net",
    version="1.0.0",
)


origins = ['*']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["GET"],
    allow_headers=["*"],
)


@app.get("/mapcollection/")
async def get_collection(
    map_type: MapTypes,
    continent: Optional[str] = None,
    country: Optional[str] = None,
    region: Optional[str] = None,
    game_type: Optional[GameTypes] = None,
):
    """
    Retrives info about several Didactalia's interactive maps based on the query parameters provided
    """
    filters = [
        (Filters.map_type, map_type),
        (Filters.continent, continent),
        (Filters.country, country),
        (Filters.region, region),
        (Filters.game_type, game_type),
    ]

    coll = CollectionGraph()
    coll.load_collection(filters)

    if (coll.query_collection()):
        return { "url": coll.url, "results": len(coll.maps), "data": coll.maps }
    else:
        raise HTTPException(status_code=404, detail="Could not find the collection")


@app.get("/map/")
async def get_map(map_path: str):
    """Get info about a Didactalia's interactive map"""
    map_graph = MapGraph()
    map_graph.load_map_ressource(map_path)

    if (map_graph.query_map_ressource()):
        return map_graph.map_info
    else:
        raise HTTPException(status_code=404, detail="Could not find the collection")