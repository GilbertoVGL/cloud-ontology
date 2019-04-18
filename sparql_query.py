import owlready2
from owlready2 import *
from pymongo import MongoClient
# pprint library is used to make the output look more pretty
from pprint import pprint


class SparqlQuery:

    def __init__(self):
        onto_path.append("/home/gilberto/PycharmProjects/cloud_ontology/Ontology/")
        # onto = get_ontology("CloudOntology.owl")
        # onto2 = get_ontology("IaaS.owl")
        # onto.imported_ontologies.append(onto2)

        # my_world = World()
        my_world2 = World()

        # my_world.get_ontology("IaaS.owl").load()
        my_world2.get_ontology("IaaS.owl").load()

        # print("This is my onto: ", onto)
        # print("This is my ontology imports: ", onto.imported_ontologies)

        sync_reasoner(my_world2)  # reasoner is started and synchronized here

        self.graph = my_world2.as_rdflib_graph()

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
            # print("\t\tItem >\t\t\t\t\t\t\t\t", item)

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
