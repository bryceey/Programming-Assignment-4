import build_data
import sys

    # purpose: extract the commands of an operations file
    # input: path of the operations file (str)
    # output: list of commands (list[str])
    def extract_commands(ops_file_path):
        with open(ops_file_path, "r") as ops_file:
            contents = ops_file.read()
        cmds_list = (contents.splitlines())
        return cmds_list

    def extract_command_parts(some_command):
        parts_of_command = some_command.split(".")
        this_commands_op = parts_of_command[0]
        command_dict = ("operation", this_commands_op)

        if this_commands_op == "filter state":
            command_dict["state abbreviation"]= parts_of_command[1]
        elif this_commands_op == "filter-gt" or this_commands_op == "filter-lt" or \
                this_commands_op == "population" or this_commands_op == "percent":
            command_dict["field"] = parts_of_command[1]
            if this_commands_op == "filter-gt" or this_commands_op == "filter-lt":
                command_dict["number"] = float(parts_of_command)
        return command_dict

    if __name__ == "__main__":
        full_data = build_data.get_data
        num_records = len(full_data)
        out_num_records = "{records loaded}".format(num_records)
        print(out_num_records)

        command_line_args_list = sys.argv
        name_of_ops_file = command_line_args_list[1]
        extract_commands(name_of_ops_file)
        path_of_ops_file = ". /inputs/" + name_of_ops_file
        list_of_commands = extract_commands(path_of_ops_file)
