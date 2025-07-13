# main.py
from fastapi import FastAPI, HTTPException, Path, Body, status
from pydantic import BaseModel, Field
from typing import List, Dict
import uuid
import uvicorn

# Initialize FastAPI app
app = FastAPI(
    title="RPN API",
    description="A simple RPN calculator API using FastAPI",
    version="1.0"
)

# In-memory data store for stacks
stacks: Dict[str, List[float]] = {}

# --- Pydantic Models ---
# Model for the input value to be pushed onto the stack
class Value(BaseModel):
    value: float = Field(..., description="The value to push onto the stack")

# Model for a stack, including its ID and content
class StackModel(BaseModel):
    stack_id: str = Field(..., description="The stack unique identifier")
    stack: List[float] = Field(..., description="The content of the stack")

# --- Helper Functions ---
def apply_operation(stack: List[float], operator: str) -> bool:
    """
    Applies a mathematical operation to the stack.

    Args:
        stack (list): The stack to operate on.
        operator (str): The operator to apply (+, -, *, /).

    Returns:
        bool: True if the operation was successful, False otherwise.
    """
    if len(stack) < 2:
        return False
    b = stack.pop()
    a = stack.pop()
    if operator == '+':
        stack.append(a + b)
    elif operator == '-':
        stack.append(a - b)
    elif operator == '*':
        stack.append(a * b)
    elif operator == '/':
        if b == 0:
            # Restore stack if division by zero
            stack.extend([a, b])
            return False
        stack.append(a / b)
    return True

# --- API Endpoints ---

# Group endpoints with a tag for better organization in Swagger UI
TAG = "rpn"

@app.get("/rpn/stack", response_model=List[StackModel], tags=[TAG])
def list_stacks():
    """List all available stacks"""
    return [{'stack_id': sid, 'stack': s} for sid, s in stacks.items()]

@app.post("/rpn/stack", response_model=StackModel, status_code=status.HTTP_201_CREATED, tags=[TAG])
def create_stack():
    """Create a new stack"""
    stack_id = str(uuid.uuid4())
    stacks[stack_id] = []
    return {'stack_id': stack_id, 'stack': []}

@app.get("/rpn/stack/{stack_id}", response_model=StackModel, tags=[TAG])
def get_stack(stack_id: str = Path(..., title="The stack identifier")):
    """Get a stack by its ID"""
    if stack_id not in stacks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stack {stack_id} not found")
    return {'stack_id': stack_id, 'stack': stacks[stack_id]}

@app.post("/rpn/stack/{stack_id}", response_model=StackModel, tags=[TAG])
def push_value_to_stack(
    stack_id: str = Path(..., title="The stack identifier"),
    value: Value = Body(...)
):
    """Push a new value to a stack"""
    if stack_id not in stacks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stack {stack_id} not found")
    stacks[stack_id].append(value.value)
    return {'stack_id': stack_id, 'stack': stacks[stack_id]}

@app.delete("/rpn/stack/{stack_id}", status_code=status.HTTP_204_NO_CONTENT, tags=[TAG])
def delete_stack(stack_id: str = Path(..., title="The stack identifier")):
    """Delete a stack"""
    if stack_id not in stacks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stack {stack_id} not found")
    del stacks[stack_id]
    return None

@app.get("/rpn/op", tags=[TAG])
def list_operands():
    """List all available operands"""
    return {'operands': ['+', '-', '*', '/']}

@app.post("/rpn/op/{op}/stack/{stack_id}", response_model=StackModel, tags=[TAG])
def apply_operand(
    op: str = Path(..., title="The operand to apply", pattern=r"^[\+\-\*\/]$"),
    stack_id: str = Path(..., title="The stack identifier")
):
    """Apply an operand to a stack"""
    if stack_id not in stacks:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Stack {stack_id} not found")

    if not apply_operation(stacks[stack_id], op):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Insufficient values on the stack for operation or division by zero"
        )

    return {'stack_id': stack_id, 'stack': stacks[stack_id]}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
