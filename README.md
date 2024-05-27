# AirBnB clone - The console
## Description

This Airbnb Clone project aims to provide a simplified version of Airbnb's functionality, allowing users to manage and interact with property listings through a command-line interface (CLI). The project utilizes a custom command interpreter built with Python, enabling users to perform various operations such as creating, viewing, updating, and deleting property listings.

To start the command interpreter, follow these steps:

1. Clone the Airbnb Clone project repository from GitHub to your local machine.
2. Ensure you have Python 3 installed.
3. Navigate to the project directory in your terminal or command prompt.
4. Run the command `python3 console.py` to start the command interpreter.

Once the command interpreter is running, you can use various commands to interact with the property listings. Here are some of the available commands and their usage:

- `create <class name>`: Create a new instance of a supported class.
- `all [<class name>]`: Display all instances or instances of a specified class.
- `show <class name> <instance id>`: Display details of a specific instance.
- `destroy <class name> <instance id>`: Delete an instance based on the class name and instance id.
- `update <class name> <instance id> <attribute name> <new value>`: Update attributes of an instance.

### Examples

- To create a new property listing:
```bash
create Listing
```
- To view all property listings:
```bash
all Listing
```
- To display details of a specific property listing:
```bash
show Listing 1234-5678-9012
```
- To update the price of a property listing:
```bash
update Listing 1234-5678-9012 price 150
```
- To delete a property listing:
```bash
destroy Listing 1234-5678-9012
```
By following these instructions and examples, users can effectively utilize the command interpreter to manage property listings in the Airbnb Clone project.
