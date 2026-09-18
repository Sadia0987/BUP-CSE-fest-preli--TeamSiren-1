from fastapi import FastAPI, HTTPException

from models.schemas import (
    OptimizationRequest,
    OptimizationResponse,
    QueryRequest,
    QueryResponse
)

from optimizer.energy_optimizer import optimize_energy
from llm.interpreter import interpret_query
from guardrails.validator import validate_energy_data


app = FastAPI(
    title="BUP GridWise LLM",
    description="Smart Energy Optimization and LLM-based Grid Assistant",
    version="1.0.0"
)


@app.get("/")
def home():
    return {
        "message": "BUP GridWise LLM API is running!"
    }


@app.get("/health")
def health():
    return {
        "status": "OK"
    }


@app.post("/optimize", response_model=OptimizationResponse)
def optimize(request: OptimizationRequest):

    # Guardrails validation
    valid, message = validate_energy_data(
        request.current_load,
        request.solar_generation,
        request.battery_level
    )

    if not valid:
        raise HTTPException(
            status_code=400,
            detail=message
        )

    # Energy optimization
    result = optimize_energy(
        current_load=request.current_load,
        solar_generation=request.solar_generation,
        battery_level=request.battery_level
    )

    return {
        "building_id": request.building_id,
        "recommended_action": result["recommended_action"],
        "estimated_saving": result["estimated_saving"],
        "message": result["message"]
    }


@app.post("/interpret", response_model=QueryResponse)
def interpret(request: QueryRequest):

    result = interpret_query(request.question)

    return {
        "answer": (
            f"Current load: {result['current_load']}, "
            f"Solar generation: {result['solar_generation']}, "
            f"Battery level: {result['battery_level']}%"
        )
    }
@app.post("/ask")
def ask(request: QueryRequest):

    # Step 1: Natural language থেকে data বের করা
    result = interpret_query(request.question)

    current_load = result["current_load"]
    solar_generation = result["solar_generation"]
    battery_level = result["battery_level"]

    # Step 2: Missing data check
    missing_data = []

    if current_load is None:
        missing_data.append("current load")

    if solar_generation is None:
        missing_data.append("solar generation")

    if battery_level is None:
        missing_data.append("battery level")

    if missing_data:
        return {
            "question": request.question,
            "message": (
                "Please provide: " +
                ", ".join(missing_data)
            )
        }

    # Step 3: Guardrails validation
    valid, message = validate_energy_data(
        current_load,
        solar_generation,
        battery_level
    )

    if not valid:
        raise HTTPException(
            status_code=400,
            detail=message
        )

    # Step 4: Energy optimization
    optimization = optimize_energy(
        current_load=current_load,
        solar_generation=solar_generation,
        battery_level=battery_level
    )

    # Step 5: Final response
    return {
    "question": request.question,
    "current_load": current_load,
    "solar_generation": solar_generation,
    "battery_level": battery_level,
    "recommended_action": optimization["recommended_action"],
    "estimated_saving": optimization["estimated_saving"],
    "remaining_load": optimization["remaining_load"],
    "message": optimization["message"]
}