#!/usr/bin/python3
"""
Custom class for cli program
"""
import cmd
import models
from datetime import datetime
from models.amenity import Amenity
from models.base_model import BaseModel
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User
import shlex

classes = {"Amenity": Amenity, "BaseModel": BaseModel, "City": City,
           "Place": Place, "Review": Review, "State": State, "User": User}


class HBNBCommand(cmd.Cmd):
    """HBNBCommand class"""
    prompt = '(hbnb) '

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """EOF command to exit the program"""
        return True

    def emptyline(self):
        """Empty line"""
        pass

    def default(self, arg):
        '''Usage: <class name>.<command>(<parameters>)'''
        args = arg.split(".")
        if len(args) == 2:
            if args[0] in classes and args[1] == "all()":
                self.do_all(args[0])
            elif args[0] in classes and args[1] == "count()":
                self.do_count(args[0])
            elif args[0] in classes and args[1].startswith("show("):
                args[1] = args[1].replace("show(", "")
                args[1] = args[1].replace(")", "")
                args[1] = args[1].replace('"', "")
                self.do_show(args[0] + " " + args[1])
            elif args[0] in classes and args[1].startswith("destroy("):
                args[1] = args[1].replace("destroy(", "")
                args[1] = args[1].replace(")", "")
                args[1] = args[1].replace('"', "")
                self.do_destroy(args[0] + " " + args[1])
            elif args[0] in classes and args[1].startswith("update("):
                args[1] = args[1].replace("update(", "")
                args[1] = args[1].replace(")", "")
                args[1] = args[1].replace('"', "")
                if "," in args[1]:
                    args[1] = args[1].split(",")
                    self.do_update(args[0] + " " + args[1][0] + " " +
                                   args[1][1] + " " + args[1][2])
                else:
                    self.do_update(args[0] + " " + args[1])
            else:
                cmd.Cmd.default(self, arg)
        else:
            cmd.Cmd.default(self, arg)

    def do_create(self, arg):
        """Creates a new instance of a class"""
        args = arg.split()
        name_of_class = args[0]
        if len(args) == 0:
            print("** class name missing **")
            return False

        if args[0] not in classes:
            print("** class doesn't exist **")
            return False

        new_dict = {}
        for arg in args[1:]:
            if "=" in arg:
                val_value = arg.split('=', 1)
                key = val_value[0]
                value = val_value[1]
                if value[0] == value[-1] == '"':
                    value = shlex.split(value)[0].replace('_', ' ')
                else:
                    try:
                        value = int(value)
                    except ValueError:
                        try:
                            value = float(value)
                        except ValueError:
                            continue
                new_dict[key] = value
        instance = classes[args[0]](**new_dict)
        instance.save()
        print(instance.id)

    # def _check_value(self, args):
    #     params = {}
    #     for arg in args[1:]:
    #         if "=" in arg:
    #             key, value = arg.split("=")
    #             if value[0] == value[-1] == '"':
    #                 value = value[1:-1]
    #             elif '.' in value:
    #                 try:
    #                     value = float(value)
    #                 except ValueError:
    #                     pass
    #             else:
    #                 try:
    #                     value = int(value)
    #                 except ValueError:
    #                     pass
    #             params[key] = value
    #     return params

    # def do_create(self, arg):
    #     """Creates a new instance of BaseModel,
    #     saves it (to the JSON file) and prints the id
    #     """
    #     args = arg.split()
    #     if len(args) == 0:
    #         print("** class name missing **")
    #         return
    #     elif args[0] not in classes:
    #         print("** class doesn't exist **")
    #         return
    #     elif args[0] in classes:
    #         params = self._check_value(args)
    #         new_instance = classes[args[0]](**params)
    #         new_instance.save()
    #         print(new_instance.id)

    def do_show(self, arg):
        '''
        Prints the string representation of
    an instance based on the class name and id
        '''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) < 2:
            print("** instance id missing **")
            return
        key = args[0] + "." + args[1]
        if key in models.storage.all():
            print(models.storage.all()[key])
        else:
            print("** no instance found **")
            return

    def do_destroy(self, arg):
        """
        Deletes an instance based on the class name and
        id (save the change into the JSON file)
        """
        args = arg.split()

        if len(args) == 0:
            print("** class name missing **")
            return

        if args[0] not in classes:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all():
            print("** no instance found **")
            return

        del models.storage.all()[key]
        models.storage.save()

    def do_all(self, arg):
        '''Usage: all <classname> or all '''
        if len(arg) > 0 and arg not in classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in models.storage.all().values():
                if obj.__class__.__name__ == arg:
                    obj_list.append(obj.__str__())
            print(obj_list)

    def do_update(self, arg):
        '''Usage: update <class name> <id> <attribute name> "<attribute value>"
        Updates an instance based on the class name and id'''
        args = arg.split()
        if len(args) == 0:
            print("** class name missing **")
            return
        if args[0] not in classes:
            print("** class doesn't exist **")
            return
        if len(args) == 1:
            print("** instance id missing **")
            return
        key = "{}.{}".format(args[0], args[1])
        if key not in models.storage.all().keys():
            print("** no instance found **")
            return
        if len(args) == 2:
            print("** attribute name missing **")
            return
        if len(args) == 3:
            print("** value missing **")
            return
        if len(args) == 4:
            try:
                value = int(args[3])
            except ValueError:
                try:
                    value = float(args[3])
                except ValueError:
                    value = args[3].strip('"')
            setattr(models.storage.all()[key], args[2], value)
            models.storage.all()[key].save()

    def do_count(self, arg):
        '''Usage: count <class name> or count'''
        args = arg.split()
        count = 0
        for obj in models.storage.all().values():
            if obj.__class__.__name__ == args[0]:
                count += 1
        print(count)

    def do_all(self, arg):
        '''Usage: all <class name> or all'''
        args = arg.split()
        if len(args) > 0 and args[0] not in classes:
            print("** class doesn't exist **")
        else:
            obj_list = []
            for obj in models.storage.all().values():
                if len(args) == 0 or obj.__class__.__name__ == args[0]:
                    obj_list.append(obj.__str__())
                elif len(args) == 0:
                    obj_list.append(obj.__str__())
            print(obj_list)


if __name__ == '__main__':
    HBNBCommand().cmdloop()
