from pydantic import BaseModel, Field, Validator
from typing import Optional
from bson.objectid import ObjectId

class Project(BaseModel):
    _id: Optional[ObjectId]
    project_id: str = Field(...,min_length=1)
    
    #you can make your own custom validation like that
    @Validator("project_id")
    def validate_project_id(cls, value):
        if not value.isalnum():
            raise ValueError('project_id must be alphanumeric')
        return
    
    class config:
        arbitrary_type_allowed = True