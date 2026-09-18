from pydantic import BaseModel, Field
from typing import Optional


class EnergyInput(BaseModel):
    building_id: str
    current_load: float = Field(..., ge=0)
    solar_generation: float = Field(0, ge=0)
    battery_level: float = Field(0, ge=0, le=100)
    temperature: Optional[float] = None


class OptimizationRequest(BaseModel):
    building_id: str
    current_load: float = Field(..., ge=0)
    solar_generation: float = Field(0, ge=0)
    battery_level: float = Field(0, ge=0, le=100)


class OptimizationResponse(BaseModel):
    building_id: str
    recommended_action: str
    estimated_saving: float
    message: str


class QueryRequest(BaseModel):
    question: str


class QueryResponse(BaseModel):
    answer: str