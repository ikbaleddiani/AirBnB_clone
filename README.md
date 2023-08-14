## **ALX AFRICA SE Program**

### **project: 0x00. AirBnB clone - the console** <sup>``Group project`` ``Python`` ``OOP``</sup>

**Team:**
- Ikbal Eddiani <sup>[ikbaleddiani](https://github.com/ikbaleddiani)</sup>
- Ahmed Rifki <sup>[AhmedSeeker](https://github.com/AhmedSeeker)</sup>

#### **About Project:**
> - A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
> - This is the first step towards building a first full web application: the AirBnB clone.
> - This project will be used with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

#### **Use_case of the command interpreter:**
> - Create a new object (ex: a new User or a new Place)
> - Retrieve an object from a file, a database etc…
> - Do operations on objects (count, compute stats, etc…)
> - Update attributes of an object
> - Destroy an object

#### **how to start it:**
> - clone this repository on your machine by typing on your cmd prompt:
>   - git clone https://github.com/ikbaleddiabi/AirBnB_clone.git
> - navigate to the repository AirBnB_clone using cd command like this: cd AirBnB_clone
> - Type ``./console`` to run the command interpreter
> - this prompt message (hbnb) will appear

#### **Usage:**
> - type ``help`` to show a list of available commands: create show quit EOF
> - to create an object, use create command as follow: ``create <class name>``
> - to display an object you will use show command with the id of the object: ``show <class name>(<id>)`` or ``<class name>.show(<id>)``
> - use all command to displays all objects of a class: ``all <class name>()`` or ``<class name>.all()``
> - using ``all`` command without class name it will show all objects of all classes: ``all``
> - to update an attribute or add new one use update command:
>   - ``update <class name> <id> <atttibute name> <attribute value>``
>   - or
>   - `` <class name>.update(<id>, dict)``
> - to deletes an object, use destroy command: ``destroy <class name> <id>`` or ``<class name>.destroy(<id>)``
> - to prints the number of objects of class, use: ``<class name>.count()``

#### **Examples:**
> - help
>   - output:
>     - Documented commands (type help <topic>):
>     - ========================================
>     - EOF  all  count  create  destroy  help  quit  show  update
> - help create
>   - output:
>     - ** Updates or add new attributes to the instance **
>     - syntax:
>     - ``update <class name> <id> <attribute name> <attribute value>``
>     - or
>     - ``<class name>.update(<id>, [dict])``
>     - -------------------------------------------------------------------
>     - Note: attribute value with a space must be between double quote
> - create User:
>   - output
>     - 07f4106a-bd58-4635-a1a0-e2cb68799e69
> - User.show(07f4106a-bd58-4635-a1a0-e2cb68799e69)
>   - output
>     - ``[User](07f4106a-bd58-4635-a1a0-e2cb68799e69) {'id': '07f4106a-bd58-4635-a1a0-e2cb68799e69', 'created_at': datetime.datetime(2023, 8, 13, 7, 2
3, 42, 267697), 'updated_at': datetime.datetime(2023, 8, 13, 7, 23, 42, 267708)}``
> - User.destroy(07f4106a-bd58-4635-a1a0-e2cb68799e69)

## AUTHORS:
- Ikbal Eddiani <sup>[ikbaleddiani](https://github.com/ikbaleddiani)</sup>
- Ahmed Rifki <sup>[AhmedSeeker](https://github.com/AhmedSeeker)</sup>
