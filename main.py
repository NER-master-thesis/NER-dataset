import yaml

from classification.Wikidata_classification import Wikidata_classification
from properties_graph.Subclass_graph_builder import Subclass_graph_builder

if __name__ == '__main__':
    #Instance_subclass_collector.collect_instance_and_sublass()



    #subclass_graph_builder = Subclass_graph_builder(folder)
    #subclass_graph_builder.build_graph()
    #subclass_graph_builder.build_mapping_to_NER_class()


    wd_classification = Wikidata_classification()
    #wd_classification.build_mapping_to_NER_class()
    wd_classification.classify_article()