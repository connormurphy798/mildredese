def organize_tags(tags, sys_args):
    for arg in sys_args[1:]:
        if arg.startswith('-'):
            if arg not in [tag for pair in tags for tag in pair]:
                print(f"Error: unrecognized tag {arg}")
                exit(1)
    
    indices = {}
    for long, short in tags:
        if long in sys_args and short in sys_args:
            print(f"Error: cannot use both {long} and {short} at the same time.")
            exit(1)
        if long in sys_args:
            indices[long] = sys_args.index(long)
        elif short in sys_args:
            indices[long] = sys_args.index(short)

    tag_indices = sorted(indices.items(), key=lambda x: x[1])
    user_input = {}
    for i in range(len(tag_indices)):
        tag, index = tag_indices[i]
        if i == len(tag_indices)-1:
            user_input[tag] = sys_args[index+1:]
        else:
            next_index = tag_indices[i+1][1]
            user_input[tag] = sys_args[index+1:next_index]
    if tag_indices[0][1] > 1:
        user_input["--default"] = sys_args[1:tag_indices[0][1]]
    return user_input
    