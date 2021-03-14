from typing import Optional

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from didmap_api.enums.filters import Filters
from didmap_api.enums.map_types import MapTypes
from didmap_api.enums.game_types import GameTypes
from didmap_api.rdf_utils.collection_graph import CollectionGraph
from didmap_api.rdf_utils.map_graph import MapGraph

app = FastAPI()


@app.get("/mapcollection/")
async def read_user_me(
    map_type: MapTypes,
    continent: Optional[str] = None,
    country: Optional[str] = None,
    region: Optional[str] = None,
    game_type: Optional[GameTypes] = None,
):
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
async def read_user(map_path: str):
    map_graph = MapGraph()
    map_graph.load_map_ressource(map_path)

    if (map_graph.query_map_ressource()):
        return map_graph.map_info
    else:
        raise HTTPException(status_code=404, detail="Could not find the collection")