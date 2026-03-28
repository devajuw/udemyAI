from typing_extensions import TypedDict
from typing import Annotated
from langgraph.graph.message import add_messages
from langgraph.graph import StateGraph, START, END
from langchain_ollama import ChatOllama

llm = ChatOllama(
    model="gemma3:1b"
)

class State(TypedDict):
    messages: Annotated[list, add_messages]
def chatbot(state: State):
    response = llm.invoke(state.get("messages"))
    return {"messages": [response]}
def samplenode(state:State):
    print("\n\n Inside SampleNode Node", state)
    return {"messages":["Sample Message"]}
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot", chatbot)
graph_builder.add_node("samplenode", samplenode)

# Defining Edges

graph_builder.add_edge(START, "chatbot")
graph_builder.add_edge("chatbot", "samplenode")
graph_builder.add_edge("samplenode", END)

graph =graph_builder.compile()

updated_state = graph.invoke(State({"messages": ["Hi,my name is Dev Raj"]}))
print("\n\n updated_state: ", updated_state)