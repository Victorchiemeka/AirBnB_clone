# 😶‍🌫️ AirBnB clone 😶‍🌫️

![Airbnb Clone](https://user-images.githubusercontent.com/69850751/175876062-f252cc1b-bd44-46b3-9ddb-a7692b2eede4.png)

## 🫠 Description

Airbnb Clone is a comprehensive web application that replicates Airbnb's functionality, integrating database storage, a back-end API, and front-end interfacing. At present, the project focuses on implementing the back-end console.

## 🧑🏿‍💻 Classes

Airbnb utilizes various classes:

- **BaseModel**: Represents the base model with attributes `id`, `created_at`, and `updated_at`.
- **FileStorage**: Manages file storage and object serialization.
- **User**: Inherits from `BaseModel` and includes attributes like `email`, `password`, `first_name`, and `last_name`.
- **State**: Inherits from `BaseModel` with attributes like `name`.
- **City**: Inherits from `BaseModel` with attributes `state_id` and `name`.
- **Amenity**: Inherits from `BaseModel` with the `name` attribute.
- **Place**: Inherits from `BaseModel` with numerous attributes like `place_id`, `user_id`, and more.
- **Review**: Inherits from `BaseModel` with attributes `place_id`, `user_id`, and `text`.

## Storage

These classes are managed by the abstracted storage engine defined in the `FileStorage` class. Upon initialization, Airbnb Clone creates an instance of `FileStorage` called `storage`, which loads and reloads data from `file.json`. As instances of classes are created, updated, or deleted, `storage` keeps the `file.json` file synchronized.

## Airbnb Console

The Airbnb Console is a command-line interpreter used to manage the backend of Airbnb Clone. It allows for manipulation of all classes utilized by the application through calls to the `storage` object.

### Console Usage

The Airbnb Console can be run interactively or non-interactively. In non-interactive mode, you can pipe commands into `console.py`, while in interactive mode, you directly run `console.py`.

Example (non-interactive mode):

```bash
$ echo "help" | ./console.py
```

Example (interactive mode):

```bash
$ ./console.py
```

### Console Commands

The Airbnb Console supports various commands:

- **create**: Creates a new instance of a given class.
- **show**: Prints the string representation of a class instance based on an ID.
- **destroy**: Deletes a class instance based on an ID.
- **all**: Prints string representations of instances, either of a specific class or all classes.
- **count**: Retrieves the number of instances of a given class.
- **update**: Updates a class instance based on an ID with a given attribute or a dictionary of attributes.

## Testing

Unit tests for the Airbnb Clone project can be found in the `tests` folder. You can run the entire test suite or specific test files using Python's `unittest` module.

To run the entire test suite:

```bash
$ python3 -m unittest discover tests
```

To run a specific test file:

```bash
$ python3 -m unittest tests/test_console.py
```

## Author

- **Victor Chukwuemeka** - [GitHub Profile](https://github.com/victorchiemeka)
  
  
