from rdflib import Graph, Namespace
import rdflib.namespace as NS
from SPARQLWrapper import SPARQLWrapper, N3
import requests, re


class MapGraph(Graph):
    """
    Graph with data about the result set of a query from https://mapasinteractivos.didactalia.net/
    """

    url = "https://mapasinteractivos.didactalia.net/en/community/mapasflashinteractivos/resource/"
    """Url of Didactialia's ressources"""

    def __init__(self):
        super().__init__()

        # Namespaces
        self.NS = NS
        self.NS.SIOC_T = Namespace('http://rdfs.org/sioc/types#')
        self.NS.SIOC = Namespace('http://rdfs.org/sioc/ns#')
        self.NS.DIDMAP = Namespace('http://onto.didactalia.net/map#')
        self.NS.RES = Namespace('http://www.w3.org/2005/sparql-results#')
        self.item_query_NS = [
            self.NS.DCTERMS.created, 
            self.NS.RDFS.label, 
            self.NS.DC.creator
        ]
        self.map_query_NS = [
            self.NS.DIDMAP.continent,
            self.NS.DIDMAP.country,
            self.NS.DIDMAP.image,
            self.NS.DIDMAP.latMapCenter,
            self.NS.DIDMAP.longMapCenter,
            self.NS.DIDMAP.type,
            self.NS.DIDMAP.mapType,
        ]

        self.map_info = {}

    def load_map_ressource(self, path: str):
        """Retrieves the rdf data from Didactalia and parses it"""
        try:
            ressource = requests.get(MapGraph.url+path, headers={"content-type": "application/rdf+xml"})
            self.parse(data=ressource.content)
            
            return True
        except Exception as e:
            return False

    def query_map_ressource(self):
        """Query the graph to extract the relevant data"""
        # we reset the maps list
        self.map_info = {}

        try:
            # item info
            map_item = self.value(predicate=self.NS.RDF.type, object=self.NS.SIOC.Item)

            self.map_info["url"] = str(map_item)

            for pred in self.item_query_NS:
                self.map_info[pred.n3(self.namespace_manager).split(':')[1]] = str(self.value(map_item, pred))


            # Map info
            map_map = self.value(predicate=self.NS.RDF.type, object=self.NS.DIDMAP.Map)

            for pred in self.map_query_NS:
                if ("image" in pred.n3()):
                    obj = f"https://mapasinteractivos.didactalia.net/{str(self.value(map_map, pred))}"
                else:
                    obj = str(self.value(map_map, pred))
                
                self.map_info[pred.n3(self.namespace_manager).split(':')[1]] = obj

            # Map tags
            self.map_info["tags"] = [str(self.label(s)) for s, p, o in self.triples((None, None, self.NS.SIOC_T.Tag))]

            # enrich data
            for geo in ['country', 'continent']:
                geoname_country = re.findall(r"\d+", self.map_info[geo])

                if len(geoname_country) > 0:
                    data = self._query_dbpedia(geoname_country[0], geo == "country")

                    if (data):
                        self.map_info[f"{geo}_data"] = data

            return True
        except Exception as e:
            return False

    def _query_dbpedia(self, geonames_code: str, is_country: bool = False):
        """Get geographic data from DBpedia"""
        if (not geonames_code):
            return False
        
        try:
            sparql = SPARQLWrapper("http://dbpedia.org/sparql")

            if (is_country):
                query = sparql.setQuery("PREFIX owl: <http://www.w3.org/2002/07/owl#> PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX dbp: <http://dbpedia.org/property/> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> SELECT ?country ?countryLabel ?tel_code ?currency ?capital ?time_zone ?population (count(?wikilinks) as ?n_wikilinks) ?external_links WHERE { ?country owl:sameAs <http://sws.geonames.org/"+geonames_code+"/>; rdfs:label ?countryLabel; dbo:countryCode ?tel_code; dbp:capital [ rdfs:label ?capital ]; dbp:currency ?currency; dbp:timeZone ?time_zone; dbo:populationTotal ?population; dbo:wikiPageWikiLink ?wikilinks; dbo:wikiPageExternalLink ?external_links. FILTER(LANG(?capital) = 'es') FILTER(LANG(?countryLabel) = 'es') }")
            else:
                query = sparql.setQuery("PREFIX owl: <http://www.w3.org/2002/07/owl#> PREFIX dbo: <http://dbpedia.org/ontology/> PREFIX dbp: <http://dbpedia.org/property/> PREFIX rdfs: <http://www.w3.org/2000/01/rdf-schema#> SELECT ?continent ?continentLabel ?time_z ?population (count(?wikilinks) as ?n_wikilinks) ?external_links WHERE { ?continent owl:sameAs <http://sws.geonames.org/"+geonames_code+"/>;  rdfs:label ?continentLabel; dbp:time ?time_z; dbo:populationTotal ?population; dbo:wikiPageWikiLink ?wikilinks; dbo:wikiPageExternalLink ?external_links. FILTER(LANG(?continentLabel) = 'es') }")

            sparql.setReturnFormat(N3)
            results = sparql.query().convert()

            # we add the results to an empty graph
            g = Graph()
            g.parse(data=results, format="n3")

            # prepare output
            b_nodes = [s for s in g.subjects(self.NS.RES.value)]
            raw_data = set([(str(g.value(s, self.NS.RES.variable)), str(g.value(s, self.NS.RES.value))) for s in b_nodes])
            links = []
            data = {k:v if k != 'external_links' else links.append(v) for k, v in raw_data}
            data['external_links'] = links

            return data
        except Exception as e:
            return False