from pydantic import BaseModel

class Document(BaseModel):
    page_content: str
    metadata: dict