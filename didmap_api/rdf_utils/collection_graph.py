from rdflib import Graph, Namespace
import rdflib.namespace as NS
import requests, html


class CollectionGraph(Graph):
    """
    Graph with data about the result set of a query from https://mapasinteractivos.didactalia.net/
    """

    endpoint = "https://mapasinteractivos.didactalia.net/comunidad/mapasflashinteractivos/MapasDidactalia"
    """Endpoint of Didactalia - Mapas interactivos"""

    def __init__(self):
        super().__init__()

        # Namespaces
        self.NS = NS
        self.NS.SIOC = Namespace('http://rdfs.org/sioc/ns#')
        self.query_NS = [self.NS.DCTERMS.created, self.NS.RDFS.label, self.NS.SIOC.topic, self.NS.SIOC.has_creator]

        self.maps = []
        self.url = ""

    def load_collection(self, params: list):
        """Retrieves the rdf data from Didactalia and parses it"""
        try:
            self._set_url_endpoint(params)
            ressource = requests.get(self.url, headers={"content-type": "application/rdf+xml"})
            self.parse(data=ressource.text)

            return True
        except Exception as e:
            return False

    def query_collection(self):
        """Query the graph to extract the relevant data"""
        # we reset the maps list
        self.maps = []

        try:
            for map_item, _, _ in self.triples((None, None, self.NS.SIOC.Item)):
                map_info = {
                    'uri': str(map_item)
                }

                for pred in self.query_NS:
                    if ("topic" in pred.n3()):
                        obj = [str(self.value(tag, self.NS.RDFS.label)) for tag in self.objects(map_item, pred)]
                    elif ("has_creator" in pred.n3()):
                        obj = str(self.value(self.value(map_item, pred), self.NS.FOAF.name))
                    else:
                        obj = str(self.value(map_item, pred))

                    map_info[pred.n3(self.namespace_manager).split(':')[1]] = obj

                self.maps.append(map_info)

            return True
        except Exception as e:
            return False

    def _set_url_endpoint(self, params: list):
        """Adds the query parameters to the endpoint url"""
        query_params = "&".join([f"{p[0]}={p[1]}" for p in params if p[1]])
        
        self.url = f"{CollectionGraph.endpoint}?{query_params}"