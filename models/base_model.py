#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    Represents a base model with common attributes and methods.
    """

    def __init__(self, *extra_args, **extra_kwargs):
        """Initialize the BaseModel class

        Args:
            self (BaseModel): the current instance
            extra_args (any): not used here
            extra_kwargs (dict): dictionary of key/value pair attributes

        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()
        default_datetime_value = datetime.today()
        iso_format = "%Y-%m-%dT%H:%M:%S.%f"

        for key, value in extra_kwargs.items():
            if key in ["created_at", "update_at"]:
                try:
                    setattr(self, key, datetime.strptime(value, iso_format))
                except ValueError:
                    # Handle the invalid datetime format gracefully (e.g., log an error or assign a default value).
                    print(
                        f"Warning: Invalid datetime format for key '{key}' - Using a default value."
                    )
                    # Assign a default datetime value or take appropriate action.
                    setattr(self, key, default_datetime_value)
            else:
                setattr(self, key, value)

        if not extra_kwargs:
            models.storage.new(self)

    def save(self):
        """
        Saves the instance and updates the `updated_at` attribute.
        """
        try:
            self.updated_at = datetime.today()
            models.storage.save()
        except Exception as e:
            print(f"An error occurred while saving: {e}")

    # def to_dict(self):
    #     """
    #     Converts the instance to a dictionary representation.
    #     Returns:
    #         dict: A dictionary representation of the instance.
    #     """
    #     result = {
    #         "_class": self.__class__.__name__,
    #         "id": self.id,
    #         "created_at": self.created_at,
    #         "updated_at": self.updated_at,
    #     }
    #     result.update(self.__dict__)  # Add instance attributes
    #     return result
    def to_dict(self):
        """Returns a dictionary containing all \
            keys/values of __dict__ of the instance."""
        dict_copy = self.__dict__.copy()
        dict_copy["created_at"] = self.created_at
        dict_copy["updated_at"] = self.updated_at
        dict_copy["__class__"] = self.__class__.__name__

        return dict_copy

    def __str__(self):
        """
        Returns the string representation of the class.
        Returns:
            str: The string representation of the class.
        """
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"
