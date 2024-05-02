from neo4j import GraphDatabase

class MyNeo4j:

    def __init__(self, uri, user, password):
        self.driver = GraphDatabase.driver(uri, auth=(user, password))

    def close(self):
        self.driver.close()

    def create_note(self, asset_name, asset_type, asset_cluster):
        summary = self.driver.execute_query(
            "CREATE (:Asset {AssetName: $asset_name, AssetType: $asset_type, AssetCluster: $asset_cluster})",
            asset_name=asset_name,
            asset_type=asset_type,
            asset_cluster=asset_cluster,
            database_="neo4j",
        ).summary
        print("Created {nodes_created} nodes in {time} ms.".format(
            nodes_created=summary.counters.nodes_created,
            time=summary.result_available_after
        ))
    
    def create_relation(self, needs_asset_name, needs_asset_type, needs_asset_cluster, offers_asset_name, offers_asset_type, offers_asset_cluster):
        summary = self.driver.execute_query(
            """
              MATCH (as1:Asset), (as2:Asset)
              WHERE 
                as1.AssetName = $needs_asset_name AND as1.AssetType = $needs_asset_type AND as1.AssetCluster = $needs_asset_cluster AND 
                as2.AssetName = $offers_asset_name AND as2.AssetType = $offers_asset_type AND as2.AssetCluster = $offers_asset_cluster
              CREATE (as1)-[rel:RELATION]->(as2)""",
            needs_asset_name=needs_asset_name,
            needs_asset_type=needs_asset_type,
            needs_asset_cluster=needs_asset_cluster,
            offers_asset_name=offers_asset_name,
            offers_asset_type=offers_asset_type,
            offers_asset_cluster=offers_asset_cluster,
            database_="neo4j",
        ).summary
        print("Created {nodes_created} relation in {time} ms.".format(
            nodes_created=summary.counters.relationships_created,
            time=summary.result_available_after
        ))


if __name__ == "__main__":
    greeter = MyNeo4j("bolt://localhost:7687", "neo4j", "deneme123_")
    greeter.create_relation(
        needs_asset_name='New Jersey',
        needs_asset_type='Middleware',
        needs_asset_cluster='Edge',
        offers_asset_name='Delaware',
        offers_asset_type='Application',
        offers_asset_cluster='Cloud'
    )
    greeter.close()