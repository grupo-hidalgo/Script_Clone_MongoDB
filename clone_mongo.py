from pymongo import MongoClient
import argparse
import time

def clone_entire_db(uri, source_db, target_db):
    """
    Clona todas las colecciones de una base de datos de origen a una base de datos de destino.
    """
    client = MongoClient(uri)
    db = client[source_db]
    target = client[target_db]

    # Listar todas las colecciones en la base de datos de origen
    collections = db.list_collection_names()
    print(f"[INFO] Colecciones en la base de datos '{source_db}': {collections}")
    
    # Recorrer cada colección para clonar sus documentos
    for collection_name in collections:
        print(f"[INFO] Clonando colección: {collection_name}")
        source_collection = db[collection_name]
        target_collection = target[collection_name]
        
        # Copiar documentos de una colección a otra
        documents = list(source_collection.find())
        if documents:
            target_collection.insert_many(documents)
            print(f"[INFO] {len(documents)} documentos clonados de la colección '{collection_name}'")
        else:
            print(f"[INFO] La colección '{collection_name}' está vacía.")
    
    client.close()
    print("[INFO] Clonación de la base de datos completa.")


def clone_specific_collections(uri, source_db, target_db, collections):
    """
    Clona colecciones específicas de una base de datos de origen a una base de datos de destino.
    """
    client = MongoClient(uri)
    db = client[source_db]
    target = client[target_db]

    for collection_name in collections:
        print(f"[INFO] Clonando colección específica: {collection_name}")
        source_collection = db[collection_name]
        target_collection = target[collection_name]
        
        # Copiar documentos de una colección a otra
        documents = list(source_collection.find())
        if documents:
            target_collection.insert_many(documents)
            print(f"[INFO] {len(documents)} documentos clonados de la colección '{collection_name}'")
        else:
            print(f"[INFO] La colección '{collection_name}' está vacía.")
    
    client.close()
    print("[INFO] Clonación de colecciones específicas completa.")


def main():
    parser = argparse.ArgumentParser(description="Clonar una base de datos MongoDB o colecciones específicas.")
    parser.add_argument('--uri', required=True, help="URI de conexión a MongoDB.")
    parser.add_argument('--source_db', required=True, help="Base de datos de origen.")
    parser.add_argument('--target_db', required=True, help="Base de datos de destino.")
    parser.add_argument('--collections', nargs='+', help="Colecciones específicas a clonar (opcional). Si no se especifica, se clonará toda la base de datos.")
    
    args = parser.parse_args()

    # Medir tiempo de ejecución
    start_time = time.time()

    if args.collections:
        print(f"[INFO] Iniciando clonación de colecciones específicas: {args.collections}")
        clone_specific_collections(args.uri, args.source_db, args.target_db, args.collections)
    else:
        print("[INFO] Iniciando clonación de toda la base de datos.")
        clone_entire_db(args.uri, args.source_db, args.target_db)
    
    elapsed_time = time.time() - start_time
    print(f"[INFO] Proceso completado en {elapsed_time:.2f} segundos.")


if __name__ == "__main__":
    main()
