from pydantic import BaseModel, Field
from typing import List

class ReviewAnalysis(BaseModel):
    sentiment: str = Field(description="positive, negative, or neutral")
    rating: int
    key_features: List[str]
    improvement_suggestions: List[str]

fake_llm_output = {
    "sentiment": "positive",
    "rating": 4,
    "key_features": ["performance", "battery"],
    "improvement_suggestions": ["reduce fan noise", "improve keyboard quality"]
}

result = ReviewAnalysis(**fake_llm_output)

print("Structured and Validated Output:")
print("Sentiment:", result.sentiment)
print("Rating:", result.rating)
print("Key Features:", result.key_features)
print("Improvement Suggestions:", result.improvement_suggestions)

