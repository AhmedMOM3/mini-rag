APP_NAME="mini-RAG"
APP_VERSION="0.1"
OPEN_API_KEY=""

FILE_ALLOWED_TYPES=["text/plain", "application/pdf"]
FILE_MAX_SIZE=10
FILE_DEFAULT_CHUNK_SIZE=512000  #512kb

# MONGODB_URL="mongodb://admin:admin@localhost:27007"
# MONGODB_DATABASE="mini-rag"

POSTGRES_USERNAME= "postgres"
POSTGRES_PASSWORD= "postgres_password"
POSTGRES_HOST= "pgvector"             # hostname: it is the service name in docker
POSTGRES_PORT= 5432
POSTGRES_MAIN_DATABASE= "minirag"

#=========================== LLM Config ===========================
GENERATION_BACKEND = "OPENAI"
EMBEDDING_BACKEND = "COHERE"


OPENAI_API_KEY=""  #using github key
OPENAI_API_URL="https://models.github.ai/inference"
COHERE_API_KEY=""

GENERATION_MODEL_ID="openai/gpt-4o-mini" #from github
EMBEDDING_MODEL_ID="embed-multilingual-v3.0"
EMBEDDING_MODEL_SIZE=1024

INPUT_DEFAULT_MAX_CHARACTERS=1024
GENERATION_DEFAULT_MAX_TOKENS=200
GENERATION_DEFAULT_TEMPERATURE=0.1

#=========================== Vector DB Config ===========================
VECTOR_DB_BACKEND_LITERAL = ["QDRANT", "PGVECTOR"]
VECTOR_DB_BACKEND = "PGVECTOR"
VECTOR_DB_PATH = "qdrant_db"
VECTOR_DB_DISTANCE_METHOD = "cosine"
VECTOR_DB_PGVEC_INDEX_THRESHOLD = 100  # it is up to you, you can make it 10000

#=========================== Template Config ===========================
PRIMARY_LANG ="en"
DEFAULT_LANG ="en"
