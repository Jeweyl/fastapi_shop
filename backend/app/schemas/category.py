from pydantic import BaseModel, Field


class CategoryBase(BaseModel):
    name: str = Field(
        ..., min_length=5, max_length=100, description="Category name", default=None
    )
    slug: str = Field(
        ...,
        min_length=5,
        max_length=100,
        description="URL friendly category name",
        default=None,
    )


class CategoryCreate(CategoryBase):
    pass

class CategoryResponse(CategoryBase):
    id: int = Field(..., description="Unique category id", default=None)

    class Config:
        # позволяет создавать дополнительные атрибуты из модели
        form_attributes = True 