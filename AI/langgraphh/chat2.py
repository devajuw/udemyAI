
from typing_extensions import TypedDict
from typing import Optional, Literal
from langgraph.graph import StateGraph, START, END
from openai import OpenAI

client = OpenAI(
        base_url="http://localhost:11434/v1",
    api_key="ollama",
)
Model = "gemma3:1b"
Model_2 = "gemma3:4b"
class State(TypedDict):
    user_query: str
    llm_output: Optional[str]
    is_good: Optional[bool]
def chatbot(state: State):
    print("ChatBot Node", state)
    response=client.chat.completions.create(
    model=Model,
        messages=[
            {"role": "user","content": state.get("user_query")}
    ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state
def evaluate_resp(state:State) -> Literal["chatbot_gemini","endnode"]:
    print("Evaluate_resp Node", state)
    # Evaluate the response quality based on state
    if state.get("llm_output"):
        return "endnode"
    return "chatbot_gemini"
def chatbot_gemini(state:State):
    print("chatbot_gemini Node", state)
    response=client.chat.completions.create(
    model=Model_2,
        messages=[
            {"role": "user","content": state.get("user_query")}
    ]
    )
    state["llm_output"] = response.choices[0].message.content
    return state
def endnode(state:State):
    print("endnode", state)
    return state
graph_builder = StateGraph(State)
graph_builder.add_node("chatbot",chatbot)
graph_builder.add_node("chatbot_gemini",chatbot_gemini)
graph_builder.add_node("endnode", endnode)

graph_builder.add_edge(START, "chatbot")
graph_builder.add_conditional_edges("chatbot", evaluate_resp)
graph_builder.add_edge("chatbot_gemini", "endnode")
graph_builder.add_edge("endnode", END)

graph = graph_builder.compile()
updated_state = graph.invoke(State({"user_query": "Hi,what is 7+9"}))
print("\n\n updated_state: ", updated_state)