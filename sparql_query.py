from owlready2 import *
from pprint import pprint


class SparqlQuery:

    def __init__(self):
        onto_path.append("/home/gilberto/PycharmProjects/cloud_ontology/Ontology/")

        default_world.get_ontology("CloudOntology.owl").load()

        sync_reasoner()  # reasoner is started and synchronized here

        self.graph = default_world.as_rdflib_graph()

    def search(self):
        # Search query is given here
        # Base URL of your ontology has to be given here
        query = """ PREFIX ab: <http://www.owl-ontologies.com/CloudOntology.owl>
                SELECT ?s ?p ?o
                WHERE {
                ?s ?p ?o .
                } """
        print(query)
        # query is being run
        resultsList = self.graph.query(query)

        # creating json object
        response = []
        for item in resultsList:

            s = str(item['s'].toPython())
            s = re.sub(r'.*#', "", s)

            p = str(item['p'].toPython())
            p = re.sub(r'.*#', "", p)

            o = str(item['o'].toPython())
            o = re.sub(r'.*#', "", o)

            response.append({'s': s, 'p': p, 'o': o})

        return response


runQuery = SparqlQuery()
response = runQuery.search()

pprint(response)  # just to show the output
