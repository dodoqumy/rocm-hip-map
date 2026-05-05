---
title: "Constructing a RAG system using LlamaIndex and Ollama &#8212; Tutorials for AI developers 12.0"
source_url: "https://rocm.docs.amd.com/projects/ai-developer-hub/en/latest/notebooks/inference/rag_ollama_llamaindex.html"
source_type: official
source_org: amd
credibility: 5
lifecycle: latest
fetched_at: 2026-05-04T15:25:36.572052+00:00
content_hash: "2f5fb98d587a28c4"
---

# Constructing a RAG system using LlamaIndex and Ollama[#](#constructing-a-rag-system-using-llamaindex-and-ollama)

**Author**: Alex He

**Knowledge level**: Beginner

AMD Radeon™ GPUs are officially supported by [ROCm](https://rocm.docs.amd.com/en/latest/index.html), ensuring compatibility with industry-standard software frameworks. This Jupyter notebook leverages [Ollama](https://ollama.com/) and [LlamaIndex](https://docs.llamaindex.ai/en/stable/), powered by ROCm, to build a Retrieval-Augmented Generation (RAG) application. LlamaIndex facilitates the creation of a pipeline from reading PDFs to indexing datasets and building a query engine, while Ollama provides the backend service for large language model (LLM) inference.

## Prerequisites[#](#prerequisites)

This tutorial was developed and tested using the following setup:

### Hardware[#](#hardware)

**AMD Radeon GPUs**: Ensure you are using an[AMD Radeon GPU](https://rocm.docs.amd.com/projects/radeon/en/latest/index.html)that supports ROCm. This tutorial was tested on the AMD Radeon PRO W7900.

### Software[#](#software)

**ROCm 6.2**: Install ROCm by following the[Radeon GPU install guide](https://rocm.docs.amd.com/projects/radeon/en/latest/docs/install/native_linux/install-radeon.html).**Python 3.8**: Ensure Python is installed and accessible in your environment.

### Environment[#](#environment)

Root or

`sudo`

access is required to install and configure the software.

## Install and launch Jupyter Notebooks[#](#install-and-launch-jupyter-notebooks)

If Jupyter is not already installed on your system, install it and launch JupyterLab using the following commands:

```
install jupyter
jupyter-lab --ip=0.0.0.0 --port=8888 --no-browser --allow-root
```

**Note**: Ensure port `8888`

is not already in use on your system before running the above command. If it is, you can specify a different port by replacing `--port=8888`

with another port number, for example, `--port=8890`

.

After the command executes, the terminal output displays a URL and token. Copy and paste this URL into your web browser on the host machine to access JupyterLab. After launching JupyterLab, upload this notebook to the environment and continue to follow the steps in this tutorial.

## Install Ollama[#](#install-ollama)

Ollama provides seamless support for AMD ROCm GPUs, offering optimized performance without further configuration. To install Ollama on Linux, use the following command:

```
!curl -fsSL https://ollama.com/install.sh | sh
```

Start Ollama and verify it’s running:

**Note**: The Ollama installation guide is available [here](https://github.com/ollama/ollama/blob/main/docs/linux.mdx).

```
!sudo systemctl start ollama
!sudo systemctl status ollama
```

## Download the models[#](#download-the-models)

Use Ollama to pull the required models for RAG:

**Important**: If the Ollama server is running as a foreground process from the previous step, you must run the rest of this notebook in a new instance.

```
!ollama pull nomic-embed-text
!ollama pull llama3.1:8b
```

Verify the downloaded models:

```
!ollama list llama3.1
```


See the [Ollama documentation](https://github.com/ollama/ollama) for more details.

**Note**: Alternative models are available to use [here](https://ollama.com/search).

## Install PyTorch (optional)[#](#install-pytorch-optional)

PyTorch is optional for this tutorial. This section uses PyTorch utilities for verification purposes.

```
!pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm6.2
```

Verify the list of installed packages:

```
!pip list | grep torch
```


Verify the GPU functionality:

```
import os
import torch
# Query GPU
if torch.cuda.is_available():
device = torch.device("cuda") # a CUDA device object
print('Using GPU:', torch.cuda.get_device_name(0))
print('GPU properties:', torch.cuda.get_device_properties(0))
else:
device = torch.device("cpu")
print('Using CPU')
```

## Install LlamaIndex and dependencies[#](#install-llamaindex-and-dependencies)

Use the following command to install LlamaIndex and related packages:

```
!pip install llama-index llama-index-llms-ollama llama-index-embeddings-ollama llama-index-vector-stores-chroma chromadb
```

Verify the installations:

```
!pip list | grep llama-index
```


## Build the RAG pipeline[#](#build-the-rag-pipeline)

This section explains how to configure and build the RAG pipeline.

### Set up indexing and the query engine[#](#set-up-indexing-and-the-query-engine)

Import the necessary libraries:

```
import chromadb
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import StorageContext
from llama_index.vector_stores.chroma import ChromaVectorStore
from llama_index.embeddings.ollama import OllamaEmbedding
from llama_index.llms.ollama import Ollama
```

### Configure embedding and LLM models[#](#configure-embedding-and-llm-models)

LlamaIndex implements the Ollama client interface to interact with the Ollama service. In this example, it requests both embedding and LLM services from Ollama.

```
# Set embedding model
emb_fn="nomic-embed-text"
Settings.embed_model = OllamaEmbedding(model_name=emb_fn)
# Set ollama model
Settings.llm = Ollama(model="llama3.1:8b", request_timeout=120.0)
```

### Download data for RAG[#](#download-data-for-rag)

Download a PDF (for example, the ROCm Radeon documentation) and save it to the `./data`

directory:

```
!mkdir ./data && cd ./data && wget --recursive --level=1 --content-disposition --accept=pdf -np -nH --cut-dirs=6 https://rocm.docs.amd.com/_/downloads/radeon/en/latest/pdf/ && cd ..
```

The SimpleDirectoryReader is the most commonly used data connector. Provide it with an input directory or a list of files and it selects the best file reader based on the file extensions.

```
documents = SimpleDirectoryReader(input_dir="./data/").load_data()
# Check the content
print(documents[10])
```

### Create a vector dataset with Chroma[#](#create-a-vector-dataset-with-chroma)

[Chroma DB](https://www.trychroma.com/) is a database that stores and queries embeddings, documents, and metadata for LLM apps that integrates well with LlamaIndex. It creates the vector dataset by sourcing the PDF file.

```
# Initialize client and save data
db = chromadb.PersistentClient(path="./chroma_db/rocm_db")
# create collection
chroma_collection = db.get_or_create_collection("rocm_db")
# assign chroma as the vector_store to the context
vector_store = ChromaVectorStore(chroma_collection=chroma_collection)
storage_context = StorageContext.from_defaults(vector_store=vector_store)
```

```
# Build vector index per-document
vector_index = VectorStoreIndex.from_documents(
documents,
storage_context=storage_context,
transformations=[SentenceSplitter(chunk_size=512, chunk_overlap=20)],
)
```

### Create the query engine[#](#create-the-query-engine)

Next, create the query engine with a response mode. Select the response mode based on your specific needs. For detailed guidance, see the [LlamaIndex response modes documentation](https://docs.llamaindex.ai/en/v0.10.19/module_guides/deploying/query_engine/response_modes.html).

```
# Query your data
query_engine = vector_index.as_query_engine(response_mode="refine", similarity_top_k=10)
```

## Customize the query prompts[#](#customize-the-query-prompts)

Define task-specific prompts:

```
# Updating Prompt for Q&A
from llama_index.core import PromptTemplate
template = (
"You are a car product expert who is very familiar with the car user manual and provides the guide to the end user.\n"
"---------------------\n"
"{context_str}\n"
"---------------------\n"
"Given the information from multiple sources and not prior knowledge\n"
"answer the question according to the index dataset.\n"
"if the question is not related to ROCm and Radeon GPU, just say it is not related to my knowledge base.\n"
"if you don't know the answer, just say that I don't know.\n"
"Answers need to be precise and concise.\n"
"if the question is in Chinese, please translate Chinese to English in advance"
"Query: {query_str}\n"
"Answer: "
)
qa_template = PromptTemplate(template)
query_engine.update_prompts(
{"response_synthesizer:text_qa_template": qa_template}
)
template = (
"The original query is as follows: {query_str}.\n"
"We have provided an existing answer: {existing_answer}.\n"
"We have the opportunity to refine the existing answer (only if needed) with some more context below.\n"
"-------------\n"
"{context_msg}\n"
"-------------\n"
"Given the new context, refine the original answer to better answer the query. If the context isn't useful, return the original answer.\n"
"if the question is 'who are you', just say I am an expert of AMD ROCm.\n"
"Answers need to be precise and concise.\n"
"Refined Answer: "
)
qa_template = PromptTemplate(template)
query_engine.update_prompts(
{"response_synthesizer:refine_template": qa_template}
)
```

## Query examples[#](#query-examples)

Run the following queries:

Query 1: Briefly describe the steps to install ROCm?


```
response = query_engine.query("Briefly describe the steps to install ROCm?")
print(response)
```

Query 2: Which chapter is about installing PyTorch?


```
response = query_engine.query("Which chapter is about installing PyTorch?")
print(response)
```

Query 3: How to verify a PyTorch installation?


```
response = query_engine.query("How to verify a PyTorch installation?")
print(response)
```

Query 4: Could ONNX run on a Radeon GPU?


```
response = query_engine.query("Could ONNX run on a Radeon GPU?")
print(response)
```

## Conclusion[#](#conclusion)

This tutorial demonstrates how to construct a RAG pipeline using LlamaIndex and Ollama on AMD Radeon GPUs with ROCm. For further details, see the documentation for the different components.
