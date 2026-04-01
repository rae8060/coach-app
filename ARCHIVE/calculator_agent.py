# --- Core Imports ---
from typing import List, Dict, TypedDict, Any
from langgraph.graph import StateGraph, END
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage
from langchain_core.tools import tool
# from langchain_anthropic import ChatAnthropic # Uncomment if using real model

# --- Define the State Structure ---
class AgentState(TypedDict):
    messages: List[Dict[str, Any]]

# --- Define Calculator Tools ---
@tool
def add(a: int, b: int) -> int:
    """Adds `a` and `b`."""
    return a + b

@tool
def multiply(a: int, b: int) -> int:
    """Multiplies `a` and `b`."""
    return a * b

# --- Agent Node Simulation ---
def agent_node(state: AgentState) -> Dict[str, Any]:
    last_human_message = None
    for msg_dict in reversed(state['messages']):
        if msg_dict['type'] == 'human':
            last_human_message = HumanMessage(**msg_dict['data'])
            break
            
    if last_human_message is None:
        return {"messages": [AIMessage(content="Error: No human message found.")]}

    user_input = last_human_message.content.lower()
    
    if "add" in user_input:
        try:
            parts = user_input.split()
            num1 = int(parts[parts.index("add") + 1])
            num2 = int(parts[parts.index("add") + 2])
            # Simulate tool output directly for now
            return {"messages": [ToolMessage(content=str(add(num1, num2)), tool_call_id="add_tool")]}
        except (ValueError, IndexError):
            return {"messages": [AIMessage(content="Could not parse numbers for addition. Format: 'add X and Y'.")]}
            
    elif "multiply" in user_input:
        try:
            parts = user_input.split()
            num1 = int(parts[parts.index("multiply") + 1])
            num2 = int(parts[parts.index("multiply") + 2])
            # Simulate tool output directly for now
            return {"messages": [ToolMessage(content=str(multiply(num1, num2)), tool_call_id="multiply_tool")]}
        except (ValueError, IndexError):
            return {"messages": [AIMessage(content="Could not parse numbers for multiplication. Format: 'multiply X by Y'.")]}

    else:
        return {"messages": [AIMessage(content="I can only perform add or multiply. How can I help?")]}

# --- Tool Node Simulation (Simplified) ---
def tool_node(state: AgentState) -> Dict[str, Any]:
    # Simplified: agent_node directly returns the outcome in this simulation
    if state['messages'] and state['messages'][-1]['type'] == 'tool_message':
        tool_output = state['messages'][-1]['data']['content']
        return {"messages": [ToolMessage(content=tool_output, tool_call_id="simulated_tool_call")]}
    else:
        return {"messages": [AIMessage(content="Internal error: Tool output simulation failed.")]}

# --- Graph Definition ---
workflow = StateGraph(AgentState)
workflow.add_node("agent", agent_node) 
# Tool node is implicitly handled by agent_node's simulation output in this example
workflow.set_entry_point("agent")
workflow.set_finish_point("agent") 
app = workflow.compile()

# --- Helper to format messages ---
def format_message(message):
    # Changed .dict() to .model_dump()
    return {"type": message.__class__.__name__.lower().replace("message", ""), "data": message.model_dump()}

# --- Simulation ---
input_text = "What is 5 plus 3?"
initial_state = {"messages": [format_message(HumanMessage(content=input_text))]} 

print(f"--- Simulating agent run with input: '{input_text}' ---")
try:
    final_state = app.invoke(initial_state)
    
    # Directly access the last message content for printing
    if 'messages' in final_state and final_state['messages']:
        # Get the last item from the messages list
        last_message_item = final_state['messages'][-1]

        message_content = None
        message_type = "Unknown"

        # Check if the item is a dictionary (our expected format from format_message)
        if isinstance(last_message_item, dict):
            msg_type_str = last_message_item.get('type')
            msg_data = last_message_item.get('data')

            if msg_type_str == 'ai' and msg_data:
                # Reconstruct AIMessage from dict
                message_content = AIMessage(**msg_data).content
                message_type = 'AI'
            elif msg_type_str == 'tool_message' and msg_data:
                # Reconstruct ToolMessage from dict
                message_content = ToolMessage(**msg_data).content
                message_type = 'Tool'
            elif 'content' in last_message_item: # Fallback for dicts with 'content' at top level
                message_content = last_message_item['content']
                message_type = 'DirectDict'

        # Check if the item is already an AIMessage or ToolMessage object that LangGraph might return directly
        elif isinstance(last_message_item, AIMessage):
            message_content = last_message_item.content
            message_type = 'AI'
        elif isinstance(last_message_item, ToolMessage):
            message_content = last_message_item.content
            message_type = 'Tool'

        if message_content is not None:
            print(f"--- Agent's Response ({message_type}) ---")
            print(message_content)
        else:
            print("Agent did not produce a recognizable response.")

    else:
        print("Agent did not produce a final response or messages.")
        
except Exception as e:
    print(f"An error occurred: {e}")
    import traceback
    traceback.print_exc()